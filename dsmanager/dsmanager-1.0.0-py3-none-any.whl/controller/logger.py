"""@Author Rayane AMROUCHE

Logger Class
"""

import os
import logging

from dotenv import load_dotenv


def make_logger(path: str, name: str, level: int = logging.INFO) -> logging.Logger:
    """Generates a logging logger by giving file path, name and logging level

    Args:
        path (str): Logging file path
        name (str): Name of the logger
        level (int, optional): Logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: Logging logger generated
    """
    load_dotenv(".env")

    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S",
    )

    os.makedirs("logs", exist_ok=True)
    os.makedirs(os.path.join("logs/", path), exist_ok=True)

    file_handler = logging.FileHandler(
        os.path.join("logs/", path, name + ".log"))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    global_handler = logging.FileHandler("logs/all.log")
    global_handler.setFormatter(formatter)
    logger.addHandler(global_handler)

    if os.environ.get("CONSOLE_LOGGER") == "True":
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
