# Minimal makefile for Sphinx documentation

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
	@rm -rf "./$(SOURCEDIR)/pages/community/changelog.md"
	@rm -rf "./$(SOURCEDIR)/pages/community/contributing.md"
	@rm -rf "./$(SOURCEDIR)/pages/community/code_of_conduct.md"

copy-changelog:
	@echo "[INFO] Copying CHANGELOG.md in "docs/$(SOURCEDIR)""
	@cp -r ../CHANGELOG.md "$(SOURCEDIR)/pages/community/changelog.md"

copy-contributing:
	@echo "[INFO] Copying CONTRIBUTING.md in "docs/$(SOURCEDIR)""
	@cp -r ../CONTRIBUTING.md "$(SOURCEDIR)/pages/community/contributing.md"

copy-code-of-conduct:
	@echo "[INFO] Copying CODE_OF_CONDUCT.md in "docs/$(SOURCEDIR)""
	@cp -r ../CODE_OF_CONDUCT.md "$(SOURCEDIR)/pages/community/code_of_conduct.md"

doc:
	@echo "[INFO] Build documentation"
	@$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)"

build-docs: clean copy-changelog copy-contributing copy-code-of-conduct doc
