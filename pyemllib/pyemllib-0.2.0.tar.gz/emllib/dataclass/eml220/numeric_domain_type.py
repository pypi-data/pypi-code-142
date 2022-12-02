from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.number_type import NumberType

__NAMESPACE__ = "https://eml.ecoinformatics.org/attribute-2.2.0"


@dataclass
class NumericDomainType:
    number_type: Optional[NumberType] = field(
        default=None,
        metadata={
            "name": "numberType",
            "type": "Element",
            "namespace": "",
        },
    )
    bounds: List["NumericDomainType.Bounds"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["NumericDomainType.References"] = field(
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

    @dataclass
    class Bounds:
        minimum: Optional["NumericDomainType.Bounds.Minimum"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        maximum: Optional["NumericDomainType.Bounds.Maximum"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class Minimum:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )
            exclusive: Optional[bool] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class Maximum:
            value: Optional[float] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )
            exclusive: Optional[bool] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
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
