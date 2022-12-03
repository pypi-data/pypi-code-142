# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from baitoolkit.common.constant import ConstBase

SUCCESS_CODE = 'OK'
SUCCESS_MESSAGE = 'SUCCESS'
UNKNOWN_ERROR_CODE = 'UNKNOWN_ERROR'


class HttpStatus(ConstBase):
    HTTP_SUCCESS = 200
    HTTP_REDIRECT = 301
    HTTP_REDIRECT_AJAX = 311
    HTTP_BAD_REQUEST = 400
    HTTP_NOT_FOUND = 404
    HTTP_FORBIDDEN = 403
    HTTP_NO_AUTHORIZATION = 401
    HTTP_INTERVAL_ERROR = 500


class HttpMethod(ConstBase):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class HttpHeader(ConstBase):
    CONTENT_TYPE = 'Content-Type'


class HttpContentType(ConstBase):
    JSON = 'application/json'
