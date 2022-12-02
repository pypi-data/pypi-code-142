from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.address import Address
from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType
from emllib.dataclass.eml220.person import Person
from emllib.dataclass.eml220.scope_type import ScopeType

__NAMESPACE__ = "https://eml.ecoinformatics.org/party-2.2.0"


@dataclass
class ResponsibleParty:
    individual_name: List[Person] = field(
        default_factory=list,
        metadata={
            "name": "individualName",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    organization_name: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "organizationName",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    position_name: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "positionName",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    phone: List["ResponsibleParty.Phone"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    electronic_mail_address: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "electronicMailAddress",
            "type": "Element",
            "namespace": "",
        },
    )
    online_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "onlineUrl",
            "type": "Element",
            "namespace": "",
        },
    )
    user_id: List["ResponsibleParty.UserId"] = field(
        default_factory=list,
        metadata={
            "name": "userId",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["ResponsibleParty.References"] = field(
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
    class Phone:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        phonetype: str = field(
            default="voice",
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class UserId:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        directory: Optional[str] = field(
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
