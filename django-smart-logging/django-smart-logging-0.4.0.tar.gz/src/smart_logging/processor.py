import json
import logging.config
from json import JSONDecodeError

from smart_logging.manager import manager
from smart_logging.utils import get_signature

logger = logging.getLogger(__name__)


class Processor:
    def process(self, message: dict) -> None:
        try:
            payload = json.loads(message["data"])
            if payload["__sender__"] != get_signature():
                config = payload["config"]
                logger_name = config.get("logger", None)
                if logger_name in manager.loggers:
                    manager.configure_logger(logger_name, **config)
                logger.info(f"logging configuration updated {payload}")
                return payload
        except (JSONDecodeError, TypeError) as e:
            logger.exception(e)
            raise
