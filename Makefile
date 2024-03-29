.PHONY: docs lint test format test

format:
	poetry run autoflake  --in-place --remove-all-unused-imports  --ignore-init-module-imports --recursive annoworkapi tests
	poetry run isort annoworkapi tests
	poetry run black annoworkapi tests

lint:
	poetry run mypy annoworkapi
	poetry run flake8 annoworkapi
	poetry run pylint annoworkapi

test:
	poetry run pytest -n auto  --cov=annoworkapi --cov-report=html tests

docs:
	cd docs && poetry run make html
