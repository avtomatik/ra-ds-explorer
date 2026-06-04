#!/usr/bin/env bash
set -euo pipefail

APP="gostra-gui"
VERSION=$(./build/version.sh)
IMAGE="${APP}:${VERSION}"

WORKDIR="/tmp/gostra-build"
rm -rf "$WORKDIR"
mkdir -p "$WORKDIR"

cp -r gostra app requirements.txt "$WORKDIR/"
cd "$WORKDIR"

########################################
# OFFLINE MODE
########################################
OFFLINE=${OFFLINE:-0}

########################################
# CACHE TAGS
########################################
BASE_CACHE="gostra-cache:base"
PY_CACHE="gostra-cache:python"
REQ_HASH=$(sha256sum requirements.txt | awk '{print $1}')
DEPS_CACHE="gostra-cache:deps:${REQ_HASH}"

########################################
# 1. BASE IMAGE LAYER
########################################
echo "[1/4] Base layer..."

if ! sudo buildah images | grep -q "$BASE_CACHE"; then
  base=$(sudo buildah from debian:bookworm-slim)

  sudo buildah run "$base" -- apt-get update
  sudo buildah run "$base" -- apt-get install -y --no-install-recommends \
    curl wget ca-certificates build-essential \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev libffi-dev liblzma-dev tk-dev xz-utils uuid-dev

  sudo buildah commit "$base" "$BASE_CACHE"
  sudo buildah rm "$base"
fi

########################################
# 2. PYTHON BUILD (CACHED)
########################################
echo "[2/4] Python 3.12.13..."

if ! sudo buildah images | grep -q "$PY_CACHE"; then
  py=$(sudo buildah from "$BASE_CACHE")

  sudo buildah run "$py" -- bash -c '
    set -e
    PYVER=3.12.13

    cd /tmp

    if [ "$OFFLINE" = "1" ]; then
      cp /cache/Python-${PYVER}.tar.xz .
    else
      curl -fsSLO https://www.python.org/ftp/python/${PYVER}/Python-${PYVER}.tar.xz
    fi

    tar -xf Python-${PYVER}.tar.xz
    cd Python-${PYVER}

    ./configure --prefix=/opt/python --enable-optimizations --with-ensurepip=install
    make -j$(nproc)
    make install
  '

  sudo buildah commit "$py" "$PY_CACHE"
  sudo buildah rm "$py"
fi

########################################
# 3. DEPENDENCIES (HASH CACHE)
########################################
echo "[3/4] Dependencies..."

deps=$(sudo buildah from "$PY_CACHE")

sudo buildah copy "$deps" . /app

sudo buildah run "$deps" -- /opt/python/bin/python3.12 -m pip install --upgrade pip setuptools wheel

if [ "$OFFLINE" = "1" ]; then
  sudo buildah run "$deps" -- /opt/python/bin/python3.12 -m pip install \
    --no-index \
    --find-links /cache/wheels \
    -r /app/requirements.txt
else
  sudo buildah run "$deps" -- /opt/python/bin/python3.12 -m pip install \
    --no-cache-dir \
    -r /app/requirements.txt
fi

sudo buildah commit "$deps" "$DEPS_CACHE"
sudo buildah rm "$deps"

########################################
# 4. FINAL IMAGE
########################################
echo "[4/4] Final image..."

final=$(sudo buildah from "$DEPS_CACHE")

sudo buildah config \
  --workingdir /app \
  --env PYTHONUNBUFFERED=1 \
  --env PYTHONDONTWRITEBYTECODE=1 \
  "$final"

sudo buildah config \
  --cmd "/opt/python/bin/python3.12 -m uvicorn gostra.interfaces.main:app --host 0.0.0.0 --port 8000" \
  "$final"

sudo buildah commit "$final" "$IMAGE"
sudo buildah rm "$final"

########################################
# EXPORT ARTIFACT
########################################

mkdir -p artifacts

sudo podman save -o artifacts/${APP}.tar "$IMAGE"

echo "DONE → artifacts/${APP}.tar"
