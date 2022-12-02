from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.list_type import ParagraphType
from emllib.dataclass.eml220.section_type import SectionType

__NAMESPACE__ = "https://eml.ecoinformatics.org/text-2.2.0"


@dataclass
class TextType:
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "section",
                    "type": SectionType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": ParagraphType,
                    "namespace": "",
                },
                {
                    "name": "markdown",
                    "type": str,
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            ),
        },
    )
