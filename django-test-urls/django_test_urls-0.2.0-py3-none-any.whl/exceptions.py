#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" Contains exceptions that may be raised by this package.

:copyright: (c) 2022 by Alan Verresen
:license: MIT, see LICENSE for more details.
"""


class DjangoTestUtilsException(Exception):
    """ Base exception for all exceptions that may be raised by this package.
    """
    pass


class InvalidArgumentType(DjangoTestUtilsException):
    """ Used to signal that an argument with an unexpected type was passed.
    """
    pass
