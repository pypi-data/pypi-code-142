#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import palmiche
import os
import sys
import inspect
import platform


def home(dataDir=None, libDir=False):
    """Return the pathname of the palmiche root directory (or a data subdirectory).
    Parameters
    ----------
    dataDir : str
        If not None, return the path to a specific data directory
    libDir : bool
        If True, return path to the lib directory
    Returns
    -------
    dir : str
        The directory
    Example
    -------
    >>> from palmiche.home import home
    >>> home()                                 # doctest: +ELLIPSIS
    '.../palmiche'
    >>> home(dataDir="test-charge")                   # doctest: +ELLIPSIS
    '.../data/test-charge'
    >>> os.path.join(home(dataDir="test-charge"),"H2O.mol2")  # doctest: +ELLIPSIS
    '.../data/test-charge/H2O.mol2'
    """

    homeDir = os.path.dirname(inspect.getfile(palmiche))
    try:
        if sys._MEIPASS:
            homeDir = sys._MEIPASS
    except Exception:
        pass

    if dataDir:
        return os.path.join(homeDir, "data", dataDir)
    elif libDir:
        libdir = os.path.join(homeDir, "lib", platform.system())
        if not os.path.exists(libdir):
            raise FileNotFoundError("Could not find libs.")
        return libdir
    else:
        return homeDir

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    h = home()
    print(h)
