from docutils import nodes
from docutils.parsers.rst import roles

def tooltip_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom Sphinx role to create hover tooltips.

    Syntax in .rst:
    :tooltip:`Visible Text|Hover Text`
    """
    try:
        display_text, tooltip_text = text.split("|", 1)
    except ValueError:
        # If no '|' is provided, just show the visible text
        display_text, tooltip_text = text, ""
    
    # Create an inline node with the tooltip clas
