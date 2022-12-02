from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.access_rule import AccessRule
from emllib.dataclass.eml220.access_type_order import AccessTypeOrder
from emllib.dataclass.eml220.scope_type import ScopeType

__NAMESPACE__ = "https://eml.ecoinformatics.org/access-2.2.0"


@dataclass
class AccessType:
    allow: List[AccessRule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    deny: List[AccessRule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["AccessType.References"] = field(
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
    order: AccessTypeOrder = field(
        default=AccessTypeOrder.ALLOW_FIRST,
        metadata={
            "type": "Attribute",
        },
    )
    auth_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "authSystem",
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
