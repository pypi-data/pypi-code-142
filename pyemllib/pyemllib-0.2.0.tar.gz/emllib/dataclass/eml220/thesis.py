from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.responsible_party import ResponsibleParty

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class Thesis:
    degree: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    institution: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    total_pages: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalPages",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
