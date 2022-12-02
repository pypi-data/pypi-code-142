from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"


class CornerPointPointInPixel(Enum):
    UPPER_LEFT = "upperLeft"
    UPPER_RIGHT = "upperRight"
    LOWER_RIGHT = "lowerRight"
    LOWER_LEFT = "lowerLeft"
    CENTER = "center"
