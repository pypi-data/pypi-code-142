import logging
import logging.config
import os
from pathlib import Path

import coloredlogs  # type: ignore
import pkg_resources
import yaml


def setup_logging(
    path: str | Path | None = None,
    default_path: str = "logging.yaml",
    default_level: int = logging.INFO,
    env_key: str = "PY2OF_LOGGING_YAML",
) -> None:
    """Loads logging.yaml and configure logging accordingly.

    Arguments:
        path:               Path to logging.yaml, defaults to None, in which case
                            the package default logging.yaml will be used.
        default_path:       Name of the default logging.yaml.
        default_level:      Default level.
        env_key:            Alternatively, path to logging.yaml might be found
                            in ENV var of this name.

    Return:
        None
    """
    if path is None:
        # we got no yaml path directly

        # try to use env var
        value = os.getenv(env_key, None)
        if value:
            path = value

        if path is None:
            # there is no env var either! Use the default path...
            path = pkg_resources.resource_filename("py2of", default_path)

    if os.path.exists(path):
        with open(path) as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                # coloredlogs.install()
            except Exception as e:
                print(e)
                print("Error in Logging Configuration. Using default configs")
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print("Failed to load configuration file. Using default configs")


def set_logger(log: str = "info") -> None:
    """Sets logging level for root logger and it's handler."""
    root_logger = logging.getLogger()

    verbosity_mapping = {
        "info": logging.INFO,
        "debug": logging.DEBUG,
        "error": logging.ERROR,
        "warning": logging.WARNING,
    }

    level = verbosity_mapping.get(log)
    if level is None:
        raise KeyError(f"log level {log} not known")

    root_logger.setLevel(level)
    root_logger.handlers[0].setLevel(level)
