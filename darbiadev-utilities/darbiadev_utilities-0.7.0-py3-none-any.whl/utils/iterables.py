"""Assorted utility functions"""

from __future__ import annotations

from collections.abc import Generator, Iterable
from itertools import islice
from typing import TypeVar

T = TypeVar("T")


def enumerate2(
    iterable: Iterable[T],
    start: int = 0,
    step: int = 1,
) -> Generator[tuple[int, T], None, None]:
    """
    Yield items from an iterable with a custom index.

    Yields
    ------
    index, item
        The next item and the next number per step

    See Also
    --------
    https://stackoverflow.com/a/24290026/8160821
    """
    for item in iterable:
        yield start, item
        start += step


def chunks(
    iterable: Iterable[T],
    size: int,
) -> Generator[tuple[T, ...], None, None]:
    """
    Yield successive n-sized chunks from iterable.

    Yields
    ------
    chunk
        An n-sized chunk of the iterable

    See Also
    --------
    https://stackoverflow.com/a/312464/8160821
    """
    it = iter(iterable)
    while chunk := tuple(islice(it, size)):
        yield chunk


def flatten(
    iterable: Iterable[Iterable[T]],
) -> Iterable[T]:
    """
    Flattens a list of lists into a single list.

    Parameters
    ----------
    iterable
        The nested lists to flatten.

    Returns
    -------
    flattend_iterable
        The flattened iterable.

    Examples
    --------
    >>> flatten([['a'],['b']])
    ['a', 'b']

    See Also
    --------
    https://stackoverflow.com/a/952952
    """
    return [item for sub_iter in iterable for item in sub_iter]
