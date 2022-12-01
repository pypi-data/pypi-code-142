import logging
import os
import sys
from datetime import datetime
from pathlib import Path

LOG_PATH = Path(os.path.dirname(os.path.realpath(__file__))).parent / "logs"


class TestLogger(logging.Logger):
    def __init__(self, *, folder='new', log_name='log', stdout=False):
        super().__init__("logger")
        if stdout:
            self.addHandler(_StdOutHHandler())
        self.addHandler(TxtFileHandler(folder=folder, log_name=log_name))
        self.handled_element_exceptions: list[dict[
                                              str:str,
                                              str:str,
                                              str:list[str],
                                              str:bool]] = []


class _StdOutHHandler(logging.StreamHandler):
    def __init__(self):
        self.stream = sys.stdout
        self.level = logging.DEBUG
        super().__init__(self.stream)
        self.setFormatter(StdOutFormatter())


class TxtFileHandler(logging.FileHandler):
    def __init__(self, *, folder='new', log_name):
        self.filename = f'{log_name}_{datetime.now().strftime("%d-%m-%y__%H-%M-%S")}.log'
        (LOG_PATH / folder).mkdir(exist_ok=True, parents=True)
        super().__init__(str(LOG_PATH / folder / self.filename))
        self.setFormatter(TxtFileFormatter())


class TxtFileFormatter(logging.Formatter):
    def __init__(self):
        self.fmt = '%(asctime)s | %(levelname)8s | %(message)s'
        super().__init__(self.fmt)


class StdOutFormatter(logging.Formatter):
    """Logging colored formatter for stdout"""
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self):
        super().__init__()
        self.fmt = '%(asctime)s | %(levelname)8s | %(message)s'
        self.formats = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


if __name__ == '__main__':
    logger = TestLogger(folder='test-logger', stdout=True)
    logger.info('test')
    logger.debug('test')
    logger.warning('test')
    logger.error('test')
    logger.fatal('test')
