# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import re

import chardet
from lxml import etree


def decode_html(html, encodings=['utf-8', 'gbk']):
    """
        Decode the html with the encoding defined in html by <meta charset>.
        :param html:str: html string
        :param encodings:str: if decoding is wrong through <meta charset> try to decode by these encodings.
        :rtype str: the html being converted.
    """

    def decode(html1, encoding1):
        try:
            result1 = html1.decode(encoding1)
            return result1
        except UnicodeDecodeError:
            return None

    charset = re.compile('charset="?([A-Za-z0-9-]+)"?>')
    encoding = charset.search(str(html))
    if encoding is not None:
        encoding = encoding.group(1)
    encoding = 'utf-8' if encoding is None else encoding
    result = decode(html, encoding)
    if result is None:
        encodings.remove(encoding.lower())
        for code in encodings:
            result = decode(html, code)
            if result is not None:
                return result
            else:
                continue
    code = chardet.detect(html)['encoding']
    result = html.decode(code, errors='ignore')
    return result


def get_node_html(node, encoding='utf-8'):
    """
    Get html from etree.Element or str.
    :param node:str|etree.Element:
    :param encoding:str: the encoding of node string
    :return: html:str
    """
    if node is None:
        return ""
    if (str(type(node))).lower().find('str') > 0:
        return str(node)
    else:
        return etree.tostring(node).decode(encoding)


def get_node_text(node, sep=' '):
    """
    Get all texts from etree.Element and its child nodes.
    :param node:etree.Element
    :param sep:str: the separator of multiple node texts. if sep is null, means just to get current node text.
    :return: text:str
    """

    def __get(nod, arr):
        if hasattr(nod, 'tag') and isinstance(nod.tag, str) and node.tag.lower() not in ['script', 'style', 'comment']:
            t = nod.text
            if t is not None:
                t = t.strip()
                if t != '':
                    arr.append(t)
            t = nod.tail
            if t is not None:
                t = t.strip()
                if t != '':
                    arr.append(t)
            for sub in node.iterchildren():
                __get(sub, arr)

    if node is None:
        return ""
    texts = []
    __get(node, texts)
    return sep.join(texts)
