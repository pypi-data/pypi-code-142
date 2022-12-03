from enum import Enum, unique


@unique
class Concept(str, Enum):
    ALQ = "ALQ"
    CUO = "CUO"
    EXP = "EXP"
    FAC = "FAC"
    PRE = "PRE"
    SEG = "SEG"
    HON = "HON"
    HAB = "HAB"
    VAR = "VAR"
