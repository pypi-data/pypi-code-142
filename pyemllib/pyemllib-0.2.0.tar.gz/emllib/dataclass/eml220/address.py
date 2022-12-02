from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType
from emllib.dataclass.eml220.scope_type import ScopeType

__NAMESPACE__ = "https://eml.ecoinformatics.org/party-2.2.0"


@dataclass
class Address:
    delivery_point: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "deliveryPoint",
            "type": "Element",
            "namespace": "",
        },
    )
    city: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    administrative_area: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "administrativeArea",
            "type": "Element",
            "namespace": "",
        },
    )
    postal_code: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "",
        },
    )
    country: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["Address.References"] = field(
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
