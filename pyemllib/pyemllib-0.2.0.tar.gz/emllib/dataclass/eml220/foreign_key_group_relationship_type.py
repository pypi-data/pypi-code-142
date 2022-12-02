from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/constraint-2.2.0"


class ForeignKeyGroupRelationshipType(Enum):
    IDENTIFYING = "identifying"
    NON_IDENTIFYING = "non-identifying"
