# -*- coding: utf-8 -*-

import os
from types import ModuleType


def module_directory(module: ModuleType) -> str:
    module_file = getattr(module, "__file__", None)
    if module_file:
        assert isinstance(module_file, str)
        return os.path.dirname(module_file)

    raise RuntimeError(f"The '{module.__name__}' module path is unknown")
