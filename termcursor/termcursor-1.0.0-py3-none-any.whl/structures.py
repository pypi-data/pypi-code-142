#!/usr/bin/env python3
"""
termcursor
================================================================================

submodule: Structures
"""

from ctypes import c_int, c_byte, Structure


# pylint: disable=too-few-public-methods
class _CursorInfoForWindows(Structure):
    """
    Class to handle dll calls to hide or show the console cursor
    ============================================================

    Attributes
    ----------
    size : c_int (int)
        Size of the console cursor.
    visible : c_byte (bool)
        Whether the console cursor is visible or not.

    References
    ----------
    I.  Decription of the CONSOLE_CURSOR_INFO structure
        https://learn.microsoft.com/en-us/windows/console/console-cursor-info-str
    """
    _fields_ = [('size', c_int), ('visible', c_byte)]
