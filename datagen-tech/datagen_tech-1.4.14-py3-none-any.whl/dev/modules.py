import inspect
import json
from pathlib import Path
from types import ModuleType
from typing import Any

import pandas as pd

INVOKING_MODULE_FRAME_IDX = 2


class ModuleFunctionalityWrapper:
    """
    Hack - Python versions < 3.7 modules cannot implement __getattr__ and __dir__
    """

    def __init__(self, functionality: object, module: ModuleType = None):
        self._module = module if module is not None else self._get_invoking_module()
        self._functionality = functionality

    def _get_invoking_module(self) -> ModuleType:
        """
        Current call stack illustration:
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        Fr.#0  ║  self._get_invoking_module()          ║ (Current)
        ‾‾‾‾‾  ╠═══════════════════════════════════════╣
        Fr.#1  ║  self.__init__()                      ║
        ‾‾‾‾‾  ╠═══════════════════════════════════════╣
        Fr.#2  ║  module we're actually interested in  ║ (INVOKING_MODULE_FRAME_IDX)
        ‾‾‾‾‾  ╠═══════════════════════════════════════╣
         ...   ║  ...                                  ║
               ╚═══════════════════════════════════════╝
        """
        invoking_frame = inspect.stack()[INVOKING_MODULE_FRAME_IDX]
        invoking_module = inspect.getmodule(invoking_frame[0])
        return invoking_module

    def __getattr__(self, name):
        try:
            return getattr(self._functionality, name)
        except AttributeError:
            return getattr(self._module, name)


def get_resource_path(*path_components: str) -> Path:
    invoking_frame = inspect.stack()[1]
    invoking_module = inspect.getmodule(invoking_frame[0])
    return Path(invoking_module.__file__).parent.joinpath(*path_components)


def load_resource(*path_components: str) -> Any:
    invoking_frame = inspect.stack()[1]
    invoking_module = inspect.getmodule(invoking_frame[0])
    pkg_resource_file_path = Path(invoking_module.__file__).parent.joinpath(*path_components)
    if pkg_resource_file_path.suffix == ".json":
        return json.loads(pkg_resource_file_path.read_text())
    elif pkg_resource_file_path.suffix == ".csv":
        return pd.read_csv(pkg_resource_file_path)
