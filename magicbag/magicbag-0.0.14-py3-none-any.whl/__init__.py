"""Magicbag init file."""

from .check import prefix_check
from .mock.date import random_date, random_datetime
from .mock.decimal import random_decimal
from .mock.time import random_timestamp

__all__ = ["prefix_check",
           "random_date",
           "random_datetime",
           "random_timestamp",
           "random_decimal"]

from . import _version
__version__ = _version.get_versions()['version']
