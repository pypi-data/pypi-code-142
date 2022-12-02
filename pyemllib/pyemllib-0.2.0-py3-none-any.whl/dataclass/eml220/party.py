from dataclasses import dataclass

from emllib.dataclass.eml220.responsible_party import ResponsibleParty

__NAMESPACE__ = "https://eml.ecoinformatics.org/party-2.2.0"


@dataclass
class Party(ResponsibleParty):
    class Meta:
        name = "party"
        namespace = "https://eml.ecoinformatics.org/party-2.2.0"
