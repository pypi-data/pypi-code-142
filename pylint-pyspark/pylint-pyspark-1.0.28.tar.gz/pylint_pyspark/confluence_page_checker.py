from __future__ import annotations

import tokenize

import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker
from pylint.checkers import utils

from astroid import nodes
from typing import Optional

class ConfluencePageChecker(BaseChecker):
    __implements__ = IRawChecker,

    name = 'missing-documentation-link'
    priority = -1
    msgs = {
        'E9999': (
            'Module docstring must link to a *.atlassian.net page.',
            'missing-documentation-link',
            'This module is missing a link to a Confluence documentation page. Each module should have a corresponding documentation page.'
        ),
    }

    def __init__(self, linter: Optional["PyLinter"] = None) -> None:
        super(ConfluencePageChecker, self).__init__(linter)
        self._function_stack = []


    def visit_module(self, node: nodes.Module) -> None:
        self._check_documentation_link(node)

    def _infer_dunder_doc_attribute(node: nodes.Module) -> str | None:
        # Try to see if we have a `__doc__` attribute.
        try:
            docstring = node["__doc__"]
        except KeyError:
            return None

        docstring = utils.safe_infer(docstring)
        if not docstring:
            return None
        if not isinstance(docstring, nodes.Const):
            return None
        return str(docstring.value)

    def _contains_documentation_link(self, node: nodes.Module, report_missing: bool = True) -> None:
        docstring = node.doc_node.value if node.doc_node else None
        if docstring is None:
            docstring = self._infer_dunder_doc_attribute(node)
        if docstring is None:
            if not report_missing:
                return
        elif "atlassian.net" not in docstring:
            self.add_message('missing-documentation-link', node=node)