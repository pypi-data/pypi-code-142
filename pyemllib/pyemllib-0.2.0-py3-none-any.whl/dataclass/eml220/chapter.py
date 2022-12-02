from dataclasses import dataclass, field
from typing import List, Optional

from emllib.dataclass.eml220.book import Book
from emllib.dataclass.eml220.responsible_party import ResponsibleParty

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class Chapter(Book):
    chapter_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "chapterNumber",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    editor: List[ResponsibleParty] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    book_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "bookTitle",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    page_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "pageRange",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
