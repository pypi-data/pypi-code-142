from dataclasses import dataclass, field
from typing import List

from emllib.dataclass.eml220.access_rule_value import AccessRuleValue

__NAMESPACE__ = "https://eml.ecoinformatics.org/access-2.2.0"


@dataclass
class AccessRule:
    principal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    permission: List[AccessRuleValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
