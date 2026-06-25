#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

VERSION=$(./ci/release/version.sh)
IMAGE="rads_explorer:${VERSION}"

mkdir -p artifacts

docker save "$IMAGE" -o "artifacts/rads_explorer-${VERSION}.tar"
sha256sum "artifacts/rads_explorer-${VERSION}.tar" > "artifacts/rads_explorer-${VERSION}.tar.sha256"

echo "[EXPORT] artifacts/rads_explorer-${VERSION}.tar"
echo "[EXPORT] checksum artifacts/rads_explorer-${VERSION}.tar.sha256"
