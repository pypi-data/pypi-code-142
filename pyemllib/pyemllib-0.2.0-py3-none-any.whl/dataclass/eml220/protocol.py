from dataclasses import dataclass

from emllib.dataclass.eml220.procedure_step_type import ProtocolType

__NAMESPACE__ = "https://eml.ecoinformatics.org/protocol-2.2.0"


@dataclass
class Protocol(ProtocolType):
    class Meta:
        name = "protocol"
        namespace = "https://eml.ecoinformatics.org/protocol-2.2.0"
