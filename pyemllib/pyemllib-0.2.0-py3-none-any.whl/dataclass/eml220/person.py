from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType

__NAMESPACE__ = "https://eml.ecoinformatics.org/party-2.2.0"


@dataclass
class Person:
    salutation: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    given_name: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "",
        },
    )
    sur_name: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "surName",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
