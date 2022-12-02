from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.enumerated_domain_enforced import EnumeratedDomainEnforced
from emllib.dataclass.eml220.single_date_time_type import CitationType

__NAMESPACE__ = "https://eml.ecoinformatics.org/attribute-2.2.0"


@dataclass
class NonNumericDomainType:
    enumerated_domain: List["NonNumericDomainType.EnumeratedDomain"] = field(
        default_factory=list,
        metadata={
            "name": "enumeratedDomain",
            "type": "Element",
            "namespace": "",
        },
    )
    text_domain: List["NonNumericDomainType.TextDomain"] = field(
        default_factory=list,
        metadata={
            "name": "textDomain",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["NonNumericDomainType.References"] = field(
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

    @dataclass
    class EnumeratedDomain:
        code_definition: List["NonNumericDomainType.EnumeratedDomain.CodeDefinition"] = field(
            default_factory=list,
            metadata={
                "name": "codeDefinition",
                "type": "Element",
                "namespace": "",
            },
        )
        external_code_set: Optional["NonNumericDomainType.EnumeratedDomain.ExternalCodeSet"] = field(
            default=None,
            metadata={
                "name": "externalCodeSet",
                "type": "Element",
                "namespace": "",
            },
        )
        entity_code_list: Optional["NonNumericDomainType.EnumeratedDomain.EntityCodeList"] = field(
            default=None,
            metadata={
                "name": "entityCodeList",
                "type": "Element",
                "namespace": "",
            },
        )
        enforced: EnumeratedDomainEnforced = field(
            default=EnumeratedDomainEnforced.YES,
            metadata={
                "type": "Attribute",
            },
        )

        @dataclass
        class CodeDefinition:
            code: Optional[str] = field(
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
            source: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            order: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )

        @dataclass
        class ExternalCodeSet:
            codeset_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "codesetName",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            citation: List[CitationType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "sequential": True,
                },
            )
            codeset_url: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "codesetURL",
                    "type": "Element",
                    "namespace": "",
                    "sequential": True,
                },
            )

        @dataclass
        class EntityCodeList:
            entity_reference: Optional[str] = field(
                default=None,
                metadata={
                    "name": "entityReference",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            value_attribute_reference: Optional[str] = field(
                default=None,
                metadata={
                    "name": "valueAttributeReference",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            definition_attribute_reference: Optional[str] = field(
                default=None,
                metadata={
                    "name": "definitionAttributeReference",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            order_attribute_reference: Optional[str] = field(
                default=None,
                metadata={
                    "name": "orderAttributeReference",
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

    @dataclass
    class TextDomain:
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
        pattern: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        source: Optional[str] = field(
            default=None,
            metadata={
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
