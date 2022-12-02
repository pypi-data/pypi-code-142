from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import SpatialVectorType

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialVector-2.2.0"


@dataclass
class SpatialVector(SpatialVectorType):
    class Meta:
        name = "spatialVector"
        namespace = "https://eml.ecoinformatics.org/spatialVector-2.2.0"
