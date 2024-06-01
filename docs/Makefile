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
	@rm -rf "./$(SOURCEDIR)/pages/community/changelog.rst"
	@rm -rf "./$(SOURCEDIR)/pages/community/contributing.rst"
	@rm -rf "./$(SOURCEDIR)/pages/community/code_of_conduct.rst"

copy-changelog:
	@echo "[INFO] Generating changelog.rst file and copying into "docs/$(SOURCEDIR)""
	@m2r2 ../CHANGELOG.md
	@mv ../CHANGELOG.rst "$(SOURCEDIR)/pages/community/changelog.rst"

copy-contributing:
	@echo "[INFO] Generating contributing.rst and copying into "docs/$(SOURCEDIR)""
	@m2r2 ../CONTRIBUTING.md
	@mv ../CONTRIBUTING.rst "$(SOURCEDIR)/pages/community/contributing.rst"

copy-code-of-conduct:
	@echo "[INFO] Generating code_of_conduct.rst and copying into "docs/$(SOURCEDIR)""
	@m2r2 ../CODE_OF_CONDUCT.md
	@mv ../CODE_OF_CONDUCT.rst "$(SOURCEDIR)/pages/community/code_of_conduct.rst"

doc:
	@echo "[INFO] Build documentation"
	@$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)"

build-docs: clean copy-changelog copy-contributing copy-code-of-conduct doc
