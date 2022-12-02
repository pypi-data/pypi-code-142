from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

from emllib.dataclass.eml220.dependency_type import SoftwareType
from emllib.dataclass.eml220.distribution_type import DistributionType
from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType
from emllib.dataclass.eml220.key_type_code import KeyTypeCode
from emllib.dataclass.eml220.license_type import LicenseType
from emllib.dataclass.eml220.responsible_party import ResponsibleParty
from emllib.dataclass.eml220.role_type_value import RoleTypeValue
from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.semantic_annotation import SemanticAnnotation
from emllib.dataclass.eml220.single_date_time_type import CitationType, Coverage
from emllib.dataclass.eml220.text_type import TextType


@dataclass
class ProcedureStepType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/methods-2.2.0"

    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
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
    protocol: List["ProtocolType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        },
    )
    instrumentation: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    software: List[SoftwareType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    sub_step: List["ProcedureStepType"] = field(
        default_factory=list,
        metadata={
            "name": "subStep",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ProtocolType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/protocol-2.2.0"

    alternate_identifier: List["ProtocolType.AlternateIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "alternateIdentifier",
            "type": "Element",
            "namespace": "",
        },
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    title: List[I18NNonEmptyStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    creator: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    metadata_provider: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "name": "metadataProvider",
            "type": "Element",
            "namespace": "",
        },
    )
    associated_party: List["ProtocolType.AssociatedParty"] = field(
        default_factory=list,
        metadata={
            "name": "associatedParty",
            "type": "Element",
            "namespace": "",
        },
    )
    pub_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "pubDate",
            "type": "Element",
            "namespace": "",
        },
    )
    language: Optional[I18NNonEmptyStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    abstract: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    keyword_set: List["ProtocolType.KeywordSet"] = field(
        default_factory=list,
        metadata={
            "name": "keywordSet",
            "type": "Element",
            "namespace": "",
        },
    )
    additional_info: List[TextType] = field(
        default_factory=list,
        metadata={
            "name": "additionalInfo",
            "type": "Element",
            "namespace": "",
        },
    )
    intellectual_rights: Optional[TextType] = field(
        default=None,
        metadata={
            "name": "intellectualRights",
            "type": "Element",
            "namespace": "",
        },
    )
    licensed: List[LicenseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    distribution: List[DistributionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    coverage: Optional[Coverage] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    annotation: List[SemanticAnnotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    procedural_step: List[ProcedureStepType] = field(
        default_factory=list,
        metadata={
            "name": "proceduralStep",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["ProtocolType.References"] = field(
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
    class AlternateIdentifier:
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
    class AssociatedParty(ResponsibleParty):
        role: Optional[Union[str, RoleTypeValue]] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )

    @dataclass
    class KeywordSet:
        keyword: List["ProtocolType.KeywordSet.Keyword"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
        keyword_thesaurus: Optional[str] = field(
            default=None,
            metadata={
                "name": "keywordThesaurus",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )

        @dataclass
        class Keyword(I18NNonEmptyStringType):
            keyword_type: Optional[KeyTypeCode] = field(
                default=None,
                metadata={
                    "name": "keywordType",
                    "type": "Attribute",
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
