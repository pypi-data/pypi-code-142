from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import DataTableType

__NAMESPACE__ = "https://eml.ecoinformatics.org/dataTable-2.2.0"


@dataclass
class DataTable(DataTableType):
    class Meta:
        name = "dataTable"
        namespace = "https://eml.ecoinformatics.org/dataTable-2.2.0"
