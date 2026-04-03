.PHONY: install generate tidy lint test test-ci validate

# OpenAPI spec location (relative to this directory)
OPENAPI_SPEC := ../../provenance-api/internal/api/spec/public/openapi.bundled.yaml

install:
	@poetry install --no-interaction

generate: install
	@poetry run openapi-python-client generate \
		--path "$(OPENAPI_SPEC)" \
		--output-path src/netrise_provenance_sdk_client \
		--config openapi-generator-config.yaml \
		--meta none \
		--overwrite

tidy:
	@echo "No tidy needed for Python SDK"

lint:
	@poetry run ruff check src/ tests/ || true

test: generate
	@poetry run pytest

test-ci: generate
	@poetry run pytest --cov=netrise_provenance_sdk --cov-report=term-missing

validate:
	@echo "No validate needed for Python SDK"
