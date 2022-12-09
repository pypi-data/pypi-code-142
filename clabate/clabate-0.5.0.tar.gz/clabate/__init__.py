'''
Clabate: class based templates.

This minimalistic template system utilizes python class hierarchy,
class attributes, and string formatting.

Copyright 2019-2022 AXY axy@declassed.art
License: BSD, see LICENSE for details.

'''

__version__ = '0.5.0'

# shortcut imports
from .core import (
    Template, LeanTemplate,
    alter_braces, depends_on, escape_braces, superattr
)
from .markup import (
    MarkupTemplate, MinifiedMarkupTemplate, Markup, Escaped,
    make_escaped, minify_markup
)
