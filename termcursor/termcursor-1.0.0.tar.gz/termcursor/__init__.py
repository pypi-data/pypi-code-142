#!/usr/bin/env python3
"""
termcursor
================================================================================

Hiding or showing the console cursor on Windows and Unix platforms with the
Python Standard Library only
--------------------------------------------------------------------------------
"""

__author__ = 'Richárd Ádám Vécsey Dr.'
__copyright__ = 'Copyright 2022, termcursor'
__credits__ = ['Richárd Ádám Vécsey Dr.']
__license__ = 'MIT'
__version__ = '1.0.0'
__status__ = 'Alpha'

from .termcursor import hidecursor, showcursor


__all__ = ['hidecursor', 'showcursor']
