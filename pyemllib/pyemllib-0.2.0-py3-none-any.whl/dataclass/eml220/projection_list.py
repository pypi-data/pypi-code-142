from dataclasses import dataclass, field
from typing import List

from emllib.dataclass.eml220.horiz_coord_sys_type import HorizCoordSysType

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialReference-2.2.0"


@dataclass
class ProjectionList:
    class Meta:
        name = "projectionList"
        namespace = "https://eml.ecoinformatics.org/spatialReference-2.2.0"

    horiz_coord_sys_def: List[HorizCoordSysType] = field(
        default_factory=list,
        metadata={
            "name": "horizCoordSysDef",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
