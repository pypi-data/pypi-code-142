from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


@dataclass
class OfflineType:
    medium_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    medium_density: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumDensity",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    medium_density_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumDensityUnits",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    medium_volume: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumVolume",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    medium_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "mediumFormat",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    medium_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediumNote",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
