from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"


class CellGeometryType(Enum):
    PIXEL = "pixel"
    MATRIX = "matrix"
