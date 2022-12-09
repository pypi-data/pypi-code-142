import asyncio
import time
from typing import Any, AsyncIterable, Awaitable, Callable, Iterable, Optional, Union

MaybeAwaitable = Union[Awaitable, Callable]
MaybeAwaitableIterable = Union[AsyncIterable, Iterable]

__all__ = ["chunk", "get"]


def _sync_chunk(iterable: Iterable, max_size: int) -> Iterable[list[Any]]:
    final = []
    current = 0

    for item in iterable:
        if current == max_size:
            yield final
            final = []
            current = 0

        final.append(item)
        current += 1

    if final:
        yield final


async def _async_chunk(
    iterable: AsyncIterable, max_size: int
) -> AsyncIterable[list[Any]]:
    final = []
    current = 0

    async for item in iterable:
        if current == max_size:
            yield final
            final = []
            current = 0

        final.append(item)
        current += 1

    if final:
        yield final


def chunk(iterable: MaybeAwaitableIterable, max_size: int) -> MaybeAwaitableIterable:
    """|awaitable|

    Chunks the given iterable into chunks of the given size

    Parameters
    ----------
    iterable: Union[`typing.AsyncIterable`, `typing.Iterable`]
        The iterable you want to chunk
    max_size: `int`
        the max size of the chunks
    """

    if max_size <= 0:
        raise TypeError("max_size must be bigger than 0")

    if hasattr(iterable, "__aiter__"):
        return _async_chunk(iterable, max_size)  # type: ignore
    else:
        return _sync_chunk(iterable, max_size)  # type: ignore


def _sync_get(iterable: Iterable, **attrs: Any) -> Optional[Any]:
    for item in iterable:
        for attr in attrs.keys():
            if hasattr(item, attr):
                if getattr(item, attr) == attrs[attr]:
                    return item

    return None


async def _async_get(iterable: AsyncIterable, **attrs: Any) -> Optional[Any]:
    async for item in iterable:
        for attr in attrs.keys():
            if hasattr(item, attr):
                if getattr(item, attr) == attrs[attr]:
                    return item

    return None


def get(iterable: MaybeAwaitableIterable, /, **attrs: Any) -> Optional[Any]:
    """|awaitable|

    Gets an item from the given iterable with sertain attributes

    Parameters
    ----------
    iterable: Union[`typing.AsyncIterable`, `typing.Iterable`]
        The item you want to be iterated through
    **attrs: `typing.Any`
        The attribute(s) to check for
    """

    if hasattr(iterable, "__aiter__"):
        return _async_get(iterable, **attrs)  # type: ignore
    else:
        return _sync_get(iterable, **attrs)  # type: ignore
