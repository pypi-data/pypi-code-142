# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from baitoolkit.exception.errors import RequiredError, TypeInvalidError, ChoiceError, CompareError, LengthError, \
    RangeError, InvalidError


def assert_required(value, label):
    """
        check if value is None or empty str.
    """
    if value is None:
        raise RequiredError(label)
    if type(value) == str and len(value.strip()) == 0:
        raise RequiredError(label)
    if isinstance(value, list) and len(value) == 0:
        raise RequiredError(label)
    if isinstance(value, dict) and len(value) == 0:
        raise RequiredError(label)
    return True


def assert_type(value, expected_type, label):
    """
    @param any value:
    @param int|float|bool|list|dict|str|types.GeneratorType|types.FunctionType expected_type:
    @param str label:
    """
    if value is not None and type(value) != expected_type:
        raise TypeInvalidError(str(expected_type), label)
    return True


def assert_in(value, choices, label):
    if value is not None and value not in choices:
        raise ChoiceError(label, choices)
    return True


def assert_equal(value1, value2, label1, label2):
    if value1 != value2:
        raise CompareError(label1, "=", label2, '')


def assert_not_equal(value1, value2, label1, label2):
    if value1 == value2:
        raise CompareError(label1, "!=", label2, '')


def assert_zero_length(value, label):
    if type(value) == list or type(value) == dict:
        if value is None or len(value) == 0:
            raise LengthError(label, 0, 'infinity')


def assert_range(value, minimum, maximum, label):
    if value < minimum or value > maximum:
        raise RangeError(label, minimum, maximum, data=value)


def assert_page(page, per_page):
    assert_required(page, 'Page')
    assert_required(per_page, 'Per Page')
    assert_type(page, int, 'Page')
    assert_type(per_page, int, 'Per Page')


def assert_http_url(url, label):
    assert_type(url, str, label)
    url = url.lower()
    if not url.startswith('http://') and not url.startswith('https://'):
        raise InvalidError(label, data=url)
