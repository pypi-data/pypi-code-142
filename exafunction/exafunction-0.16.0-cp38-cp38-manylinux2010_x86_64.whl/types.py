# Copyright Exafunction, Inc.
"""Defines common Exafunction types."""

# pylint: disable=useless-import-alias

import abc
import enum
from typing import Any, Dict, Tuple, Union

import numpy as np
from typing_extensions import TypedDict as TypedDict  # pylint: disable=unused-import

from exa.py_value.value import Value as Value

Picklable = object
ValueLike = Union[Value, np.ndarray, bytes, Picklable]
ValueDict = Dict[str, Value]
ValueTuple = Tuple[Value, ...]
MethodOutput = Union[ValueDict, ValueTuple, Value]


def get(method_output: MethodOutput) -> Any:
    """Get the underlying value from a MethodOutput."""
    if isinstance(method_output, dict):
        return {k: v.get() for k, v in method_output.items()}
    if isinstance(method_output, tuple):
        return tuple(v.get() for v in method_output)
    if not isinstance(method_output, Value):
        raise TypeError(f"Invalid method outptu type {type(method_output)}")
    return method_output.get()


class ExaMethodOutputType(enum.Enum):
    """The type of an Exafunction PyModule method output."""

    VALUE = enum.auto()
    VALUE_TUPLE = enum.auto()
    VALUE_DICT = enum.auto()


class ExportDecoratorBase(abc.ABC):
    """Sentinel base class to identify export decorated functions."""

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class BaseModuleBase(abc.ABC):
    """Abstract base class for Exafunction PyModules."""


class AutoModuleBase(abc.ABC):
    """Abstract base class for Exafunction Auto PyModules."""
