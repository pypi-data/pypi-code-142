from dataclasses import dataclass

from emllib.dataclass.eml220.access_type import AccessType

__NAMESPACE__ = "https://eml.ecoinformatics.org/access-2.2.0"


@dataclass
class Access(AccessType):
    class Meta:
        name = "access"
        namespace = "https://eml.ecoinformatics.org/access-2.2.0"
