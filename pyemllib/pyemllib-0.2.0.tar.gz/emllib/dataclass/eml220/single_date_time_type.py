from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod, XmlTime

from emllib.dataclass.eml220.article import Article
from emllib.dataclass.eml220.audio_visual import AudioVisual
from emllib.dataclass.eml220.book import Book
from emllib.dataclass.eml220.chapter import Chapter
from emllib.dataclass.eml220.conference_proceedings import ConferenceProceedings
from emllib.dataclass.eml220.distribution_type import DistributionType
from emllib.dataclass.eml220.generic import Generic
from emllib.dataclass.eml220.geographic_coverage import GeographicCoverage
from emllib.dataclass.eml220.i18n_non_empty_string_type import I18NNonEmptyStringType
from emllib.dataclass.eml220.key_type_code import KeyTypeCode
from emllib.dataclass.eml220.license_type import LicenseType
from emllib.dataclass.eml220.manuscript import Manuscript
from emllib.dataclass.eml220.map import Map
from emllib.dataclass.eml220.personal_communication import PersonalCommunication
from emllib.dataclass.eml220.presentation import Presentation
from emllib.dataclass.eml220.report import Report
from emllib.dataclass.eml220.responsible_party import ResponsibleParty
from emllib.dataclass.eml220.role_type_value import RoleTypeValue
from emllib.dataclass.eml220.scope_type import ScopeType
from emllib.dataclass.eml220.semantic_annotation import SemanticAnnotation
from emllib.dataclass.eml220.taxonomic_classification_type import (
    TaxonomicClassificationType,
)
from emllib.dataclass.eml220.text_type import TextType
from emllib.dataclass.eml220.thesis import Thesis


