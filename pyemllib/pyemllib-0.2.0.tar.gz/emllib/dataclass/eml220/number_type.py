from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/attribute-2.2.0"


class NumberType(Enum):
    NATURAL = "natural"
    WHOLE = "whole"
    INTEGER = "integer"
    REAL = "real"
