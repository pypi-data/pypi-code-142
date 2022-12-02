"""Magicbag mock init file."""

from .date import random_date, random_datetime
from .decimal import random_decimal
from .int import random_fixed_int
from .time import random_timestamp

__all__ = [
    "random_date",
    "random_datetime",
    "random_timestamp",
    "random_decimal",
    "random_fixed_int",
]
