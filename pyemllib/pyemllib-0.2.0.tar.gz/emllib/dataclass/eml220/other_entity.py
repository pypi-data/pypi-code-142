from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import OtherEntityType

__NAMESPACE__ = "https://eml.ecoinformatics.org/entity-2.2.0"


@dataclass
class OtherEntity(OtherEntityType):
    class Meta:
        name = "otherEntity"
        namespace = "https://eml.ecoinformatics.org/entity-2.2.0"
