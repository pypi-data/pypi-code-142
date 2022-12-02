from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import SpatialRasterType

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"


@dataclass
class SpatialRaster(SpatialRasterType):
    class Meta:
        name = "spatialRaster"
        namespace = "https://eml.ecoinformatics.org/spatialRaster-2.2.0"
