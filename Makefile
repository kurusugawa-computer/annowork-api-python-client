
ifndef SOURCE_FILES
	export SOURCE_FILES:=annoworkapi
endif
ifndef TEST_FILES
	export TEST_FILES:=tests
endif

.PHONY: docs lint test format test

format:
	poetry run ruff format ${SOURCE_FILES} ${TEST_FILES}
	poetry run ruff check ${SOURCE_FILES} ${TEST_FILES} --fix-only --exit-zero

lint:
	poetry run ruff check ${SOURCE_FILES} ${TEST_FILES}
	# テストコードはチェックを緩和するためmypy, pylintは実行しない
	poetry run mypy ${SOURCE_FILES}
	poetry run pylint --jobs=0 ${SOURCE_FILES}

test:
	poetry run pytest -n auto  --cov=annoworkapi --cov-report=html tests

docs:
	cd docs && poetry run make html
