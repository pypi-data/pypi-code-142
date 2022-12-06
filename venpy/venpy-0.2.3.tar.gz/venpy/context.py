from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

from typing_extensions import Self


class ContextMixin:
    """Mixin to create a class contextmanager in the form of a
    generator-contextmanager.

    The main utility of this class is to avoid thinking about __enter__() and
    __exit__() separately, and one can implement their contextmanager by
    overriding __context__()

    This allows usage like

    with Klass() as c:
         ...

    """

    def __enter__(self):
        self.__context = self.__context__()
        return self.__context.__enter__()

    def __exit__(self, *args):
        return self.__context.__exit__(*args)

    @contextmanager
    def __context__(self) -> Generator[Self, None, None]:
        yield self
