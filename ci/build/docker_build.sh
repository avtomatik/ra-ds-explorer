#!/usr/bin/env bash
set -euo pipefail

export DOCKER_BUILDKIT=0
export BUILDKIT_PROGRESS=plain

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

VERSION="$(./ci/release/version.sh)"
IMAGE="rads_explorer:${VERSION}"

echo "[BUILD] version: $VERSION"

./ci/validate/lock_check.sh

echo "[BUILD] context: $ROOT_DIR"

# docker build --no-cache \
docker build \
  --network=default \
  --pull=false \
  -t "$IMAGE" \
  -f "$ROOT_DIR/docker/Dockerfile" \
  "$ROOT_DIR"

echo "[DONE] built $IMAGE"
