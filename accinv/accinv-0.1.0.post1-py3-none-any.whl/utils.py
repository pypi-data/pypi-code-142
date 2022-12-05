# SPDX-FileCopyrightText: 2022 Dominik Vilsmeier
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from collections.abc import Container
from functools import reduce, wraps
import re
from typing import Callable, Collection, Iterator, Sequence, Union


class RegexContainer(Container):
    """Instances of this class test membership via :func:`re.fullmatch`.

    Args:
        pattern: Strings are converted to patterns via ``re.compile``.
            Note that this uses the default flags.
    """

    def __init__(self, pattern: Union[str, re.Pattern]):
        self.pattern = re.compile(pattern) if isinstance(pattern, str) else pattern

    def __contains__(self, other):
        return isinstance(other, str) and self.pattern.fullmatch(other)


def chain_function_calls(funcs: Sequence[Callable], unpack: bool = False) -> Callable:
    """Create a wrapper that chains the given functions from left (outermost)
       to right (innermost).

    Args:
        funcs: The functions to be chained.
        unpack: If true, then the return values of functions will be unpacked
            for the next function call (i.e. ``f(*x)`` as opposed to ``f(x)``).

    Returns:
        A wrapper function which will chain the various individual function calls.
    """
    if not funcs:
        raise TypeError('At least one function must be given')

    @wraps(funcs[0])
    def wrapper(*args, **kwargs):
        if unpack:
            def call(result, func):
                return func(*result)
        else:
            def call(result, func):
                return func(result)
        return reduce(
            call,
            funcs[-2::-1],
            funcs[-1](*args, **kwargs),
        )

    return wrapper


def ensuresuffix(string, suffix, /):
    """Append `suffix` if it is not already present in `string`."""
    if not string.endswith(suffix):
        string = f'{string}{suffix}'
    return string


def is_iterator_exhausted(i: Iterator) -> bool:
    """Return ``True`` if the given iterator `i` contains no more elements, and ``False`` otherwise.

    .. note::
       This tries to consume an element from the given iterator via :func:`next`. If there was an
       element to consume, it will not be put back into the iterator (as this is not possible for
       general iterators).
    """
    try:
        next(i)
    except StopIteration:
        return True
    else:
        return False


def lowercase(data: Collection[str]) -> list[str]:
    """Convert all elements of the given collection to lowercase and return the result as a list."""
    return [s.lower() for s in data]
