# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ab-testing-analysis'
copyright = '2022, Mihir'
author = 'Mihir'
release = '1.2.7'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_static_path = ['_static']

html_favicon = 'favicon.ico'

# If specified, this will be used in the nav bar instead.
html_short_title = "AB Testing Analysis Docs"

html_theme_options = {
    "source_url": 'https://github.com/mihirdeo16/ab-testing',
    "source_icon": "github"
}