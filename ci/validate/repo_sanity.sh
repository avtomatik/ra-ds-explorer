#!/usr/bin/env bash
set -euo pipefail

test -f pyproject.toml
test -f uv.lock
test -f Dockerfile

echo "[OK] repo structure valid"
