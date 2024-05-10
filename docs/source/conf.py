# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# NOTE:
# pip install sphinx_rtd_theme, numpydoc
# is needed in order to build the documentation

import sys
from pathlib import Path
from datetime import datetime

sys.path.append(str(Path.cwd().parent.parent))

from symmetria import __version__

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "symmetria"
copyright = f"{datetime.now().year}, Vasco Schiavo"
author = "Vasco Schiavo"
version = f"{__version__}"
language = "en"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# 'sphinx_rtd_theme', 'cloud'
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
