import sys
import warnings
from importlib import abc, util

from qtpy import *  # noqa

warnings.warn(
    "The superqt.qtcompat module is deprecated as of v0.3.0. "
    "Please import from `qtpy` instead."
)


# forward any requests for superqt.qtcompat.* to qtpy.*
class SuperQtImporter(abc.MetaPathFinder):
    def find_spec(self, fullname: str, path, target=None):  # type: ignore
        if fullname.startswith(__name__):
            return util.find_spec(fullname.replace(__name__, "qtpy"))


sys.meta_path.append(SuperQtImporter())
