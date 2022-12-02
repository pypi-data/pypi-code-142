from dataclasses import dataclass

from emllib.dataclass.eml220.physical_type import PhysicalType

__NAMESPACE__ = "https://eml.ecoinformatics.org/physical-2.2.0"


@dataclass
class Physical(PhysicalType):
    class Meta:
        name = "physical"
        namespace = "https://eml.ecoinformatics.org/physical-2.2.0"
