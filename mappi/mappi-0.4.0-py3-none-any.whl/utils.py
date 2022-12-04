import logging
from pathlib import Path

import yaml

from mappi import config, schema

logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger(__package__)


def read_configuration(filename: Path) -> schema.Config:
    logger.debug(f"Reading configuration from a {filename}")
    with open(filename) as f:
        return schema.Config.parse_obj(yaml.load(f.read(), Loader=yaml.FullLoader))
