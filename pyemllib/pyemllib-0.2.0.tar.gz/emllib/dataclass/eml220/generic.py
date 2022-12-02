from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.responsible_party import ResponsibleParty

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class Generic:
    publisher: Optional[ResponsibleParty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    publication_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicationPlace",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    reference_type: Optional[object] = field(
        default=None,
        metadata={
            "name": "referenceType",
            "type": "Element",
            "namespace": "",
        },
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    number_of_volumes: Optional[str] = field(
        default=None,
        metadata={
            "name": "numberOfVolumes",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    total_pages: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalPages",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    total_figures: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalFigures",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    total_tables: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalTables",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    edition: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    original_publication: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalPublication",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    reprint_edition: Optional[str] = field(
        default=None,
        metadata={
            "name": "reprintEdition",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    reviewed_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "reviewedItem",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    isbn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    issn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
