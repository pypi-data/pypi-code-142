from dataclasses import dataclass

from emllib.dataclass.eml220.attribute_type import DatasetType

__NAMESPACE__ = "https://eml.ecoinformatics.org/dataset-2.2.0"


@dataclass
class Dataset(DatasetType):
    class Meta:
        name = "dataset"
        namespace = "https://eml.ecoinformatics.org/dataset-2.2.0"
