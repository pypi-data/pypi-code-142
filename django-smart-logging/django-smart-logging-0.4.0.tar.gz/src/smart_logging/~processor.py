import json
import logging.config
from json import JSONDecodeError

from django.conf import settings
from smart_logging.signals import logger_changed

logger = logging.getLogger(__name__)

"""
message = {logger: {info}

"""


class Processor:
    def __init__(self):
        pass

    def process(self, message: dict) -> None:
        try:
            payload = json.loads(message["data"])
            cfg = self.get_config(payload)
            logging.config.dictConfig(cfg)
            logger.info(f"logging configuration updated {cfg}")
        except (JSONDecodeError, TypeError) as e:
            logger.exception(e)

    def get_config(self, payload: dict) -> dict:
        try:
            action = payload["action"]
            config = payload.get("data", {})
            config.setdefault("version", 1)
            if action == "reset":
                return settings.LOGGING
            elif action == "patch":
                config["incremental"] = True
                return config
            elif action == "get":
                target = config.get("target", "logggers")
                log = logging.root.manager.loggerDict[target]
                return {
                    "handlers": log.handlers,
                    "level": logging._levelToName[log.getEffectiveLevel()],
                    "propagate": log.propagate,
                }
            elif action == "set":
                config = payload["data"]
                config["incremental"] = False
                config.setdefault("disable_existing_loggers", False)
                return config
            else:
                raise ValueError("Invalid action")
        except Exception as e:
            logger.exception(e)
