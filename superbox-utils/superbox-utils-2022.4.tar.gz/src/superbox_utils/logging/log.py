import logging
from collections import OrderedDict
from typing import Dict
from typing import Final

DEFAULT_LOG_FORMAT: Final[str] = "%(levelname)s | %(message)s"
DATETIME_LOG_FORMAT: Final[str] = "%(asctime)s | %(levelname)s | %(message)s"

LOG_LEVEL: Final[Dict[str, int]] = OrderedDict(
    {
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG,
    }
)
