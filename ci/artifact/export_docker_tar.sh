#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

VERSION=$(./ci/release/version.sh)
IMAGE="gostra:${VERSION}"

mkdir -p artifacts

docker save "$IMAGE" -o "artifacts/gostra-${VERSION}.tar"
sha256sum "artifacts/gostra-${VERSION}.tar" > "artifacts/gostra-${VERSION}.tar.sha256"

echo "[EXPORT] artifacts/gostra-${VERSION}.tar"
echo "[EXPORT] checksum artifacts/gostra-${VERSION}.tar.sha256"
