from __future__ import annotations

import json
import logging
from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, Iterator, Optional

from suppy.utils import context
from suppy.utils.handlers import JsonRotatingFileHandler

if TYPE_CHECKING:
    from suppy import Node

logger = logging.getLogger("metrics")
# Ensure anything logged to this logger won't propagate to the root logger
logger.propagate = False


DEFAULT_FILENAME = "suppy"


def get_default_filename() -> str:
    """Return the default filename"""
    return DEFAULT_FILENAME


class MetricsExporter:
    """MetricsExporter

    Clears any handlers on the "metrics" logger on init
    while also keeping track of explicitly added handlers

    This allows for finding the output files of the handlers added by this class
    without interference of other processes adding handlers to the same logger
    """

    handlers: list[logging.Handler]
    logger: logging.Logger

    def __init__(
        self,
        filename: PathLike[str] | str | None = None,
        stream: IO[str] | None = None,
        level: int = logging.INFO,
        max_bytes: int = 0,
    ):
        self.handlers = []

        # Clear any existing log handlers
        if logger.hasHandlers():
            for hndlr in list(logger.handlers):
                logger.removeHandler(hndlr)

        # Build the default file handler
        file = Path(filename if filename else get_default_filename())
        if file.is_dir():
            file = file / get_default_filename()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        file = file.with_stem(f"{file.stem}_{timestamp}")
        file.parent.mkdir(parents=True, exist_ok=True)
        handler = JsonRotatingFileHandler(file, encoding="utf-8", max_bytes=max_bytes)

        # Format the log as json for easy parsing
        # The formatter expects the LogRecord to be created with extras:
        # node, event, quantity, period
        formatter = logging.Formatter(
            "{"
            '"timestamp": "%(asctime)s", '
            '"level": "%(levelname)s", '
            '"period": "%(period)s", '
            '"loop": "%(loop)s", '
            '"node": "%(node)s", '
            '"sku": "%(sku)s", '
            '"event": "%(event)s", '
            '"metric": "%(metric)s", '
            '"quantity": "%(quantity)s", '
            '"message": %(message)s'
            "}"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.handlers.append(handler)

        if stream is not None:
            streamhandler = logging.StreamHandler(stream)
            streamhandler.setFormatter(formatter)
            logger.addHandler(streamhandler)
            self.handlers.append(streamhandler)

        logger.setLevel(level)

        self.logger = logger

    def stop_metrics(self) -> None:
        """Flush the collected metrics and remove the handler

        Ensures the metrics are flushed to disk and the file is closed
        """
        # by default only a single handler should be available
        # but if someone tapped into the logger, we'll close all handlers
        for handler in self.handlers:
            handler.flush()
            handler.close()

    @property
    def output(self) -> Iterator[PathLike[str]]:
        """Return the Path for every metrics output file"""
        for hndlr in self.filehandlers:
            yield from hndlr.files

    @property
    def filehandlers(self) -> Iterator[JsonRotatingFileHandler]:
        """Return any FileHandler instance for this exporter"""
        for hndlr in self.handlers:
            if isinstance(hndlr, JsonRotatingFileHandler):
                yield hndlr


def setup_metrics(
    filename: PathLike[str] | str | None = None,
    level: int = logging.INFO,
    stream: Optional[IO[str]] = None,
    max_bytes: int = 0,
) -> MetricsExporter:
    """Setup the metrics

    Arguments:
        filename: if provided output the metrics to this file with the current timestamp appended.
            will create a file in the current working directory by default
            if filename points to an existing directory
            the output will be written there with the default filename
        level: log level to set for the metrics logger
            by default all metrics are logged on level INFO, setting this to a higher
            value will disable the metrics logs
        stream: If set adds an additional StreamHandler writing metrics to the provided stream.
        **kwargs: Additional arguments passed to the RotatingFileHandler

    Returns:
        Path to the logfile
    """
    return MetricsExporter(
        filename=filename, stream=stream, level=level, max_bytes=max_bytes
    )


def log_event(  # pylint: disable=too-many-arguments
    event: str,
    metric: str,
    quantity: float | None = None,
    message: Any = "",
    sku: Node | str | None = None,
    node: Node | None = None,
    level: int | None = logging.INFO,
) -> None:
    """Add an event to the metrics

    Arguments:
        node: Node emitting the event
        sku: the sku of the event, defaults to `node.id`
        event: the event triggering the log
        metric: the name of what is being measured
        quantity: quantity of the metric
        message: optional message to add to the metric
        level: optional log level to set for the metric, default: logging.INFO
    """
    from suppy import Node

    node = context.node.get() if node is None else node
    sku = node if sku is None else sku
    level = logging.INFO if level is None else level
    extra = {
        "node": node.id,
        "sku": sku.id if isinstance(sku, Node) else sku,
        "event": event,
        "metric": metric,
        "quantity": quantity,
        "period": context.period.get(),
        "loop": context.loop.get(),
    }
    logger.log(level, json.dumps(message), extra=extra)
