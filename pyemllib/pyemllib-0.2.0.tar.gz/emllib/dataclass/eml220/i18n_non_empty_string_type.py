from dataclasses import dataclass, field
from typing import List, Optional, Type

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


@dataclass
class I18NNonEmptyStringType:
    class Meta:
        name = "i18nNonEmptyStringType"

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
                    "name": "value",
                    "type": Type["I18NNonEmptyStringType.Value"],
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass
    class Value:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        lang: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
