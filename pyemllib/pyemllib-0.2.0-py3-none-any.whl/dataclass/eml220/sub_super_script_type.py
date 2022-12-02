from dataclasses import dataclass, field
from typing import List, Optional, Type

from emllib.dataclass.eml220.i18n_string import I18NString

__NAMESPACE__ = "https://eml.ecoinformatics.org/text-2.2.0"


@dataclass
class SubSuperScriptType:
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
                    "type": I18NString,
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["SubSuperScriptType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["SubSuperScriptType"],
                    "namespace": "",
                },
            ),
        },
    )
