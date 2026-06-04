#!/usr/bin/env bash
set -euo pipefail

VERSION=$(./ci/release/version.sh)
IMAGE="gostra:${VERSION}"

mkdir -p artifacts

docker save "$IMAGE" -o "artifacts/gostra-${VERSION}.tar"

echo "[EXPORT] artifacts/gostra-${VERSION}.tar"
