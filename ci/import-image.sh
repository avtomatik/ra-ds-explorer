#!/usr/bin/env bash
set -euo pipefail

mkdir -p cache/wheels cache/python

pip download -r requirements.txt -d cache/wheels

curl -o cache/Python-3.12.13.tar.xz \
  https://www.python.org/ftp/python/3.12.13/Python-3.12.13.tar.xz

echo "Offline cache ready."
