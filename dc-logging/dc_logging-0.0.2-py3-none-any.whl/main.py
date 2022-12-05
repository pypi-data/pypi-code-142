"""Module to setup logging."""
import logging
from typing import Optional, TypedDict


# pylint: disable=missing-class-docstring
class LoggingConfigDict(TypedDict):
    name: Optional[str]
    level: int
    console_output: bool
    console_level: int
    console_formatter: logging.Formatter
    file_output: bool
    file_name: Optional[str]
    file_mode: str
    file_level: int
    file_formatter: logging.Formatter
    propagate: bool


def get_logging_formatter(*tags) -> logging.Formatter:
    """Get a predefined logging formatter."""
    logging_tags = {
        "time": "%(asctime)s",
        "name": "%(name)-12s",
        "file": "%(filename)s",
        "function": "%(funcName)-12s",
        "level": "%(levelname)-12s",
    }

    if not tags:
        _tags: tuple[str, ...] = ("time", "name", "file", "function", "level")
    else:
        _tags = tags

    tag_strings: list[str] = []

    for tag in _tags:
        tag_strings.append(logging_tags[tag])

    formatter_str = " : ".join(tag_strings) + " :: %(message)s"

    formatter = logging.Formatter(formatter_str)

    return formatter


DEFAULT_CONFIG: LoggingConfigDict = {
    "name": None,
    "level": logging.INFO,
    "console_output": False,
    "console_level": logging.INFO,
    "console_formatter": get_logging_formatter("time", "name", "level"),
    "file_output": False,
    "file_name": None,
    "file_mode": "a",
    "file_level": logging.INFO,
    "file_formatter": get_logging_formatter(),
    "propagate": True,
}


def get_logger(
    name: Optional[str] = DEFAULT_CONFIG["name"],
    level: int = DEFAULT_CONFIG["level"],
    console_output: bool = DEFAULT_CONFIG["console_output"],
    console_level: int = DEFAULT_CONFIG["console_level"],
    console_formatter: logging.Formatter = DEFAULT_CONFIG["console_formatter"],
    file_output: bool = DEFAULT_CONFIG["file_output"],
    file_name: Optional[str] = DEFAULT_CONFIG["file_name"],
    file_mode: str = DEFAULT_CONFIG["file_mode"],
    file_level: int = DEFAULT_CONFIG["file_level"],
    file_formatter: logging.Formatter = DEFAULT_CONFIG["file_formatter"],
    propagate: bool = DEFAULT_CONFIG["propagate"],
) -> logging.Logger:
    """Get a logging.Logger with some predefined configuration.

    The obtained logger has some configuration predefined, making it
    easier to set up logging for small projects or simple scripts.
    """
    # Get logger by name (if it doesn't exists, it is created).
    logger = logging.getLogger(name)

    # Set logger level.
    logger.setLevel(level)

    # Setup console logging if enabled.
    if console_output:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    # Setup file logging as well, but only if there is a filename.
    if file_output and file_name:
        file_handler = logging.FileHandler(
            file_name,
            mode=file_mode,
        )
        file_handler.setLevel(file_level)
        formatter = file_formatter
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.propagate = propagate

    return logger
