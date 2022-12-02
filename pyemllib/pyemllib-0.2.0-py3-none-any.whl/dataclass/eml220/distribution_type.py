from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.inline_type import InlineType
from emllib.dataclass.eml220.offline_type import OfflineType
from emllib.dataclass.eml220.online_type import OnlineType
from emllib.dataclass.eml220.scope_type import ScopeType

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


@dataclass
class DistributionType:
    online: Optional[OnlineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    offline: Optional[OfflineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    inline: Optional[InlineType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["DistributionType.References"] = field(
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
