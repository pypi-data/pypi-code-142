from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.angle_units import AngleUnits

__NAMESPACE__ = "https://eml.ecoinformatics.org/spatialReference-2.2.0"


@dataclass
class GeogCoordSysType:
    class Meta:
        name = "geogCoordSysType"

    datum: Optional["GeogCoordSysType.Datum"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    spheroid: Optional["GeogCoordSysType.Spheroid"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    prime_meridian: Optional["GeogCoordSysType.PrimeMeridian"] = field(
        default=None,
        metadata={
            "name": "primeMeridian",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    unit: Optional["GeogCoordSysType.Unit"] = field(
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
    class Datum:
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Spheroid:
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        semi_axis_major: Optional[float] = field(
            default=None,
            metadata={
                "name": "semiAxisMajor",
                "type": "Attribute",
            },
        )
        denom_flat_ratio: Optional[float] = field(
            default=None,
            metadata={
                "name": "denomFlatRatio",
                "type": "Attribute",
            },
        )

    @dataclass
    class PrimeMeridian:
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        longitude: Optional[float] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": -180.0,
                "max_inclusive": 180.0,
            },
        )

    @dataclass
    class Unit:
        name: Optional[AngleUnits] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
