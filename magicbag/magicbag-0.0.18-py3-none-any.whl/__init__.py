"""Magicbag init file."""

from .check import prefix_check
from .mock import (
    random_date,
    random_datetime,
    random_decimal,
    random_fixed_int,
    random_timestamp,
)

__all__ = [
    "prefix_check",
    "random_date",
    "random_datetime",
    "random_timestamp",
    "random_decimal",
    "random_fixed_int",
]

from . import _version

__version__ = _version.get_versions()["version"]
