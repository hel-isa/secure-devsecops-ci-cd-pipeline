# Security Policy

## Supported Versions
This is a portfolio repository. Security fixes are provided on a best-effort basis.

## Reporting a Vulnerability
Please open a GitHub Security Advisory or create a private report in the platform you are using.
Include:
- affected component/file
- reproduction steps
- impact assessment
- suggested fix (if any)

## Hardening principles used here
- least privilege in CI (minimal permissions)
- pinned actions where practical
- artifact integrity (SBOM)
- defense-in-depth scanning gates (SAST, deps, secrets, container, IaC)
