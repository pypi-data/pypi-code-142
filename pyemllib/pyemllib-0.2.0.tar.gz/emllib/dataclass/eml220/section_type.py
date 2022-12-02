from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.i18n_string import I18NString
from emllib.dataclass.eml220.list_type import ParagraphType

__NAMESPACE__ = "https://eml.ecoinformatics.org/text-2.2.0"


@dataclass
class SectionType:
    title: Optional[I18NString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    para: List[ParagraphType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    section: List["SectionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
