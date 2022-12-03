from enum import Enum, unique


@unique
class Currency(str, Enum):
    ARS = "ARS"
    USD = "USD"
