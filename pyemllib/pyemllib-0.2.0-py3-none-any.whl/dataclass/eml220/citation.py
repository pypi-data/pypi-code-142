from dataclasses import dataclass

from emllib.dataclass.eml220.single_date_time_type import CitationType

__NAMESPACE__ = "https://eml.ecoinformatics.org/literature-2.2.0"


@dataclass
class Citation(CitationType):
    class Meta:
        name = "citation"
        namespace = "https://eml.ecoinformatics.org/literature-2.2.0"
