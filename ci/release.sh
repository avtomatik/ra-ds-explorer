#!/usr/bin/env bash
set -euo pipefail

GIT_HASH=$(git rev-parse --short HEAD 2>/dev/null || echo "nogit")
DATE=$(date -u +%Y%m%d)

echo "1.0.${DATE}.${GIT_HASH}"
