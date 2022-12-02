from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.text_type import TextType

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


@dataclass
class ConnectionDefinitionType:
    scheme_name: Optional["ConnectionDefinitionType.SchemeName"] = field(
        default=None,
        metadata={
            "name": "schemeName",
            "type": "Element",
            "namespace": "",
        },
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    parameter_definition: List["ConnectionDefinitionType.ParameterDefinition"] = field(
        default_factory=list,
        metadata={
            "name": "parameterDefinition",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["ConnectionDefinitionType.References"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: ScopeType = field(
        default=ScopeType.DOCUMENT,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class SchemeName:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        system: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Attribute",
                "tokens": True,
            },
        )

    @dataclass
    class ParameterDefinition:
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        definition: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        default_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "defaultValue",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )

    @dataclass
    class References:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        system: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Attribute",
                "tokens": True,
            },
        )
