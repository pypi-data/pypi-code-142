from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import MethodsType

__NAMESPACE__ = "https://eml.ecoinformatics.org/methods-2.2.0"


@dataclass
class Methods(MethodsType):
    class Meta:
        name = "methods"
        namespace = "https://eml.ecoinformatics.org/methods-2.2.0"
