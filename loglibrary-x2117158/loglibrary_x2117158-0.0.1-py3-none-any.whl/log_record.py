from .level import Level
from datetime import datetime


class LogRecord:
    __next_number = 0

    def __init__(self, level: Level, message: str, logger_name: str, error=None, stack_trace=None, object=None) -> None:
        self.level = level
        self.message = message
        self.logger_name = logger_name
        self.error = error
        self.stack_trace = stack_trace
        self.object = object
        self.time = datetime.now()
        self.sequenceNumber = LogRecord.__next_number
        LogRecord.__next_number += 1

    def __str__(self):
        return f'[{self.level.name}] {self.logger_name}: {self.message}'
