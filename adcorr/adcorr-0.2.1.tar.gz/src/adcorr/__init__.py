from importlib.metadata import version

from . import corrections, utils

__version__ = version("adcorr")

__all__ = ["__version__", "utils", "corrections"]
