from asyncio import get_running_loop
from functools import partial
from typing import Any

__all__ = ["run_in_executor"]


async def run_in_executor(function, *args, **kwargs) -> Any:
    """|coro|

    Runs the given function in a sync executor

    Parameters
    ----------
    function
        The sync function to be executed
    *args
        Any positional args to be passed to the function
    **kwargs
        any kwargs to be passed to the function

    Returns
    ----------
    Any
        Whatever the given function returns
    """

    func = partial(function, *args, **kwargs)
    loop = get_running_loop()
    result = loop.run_in_executor(None, func)
    return result
