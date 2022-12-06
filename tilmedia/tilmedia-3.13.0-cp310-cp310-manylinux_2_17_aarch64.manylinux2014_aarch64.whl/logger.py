from logging import Logger
from .core import CLoggerWrapper
_logger_id = 0
c_logger = {}


class LoggerWrapper():
    """
    Wrapper class for the logger. It holds the exceptions, the C wrapper, and the message functions.
    """

    def __init__(self, logger: Logger, message_container: list, format_message, format_error):
        global _logger_id
        _logger_id = _logger_id + 1
        self.c_logger = CLoggerWrapper(_logger_id, format_message, format_error)
        c_logger[_logger_id] = logger
        self.logger = logger
        self.message_container = message_container
        self.__format_message = format_message
        self.__format_error = format_error

    @property
    def format_message(self) -> int:
        return self.c_logger.format_message

    @property
    def format_error(self) -> int:
        return self.c_logger.format_error
