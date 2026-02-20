# secure-devsecops-ci-cd-pipeline

An AppSec-focused GitHub portfolio project that demonstrates how to build a **secure CI/CD pipeline** with multiple security gates, SBOM generation, and supply-chain controls — suitable as a reference repo for job interviews.

## What this repo showcases

### CI security controls (GitHub Actions)
- **SAST**
  - GitHub **CodeQL** (Python) – code scanning + SARIF upload
  - **Semgrep** – customizable rules + SARIF upload
- **Secret scanning**
  - **Gitleaks** – secrets detection (baseline-friendly)
- **Dependency security**
  - GitHub **dependency-review** (blocks risky PR dependency changes)
  - **OSV-Scanner** (Open Source Vulnerabilities)
  - **pip-audit** (Python dependencies)
- **Container security**
  - **Trivy** – image + filesystem scan + SARIF upload
  - **Grype** – image scan
- **IaC security**
  - **Checkov** – Terraform/Kubernetes/Helm scanning
- **SBOM + supply chain**
  - **CycloneDX SBOM** (application + container)
  - Optional: provenance/signing hooks (Cosign/SLSA) placeholders

### Secure coding practices (sample app)
- Minimal **Flask** API with:
  - input validation, safe error handling
  - security headers
  - structured logging
  - unit tests (pytest)
- **Dockerfile** with non-root user
- **Terraform** example with security-friendly defaults
- **Kubernetes** manifests with securityContext and network policy example

## Quick start (local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt -r app/requirements-dev.txt
pytest -q
python app/app.py
```

Run local security checks:
```bash
make security
```

## Repo structure

- `app/` — sample Flask API + tests
- `infra/terraform/` — example Terraform
- `deploy/k8s/` — example Kubernetes manifests
- `scripts/` — helper scripts (sbom, scans)
- `.github/workflows/` — CI pipelines

## Notes
- This repository is designed to be **tool-complete** yet small enough to understand quickly.
- Tune fail thresholds in workflows depending on your org’s risk appetite.

## License
MIT

_Last updated: 2026-02-20_
