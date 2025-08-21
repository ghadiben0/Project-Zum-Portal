# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Zum Portal Help hubs'
copyright = '2025, Zum-IT'
author = 'Zum-IT, Documentation is your source knowledge for quick portal understanding and integrity'.

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
    "collapse_navigation": True,
    "sticky_navigation": True,
    "titles_only": False,
    "show_relbars": True,
    "style_external_links": True,
    "display_version": True,
    "show_footer": False   # hides default "Built with Sphinx" line
}
html_context = {
    "footer_text": "Your Online Documentation hub is your knowledge source to better know application functionality."
}

html_css_files = ['custom.css']

templates_path = ['_templates']


