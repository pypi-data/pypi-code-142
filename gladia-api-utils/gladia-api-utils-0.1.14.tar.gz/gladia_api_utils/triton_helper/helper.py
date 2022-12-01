import json
import os
from logging import getLogger

logger = getLogger(__name__)


def check_if_model_needs_to_be_preloaded(model_name: str) -> bool:
    """
    Check if the model needs to be preloaded according to the GladIA's config file

    Args:
        model_name (str): name of the model to check

    Returns:
        bool: whether the model needs to be preloaded or not
    """

    path_to_config_file = os.getenv("API_CONFIG_FILE", "config.json")

    if not os.path.isfile(path_to_config_file):
        logger.warning(
            f"[TritonClient] Couldn't load config file {path_to_config_file}, setting __preload_model to False."
        )

        return False

    with open(path_to_config_file, "r") as f:
        config_file = json.load(f)

    if (
        "triton" not in config_file.keys()
        or "models_to_preload" not in config_file["triton"].keys()
    ):
        logger.warning(
            f"[TritonClient] Couldn't find 'models_to_preload' param key in the config file {path_to_config_file}, setting __preload_model to False."
        )

        return False

    return model_name in config_file["triton"]["models_to_preload"]
