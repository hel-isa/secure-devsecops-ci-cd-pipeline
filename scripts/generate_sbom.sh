#!/usr/bin/env bash
set -euo pipefail

mkdir -p sbom
echo "[*] Python SBOM (CycloneDX)..."
python -m pip install -q cyclonedx-bom
cyclonedx-py -r -i app/requirements.txt -o sbom/python.cdx.json

echo "[*] Done: sbom/python.cdx.json"