@dataclass
class SingleDateTimeType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/coverage-2.2.0"

    calendar_date: Optional[Union[XmlPeriod, XmlDate]] = field(
        default=None,
        metadata={
            "name": "calendarDate",
            "type": "Element",
            "namespace": "",
        },
    )
    time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    alternative_time_scale: Optional["SingleDateTimeType.AlternativeTimeScale"] = field(
        default=None,
        metadata={
            "name": "alternativeTimeScale",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class AlternativeTimeScale:
        time_scale_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "timeScaleName",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        time_scale_age_estimate: Optional[str] = field(
            default=None,
            metadata={
                "name": "timeScaleAgeEstimate",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        time_scale_age_uncertainty: Optional[str] = field(
            default=None,
            metadata={
                "name": "timeScaleAgeUncertainty",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        time_scale_age_explanation: Optional[str] = field(
            default=None,
            metadata={
                "name": "timeScaleAgeExplanation",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        time_scale_citation: List["CitationType"] = field(
            default_factory=list,
            metadata={
                "name": "timeScaleCitation",
                "type": "Element",
                "namespace": "",
            },
        )


@dataclass
class TaxonomicCoverage:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/coverage-2.2.0"

    taxonomic_system: Optional["TaxonomicCoverage.TaxonomicSystem"] = field(
        default=None,
        metadata={
            "name": "taxonomicSystem",
            "type": "Element",
            "namespace": "",
        },
    )
    general_taxonomic_coverage: Optional[str] = field(
        default=None,
        metadata={
            "name": "generalTaxonomicCoverage",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    taxonomic_classification: List[TaxonomicClassificationType] = field(
        default_factory=list,
        metadata={
            "name": "taxonomicClassification",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["TaxonomicCoverage.References"] = field(
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
    class TaxonomicSystem:
        classification_system: List["TaxonomicCoverage.TaxonomicSystem.ClassificationSystem"] = field(
            default_factory=list,
            metadata={
                "name": "classificationSystem",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
        identification_reference: List["CitationType"] = field(
            default_factory=list,
            metadata={
                "name": "identificationReference",
                "type": "Element",
                "namespace": "",
            },
        )
        identifier_name: List[ResponsibleParty] = field(
            default_factory=list,
            metadata={
                "name": "identifierName",
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            },
        )
        taxonomic_procedures: Optional[str] = field(
            default=None,
            metadata={
                "name": "taxonomicProcedures",
                "type": "Element",
                "namespace": "",
                "required": True,
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        taxonomic_completeness: Optional[str] = field(
            default=None,
            metadata={
                "name": "taxonomicCompleteness",
                "type": "Element",
                "namespace": "",
                "min_length": 1,
                "pattern": r"[\s]*[\S][\s\S]*",
            },
        )
        vouchers: List["TaxonomicCoverage.TaxonomicSystem.Vouchers"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
            },
        )

        @dataclass
        class ClassificationSystem:
            classification_system_citation: Optional["CitationType"] = field(
                default=None,
                metadata={
                    "name": "classificationSystemCitation",
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )
            classification_system_modifications: Optional[str] = field(
                default=None,
                metadata={
                    "name": "classificationSystemModifications",
                    "type": "Element",
                    "namespace": "",
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )

        @dataclass
        class Vouchers:
            specimen: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                    "min_length": 1,
                    "pattern": r"[\s]*[\S][\s\S]*",
                },
            )
            repository: Optional["TaxonomicCoverage.TaxonomicSystem.Vouchers.Repository"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                    "required": True,
                },
            )

            @dataclass
            class Repository:
                originator: List[ResponsibleParty] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                        "min_occurs": 1,
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


@dataclass
class TemporalCoverage:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/coverage-2.2.0"

    single_date_time: List[SingleDateTimeType] = field(
        default_factory=list,
        metadata={
            "name": "singleDateTime",
            "type": "Element",
            "namespace": "",
        },
    )
    range_of_dates: Optional["TemporalCoverage.RangeOfDates"] = field(
        default=None,
        metadata={
            "name": "rangeOfDates",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["TemporalCoverage.References"] = field(
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
    class RangeOfDates:
        begin_date: Optional[SingleDateTimeType] = field(
            default=None,
            metadata={
                "name": "beginDate",
                "type": "Element",
                "namespace": "",
                "required": True,
            },
        )
        end_date: Optional[SingleDateTimeType] = field(
            default=None,
            metadata={
                "name": "endDate",
                "type": "Element",
                "namespace": "",
                "required": True,
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


@dataclass
class Coverage:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/coverage-2.2.0"

    geographic_coverage: List[GeographicCoverage] = field(
        default_factory=list,
        metadata={
            "name": "geographicCoverage",
            "type": "Element",
            "namespace": "",
        },
    )
    temporal_coverage: List["Coverage.TemporalCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "temporalCoverage",
            "type": "Element",
            "namespace": "",
        },
    )
    taxonomic_coverage: List["Coverage.TaxonomicCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "taxonomicCoverage",
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["Coverage.References"] = field(
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
    class TemporalCoverage(TemporalCoverage):
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
    class TaxonomicCoverage(TaxonomicCoverage):
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


@dataclass
class CitationType:
    class Meta:
        target_namespace = "https://eml.ecoinformatics.org/literature-2.2.0"

    alternate_identifier: List["CitationType.AlternateIdentifier"] = field(
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
    associated_party: List["CitationType.AssociatedParty"] = field(
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
    keyword_set: List["CitationType.KeywordSet"] = field(
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
    contact: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    article: Optional[Article] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    book: Optional[Book] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    chapter: Optional[Chapter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    edited_book: Optional[Book] = field(
        default=None,
        metadata={
            "name": "editedBook",
            "type": "Element",
            "namespace": "",
        },
    )
    manuscript: Optional[Manuscript] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    report: Optional[Report] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    thesis: Optional[Thesis] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    conference_proceedings: Optional[ConferenceProceedings] = field(
        default=None,
        metadata={
            "name": "conferenceProceedings",
            "type": "Element",
            "namespace": "",
        },
    )
    personal_communication: Optional[PersonalCommunication] = field(
        default=None,
        metadata={
            "name": "personalCommunication",
            "type": "Element",
            "namespace": "",
        },
    )
    map: Optional[Map] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    generic: Optional[Generic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    audio_visual: Optional[AudioVisual] = field(
        default=None,
        metadata={
            "name": "audioVisual",
            "type": "Element",
            "namespace": "",
        },
    )
    presentation: Optional[Presentation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    bibtex: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    references: Optional["CitationType.References"] = field(
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
        keyword: List["CitationType.KeywordSet.Keyword"] = field(
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
