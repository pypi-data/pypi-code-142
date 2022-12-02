from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.responsible_party import ResponsibleParty

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class PersonalCommunication:
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
    communication_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "communicationType",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    recipient: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
