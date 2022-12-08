# =============================================================================
# Docdocdoc Library Endpoint
# =============================================================================
#
from docdocdoc.build import (
    build_fn,
    build_toc,
    build_docs
)

from docdocdoc.parts import (
    get_article,
    get_references,
    get_function,
    template_params,
    template_references,
    template_return,
    assembling_description
)

from docdocdoc.utils import (
    collapse,
    clean_line_break,
    clean_multiple
)
