#!/usr/bin/env python3
"""
termcursor
================================================================================

submodule: Constants
"""
from enum import Enum


class OperationSystem(Enum):
    """
    Constants for the supported platforms
    =====================================
    """
    WINDOWS = 'nt'
    UNIX = 'posix'


class StdHandle(Enum):
    """
    Constants for handling a specified standard device
    ==================================================

    References
    ----------
    I.  Available parameters
        https://learn.microsoft.com/en-us/windows/console/getstdhandle
    """

    STD_INPUT_HANDLE = -10
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12


class VisibilityOnUnix(Enum):
    """
    Constants for the available visibility values on Unix platforms
    ===============================================================

    References
    ----------
    I.  ANSI escape codes
        https://en.wikipedia.org/wiki/ANSI_escape_code
    """
    HIDE = '\033[?25l'
    SHOW = '\033[?25h'


class VisibilityOnWindows(Enum):
    """
    Constants for the available visibility values on Windows platforms
    ==================================================================
    """
    HIDE = False
    SHOW = True
