from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType

__NAMESPACE__ = "https://eml.ecoinformatics.org/project-2.2.0"


@dataclass
class AwardType:
    funder_name: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "funderName",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    funder_identifier: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "name": "funderIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    award_number: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "awardNumber",
            "type": "Element",
            "namespace": "",
        },
    )
    title: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    award_url: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "name": "awardUrl",
            "type": "Element",
            "namespace": "",
        },
    )
