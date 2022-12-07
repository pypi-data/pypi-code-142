import os
from pathlib import Path
from typing import Any, Dict

CURRENT_DIR = Path(__file__).parent.resolve()

DEBUG = bool(os.getenv("MAPPI_DEBUG", default=""))
DATA_DIR = CURRENT_DIR / "data"
MAPPI_CONFIG_FILENAME = "mappi.yml"
DEFAULT_CONFIG_FILEPATH = DATA_DIR / "config-default.yml"


MAPPI_LOGO = r"""
                                      oo

88d8b.d8b. .d8888b. 88d888b. 88d888b. dP
88'`88'`88 88'  `88 88'  `88 88'  `88 88
88  88  88 88.  .88 88.  .88 88.  .88 88
dP  dP  dP `88888P8 88Y888P' 88Y888P' dP
                    88       88
                    dP       dP
"""

CONFIG_MESSAGE = """
Here is your configuration.
Copy highlighted code below into [green]mappi.yml[/] file
or redirect output to the file using

$ [green]mappi config > mappi.yml[/]

For the complete list of available options use

$ [green]mappi config --full > mappi.yml[/]
""".strip()

CONFIG_MISSING_MESSAGE = """
[green]mappi.yml[/] config file is missing.
We have created a default one for you. Adjust it as needed
or provide [green]--config[/] flag to specify your own file.
""".strip()

DEFAULT_LOGGER_LEVEL = "DEBUG" if DEBUG else "INFO"

LOGGING_CONFIG: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "mappi": {
            "handlers": ["default"],
            "level": DEFAULT_LOGGER_LEVEL,
            "propagate": False,
        },
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
    },
}
