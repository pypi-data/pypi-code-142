from dataclasses import dataclass

from emllib.dataclass.eml220.text_type import TextType

__NAMESPACE__ = "https://eml.ecoinformatics.org/documentation-2.2.0"


@dataclass
class Example(TextType):
    class Meta:
        name = "example"
        namespace = "https://eml.ecoinformatics.org/documentation-2.2.0"
