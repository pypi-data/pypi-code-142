class Configuration:
    """
    Configuration object for flaskez.

    Properties:
    SUPPRESS_WARNINGS - False to show all warnings in the console, True to hide all warnings.
    """
    def __init__(self) -> None:
        self.__SUPPRESS = False

    def _false(self) -> None:
        raise ValueError("'value' has to be a bool.")

    @property
    def SUPPRESS_WARNINGS(self) -> bool | None:
        return self.__SUPPRESS

    @SUPPRESS_WARNINGS.setter
    def SUPPRESS_WARNINGS(self, value: bool) -> None:
        self.__SUPPRESS = value if isinstance(value, bool) else self._false()


config = Configuration()
