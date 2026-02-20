# Threat Model (Lightweight)

## Assets
- API availability & integrity
- Secrets (none stored in repo; use env/secrets manager)
- Container image integrity

## Entry points
- `/hello` JSON input
- CI pipeline dependencies (actions, external tools)
- Container build context

## Threats & mitigations
- Injection -> strict input validation + safe error handling
- Secrets leakage -> gitleaks + .gitignore + no hard-coded secrets
- Dependency CVEs -> dependency-review, osv-scanner, pip-audit
- Supply-chain attacks -> SBOM generation, least-privilege CI permissions, pin actions where possible
- Container breakout -> non-root, dropped capabilities, read-only FS, seccomp profile in K8s
