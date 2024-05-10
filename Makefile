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
	@echo " * build: build and check dist."
	@echo " * build-docs: build documentation."
	@echo " * build-docs-open: build documentation and open it."
	@echo " * clean: clean caches and others."
	@echo " * init: install dependencies."
	@echo " * init-docs: install docs dependencies."
	@echo " * init-dev: install dev dependencies."
	@echo " * pre-commit: run pre-commit."
	@echo " * release: release a dist."
	@echo " * test: run tests."
	@echo " * test-report: run tests with coverage report."
	@echo " * test-report-open: run tests with coverage and open it."

.PHONY: help Makefile

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

init:
	@echo "[INFO] Install dependencies"
	@pip install .

init-docs:
	@echo "[INFO] Install docs dependencies"
	@pip install '.[docs]'

init-dev:
	@echo "[INFO] Install dev dependencies"
	@pip install '.[dev]'

pre-commit:
	@echo "[INFO] Run pre-commit"
	@pre-commit run --all-files

release:
	@echo "[INFO] Release dist"
	@twine upload "./$(DISTDIR)/*" -u __token__ -p $(PYPI_PASSWORD)

test:
	@echo "[INFO] Run tests"
	@pytest "./$(TESTSDIR)"

test-report:
	@echo "[INFO] Run tests with coverage report"
	@pytest --cov="./$(SOURCEDIR)" --cov-report term-missing

test-report-html:
	@echo "[INFO] Run tests with coverage and open it"
	@pytest --cov="./$(SOURCEDIR)" --cov-report term-missing --cov-report html
	@open ./htmlcov/index.html