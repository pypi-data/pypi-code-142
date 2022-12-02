"""Version information envvar."""

__all__ = ["VERSION", "get_version"]

VERSION = "0.0.1"


def get_version() -> str:
    """returns the current version of the library

    Returns:
        str: version
    """
    return VERSION
