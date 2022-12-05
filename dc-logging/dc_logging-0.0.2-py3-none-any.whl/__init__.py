"""DC Logging Library.

DC Logging is a tiny library to quickly set up loggers with a default
configuration. It's useful to avoid re-writting the code to set up
loggers in many different small projects. For bigger projects it's
better to set up custom logging setup."""

from dc_logging.main import get_logger

__version__ = "0.0.2"
