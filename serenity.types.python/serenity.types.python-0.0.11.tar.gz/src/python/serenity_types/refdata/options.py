from enum import Enum


class OptionStyle(Enum):
    """
    Variety of option supported. Right now we only support vanialla European options.
    """
    EUROPEAN = "EUROPEAN"


class OptionType(Enum):
    """
    Put/call flag for options.
    """
    PUT = "PUT"
    CALL = "CALL"
