from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/resource-2.2.0"


class KeyTypeCode(Enum):
    PLACE = "place"
    STRATUM = "stratum"
    TEMPORAL = "temporal"
    THEME = "theme"
    TAXONOMIC = "taxonomic"
