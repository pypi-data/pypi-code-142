
# =============================================================================
# Build documentation Function
# =============================================================================
#
# Functions to build the library documentation
#
from io import StringIO
from functools import partial

from docdocdoc.parts import (
    get_function,
    template_params,
    template_references,
    template_return
)


def build_fn(fn):
    """
    Function returning the function or class documentation written in Markdown.

    Args:
        fn (str): str of the function or class name".
    Returns:
        str: function or class documentation written in Markdown.
    """

    lines = []

    fn_doc = get_function(fn)

    lines.append("#### %s\n" % fn_doc["name"])
    lines.append(fn_doc["description"])

    if fn_doc["article"] is not None:
        lines.append("\n*Article*")
        lines.append("> " + fn_doc["article"])

    if fn_doc["references"]:
        lines.append("\n*References*\n")
        lines.append(template_references(fn_doc))

    for example in fn_doc["examples"]:
        lines.append("\n```python")
        lines.append(example.description)
        lines.append("```")

    lines.append("\n*Arguments*\n")
    lines.append(template_params(fn_doc))

    if fn_doc["returns"]:
        lines.append("\n*Yields*\n" if fn_doc["returns"].is_generator else "\n*Returns*\n")
        lines.append(template_return(fn_doc))

    return "\n".join(lines)


def build_toc(data):
    """
    Function returning the table of content written in Markdown.

    Args:
        data (list): list of dicts with the keys "title" and "fns".
            "title" contains the name of the section and "fns" contains the
            name of the functions in the section.
    Returns:
        str: table of content written in Markdown.
    """

    lines = []

    for item in data:
        lines.append(
            "* [%s](#%s)" % (item["title"], item["title"].lower().replace(" ", "-"))
        )

        for fn in item["fns"]:
            name = fn.__name__

            lines.append("  * [%s](#%s)" % (name, name.lower()))

    return "\n".join(lines)


def build_docs(data):
    """
    Function returning the documentation written in Markdown.

    Args:
        data (list): list of dicts with the keys "title" and "fns".
            "title" contains the name of the section and "fns" contains the
            name of the functions in the section.
    Returns:
        StringIO: documentation written in Markdown.
    """

    f = StringIO()

    p = partial(print, file=f)

    for item in data:
        p()
        p("---")
        p()
        p("### %s" % item["title"])

        for fn in item["fns"]:
            p()
            p(build_fn(fn))

    result = f.getvalue()
    f.close()

    return result


def generate_readme(data):
    """
    Function printing readme.

    Args:
        data (list): list of dicts with the keys "title" and "fns".
            "title" contains the name of the section and "fns" contains the
            name of the fonctions in the section.
    """

    with open("./README.template.md") as f:
        TEMPLATE = f.read()

    readme = TEMPLATE.format(toc=build_toc(data), docs=build_docs(data)).rstrip()

    print(readme)
