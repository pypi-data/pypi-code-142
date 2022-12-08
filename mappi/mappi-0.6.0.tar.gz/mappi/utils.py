import logging
from pathlib import Path
from typing import Optional

import pkg_resources
import yaml

from mappi import config, schema

logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger(__package__)


def read_configuration(filename: Path) -> schema.Config:
    logger.debug(f"Reading configuration from a {filename}")
    with open(filename) as f:
        return schema.Config.parse_obj(yaml.load(f.read(), Loader=yaml.FullLoader))


def update_configuration(
    config: schema.Config,
    *,
    port: Optional[int],
) -> schema.Config:
    if port:
        logger.debug(f"Setting port {config.server.port} to {port}")
        config.server.port = port
    return config


def get_version() -> str:
    return pkg_resources.get_distribution(__package__).version
