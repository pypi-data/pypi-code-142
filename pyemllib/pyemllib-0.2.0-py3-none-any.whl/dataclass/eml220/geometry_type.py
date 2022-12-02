from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialVector-2.2.0"


class GeometryType(Enum):
    POINT = "Point"
    LINE_STRING = "LineString"
    LINEAR_RING = "LinearRing"
    POLYGON = "Polygon"
    MULTI_POINT = "MultiPoint"
    MULTI_LINE_STRING = "MultiLineString"
    MULTI_POLYGON = "MultiPolygon"
    MULTI_GEOMETRY = "MultiGeometry"
