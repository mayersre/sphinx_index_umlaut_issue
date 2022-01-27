# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import datetime
sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Git information -----------------------------------------------------

import git
from etc.settings import GIT_VERSION, GIT_REVISION, LOGO_DIR

LATEX_LOGO_DIR=LOGO_DIR + '/'

#
# -- Project information -----------------------------------------------------

project = 'Umlaut Issue'
copyright = 'Nobody'


author = 'Reiner Mayers'


# The short X.Y version
version = GIT_VERSION
# The full version, including alpha/beta/rc tags
release = datetime.datetime.now().strftime('%B %Y')
releasename = 'Version'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
if os.path.basename(os.path.dirname(  os.path.dirname( os.path.abspath(__file__)  ) )) == 'pdf_conf' :
    extensions = [
        'sphinx.ext.autodoc',
        #'sphinx.ext.intersphinx',
        'sphinx.ext.imgmath', # for pdf creation only
        'sphinx.ext.ifconfig',
        'sphinx.ext.graphviz',
        'sphinxcontrib.bibtex'] 
else :
    extensions = [
        'sphinx.ext.autodoc',
        #'sphinx.ext.intersphinx',
        'sphinx.ext.mathjax',
        'sphinx.ext.ifconfig',
        'sphinx.ext.graphviz',
        'sphinxcontrib.bibtex',
        'sphinx_rtd_theme']  

bibtex_bibfiles = ['references.bib','../library/allgemein/references.bib','../../library/allgemein/references.bib']

numfig=True
numfig_secnum_depth = (2)
numfig_format = {'figure': 'Abbildung %s', 'table': 'Tabelle %s', 'code-block': 'Code Block %s'}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'de'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo  = '_bilder/logo_html.png'
html_favicon = '_bilder/favicon.ico'
#
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'sticky_navigation': True,
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_copy_source = False
html_show_sourcelink = False

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.

htmlhelp_basename = 'umlaut-issue'

# -- Options for LaTeX output ------------------------------------------------
if language == 'en':
    latex_preamble = r'''

\usepackage{graphicx}
\usepackage[T1]{fontenc}
\usepackage[version=3]{mhchem}
\usepackage{shadow}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb,color}
\usepackage{multicol,pifont,mdframed,lscape}
\usepackage{nicefrac,marvosym,wasysym, textcomp, gensymb}
\usepackage[style=english]{csquotes}
\usepackage{charter}
\usepackage[defaultsans]{lato}
\usepackage{inconsolata}
\setlength{\headheight}{16pt}
\setcounter{secnumdepth}{-1}
\setcounter{tocdepth}{2}
\usepackage{hyperref,url}
\usepackage{float}
\usepackage{chemfig}
\usepackage[printwatermark]{xwatermark}
\usepackage{xcolor}

\usepackage{tikz}


\watermarkpaths*{ ./, %s , }

\newwatermark*[ oddpages, picangle=0,
  picontoptext=true,boxalign=left,
  picbb=0 0 400 70 ,picscale=0.45,picfile=somelogo,
  picfileext=png,picxpos=-83,picypos=137
]{}

\newwatermark*[ evenpages, picangle=0,
  picontoptext=true,boxalign=left,
  picbb=0 0 400 70 ,picscale=0.45,picfile=somelogo,
  picfileext=png,picxpos=37.5,picypos=137
]{}



\newsavebox\mybox
\savebox\mybox{\tikz[color=red,opacity=0.3]\node{DRAFT};}
\newwatermark*[
  pages=1-3,
  angle=45,
  scale=6,
  xpos=-20,
  ypos=15
]{\usebox\mybox}



\hypersetup{
pdftitle={Umlaut Issue},
pdfsubject={Umlaut Issue},
pdfauthor={Reiner Mayers},
pdfcreator={Reiner Mayers},
pdfproducer={Bundesfachschule Kälte-Klima-Technik},
pdfkeywords={BFS} {Kältetechnik} {Thermodynamik} {(C) BFS 2019},
}
'''%(LATEX_LOGO_DIR)
else:
        latex_preamble = r'''

\usepackage{graphicx}
\usepackage[T1]{fontenc}
\usepackage[version=3]{mhchem}
\usepackage{shadow}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb,color}
\usepackage{multicol,pifont,mdframed,lscape}
\usepackage{nicefrac,marvosym,wasysym, textcomp, gensymb}
\usepackage[style=german]{csquotes}
\usepackage{charter}
\usepackage[defaultsans]{lato}
\usepackage{inconsolata}
\setlength{\headheight}{16pt}
\setcounter{secnumdepth}{-1}
\setcounter{tocdepth}{2}
\usepackage{hyperref,url}
\usepackage{float}
\usepackage{chemfig}
\usepackage[printwatermark]{xwatermark}
\usepackage{xcolor}

\usepackage{tikz}


\watermarkpaths*{ ./, %s , }

\newwatermark*[ oddpages, picangle=0,
  picontoptext=true,boxalign=left,
  picbb=0 0 400 70 ,picscale=0.45,picfile=somelogo,
  picfileext=png,picxpos=-83,picypos=137
]{}

\newwatermark*[ evenpages, picangle=0,
  picontoptext=true,boxalign=left,
  picbb=0 0 400 70 ,picscale=0.45,picfile=somelogo,
  picfileext=png,picxpos=37.5,picypos=137
]{}



\newsavebox\mybox
\savebox\mybox{\tikz[color=red,opacity=0.3]\node{ENTWURF};}
\newwatermark*[
  pages=1-3,
  angle=45,
  scale=6,
  xpos=-20,
  ypos=15
]{\usebox\mybox}



\hypersetup{
pdftitle={Umlaut Issue},
pdfsubject={Umlaut Issue},
pdfauthor={Reiner Mayers},
pdfcreator={Reiner Mayers},
pdfproducer={Bundesfachschule Kälte-Klima-Technik},
pdfkeywords={BFS} {Kältetechnik} {Thermodynamik} {(C) BFS 2019},
}
'''%(LATEX_LOGO_DIR)

latex_show_pagerefs = False
imgmath_image_format='png'
imgmath_latex_preamble = latex_preamble

if language == 'en' :
    latex_elements = {
        'preamble': latex_preamble,
        'classoptions': 'oneside,openany',
        'releasename': "Version",
        'papersize': 'a4paper',
        'pointsize': '11pt',
        'fontpkg': '',
        'babel':    '\\usepackage[english]{babel}',
        'geometry': '\\usepackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}',
        'fncychap': '',
        'figure_align': 'H',
    
    }
else :
    latex_elements = {
        'preamble': latex_preamble,
        'classoptions': 'oneside,openany',
        'releasename': "Version",
        'papersize': 'a4paper',
        'pointsize': '11pt',
        'fontpkg': '',
        'babel':    '\\usepackage[ngerman]{babel}',
        'geometry': '\\usepackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}',
        'fncychap': '',
        'figure_align': 'H',
    
    }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'umlaut-issue.tex', u'Umlaut Issue',
     u'Reiner Mayers', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'umlaut-issue', u'Umlaut Issue',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'umlaut-issue', u'Umlaut Issue',
     author, 'umlaut-issue', 'Umlaut Issue for Sphinx',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
