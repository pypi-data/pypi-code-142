from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import AttributeListType

__NAMESPACE__ = "https://eml.ecoinformatics.org/attribute-2.2.0"


@dataclass
class AttributeList(AttributeListType):
    class Meta:
        name = "attributeList"
        namespace = "https://eml.ecoinformatics.org/attribute-2.2.0"
