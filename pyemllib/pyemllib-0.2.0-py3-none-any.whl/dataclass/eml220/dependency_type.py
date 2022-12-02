from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

from emllib.dataclass.eml220.action import Action
from emllib.dataclass.eml220.distribution_type import DistributionType
from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType
from emllib.dataclass.eml220.key_type_code import KeyTypeCode
from emllib.dataclass.eml220.license_type import LicenseType
from emllib.dataclass.eml220.physical_distribution_type import PhysicalDistributionType
from emllib.dataclass.eml220.research_project_type import ResearchProjectType
from emllib.dataclass.eml220.responsible_party import ResponsibleParty
from emllib.dataclass.eml220.role_type_value import RoleTypeValue
from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.semantic_annotation import SemanticAnnotation
from emllib.dataclass.eml220.single_date_time_type import Coverage
from emllib.dataclass.eml220.text_type import TextType

__NAMESPACE__ = "https://eml.ecoinformatics.org/software-2.2.0"


@dataclass
class DependencyType:
    action: Optional[Action] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    software: Optional["SoftwareType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class SoftwareType:
    alternate_identifier: List["SoftwareType.AlternateIdentifier"] = field(
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
    associated_party: List["SoftwareType.AssociatedParty"] = field(
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
    keyword_set: List["SoftwareType.KeywordSet"] = field(
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
    implementation: List["SoftwareType.Implementation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    dependency: List[DependencyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    license_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "licenseURL",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        },
    )
    license: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
            "sequential": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    project: Optional[ResearchProjectType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["SoftwareType.References"] = field(
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
    class Implementation:
        distribution: List[PhysicalDistributionType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
        size: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        language: List["SoftwareType.Implementation.Language"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        operating_system: List[str] = field(
            default_factory=list,
            metadata={
                "name": "operatingSystem",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        machine_processor: List[str] = field(
            default_factory=list,
            metadata={
                "name": "machineProcessor",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        virtual_machine: Optional[str] = field(
            default=None,
            metadata={
                "name": "virtualMachine",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        disk_usage: Optional[str] = field(
            default=None,
            metadata={
                "name": "diskUsage",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        runtime_memory_usage: Optional[str] = field(
            default=None,
            metadata={
                "name": "runtimeMemoryUsage",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        programming_language: List[str] = field(
            default_factory=list,
            metadata={
                "name": "programmingLanguage",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        checksum: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        dependency: List[DependencyType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class Language:
            language_value: Optional[str] = field(
                default=None,
                metadata={
                    "name": "LanguageValue",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            language_code_standard: Optional[str] = field(
                default=None,
                metadata={
                    "name": "LanguageCodeStandard",
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
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
        keyword: List["SoftwareType.KeywordSet.Keyword"] = field(
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
