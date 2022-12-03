# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import codecs
import os
import datetime

from baitoolkit.common import type_util
from baitoolkit.common.constant import ConstBase

from baitoolkit.exception.errors import CompareError, LengthError, InternalError, IllegalWordError, UniqueError, \
    RangeError, \
    InvalidError, RequiredError, ChoiceError, TypeInvalidError


class Validator(object):

    def validate(self, value, label, **kwargs):
        """To be override by sub-class"""
        raise NotImplementedError("Validator.validate")


illegal_words = list()


class IllegalValidator(Validator):

    def __init__(self, replace=False, chars="***"):
        super(IllegalValidator, self).__init__()
        self.__replace = replace
        self.__chars = chars
        global illegal_words
        if type_util.str_is_blank(illegal_words):
            illegal_words = self.__load_illegal_words()

    def validate(self, value, label, **kwargs):
        global illegal_words
        il_words = illegal_words
        if type_util.str_is_blank(il_words):
            raise InternalError("the illegal words are not loaded.")
        if not type_util.str_is_blank(il_words) and isinstance(value, str) and len(value) > 0:
            for il_word in il_words:
                if il_word in value:
                    if self.__replace:
                        value = value.replace(il_word, self.__chars)
                    else:
                        raise IllegalWordError(label, il_word)
        return value

    @staticmethod
    def __load_illegal_words():
        results = list()
        iw_path = os.path.join(os.path.dirname(__file__), "illegalwords.txt")
        if os.path.exists(iw_path):
            with codecs.open(iw_path, encoding='utf-8') as iw_file:
                il_words = iw_file.readlines()
                for il_word in il_words:
                    if len(il_word) < 1:
                        continue
                    if il_word.endswith('\n'):
                        il_word = il_word[0:-1]
                    if il_word.endswith('\r'):
                        il_word = il_word[0:-1]
                    if il_word.endswith(';'):
                        il_word = il_word[0:-1]
                    if len(il_word) > 0:
                        results.append(il_word)
        else:
            raise InternalError("{} is not found.".format(iw_path))
        return results


class UniqueValidator(Validator):

    def __init__(self, unique_column_names, unique_check_func):
        """kwargs is the arguments of unique_check_func."""
        super(UniqueValidator, self).__init__()
        self._unique_column_names = unique_column_names
        self._unique_check_func = unique_check_func

    def validate(self, value, label, **kwargs):
        """Value is dict or normal type."""
        if not self._unique_check_func(value, label, unique_column_names=self._unique_column_names, **kwargs):
            raise UniqueError(label, value)
        return value


class LengthValidator(Validator):

    def __init__(self, min_length=0, max_length=100000):
        super(LengthValidator, self).__init__()
        self._min_length = min_length
        self._max_length = max_length

    @property
    def min_length(self):
        return self._min_length

    @property
    def max_length(self):
        return self._max_length

    def validate(self, value, label, **kwargs):
        if value is None:
            return value
        value = str(value)
        length = len(value)
        if length > self._max_length or length < self._min_length:
            raise LengthError(label, self._min_length, self._max_length)
        return value


class RangeValidator(Validator):
    def __init__(self, minimum=None, maximum=None):
        super(RangeValidator, self).__init__()
        self._minimum = minimum
        self._maximum = maximum

    @property
    def minimum(self):
        return self._minimum

    @property
    def maximum(self):
        return self._maximum

    def validate(self, value, label, **kwargs):
        if value is None:
            return value

        if type(value) is str or type(value) is int or type(value) is float:
            if (self._minimum is not None and value < self._minimum) or (
                    self._maximum is not None and value > self._maximum):
                raise RangeError(label, self._minimum, self._maximum)
        elif type(value) is datetime.datetime or type(value) is datetime.date:
            if (self._minimum is not None and value < self._minimum) or (
                    self._maximum is not None and value > self._maximum):
                raise RangeError(label, self._minimum, self._maximum)
        else:
            raise InternalError("RangeValidator doesn't support type %s" % type(value))
        return value


class CompareValidator(Validator):
    _OPERATORS = ('=', '>=', '<=', ">", "<")

    def __init__(self, operator, limit):
        super(CompareValidator, self).__init__()
        if operator is None or operator not in self._OPERATORS:
            raise InvalidError("operator %s is not in %r" % (operator, self._OPERATORS))
        self._operator = operator
        self._limit = limit

    @property
    def operator(self):
        return self._operator

    @property
    def limit(self):
        return self._limit

    def validate(self, value, label, **kwargs):
        if value is None:
            return value

        lim = self._limit

        if self._operator == '=' and value != lim:
            raise CompareError(label, self._operator, label, lim)
        elif self._operator == '>=' and value < lim:
            raise CompareError(label, self._operator, label, lim)
        elif self._operator == '<=' and value > lim:
            raise CompareError(label, self._operator, label, lim)
        elif self._operator == '>' and value <= lim:
            raise CompareError(label, self._operator, label, lim)
        elif self._operator == '<' and value >= lim:
            raise CompareError(label, self._operator, label, lim)
        return value


class RequiredValidator(Validator):

    def __init__(self):
        super(RequiredValidator, self).__init__()

    def validate(self, value, label, **kwargs):
        if value is None:
            raise RequiredError(label, data=value)
        if isinstance(value, str) and len(value.strip()) == 0:
            raise RequiredError(label, data=value)
        return value


class ChoiceValidator(Validator):

    def __init__(self, choices=None):
        super(ChoiceValidator, self).__init__()
        self._choices = choices

    @property
    def choices(self):
        return self._choices

    def validate(self, value, label, **kwargs):
        if value is None:
            return value
        choices = self._choices
        if issubclass(choices.__class__, ConstBase):
            choices = self._choices.keys()
        if value not in choices:
            raise ChoiceError(label, choices, data=value)
        return value


class TypeValidator(Validator):

    def __init__(self, expected_type):
        super(TypeValidator, self).__init__()
        self._expected_type = expected_type

    @property
    def expected_type(self):
        return self._expected_type

    def validate(self, value, label, **kwargs):
        if value is not None and type(value) != self._expected_type:
            raise TypeInvalidError(str(self._expected_type), label)
        return value
