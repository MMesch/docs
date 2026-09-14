# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "emscripten-forge"
copyright = "2022, Thorsten Beier, Wolf Vollprecht, Martin Renou"
author = "Thorsten Beier, Wolf Vollprecht, Martin Renou"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
# Ship the self-contained Qt6-wasm runner at /qtapp/. `_extra/` acts as a
# wrapper because Sphinx copies the CONTENTS of each html_extra_path entry
# into the build root — so `_extra/qtapp/index.html` lands at
# `_build/html/qtapp/index.html` (which is what we want).
html_extra_path = ["_extra"]
source_suffix = [".rst", ".md"]
