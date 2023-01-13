# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# -- Options for HTML output ---------------------------------------------------

html_theme = 'book'
html_theme_path = ['themes']
html_title = "Music for Geeks and Nerds"
#html_short_title = None
#html_logo = None
#html_favicon = None
html_static_path = ['_static']
html_domain_indices = False
html_use_index = False
html_show_sphinx = False
htmlhelp_basename = 'MusicforGeeksandNerdsdoc'
html_show_sourcelink = False

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
     'papersize': '',
     'fontpkg': '',
     'fncychap': '',
     'maketitle': '\\cover',
     'pointsize': '',
     'preamble': '',
     'releasename': "",
     'babel': '',
     'printindex': '',
     'fontenc': '',
     'inputenc': '',
     'classoptions': '',
     'utf8extra': '',
     
}

latex_additional_files = ["mfgan-bw.sty", "mfgan.sty", "_static/cover.png"]

latex_documents = [
  ('index', 'music-for-geeks-and-nerds.tex', u'Music for Geeks and Nerds',
   u'Pedro Kroger', 'manual'),
]

latex_show_pagerefs = False
latex_domain_indices = False
latex_use_modindex = False
#latex_logo = None
#latex_show_urls = False

# -- Options for Epub output ---------------------------------------------------

epub_title = u'Music for Geeks and Nerds'
epub_author = u'Pedro Kroger'
epub_publisher = u'Pedro Kroger'
epub_copyright = u'2012, Pedro Kroger'

epub_theme = 'epub2'

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
epub_cover = ("_static/cover.png", "epub-cover.html")

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['_static/opensearch.xml', '_static/doctools.js',
    '_static/jquery.js', '_static/searchtools.js', '_static/underscore.js',
    '_static/basic.css', 'search.html', '_static/websupport.js']

# The depth of the table of contents in toc.ncx.
epub_tocdepth = 2

# Allow duplicate toc entries.
epub_tocdup = False


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
   'sphinx.ext.autosummary', 'sphinx.ext.intersphinx',"sphinxawesome_theme",]


autodoc_mock_imports = ["akhdefo_functions.unzip",
   "akhdefo_functions.copyImage_Data",
   "akhdefo_functions.copyUDM2_Mask_Data",
   "akhdefo_functions.Filter_PreProcess",
   "akhdefo_functions.Crop_to_AOI",
   "akhdefo_functions.Mosaic",
   "akhdefo_functions.Coregistration",
   "akhdefo_functions.DynamicChangeDetection",
   "akhdefo_functions.plot_stackNetwork",
   "akhdefo_functions.stackprep",
   "akhdefo_functions.Time_Series",
   "akhdefo_functions.akhdefo_ts_plot",
   "akhdefo_functions.rasterClip",
   "akhdefo_functions.akhdefo_viewer",
   "akhdefo_functions.Akhdefo_resample",
   "akhdefo_functions.Akhdefo_inversion",
   "akhdefo_functions.utm_to_latlon",]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
