# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from urllib.parse import urljoin

from flask import request

from baitoolkit.common import type_util
from baitoolkit.web import web_constant


def get_request_data(method=web_constant.HttpMethod.POST) -> dict:
    """Return dict data from request.data"""
    if method == web_constant.HttpMethod.GET:
        return request.args
    return type_util.json_to_object(request.data)


def get_request_locale() -> str:
    """Return request locale from request cookies."""
    locale = request.cookies.get('locale')
    if locale is not None:
        return locale
    return request.accept_languages.best_match(['en_US', 'zn_CN'])


def get_request_path(full: bool = False) -> str:
    """Return request full path or path."""
    return request.full_path if full else request.path


def get_request_head(head_name: str) -> str:
    """Return head value from request."""
    return request.headers.get(head_name)


def is_ajax_request() -> bool:
    header = request.headers.get('X-Requested-With')
    return header == 'XMLHttpRequest'


def url_join(*args, last_slash=False):
    """Join relative url segments"""
    prefix = 'http://abc/'
    url = prefix if not args[0].startswith('http://') and not args[0].startswith('https://') else args[0]
    url += '' if url.endswith('/') else '/'
    for arg in args:
        if arg is None or arg == '' or arg == prefix:
            continue
        arg += '' if arg.endswith('/') else '/'
        arg = arg[1:] if arg.startswith('/') else arg
        url = urljoin(url, arg)
    if url.startswith(prefix):
        url = url[10:]
    if last_slash:
        return url if url.endswith('/') else url + '/'
    else:
        return url[:-1] if url.endswith('/') else url
