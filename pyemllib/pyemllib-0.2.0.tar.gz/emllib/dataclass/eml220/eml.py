from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.access_type import AccessType
from emllib.dataclass.eml220.attribute_type import DatasetType
from emllib.dataclass.eml220.dependency_type import SoftwareType
from emllib.dataclass.eml220.procedure_step_type import ProtocolType
from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.semantic_annotation import SemanticAnnotation
from emllib.dataclass.eml220.single_date_time_type import CitationType

__NAMESPACE__ = "https://eml.ecoinformatics.org/eml-2.2.0"


@dataclass
class Eml:
    class Meta:
        name = "eml"
        namespace = "https://eml.ecoinformatics.org/eml-2.2.0"

    access: Optional[AccessType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dataset: Optional[DatasetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    citation: Optional[CitationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    software: Optional[SoftwareType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    protocol: Optional[ProtocolType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    annotations: Optional["Eml.Annotations"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    additional_metadata: List["Eml.AdditionalMetadata"] = field(
        default_factory=list,
        metadata={
            "name": "additionalMetadata",
            "type": "Element",
            "namespace": "",
        },
    )
    package_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "packageId",
            "type": "Attribute",
            "required": True,
        },
    )
    system: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "required": True,
            "tokens": True,
        },
    )
    scope: ScopeType = field(
        init=False,
        default=ScopeType.SYSTEM,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
    class Annotations:
        annotation: List["Eml.Annotations.Annotation"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Annotation(SemanticAnnotation):
            references: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class AdditionalMetadata:
        describes: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        metadata: Optional["Eml.AdditionalMetadata.Metadata"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
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
        class Metadata:
            any_element: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                },
            )
