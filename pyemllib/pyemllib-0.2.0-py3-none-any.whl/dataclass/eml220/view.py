from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import ViewType

__NAMESPACE__ = "https://eml.ecoinformatics.org/view-2.2.0"


@dataclass
class View(ViewType):
    class Meta:
        name = "view"
        namespace = "https://eml.ecoinformatics.org/view-2.2.0"
