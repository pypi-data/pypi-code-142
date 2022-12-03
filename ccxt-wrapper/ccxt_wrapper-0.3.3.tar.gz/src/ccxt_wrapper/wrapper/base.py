import functools
import warnings
from typing import Any, Callable, Generic, TypeVar

from ccxt.base.exchange import Exchange
from strenum import StrEnum

_Exchange = TypeVar("_Exchange", bound=Exchange)


class Verbosity(StrEnum):
    Error = "error"
    Ignore = "ignore"
    Always = "always"
    Once = "once"


_WrappedFn = TypeVar("_WrappedFn", bound=Callable[..., Any])


def _set_verbosity(action: Verbosity) -> Callable[[_WrappedFn], _WrappedFn]:
    """Set the verbosity level for the exchange wrapper."""

    def inner(func: _WrappedFn) -> _WrappedFn:
        @functools.wraps(func)
        def most_inner(*args: Any, **kwargs: Any) -> Any:
            with warnings.catch_warnings():
                warnings.simplefilter(action=action)
                result = func(*args, **kwargs)
            return result

        return most_inner  # type: ignore

    return inner


class CCXTWrapperBase(Generic[_Exchange]):
    _ex: _Exchange

    def __init__(
        self, exchange: _Exchange, verbose: Verbosity = Verbosity.Ignore  # type: ignore
    ) -> None:
        self._ex = exchange
        """
        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if name.startswith("_"):
                continue
            setattr(self, name, _set_verbosity(verbose)(method))
        """

    async def __aenter__(self) -> "CCXTWrapperBase[_Exchange]":
        await self._ex.__aenter__()
        await self._ex.load_markets(reload=False)
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self._ex.__aexit__(exc_type, exc_val, exc_tb)

    @property
    def exchange(self) -> _Exchange:
        return self._ex
