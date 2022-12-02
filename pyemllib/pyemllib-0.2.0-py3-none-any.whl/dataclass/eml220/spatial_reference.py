from dataclasses import dataclass

from emllib.dataclass.eml220.spatial_reference_type import SpatialReferenceType

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialReference-2.2.0"


@dataclass
class SpatialReference(SpatialReferenceType):
    class Meta:
        name = "spatialReference"
        namespace = "https://eml.ecoinformatics.org/spatialReference-2.2.0"
