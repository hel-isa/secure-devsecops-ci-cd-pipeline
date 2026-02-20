SHELL := /bin/bash

.PHONY: test lint security sbom

test:
	python -m pytest -q

lint:
	python -m pip install -q -r app/requirements-dev.txt
	python -m ruff check app
	python -m ruff format --check app

security:
	bash scripts/run_local_security.sh

sbom:
	bash scripts/generate_sbom.sh
