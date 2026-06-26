#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

export PYTHONPATH="$ROOT_DIR"
export RADS_TRANSPORT=curl

echo "[TEST] running GOLDEN integration tests"

pytest tests/integration -vv -m "real"
