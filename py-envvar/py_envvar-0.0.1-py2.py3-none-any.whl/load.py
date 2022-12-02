import os
from os.path import exists
from typing import Dict

import yaml

DEFAULTS_KEY = "defaults"
REQUIRED_KEY = "required"


def load(path: str, target_env: str = "local") -> None:
    """Loads env vars described at the input file at `path`
    Defaults target_env to `local` when not provided

    Args:
        path (str): input file path
        target_env (str): target env key, ie: local/develop

    Raises:
        FileExistsError: if config file does not exist
        RequiredEnvvarMissingError: when a required env var is missing
    """
    if not exists(path):
        raise FileExistsError(f"{path} does not exists")

    try:
        file = open(path, "r")

        c = parse(file_str=file.read(), target_env=target_env)

        for key in c[DEFAULTS_KEY]:
            os.environ[key] = c[DEFAULTS_KEY][key]

        for key in c[target_env]:
            os.environ[key] = str(c[target_env][key])

        for env in c[REQUIRED_KEY]:
            if os.environ.get(env) is None:
                raise RequiredEnvvarMissingError(f"{env} is missing")

    finally:
        file.close()


def parse(
    file_str: str,
    target_env: str,
) -> Dict:

    """parses a yaml str and turn into
    envvar internal structure, this method is useful for testing

    Args:
        file_str: str - yaml string
        target_env: str - target env
    Returns:
        Dict[str:Dict, str:Dict, str:List]: return object ie:
        {
            "defaults": {"HOST": "0.0.0.0"},
            "requireds": ["HOST"],
            "local": {"HOST": "0.0.0.0"},
        }
    """

    yaml_contents = yaml.safe_load(file_str)

    parsed = {}
    parsed[DEFAULTS_KEY] = {}
    parsed[REQUIRED_KEY] = []
    parsed[target_env] = {}

    if yaml_contents.get(DEFAULTS_KEY) is not None:
        for key in yaml_contents[DEFAULTS_KEY]:
            parsed[DEFAULTS_KEY][key] = str(yaml_contents[DEFAULTS_KEY][key])

    if yaml_contents.get(target_env) is not None:
        for key in yaml_contents[target_env]:
            parsed[target_env][key] = str(yaml_contents[target_env][key])

    if yaml_contents.get(REQUIRED_KEY) is not None:
        for env in yaml_contents[REQUIRED_KEY]:
            parsed[REQUIRED_KEY].append(env)

    return parsed


class RequiredEnvvarMissingError(Exception):
    """
    This error is thrown when a required environment variable is missing
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
