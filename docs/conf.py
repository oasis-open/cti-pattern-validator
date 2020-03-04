# -*- coding: utf-8 -*-

project = 'stix2-patterns'
copyright = '2018, OASIS Open'
author = 'OASIS Open'

version = '1.3.0'
release = '1.3.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx-prompt',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'


html_theme = 'alabaster'

html_static_path = ['_static']

htmlhelp_basename = 'stix2-patternsdoc'


latex_elements = {}

latex_documents = [
    (master_doc, 'stix2-patterns.tex', 'stix2-patterns Documentation',
     'OASIS Open', 'manual'),
]

man_pages = [
    (master_doc, 'stix2-patterns', 'stix2-patterns Documentation',
     [author], 1)
]


texinfo_documents = [
    (master_doc, 'stix2-patterns', 'stix2-patterns Documentation',
     author, 'stix2-patterns', 'One line description of project.',
     'Miscellaneous'),
]
