import inspect
import signal
from types import TracebackType
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Tuple,
)
from graceful_exit.custom_logger.custom_logging import get_logger
from graceful_exit.exeptions.signal_exceptions import SigInt, SigTerm
from graceful_exit.typings.generics import App

logger = get_logger("GracefulExit")


class GracefulExit(Generic[App], object):
    def __init__(
        self,
        app: App,
        exit_handler: Optional[Callable[..., None | Awaitable[None]]] = None,
        exit_signals: List[signal.Signals] = [signal.SIGTERM, signal.SIGINT],
    ):
        self._app = app
        self._exit_handler = exit_handler
        self.__register_exit_signals(exit_signals)

    def __register_exit_signals(self, exit_signals: List[signal.Signals]) -> None:
        """
        Registers exit signals as custom exceptions to enable context manager clean up
        """
        for exit_signal in exit_signals:
            signal.signal(
                exit_signal,
                lambda *args, **kwargs: self.__term_cb(*args, **kwargs),
            )

    @staticmethod
    def __term_cb(
        signal_type: int, *args: Tuple[Any], **kwargs: Dict[str, Any]
    ) -> None:
        """
        Callback function catching SIGINT and SIGTERM.
        Raises signals as custom exceptions
        """
        if signal_type == signal.SIGTERM:
            raise SigTerm(1)
        elif signal_type == signal.SIGINT:
            raise SigInt(1)
        else:
            raise SystemExit(1)

    async def __aenter__(self) -> App:
        logger.debug("__aenter__")
        return self._app

    async def __aexit__(
        self, type: type[BaseException], value: BaseException, traceback: TracebackType
    ) -> bool:
        logger.debug("__aexit__")
        if self._exit_handler and inspect.iscoroutinefunction(self._exit_handler):
            await self._exit_handler(type, value, traceback)
        return True

    def __enter__(self) -> App:
        logger.debug("__enter__")
        return self._app

    def __exit__(
        self, type: type[BaseException], value: BaseException, traceback: TracebackType
    ) -> bool:
        logger.debug("__exit__")
        if self._exit_handler and not inspect.iscoroutinefunction(self._exit_handler):
            self._exit_handler(type, value, traceback)
        return True
