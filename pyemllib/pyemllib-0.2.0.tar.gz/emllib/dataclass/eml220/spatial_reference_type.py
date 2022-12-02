from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.horiz_coord_sys_type import HorizCoordSysType
from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.spatial_reference_type_horiz_coord_sys_name import (
    SpatialReferenceTypeHorizCoordSysName,
)

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialReference-2.2.0"


@dataclass
class SpatialReferenceType:
    horiz_coord_sys_name: Optional[SpatialReferenceTypeHorizCoordSysName] = field(
        default=None,
        metadata={
            "name": "horizCoordSysName",
            "type": "Element",
            "namespace": "",
        },
    )
    horiz_coord_sys_def: Optional[HorizCoordSysType] = field(
        default=None,
        metadata={
            "name": "horizCoordSysDef",
            "type": "Element",
            "namespace": "",
        },
    )
    vert_coord_sys: Optional["SpatialReferenceType.VertCoordSys"] = field(
        default=None,
        metadata={
            "name": "vertCoordSys",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["SpatialReferenceType.References"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class VertCoordSys:
        altitude_sys_def: Optional["SpatialReferenceType.VertCoordSys.AltitudeSysDef"] = field(
            default=None,
            metadata={
                "name": "altitudeSysDef",
                "type": "Element",
                "namespace": "",
            },
        )
        depth_sys_def: Optional["SpatialReferenceType.VertCoordSys.DepthSysDef"] = field(
            default=None,
            metadata={
                "name": "depthSysDef",
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class AltitudeSysDef:
            altitude_datum_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "altitudeDatumName",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            altitude_resolution: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "altitudeResolution",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            altitude_distance_units: Optional[str] = field(
                default=None,
                metadata={
                    "name": "altitudeDistanceUnits",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            altitude_encoding_method: Optional[str] = field(
                default=None,
                metadata={
                    "name": "altitudeEncodingMethod",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

        @dataclass
        class DepthSysDef:
            depth_datum_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "depthDatumName",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            depth_resolution: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "depthResolution",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            depth_distance_units: Optional[str] = field(
                default=None,
                metadata={
                    "name": "depthDistanceUnits",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            depth_encoding_method: Optional[str] = field(
                default=None,
                metadata={
                    "name": "depthEncodingMethod",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

    @dataclass
    class References:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        system: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Attribute",
                "tokens": True,
            },
        )
