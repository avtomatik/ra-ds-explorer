#!/usr/bin/env bash
set -euo pipefail

export DOCKER_BUILDKIT=1

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

VERSION="$(./ci/release/version.sh)"
IMAGE="rads_explorer:${VERSION}"

echo "[BUILD] version: $VERSION"

./ci/validate/lock_check.sh

echo "[BUILD] building image: $IMAGE"

docker build \
  --pull \
  -t "$IMAGE" \
  -f "$ROOT_DIR/docker/Dockerfile" \
  "$ROOT_DIR"

echo "[DONE] built $IMAGE"
