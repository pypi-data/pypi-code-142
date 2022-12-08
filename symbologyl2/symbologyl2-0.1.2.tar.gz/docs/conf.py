# pylint: disable=missing-module-docstring, redefined-builtin, invalid-name

import os
import sys

sys.path.insert(0, os.path.abspath("../symbologyl2"))

project = "symbologyl2"
copyright = "2022, OneChronos Engineering"
author = "OneChronos Engineering"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
]

napoleon_use_ivar = True
napoleon_google_docstring = False
napoleon_use_param = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

master_doc = "index"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
