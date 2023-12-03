ENVIRONMENT_NAME=aoc

.PHONY: clean
clean:
	find . -type d -name ".mypy_cache" | xargs rm -rf
	find . -type d -name ".pytest_cache" | xargs rm -rf
	find . -type d -name "__pycache__" | xargs rm -rf
	find `pwd`/src -type d -name "*.egg-info" | xargs rm -rf

.PHONY: remove-env
remove-env:
	find `pwd` -type d -name ".venv*" | xargs rm -rf

.PHONY: env
env:
	python3 -m venv .venv@${ENVIRONMENT_NAME}

.PHONY: install
install:
	python3 -m pip install -r requirements.txt

.PHONY: setup
setup: clean remove-env env install


.PHONY: format
format:
	pautoflake `pwd`/src `pwd`/tests
	isort `pwd`/src `pwd`/tests
	black `pwd`/src `pwd`/tests

.PHONY: lint
lint:
	pflake8 `pwd`/src

.PHONY: types
types:
	mypy `pwd`/src
	mypy `pwd`/tests

.PHONY: format-check
format-check:
	pautoflake `pwd`/src --check
	isort `pwd`/src --check
	black `pwd`/src --check

.PHONY: ci
ci: format-check lint types

.PHONY: ci-fix
ci-fix: format lint types

.PHONY: test
test:
	coverage run --source=src -m pytest -s -vv
	coverage report
	coverage xml
	coverage html

.PHONY: show_report
show_report: test
	open -a "Google Chrome" `pwd`/coverage/index.html
