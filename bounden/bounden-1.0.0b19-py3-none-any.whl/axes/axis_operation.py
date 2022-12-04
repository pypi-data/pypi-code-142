from enum import IntEnum, unique


@unique
class AxisOperation(IntEnum):
    """
    Axis value operations.
    """

    Add = 1
    """
    Addition.
    """

    Subtract = 2
    """
    Subtraction.
    """
