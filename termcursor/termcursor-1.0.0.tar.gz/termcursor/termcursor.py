#!/usr/bin/env python3
"""
termcursor
================================================================================

submodule: This is the core module of termcursor.
"""

from __future__ import annotations
# os.name runs faster than platform.platform or sys.plaftorm
from os import name as os_name

from .constants import OperationSystem, VisibilityOnUnix, VisibilityOnWindows
from .errors import NotSupportedPlatform, WrongParamaterValue

match os_name:
    case OperationSystem.UNIX.value:
        # pylint: disable=no-name-in-module
        from sys import stdout
    case OperationSystem.WINDOWS.value:
        from ctypes import byref, windll
        from .constants import StdHandle
        from .structures import _CursorInfoForWindows


def cursorshandlerforunix(visibility: str = VisibilityOnUnix.SHOW.value) -> None:
    """
    Show or hide the console cursor on Unix platforms
    =================================================

    Parameters
    ----------
    visibility : str, default=True
        Whether to show or hide console cursor.

    Returns
    -------
    None

    Raises
    ------
    WrongParamaterValue
        When the given parameter is not supported.

    See Also
    --------
    I.  For available visibility values see: constants.VisibilityOnUnix

    References
    ----------
    I.  For more information about the values for visibility parameter check:
        https://docs.python.org/3/library/curses.html#curses.curs_set
    """
    if visibility not in [value.value for value in VisibilityOnUnix]:
        raise WrongParamaterValue('The given value for visibility parameter ' +
                                  'is wrong.')
    stdout.write(visibility)
    stdout.flush()


def cursorshandlerforwindows(visibility: bool = True) -> None:
    """
    Show or hide the console cursor on Windows platforms
    ====================================================

    Parameters
    ----------
    visibility : bool, default=True
        Whether to show or hide console cursor.

    Returns
    -------
    None

    Raises
    ------
    WrongParamaterValue
        When the given parameter is not supported.

    See Also
    --------
    I.  For available visibility values see: constants.VisibilityOnWindows
    II. Available parameters of StdHandle: constants.StdHandle

    References
    ----------
    I.  Description of the GetConsoleCursorInfo():
        https://learn.microsoft.com/en-us/windows/console/getconsolecursorinfo
    II. Description of the SetConsoleCursorInfo():
        https://learn.microsoft.com/en-us/windows/console/setconsolecursorinfo
    III.Documentation of byref()
        https://docs.python.org/3/library/ctypes.html#ctypes.byref
    """
    if visibility not in [value.value for value in VisibilityOnWindows]:
        raise WrongParamaterValue('The given value for visibility parameter ' +
                                  'is wrong.')
    cursor_info = _CursorInfoForWindows()
    get_std_handle = windll.kernel32.GetStdHandle(
                     StdHandle.STD_OUTPUT_HANDLE.value)
    windll.kernel32.GetConsoleCursorInfo(get_std_handle,
                                         byref(cursor_info))
    # pylint: disable=attribute-defined-outside-init
    cursor_info.visible = visibility
    windll.kernel32.SetConsoleCursorInfo(get_std_handle,
                                         byref(cursor_info))


def hidecursor() -> None:
    """
    Show the console cursor
    =======================

    Returns
    -------
    None

    Raises
    ------
    NotSupportedPlatform
        It occurs when termcursor runs other platforms than Windows or Unix.
    """
    match os_name:
        case OperationSystem.WINDOWS.value:
            cursorshandlerforwindows(visibility=VisibilityOnWindows.HIDE.value)
        case OperationSystem.UNIX.value:
            cursorshandlerforunix(visibility=VisibilityOnUnix.HIDE.value)
        case _:
            raise NotSupportedPlatform('Termcursor runs only on Windows and ' +
                                       'Unix platforms.')


def showcursor() -> None:
    """
    Show the console cursor
    =======================

    Returns
    -------
    None

    Raises
    ------
    NotSupportedPlatform
        It occurs when termcursor runs other platforms than Windows or Unix.
    """
    match os_name:
        case OperationSystem.WINDOWS.value:
            cursorshandlerforwindows(visibility=VisibilityOnWindows.SHOW.value)
        case OperationSystem.UNIX.value:
            cursorshandlerforunix(visibility=VisibilityOnUnix.SHOW.value)
        case _:
            raise NotSupportedPlatform('Termcursor runs only on Windows and ' +
                                       'Unix platforms.')


if __name__ == '__main__':
    raise RuntimeError('This is a module for termcursor, not a software.')
