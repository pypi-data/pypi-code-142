#!/usr/bin/env python3
"""
termcursor
================================================================================

submodule: Errors
"""


class NotSupportedPlatform(Exception):
    """
    Custom error for a case when termcursor runs on a not supported platform
    ========================================================================

    Attributes
    ----------
    message : str
        Printable message during raising the error.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize an instance of the Exception object
        ==============================================

        Returns
        -------
        None
        """
        # for avoiding pylint error W0231 (super-init-not-called)
        super().__init__(message)
        self.message = message


class WrongParamaterValue(Exception):
    """
    Custom error for a case when a wrong parameter value were given
    ===============================================================

    Attributes
    ----------
    message : str
        Printable message during raising the error.
    """

    def __init__(self, message: str) -> None:
        """
        Initialize an instance of the Exception object
        ==============================================

        Returns
        -------
        None
        """
        # for avoiding pylint error W0231 (super-init-not-called)
        super().__init__(message)
        self.message = message
