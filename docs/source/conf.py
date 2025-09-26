# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Zum Portal Help hub'
copyright = '2025, Zum-IT'
author = 'Zum-IT, Documentation library'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    # Built-in Sphinx extensions
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',

    # Third-party extensions
    'hoverxref.extension',        # Hoverxref for hover tooltips
    'sphinxcontrib.video',       # Video embedding*
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
    "collapse_navigation": True,
    "sticky_navigation": True,
    "titles_only": False,
    "show_relbars": True, 
    "style_external_links": True,
    "display_version": True,
    "show_footer": False,    # hides default "Built with Sphinx" line
 # "ads_box": False        # add this line to hide ads below TOC
}

html_context = {
    "footer_text": "Your Online Documentation hub is your knowledge source to better know application functionality."
}

html_static_path = ['_static']
html_js_files = ['custom.js']
html_css_files = ['custom.css?v=4']  # bump the number if you update CSS 

# -- Hoverxref Configuration
hoverxref_roles = ['ref', 'doc']  # or add more as needed
hoverxref_auto_ref = True         # optional: makes regular :ref:`...` hoverable

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- company logo
html_static_path = ["_static"]
html_logo = "_static/my_logo.png"
