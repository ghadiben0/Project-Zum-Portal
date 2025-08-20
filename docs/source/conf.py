# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Zum Portal Help hub'
copyright = '2025, Zum-IT'
author = 'Zum-IT'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_show_sourcelink = False

html_theme_options = {
    'display_version': False,

}
html_static_path = ['_static']
html_js_files = ['custom.js']

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    "footer_text": "Your Online Documentation hub is your knowledge source to better know application functionality"
}
