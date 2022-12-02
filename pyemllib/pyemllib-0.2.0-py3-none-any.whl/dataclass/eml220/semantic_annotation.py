from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.scope_type import ScopeType

__NAMESPACE__ = "https://eml.ecoinformatics.org/semantics-2.2.0"


@dataclass
class SemanticAnnotation:
    property_uri: Optional["SemanticAnnotation.PropertyUri"] = field(
        default=None,
        metadata={
            "name": "propertyURI",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    value_uri: Optional["SemanticAnnotation.ValueUri"] = field(
        default=None,
        metadata={
            "name": "valueURI",
            "type": "Element",
            "namespace": "",
            "required": True,
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
    class PropertyUri:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        label: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ValueUri:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        label: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
