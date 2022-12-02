from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"


class RasterOriginType(Enum):
    UPPER_LEFT = "Upper Left"
    LOWER_LEFT = "Lower Left"
    UPPER_RIGHT = "Upper Right"
    LOWER_RIGHT = "Lower Right"
