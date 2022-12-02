from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "https://eml.ecoinformatics.org/coverage-2.2.0"


@dataclass
class TaxonomicClassificationType:
    taxon_rank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonRankName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    taxon_rank_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxonRankValue",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    common_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "commonName",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    taxon_id: List["TaxonomicClassificationType.TaxonId"] = field(
        default_factory=list,
        metadata={
            "name": "taxonId",
            "type": "Element",
            "namespace": "",
        },
    )
    taxonomic_classification: List["TaxonomicClassificationType"] = field(
        default_factory=list,
        metadata={
            "name": "taxonomicClassification",
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
    class TaxonId:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        provider: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
