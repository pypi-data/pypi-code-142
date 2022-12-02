from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.geographic_coverage import GeographicCoverage
from emllib.dataclass.eml220.responsible_party import ResponsibleParty

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class Map:
    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    edition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    geographic_coverage: List[GeographicCoverage] = field(
        default_factory=list,
        metadata={
            "name": "geographicCoverage",
            "type": "Element",
            "namespace": "",
        },
    )
    scale: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
