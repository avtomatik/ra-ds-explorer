#!/usr/bin/env bash
set -euo pipefail

uv lock --check

echo "[OK] lockfile consistent"
