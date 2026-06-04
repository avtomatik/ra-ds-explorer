#!/usr/bin/env bash
set -euo pipefail

VERSION=$(./ci/release/version.sh)
IMAGE="gostra:${VERSION}"

echo "[BUILD] version: $VERSION"

uv lock --check

docker build \
  --no-cache \
  -t "$IMAGE" \
  .

echo "[DONE] built $IMAGE"
