from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from emllib.dataclass.eml220.gring_point_type import GringPointType
from emllib.dataclass.eml220.length_unit_type import LengthUnitType
from emllib.dataclass.eml220.scope_type import ScopeType

__NAMESPACE__ = "https://eml.ecoinformatics.org/coverage-2.2.0"


@dataclass
class GeographicCoverage:
    geographic_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "geographicDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    bounding_coordinates: Optional["GeographicCoverage.BoundingCoordinates"] = field(
        default=None,
        metadata={
            "name": "boundingCoordinates",
            "type": "Element",
            "namespace": "",
        },
    )
    dataset_gpolygon: List["GeographicCoverage.DatasetGpolygon"] = field(
        default_factory=list,
        metadata={
            "name": "datasetGPolygon",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["GeographicCoverage.References"] = field(
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
    class BoundingCoordinates:
        west_bounding_coordinate: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "westBoundingCoordinate",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": Decimal("-180.0"),
                "max_inclusive": Decimal("180.0"),
            },
        )
        east_bounding_coordinate: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "eastBoundingCoordinate",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": Decimal("-180.0"),
                "max_inclusive": Decimal("180.0"),
            },
        )
        north_bounding_coordinate: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "northBoundingCoordinate",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": Decimal("-90.0"),
                "max_inclusive": Decimal("90.0"),
            },
        )
        south_bounding_coordinate: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "southBoundingCoordinate",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_inclusive": Decimal("-90.0"),
                "max_inclusive": Decimal("90.0"),
            },
        )
        bounding_altitudes: Optional["GeographicCoverage.BoundingCoordinates.BoundingAltitudes"] = field(
            default=None,
            metadata={
                "name": "boundingAltitudes",
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class BoundingAltitudes:
            altitude_minimum: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "altitudeMinimum",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            altitude_maximum: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "altitudeMaximum",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            altitude_units: Optional[LengthUnitType] = field(
                default=None,
                metadata={
                    "name": "altitudeUnits",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

    @dataclass
    class DatasetGpolygon:
        dataset_gpolygon_outer_gring: Optional["GeographicCoverage.DatasetGpolygon.DatasetGpolygonOuterGring"] = field(
            default=None,
            metadata={
                "name": "datasetGPolygonOuterGRing",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        dataset_gpolygon_exclusion_gring: List[
            "GeographicCoverage.DatasetGpolygon.DatasetGpolygonExclusionGring"
        ] = field(
            default_factory=list,
            metadata={
                "name": "datasetGPolygonExclusionGRing",
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class DatasetGpolygonOuterGring:
            g_ring_point: List[GringPointType] = field(
                default_factory=list,
                metadata={
                    "name": "gRingPoint",
                    "type": "Element",
                    "namespace": "",
                },
            )
            g_ring: Optional[str] = field(
                default=None,
                metadata={
                    "name": "gRing",
                    "type": "Element",
                    "namespace": "",
                },
            )

        @dataclass
        class DatasetGpolygonExclusionGring:
            g_ring_point: List[GringPointType] = field(
                default_factory=list,
                metadata={
                    "name": "gRingPoint",
                    "type": "Element",
                    "namespace": "",
                },
            )
            g_ring: Optional[str] = field(
                default=None,
                metadata={
                    "name": "gRing",
                    "type": "Element",
                    "namespace": "",
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
