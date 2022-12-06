from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Callable, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


# After https://stackoverflow.com/a/2912455
@dataclass
class keydefaultdict(defaultdict[K, V]):
    default_factory: Optional[Callable[[K], V]] = None  # type: ignore

    def __missing__(self, key):
        if self.default_factory is not None:
            ret = self[key] = self.default_factory(key)
            return ret
        else:
            return super().__missing__(key)
