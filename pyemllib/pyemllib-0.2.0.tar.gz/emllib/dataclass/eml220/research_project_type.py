from dataclasses import dataclass, field
from typing import List, Optional, Union

from emllib.dataclass.eml220.award_type import AwardType
from emllib.dataclass.eml220.descriptor_type_value import DescriptorTypeValue
from emllib.dataclass.eml220.responsible_party import ResponsibleParty
from emllib.dataclass.eml220.role_type_value import RoleTypeValue
from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.single_date_time_type import CitationType, Coverage
from emllib.dataclass.eml220.text_type import TextType

__NAMESPACE__ = "https://eml.ecoinformatics.org/project-2.2.0"


@dataclass
class ResearchProjectType:
    title: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    personnel: List["ResearchProjectType.Personnel"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    abstract: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    funding: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    award: List[AwardType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    study_area_description: Optional["ResearchProjectType.StudyAreaDescription"] = field(
        default=None,
        metadata={
            "name": "studyAreaDescription",
            "type": "Element",
            "namespace": "",
        },
    )
    design_description: Optional["ResearchProjectType.DesignDescription"] = field(
        default=None,
        metadata={
            "name": "designDescription",
            "type": "Element",
            "namespace": "",
        },
    )
    related_project: List["ResearchProjectType"] = field(
        default_factory=list,
        metadata={
            "name": "relatedProject",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["ResearchProjectType.References"] = field(
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
    class Personnel(ResponsibleParty):
        role: List[Union[str, RoleTypeValue]] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )

    @dataclass
    class StudyAreaDescription:
        descriptor: List["ResearchProjectType.StudyAreaDescription.Descriptor"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        citation: List[CitationType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        coverage: List[Coverage] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class Descriptor:
            descriptor_value: List["ResearchProjectType.StudyAreaDescription.Descriptor.DescriptorValue"] = field(
                default_factory=list,
                metadata={
                    "name": "descriptorValue",
                    "type": "Element",
                    "namespace": "",
                    "min_occurs": 1,
                    "sequential": True,
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
            name: Optional[Union[str, DescriptorTypeValue]] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                },
            )
            citable_classification_system: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "citableClassificationSystem",
                    "type": "Attribute",
                    "required": True,
                },
            )

            @dataclass
            class DescriptorValue:
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                name_or_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                    },
                )

    @dataclass
    class DesignDescription:
        description: List[TextType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )
        citation: List[CitationType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
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
