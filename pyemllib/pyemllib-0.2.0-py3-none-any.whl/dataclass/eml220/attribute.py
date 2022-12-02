from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import AttributeType

__NAMESPACE__ = "https://eml.ecoinformatics.org/attribute-2.2.0"


@dataclass
class Attribute(AttributeType):
    class Meta:
        name = "attribute"
        namespace = "https://eml.ecoinformatics.org/attribute-2.2.0"
