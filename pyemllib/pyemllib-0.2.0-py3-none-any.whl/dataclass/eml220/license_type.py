from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


@dataclass
class LicenseType:
    license_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "licenseName",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    identifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
