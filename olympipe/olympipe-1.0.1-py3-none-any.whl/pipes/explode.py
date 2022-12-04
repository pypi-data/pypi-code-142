from multiprocessing import Queue
from typing import Callable, Iterable, TypeVar
from .generic import GenericPipe

R = TypeVar("R")
S = TypeVar("S")


__version__ = "0.1.0"


class ExplodePipe(GenericPipe[R, S]):
    def __init__(
        self, source: "Queue[R]", task: Callable[[R], Iterable[S]], target: "Queue[S]"
    ):
        super().__init__(source, target)
        self._task = task

    def dispatch_to_next(self, processed: Iterable[S]):  # type: ignore
        for p in processed:
            super().dispatch_to_next(p)
