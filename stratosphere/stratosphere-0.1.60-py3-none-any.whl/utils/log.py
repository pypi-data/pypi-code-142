import logging
import sys
import time

# from logging import debug, info, warning, error, critical
from typing import Callable, Dict, Optional

from colorama import Back, Fore, Style
from stratosphere import config


class ColoredFormatter(logging.Formatter):
    """
    Handles the formatting of coloured logging messages.
    """

    def __init__(self, *args, colors: Optional[Dict[str, str]] = None, **kwargs) -> None:
        """Create a new color formatter.

        Args:
            colors (Optional[Dict[str, str]], optional): . Dictionary of colors and logging levels. Defaults to None.
            args: args to pass to logging.Formatter.
            kwargs: kwargs to pass to logging.Formatter.
        """
        super().__init__(*args, **kwargs)
        self.colors = colors if colors else {}

    def format(self, record) -> str:  # noqa
        """Format the record as coloured text

        Args:
            record (_type_): logging record to format.

        Returns:
            str: Resulting formatted coloured logging message.
        """

        record.color = self.colors.get(record.levelname, "")
        record.reset = Style.RESET_ALL
        return super().format(record)


def init_logging(level: int):
    """Logging intialization.

    Args:
        level (int): logging level to activate.
    """

    formatter = ColoredFormatter(
        "{color}■{reset} {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S",
        colors={
            "DEBUG": Fore.CYAN,
            "INFO": Fore.GREEN,
            "WARNING": Fore.YELLOW,
            "ERROR": Fore.RED,
            "CRITICAL": Fore.RED + Back.WHITE + Style.BRIGHT,
        },
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.handlers[:] = []
    logger.addHandler(handler)
    logger.setLevel(level)


def timeit(f: Callable) -> Callable:
    """Decorator to measure the call execution time.

    Args:
        f (Callable): Function to execute

    Returns:
        Callable: Function with decorator.
    """

    def timed(*args, **kw):
        ts = time.perf_counter()
        result = f(*args, **kw)
        te = time.perf_counter()
        logging.info(f"Elapsed time @{f.__name__}: {(te - ts):.2f}s")
        return result

    return timed


class IgnoredChainedCallLogger:
    """
    This class is designed to catch chained operations, logging that they won't
    be executed, and returning nicely."""

    def __getitem__(self, index):
        """Catching all field requests, logging them.

        Args:
            index (_type_): index to be resolved.

        Returns:
            IgnoredChainedCallLogger: Recursive instance of the same class.
        """
        logging.error(f"Ignoring chained operation: .[{index}]")
        return IgnoredChainedCallLogger()

    def __getattribute__(self, name):
        """Catching all attribute requests, logging them.

        Args:
            name (_type_): name to be resolved.

        Returns:
            IgnoredChainedCallLogger: Recursive instance of the same class.
        """

        if name == "_ipython_canary_method_should_not_exist_":
            # this is handled separately, to handle how ipython is
            # managing the objects at the end of cells.
            raise AttributeError()

        if name in ["_repr_html_", "__str__"]:
            # empty output.

            return lambda: ""

        if name not in ["__class__", "_ipython_display_"]:
            # in case a new chained operation is requested, log it.
            logging.error(f"Ignoring chained operation: .{name}(...)")

        def newfunc(*args, **kwargs):
            # recursive instantiation of IgnoredChainedCallLogger
            return IgnoredChainedCallLogger()

        return newfunc

    @staticmethod
    def _repr_html_() -> str:
        """HTML representation, empty: we already produce the logging output.

        Returns:
            str: Empty string.
        """
        return ""


def fatal(*args, **kwargs):
    """Handle fatal situations, logging them and handling over the execution
    to IgnoredChainedCallLogger to log chained operations.

    Returns:
        IgnoredChainedCallLogger: Logger of chained opeartions.
    """

    logging.error(*args, **kwargs)
    return IgnoredChainedCallLogger()


def default_exception_handler(func: Callable) -> Callable:
    """Decorator Handle exceptions occurring in chained function calls.
    e.g., (a().b().c())
    It does not always work with subscripts, e.g., x[123].

    Args:
        func (Callable): Function to decorate.

    Returns:
        Callable: Decorated function.
    """

    def inner_function(*args, **kwargs):
        if not config.log.catch_exceptions:
            return func(*args, **kwargs)
        else:
            try:
                return func(*args, **kwargs)
            except (KeyboardInterrupt, TypeError, Exception) as e:
                if type(e) == KeyboardInterrupt:
                    return fatal("Keyboard interrupt.")
                else:
                    return fatal(f"Exception {e.__class__.__name__} at .{func.__name__}(...): {e}")

    return inner_function
