from enum import IntEnum, unique


@unique
class Horizontal(IntEnum):
    Left = 1
    Center = 2
    Right = 3


@unique
class Vertical(IntEnum):
    Top = 1
    Center = 2
    Bottom = 3
