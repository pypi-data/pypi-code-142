# =============================================================================
# Parts documentation Function
# =============================================================================
#
# Functions to get and template documentation parts
#

import re
from docstring_parser.google import DEFAULT_SECTIONS, Section, SectionType
from docstring_parser import parse as docstring_parser, DocstringStyle, DocstringMeta

from docdocdoc.utils import collapse, clean_multiple, clean_line_break

DEFAULT_SECTIONS.append(Section("Article", "article", SectionType.SINGULAR))
DEFAULT_SECTIONS.append(Section("References", "references", SectionType.MULTIPLE))

DEFAULT_RE = re.compile(r".\s*Defaults? to (.+)\.", re.MULTILINE)
CLEAN_RE = re.compile(r"`")


def get_article(docstring):
    """
    Function returning the article if the docstring has one, None otherwise.

    Args:
        docstring (DocstringStyle.GOOGLE): a google docstring.

    Returns:
        string: string containing the description of the article.
    """
    for meta in docstring.meta:
        if type(meta) is DocstringMeta and meta.args == ["article"]:
            return clean_multiple(collapse(meta.description))

    return None


def get_references(docstring):
    """
    Function returning the references if the docstring has some, None otherwise.

    Args:
        docstring (DocstringStyle.GOOGLE): a google docstring.

    Returns:
        list: list containing the strings with the references.
    """

    references = []

    for meta in docstring.meta:
        if type(meta) is DocstringMeta and meta.args[0] == "references":
            references.append(clean_multiple(collapse(meta.description)))

    return references


def assembling_description(docstring):
    """
    Function returning the short description of the docstring,
    aggregated with the long description.

    Args:
        docstring (DocstringStyle.GOOGLE): a google docstring.

    Returns:
        string: description of the docstring.
    """

    d = docstring.short_description or ""

    if docstring.long_description:
        if docstring.blank_after_long_description:
            d += "\n" + docstring.long_description
        else:
            d += " " + docstring.long_description

    return clean_multiple(clean_line_break(d.strip()))


def get_function(fn):
    """
    Function returning a dict with the different part for a function (or class)
    documentation (i.e. name, description, article...).

    Args:
        fn (function): a function you defined.

    Returns:
        dict: dict with the different part of the documentation.
    """

    if isinstance(fn, str) or not isinstance(fn.__doc__, str):
        raise TypeError

    docstring = docstring_parser(fn.__doc__, DocstringStyle.GOOGLE)

    fn_doc = {
        "name": fn.__name__,
        "description": assembling_description(docstring),
        "article": get_article(docstring),
        "references": get_references(docstring),
        "examples": docstring.examples,
        "arguments": docstring.params,
        "returns": docstring.returns,
    }

    return fn_doc


def template_references(fn_doc):
    """
    Function returning templated references.

    Args:
        fn_doc (dict): a dict with the function documentation parts (returned by get_function).

    Returns:
        string: templated references.
    """

    lines = []

    for ref in fn_doc["references"]:
        lines.append("- " + ref)

    return "\n".join(lines)


def template_params(fn_doc):
    """
    Function returning templated arguments.

    Args:
        fn_doc (dict): a dict with the function documentation parts (returned by get_function).

    Returns:
        string: templated arguments.
    """

    lines = []

    for param in fn_doc["arguments"]:
        line = "* **%s** " % param.arg_name

        if param.type_name:
            if param.is_optional:
                line += "*%s, optional*" % param.type_name
            else:
                line += "*%s*" % param.type_name

        m = DEFAULT_RE.search(param.description)

        if m is not None:
            line += " `%s`" % CLEAN_RE.sub("", m.group(1))

        line += " - %s" % DEFAULT_RE.sub(".", param.description)

        lines.append(collapse(line))

    return clean_multiple("\n".join(lines))


def template_return(fn_doc):
    """
    Function returning templated arguments.

    Args:
        fn_doc (dict): a dict with the function documentation parts (returned by get_function).

    Returns:
        string: templated returns.
    """

    line = "*%s*" % fn_doc["returns"].type_name
    line += " - %s" % DEFAULT_RE.sub(".", fn_doc["returns"].description)

    return clean_multiple(collapse(line))
