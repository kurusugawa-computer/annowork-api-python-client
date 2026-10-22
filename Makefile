
ifndef SOURCE_FILES
	export SOURCE_FILES:=annoworkapi
endif
ifndef TEST_FILES
	export TEST_FILES:=tests
endif

.PHONY: docs lint test format test

format:
	uv run ruff format ${SOURCE_FILES} ${TEST_FILES}
	uv run ruff check ${SOURCE_FILES} ${TEST_FILES} --fix-only --exit-zero

lint:
	uv run ruff check ${SOURCE_FILES} ${TEST_FILES}
	# テストコードはチェックを緩和するためmypyは実行しない
	uv run mypy ${SOURCE_FILES}

test:
	uv run pytest -n auto  --cov=annoworkapi --cov-report=html tests

docs:
	cd docs && uv run make html
