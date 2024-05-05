# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

clean:
	@echo "[INFO] -- cleaning"
	@rm -rf "./$(BUILDDIR)"
	@rm -rf "./$(SOURCEDIR)/changelog.md"
	@rm -rf "./$(SOURCEDIR)/contributing.md"

copy-changelog:
	@echo "[INFO] Copying CHANGELOG.md in "docs/$(SOURCEDIR)""
	@cp -r ../CHANGELOG.md "$(SOURCEDIR)/changelog.md"

copy-contributing:
	@echo "[INFO] Copying CONTRIBUTING.md in "docs/$(SOURCEDIR)""
	@cp -r ../CONTRIBUTING.md "$(SOURCEDIR)/contributing.md"

doc:
	@echo "[INFO] Build documentation"
	@$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)"

generate-documentation: clean copy-changelog copy-contributing doc
