from __future__ import annotations

from typing import Optional, TypeVar

T = TypeVar("T")


def none_throws(x: Optional[T], errmsg="Unexpected None") -> T:
    if x is None:
        raise ValueError(errmsg)
    return x
