from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.standard_unit_dictionary import StandardUnitDictionary

__NAMESPACE__ = "https://eml.ecoinformatics.org/attribute-2.2.0"


@dataclass
class UnitType:
    standard_unit: Optional[StandardUnitDictionary] = field(
        default=None,
        metadata={
            "name": "standardUnit",
            "type": "Element",
            "namespace": "",
        },
    )
    custom_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "customUnit",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
