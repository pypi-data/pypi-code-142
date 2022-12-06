#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib

__all__ = ["import_class"]


def import_class(path):
    """
    Dynamically import a class from a given path.
    """
    # split the path for the last name, which is the class
    components = path.rsplit(".", 1)

    # import the module
    module = importlib.import_module(components[0])

    # get the class
    return getattr(module, components[-1])

