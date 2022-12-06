# Copyright Exafunction, Inc.

"""Convenience functions for using the module repository.

A default module repository is created on first use. This Python module currently
requires the use of the environment variable `EXA_MODULE_REPOSITORY_ADDRESS` to know the
location of the module repository.
"""

import atexit
import functools
from typing import Optional

from exa.py_module_repository import module_repository

_default_mr: Optional[module_repository.ModuleRepository] = None


def _get_or_create_mr() -> module_repository.ModuleRepository:
    global _default_mr  # pylint: disable=global-statement
    if _default_mr is None:
        _default_mr = module_repository.ModuleRepository()
        atexit.register(shutdown)
    return _default_mr


def shutdown():
    """
    Shuts down the default module repository.

    This is automatically called on exit.
    """
    global _default_mr  # pylint: disable=global-statement
    if _default_mr is not None:
        _default_mr.close()
        _default_mr = None


def _forward_method(name):
    prev = getattr(module_repository.ModuleRepository, name)

    @functools.wraps(prev)
    def f(*args, **kwargs):
        return getattr(_get_or_create_mr(), name)(*args, **kwargs)

    return f


# List these out individually so that mypy is happy.
register_runner_image = _forward_method("register_runner_image")
create_and_register_runner_image = _forward_method("create_and_register_runner_image")
register_py_interpreter_module = _forward_method("register_py_interpreter_module")
