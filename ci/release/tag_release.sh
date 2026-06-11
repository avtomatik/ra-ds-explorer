#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

VERSION=$(./ci/release/version.sh)

git tag "$VERSION"
git push origin "$VERSION"

echo "[RELEASE] tagged $VERSION"
