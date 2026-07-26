.PHONY: install smoke validate test generator-smoke verify build

install:
	python -m pip install -e ".[test]"

smoke:
	python scripts/smoke_agent.py

validate:
	python scripts/validate_repository_os.py

generator-smoke:
	rm -rf .tmp/generated-example
	PYTHONPATH=src python -m repo_os_generator.cli init --spec examples/project-spec.json --target .tmp/generated-example
	PYTHONPATH=src python -m repo_os_generator.cli validate .tmp/generated-example

test:
	python -m pytest -q

verify: smoke validate generator-smoke test

build:
	python -m build
