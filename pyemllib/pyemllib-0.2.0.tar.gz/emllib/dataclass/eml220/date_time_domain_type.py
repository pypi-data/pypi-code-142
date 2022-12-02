from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "https://eml.ecoinformatics.org/attribute-2.2.0"


@dataclass
class DateTimeDomainType:
    bounds: List["DateTimeDomainType.Bounds"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["DateTimeDomainType.References"] = field(
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
        minimum: Optional["DateTimeDomainType.Bounds.Minimum"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        maximum: Optional["DateTimeDomainType.Bounds.Maximum"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class Minimum:
            value: str = field(
                default="",
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
            value: str = field(
                default="",
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
