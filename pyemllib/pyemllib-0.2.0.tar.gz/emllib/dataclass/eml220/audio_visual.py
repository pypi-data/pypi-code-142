from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.responsible_party import ResponsibleParty

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class AudioVisual:
    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    publication_place: List[str] = field(
        default_factory=list,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    performer: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    isbn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
