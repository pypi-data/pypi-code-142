from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "https://eml.ecoinformatics.org/text-2.2.0"


@dataclass
class I18NString:
    class Meta:
        name = "i18nString"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
