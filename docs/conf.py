# pylint: disable=invalid-name,missing-docstring

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
]
source_suffix = ".rst"
master_doc = "index"

# General information about the project.
project = "Fava"
copyright = "2016, Dominik Aumayr"
author = "Dominik Aumayr"

exclude_patterns = ["_build"]
pygments_style = "sphinx"

extlinks = {
    "bug": ("https://github.com/beancount/fava/issues/%s", "#"),
    "user": ("https://github.com/%s", "@"),
}

autodoc_default_flags = ["members", "undoc-members"]


def skip_namedtuples(_app, _what, _name, obj, _options, _lines):
    if obj.__doc__ and obj.__doc__.startswith("Alias for field number"):
        return True
    return None


def setup(app):
    app.connect("autodoc-skip-member", skip_namedtuples)


# Options for HTML output
html_theme = "alabaster"
html_static_path = ["static"]
html_theme_options = {
    "logo": "logo.png",
    "logo_name": True,
    "logo_text_align": "center",
    "description": 'Web interface for <a href="http://furius.ca/beancount/">Beancount</a>',
    "github_user": "beancount",
    "github_repo": "fava",
    "github_button": "false",
    "show_powered_by": "false",
    "extra_nav_links": {
        "fava @ GitHub": "https://github.com/beancount/fava",
        "Issue Tracker": "https://github.com/beancount/fava/issues",
    },
    "link": "#3572b0",
    "link_hover": "#1A2F59",
}
# html_static_path = ['_static']
html_sidebars = {"**": ["about.html", "navigation.html"]}
htmlhelp_basename = "favadoc"
