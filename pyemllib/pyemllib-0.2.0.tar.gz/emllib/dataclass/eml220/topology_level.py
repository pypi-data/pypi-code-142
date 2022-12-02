from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialVector-2.2.0"


class TopologyLevel(Enum):
    GEOMETRY_ONLY = "geometryOnly"
    NON_PLANAR_GRAPH = "nonPlanarGraph"
    PLANAR_LINE_GRAPH = "planarLineGraph"
    FULL_PLANAR_GRAPH = "fullPlanarGraph"
    SURFACE_GRAPH = "surfaceGraph"
    FULL_TOPOLOGY3_D = "fullTopology3D"
