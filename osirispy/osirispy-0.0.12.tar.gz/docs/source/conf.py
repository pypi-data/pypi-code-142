import os
import sys
import mock
sys.path.insert(0, os.path.abspath('../../osirispy'))
sys.path.insert(0, os.path.abspath('../..'))

MOCK_MODULES = ['numpy',"h5py"]
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'osirispy'
copyright = '2022, Miguel Pardal'
author = 'Miguel Pardal'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
