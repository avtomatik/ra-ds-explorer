#!/usr/bin/env bash
set -euo pipefail

VERSION=$(./ci/release/version.sh)

git tag "$VERSION"
git push origin "$VERSION"

echo "[RELEASE] tagged $VERSION"
