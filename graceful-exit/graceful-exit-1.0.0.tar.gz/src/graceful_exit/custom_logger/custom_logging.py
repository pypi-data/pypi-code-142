from typing import Optional
import structlog
import logging
import os

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()


def reset_log_level() -> None:
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(
            logging._nameToLevel.get(LOGLEVEL, logging.INFO)
        ),
    )


def get_logger(
    name: Optional[str] = None, log_level_override: Optional[str] = None
) -> structlog.stdlib.BoundLogger:
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(
            logging._nameToLevel.get(log_level_override or LOGLEVEL, logging.INFO)
        ),
    )
    logger: structlog.stdlib.BoundLogger = structlog.get_logger(name or __file__)
    return logger
