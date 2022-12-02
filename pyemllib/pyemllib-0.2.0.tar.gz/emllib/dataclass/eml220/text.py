from dataclasses import dataclass

from emllib.dataclass.eml220.text_type import TextType

__NAMESPACE__ = "https://eml.ecoinformatics.org/text-2.2.0"


@dataclass
class Text(TextType):
    class Meta:
        name = "text"
        namespace = "https://eml.ecoinformatics.org/text-2.2.0"
