#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

VERSION=$(./ci/release/version.sh)
IMAGE="rads_explorer:${VERSION}"

mkdir -p artifacts/sbom

syft "$IMAGE" -o spdx-json > "artifacts/sbom/rads_explorer-${VERSION}-sbom.json"

echo "[SBOM] generated artifacts/sbom/rads_explorer-${VERSION}-sbom.json"
