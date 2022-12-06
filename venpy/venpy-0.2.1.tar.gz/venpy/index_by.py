from __future__ import annotations
from typing import (
    Iterable,
    TypeVar,
    Callable,
    Hashable,
    Union,
    Optional,
    cast,
    Literal,
    overload,
)
from collections import defaultdict


_T = TypeVar("_T")
_K = TypeVar("_K", bound=Hashable)


# These @overload definitions connect the value of `connection` to the return type
#
# https://mypy.readthedocs.io/en/stable/more_types.html#function-overloading
#
# Each definition fixes one literal value of `collection` (with no default
# value) to one return type
#
# They have to be keyword args because of the default value on `by`
#


@overload
def index_by(
    items: Iterable[_T],
    *,
    by: Optional[Callable[[_T], _K]] = ...,
) -> defaultdict[_K, _T]:
    ...


@overload
def index_by(
    items: Iterable[_T],
    *,
    by: Optional[Callable[[_T], _K]] = ...,
    collection: Literal[None],
) -> defaultdict[_K, _T]:
    ...


@overload
def index_by(
    items: Iterable[_T],
    *,
    by: Optional[Callable[[_T], _K]] = ...,
    collection: Literal["set"],
) -> defaultdict[_K, set[_T]]:
    ...


@overload
def index_by(
    items: Iterable[_T],
    *,
    by: Optional[Callable[[_T], _K]] = ...,
    collection: Literal["list"],
) -> defaultdict[_K, list[_T]]:
    ...


def index_by(
    items: Iterable[_T],
    *,
    by: Optional[Callable[[_T], _K]] = None,
    collection: Optional[Literal["set", "list"]] = None,
) -> Union[defaultdict[_K, _T], defaultdict[_K, set[_T]], defaultdict[_K, list[_T]]]:

    if collection is None:
        index = defaultdict()  # type: ignore
        adder = lambda k, x: index.update({k: x})
    elif collection == "list":
        index = defaultdict(list)
        adder = lambda k, x: cast(list[_T], index[k]).append(x)
    elif collection == "set":
        index = defaultdict(set)
        adder = lambda k, x: cast(set[_T], index[k]).add(x)
    else:
        raise RuntimeError("invalid collection")

    for i in items:
        adder(by(i) if by else i, i)

    return index
