"""Package configuration."""
import logging.config
from pathlib import Path


def configure_logging() -> None:
    """Configure logging."""
    logging.config.dictConfig(LOGGING)
    log = logging.getLogger(__name__)
    log.debug("Logging is configured.")


API_URL_SHORTEN = "https://da.gd/s"
BASE_REPO_NAME = "impredicative/dagdshort"
DEFAULT_CACHE_SIZE = 256
KNOWN_SHORT_DOMAINS = {"bit.ly", "da.gd", "git.io", "j.mp"}
MAX_ATTEMPTS = 3
MAX_WORKERS = 8
PACKAGE_NAME = Path(__file__).parent.stem
REQUEST_TIMEOUT = 3
TEST_API_ON_INIT = False
TEST_LONG_URL = "https://python.org/"

LOGGING = {  # Ref: https://docs.python.org/3/howto/logging.html#configuring-logging
    "version": 1,
    "formatters": {
        "detailed": {
            "format": "%(asctime)s %(thread)x-%(threadName)s:%(name)s:%(lineno)d:%(funcName)s:%(levelname)s: %(message)s",  # pylint: disable=line-too-long
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {PACKAGE_NAME: {"level": "DEBUG", "handlers": ["console"], "propagate": False}},
}
