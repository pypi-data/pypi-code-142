from dataclasses import dataclass, field
from typing import List, Optional, Type

from emllib.dataclass.eml220.i18n_string import I18NString
from emllib.dataclass.eml220.sub_super_script_type import SubSuperScriptType

__NAMESPACE__ = "https://eml.ecoinformatics.org/text-2.2.0"


@dataclass
class ListType:
    listitem: List["ListType.Listitem"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Listitem:
        para: List["ParagraphType"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        itemizedlist: List["ListType"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        orderedlist: List["ListType"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )


@dataclass
class ParagraphType:
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
                    "name": "itemizedlist",
                    "type": ListType,
                    "namespace": "",
                },
                {
                    "name": "orderedlist",
                    "type": ListType,
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["ParagraphType.Emphasis"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": SubSuperScriptType,
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": SubSuperScriptType,
                    "namespace": "",
                },
                {
                    "name": "literalLayout",
                    "type": Type["ParagraphType.LiteralLayout"],
                    "namespace": "",
                },
                {
                    "name": "ulink",
                    "type": Type["ParagraphType.Ulink"],
                    "namespace": "",
                },
            ),
        },
    )

    @dataclass
    class Emphasis:
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
                ),
            },
        )

    @dataclass
    class LiteralLayout:
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
                ),
            },
        )

    @dataclass
    class Ulink:
        url: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
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
                        "name": "citetitle",
                        "type": I18NString,
                        "namespace": "",
                    },
                ),
            },
        )
