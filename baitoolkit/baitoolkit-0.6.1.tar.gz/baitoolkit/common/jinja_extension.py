# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import re

from jinja2 import nodes
from jinja2.ext import Extension


class SpacelessExtension(Extension):
    """Removes whitespace between HTML tags at compile time, including tab and newline characters.
    It does not remove whitespace between jinja2 tags or variables. Neither does it remove whitespace between tags
    and their text content.
    """

    tags = set(['spaceless'])

    def parse(self, parser):
        line_no = next(parser.stream).lineno
        body = parser.parse_statements(['name:endspaceless'], drop_needle=True)
        return nodes.CallBlock(
            self.call_method('_strip_spaces', [], [], None, None),
            [], [], body,
        ).set_lineno(line_no)

    @staticmethod
    def _strip_spaces(caller=None):
        return re.sub(r'>\s+<', '><', caller().strip())


spaceless = SpacelessExtension


