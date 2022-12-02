from dataclasses import dataclass

from emllib.dataclass.eml220.dependency_type import SoftwareType

__NAMESPACE__ = "https://eml.ecoinformatics.org/software-2.2.0"


@dataclass
class Software(SoftwareType):
    class Meta:
        name = "software"
        namespace = "https://eml.ecoinformatics.org/software-2.2.0"
