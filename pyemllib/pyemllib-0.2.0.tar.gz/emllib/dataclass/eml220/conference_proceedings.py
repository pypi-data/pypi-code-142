from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.address import Address
from emllib.dataclass.eml220.chapter import Chapter

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class ConferenceProceedings(Chapter):
    conference_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "conferenceName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    conference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "conferenceDate",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    conference_location: Optional[Address] = field(
        default=None,
        metadata={
            "name": "conferenceLocation",
            "type": "Element",
            "namespace": "",
        },
    )
