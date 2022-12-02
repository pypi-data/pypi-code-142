from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import StoredProcedureType

__NAMESPACE__ = "https://eml.ecoinformatics.org/storedProcedure-2.2.0"


@dataclass
class StoredProcedure(StoredProcedureType):
    class Meta:
        name = "storedProcedure"
        namespace = "https://eml.ecoinformatics.org/storedProcedure-2.2.0"
