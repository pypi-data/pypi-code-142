from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.geog_coord_sys_type import GeogCoordSysType
from emllib.dataclass.eml220.length_units import LengthUnits

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialReference-2.2.0"


@dataclass
class HorizCoordSysType:
    class Meta:
        name = "horizCoordSysType"

    geog_coord_sys: Optional[GeogCoordSysType] = field(
        default=None,
        metadata={
            "name": "geogCoordSys",
            "type": "Element",
            "namespace": "",
        },
    )
    proj_coord_sys: Optional["HorizCoordSysType.ProjCoordSys"] = field(
        default=None,
        metadata={
            "name": "projCoordSys",
            "type": "Element",
            "namespace": "",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class ProjCoordSys:
        geog_coord_sys: Optional[GeogCoordSysType] = field(
            default=None,
            metadata={
                "name": "geogCoordSys",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        projection: Optional["HorizCoordSysType.ProjCoordSys.Projection"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )

        @dataclass
        class Projection:
            parameter: List["HorizCoordSysType.ProjCoordSys.Projection.Parameter"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                },
            )
            unit: Optional["HorizCoordSysType.ProjCoordSys.Projection.Unit"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )

            @dataclass
            class Parameter:
                name: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    },
                )
                description: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )
                value: Optional[object] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

            @dataclass
            class Unit:
                name: Optional[LengthUnits] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                    },
                )
