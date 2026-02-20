#!/usr/bin/env bash
set -euo pipefail

echo "[*] Installing dev deps..."
python -m pip install -q -r app/requirements-dev.txt

echo "[*] Running ruff..."
python -m ruff check app
python -m ruff format --check app

echo "[*] Running tests..."
python -m pytest -q

echo "[*] Running pip-audit..."
python -m pip_audit -r app/requirements.txt || true

echo "[*] Generating SBOM (CycloneDX)..."
bash scripts/generate_sbom.sh

echo "[*] Done."
