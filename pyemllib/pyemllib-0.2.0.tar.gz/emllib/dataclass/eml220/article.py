from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.responsible_party import ResponsibleParty

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class Article:
    journal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    issue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    page_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "pageRange",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    publication_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    issn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
