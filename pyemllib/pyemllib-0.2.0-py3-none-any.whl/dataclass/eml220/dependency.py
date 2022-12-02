from dataclasses import dataclass

from emllib.dataclass.eml220.dependency_type import DependencyType

__NAMESPACE__ = "https://eml.ecoinformatics.org/software-2.2.0"


@dataclass
class Dependency(DependencyType):
    class Meta:
        name = "dependency"
        namespace = "https://eml.ecoinformatics.org/software-2.2.0"
