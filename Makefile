# Minimal Makefile for development

# variables
# you can set the first variable from the environment
PYPI_PASSWORD   ?=
DISTDIR         = dist
DOCSDIR         = docs
SOURCEDIR       = symmetria
TESTSDIR        = tests

# It is first such that "make" without argument is like "make help".
help:
	@echo "[HELP] Makefile commands:"
	@echo " * all-test: run test-suite."
	@echo " * build: build and check dist."
	@echo " * build-docs: build documentation."
	@echo " * build-docs-open: build documentation and open it."
	@echo " * clean: clean caches and others."
	@echo " * doctest: run doctest."
	@echo " * init: install dependencies."
	@echo " * init-docs: install docs dependencies."
	@echo " * init-dist: install dist dependencies."
	@echo " * init-dev: install dev dependencies."
	@echo " * install-pre-commit: install/update pre-commit and install it in git-hook."
	@echo " * mypy: run mypy."
	@echo " * pre-commit: run pre-commit."
	@echo " * release: release a dist."
	@echo " * ruff: Ruff formatting and checking."
	@echo " * test: run tests."
	@echo " * test-report-xml: run tests and generate test-report.xml."
	@echo " * test-report-missing: run tests with coverage report."
	@echo " * test-report-missing-html: run tests with coverage and open it."

.PHONY: help Makefile

all-test:
	@echo "[INFO] Run test-suite"
	@make test
	@make doctest

build:
	@echo "[INFO] Build the dist"
	@python -m build
	@echo "[INFO] Check the dist"
	@twine check "./$(DISTDIR)/*"

build-docs:
	@echo "[INFO] Build documentation"
	@cd "./$(DOCSDIR)" && make build-docs

build-docs-open:
	@echo "[INFO] Build documentation and open it"
	@cd "./$(DOCSDIR)" && make build-docs
	@open "./$(DOCSDIR)/build/index.html"

clean:
	@echo "[INFO] Clean caches and others"
	@rm -rf "./$(DISTDIR)"
	@rm -rf "./htmlcov"
	@rm -rf "./.coverage"
	@rm -rf "./symmetria.egg-info"
	@rm -rf "./tests/.cache"
	@rm -rf "./test-report.xml"

doctest:
	@echo "[INFO] Run doctest"
	@pytest --doctest-modules symmetria

init:
	@echo "[INFO] Install dependencies"
	@make pip
	@pip install '.[dev]'

init-docs:
	@echo "[INFO] Install docs dependencies"
	@make pip
	@pip install '.[docs]'

init-dist:
	@echo "[INFO] Install dist dependencies"
	@make pip
	@pip install setuptools wheel twine build

init-dev:
	@echo "[INFO] Install dev dependencies"
	@make pip
	@pip install '.[dev]'

install-pre-commit:
	@echo "[INFO] Install or update pre-commit"
	@make pip
	@pip install pre-commit
	@pre-commit --version
	@echo "[INFO] Install pre-commit into git-hooks"
	@pre-commit install

mypy:
	@echo "[INFO] Run mypy"
	@mypy .

pip:
	@python -m pip install --upgrade pip

pre-commit:
	@echo "[INFO] Run pre-commit"
	@pre-commit run --all-files

release:
	@echo "[INFO] Release dist"
	@twine upload "./$(DISTDIR)/*" -u __token__ -p $(PYPI_PASSWORD)

ruff:
	@echo "[INFO] Ruff formatting and checking"
	@ruff check . --fix
	@ruff format .


test:
	@echo "[INFO] Run tests"
	@pytest "./$(TESTSDIR)"

test-report-xml:
	@echo "[INFO] Run tests and generate test-report.xml"
	@pytest "./$(TESTSDIR)" --junitxml=test-report.xml

test-report-missing:
	@echo "[INFO] Run tests with coverage report"
	@pytest --cov="./$(SOURCEDIR)" --cov-report term-missing

test-report-missing-html:
	@echo "[INFO] Run tests with coverage and open it"
	@pytest --cov="./$(SOURCEDIR)" --cov-report term-missing --cov-report html
	@open ./htmlcov/index.html
