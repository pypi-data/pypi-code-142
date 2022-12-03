from enum import IntEnum, unique


@unique
class Alignment(IntEnum):
    """
    Alignment.
    """

    Near = -1
    """
    Align to a far boundary.

    For example, refers to the left when aligning text in a left-to-right
    language.
    """

    Center = 0
    """
    Align exactly between the near and far boundaries.
    """

    Far = +1
    """
    Align to a far boundary.

    For example, refers to the right when aligning text in a left-to-right
    language.
    """
