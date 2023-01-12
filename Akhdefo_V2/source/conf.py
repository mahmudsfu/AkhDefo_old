# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
html_theme = 'sphinx_rtd_theme'
import os
import sys
sys.path.insert(0, os.path.abspath('../../akhdefo_functions/'))

project = 'akhdefo'
copyright = '2023, Mahmud Mustafa Muhammad'
author = 'Mahmud Mustafa Muhammad'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.duration',
   'sphinx.ext.doctest',
   'sphinx.ext.autodoc',
   'sphinx.ext.autosummary', 'sphinx.ext.intersphinx',]

 
pdf_documents = [('index', u'usage'),]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
