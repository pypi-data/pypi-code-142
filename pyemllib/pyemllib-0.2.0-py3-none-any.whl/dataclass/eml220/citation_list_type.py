from dataclasses import dataclass, field
from typing import List

from emllib.dataclass.eml220.single_date_time_type import CitationType

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class CitationListType:
    citation: List[CitationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    bibtex: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
