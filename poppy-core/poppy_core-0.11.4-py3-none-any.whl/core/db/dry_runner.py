#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from poppy.core.logger import logger

from functools import wraps
from poppy.core.generic.metaclasses import Singleton

__all__ = ["DryRunner"]




class DryRunnerMeta(Singleton):
    """
    Override the singleton metaclass to initialize some parameters.
    """
    def __init__(cls, *args, **kwargs):
        # init the class as usual
        super(DryRunnerMeta, cls).__init__(*args, **kwargs)

        # set it not activated by default for all derived classes
        cls.activated = False


class DryRunner(object, metaclass=DryRunnerMeta):
    """
    A class to manage methods to be dry run.
    """
    @classmethod
    def dry_run(cls, func):
        """
        A decorator to put a method or function in dry run mode according to
        the parameter stored into the singleton.
        """
        # define the wrapper function
        @wraps(func)
        def wrapper(*args, **kwargs):
            # if not dry run
            if not cls.activated:
                # call effectively the function
                return func(*args, **kwargs)
            # else do nothing
            return None

        return wrapper

    @classmethod
    def activate(cls):
        """
        Activate the dry run mode.
        """
        logger.debug("Activating dry run")
        cls.activated = True

    @classmethod
    def deactivate(cls):
        """
        Deactivate the dry run mode.
        """
        logger.debug("Deactivating dry run")
        cls.activated = False


# vim: set tw=79 :
