from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


@dataclass
class InlineType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
