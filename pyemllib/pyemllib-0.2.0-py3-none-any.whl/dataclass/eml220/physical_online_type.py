from dataclasses import dataclass, field
from typing import Optional

from emllib.dataclass.eml220.connection_type import ConnectionType
from emllib.dataclass.eml220.url_type import UrlType

__NAMESPACE__ = "https://eml.ecoinformatics.org/physical-2.2.0"


@dataclass
class PhysicalOnlineType:
    online_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "onlineDescription",
            "type": "Element",
            "namespace": "",
            "min_length": 1,
            "pattern": r"[\s]*[\S][\s\S]*",
        },
    )
    url: Optional[UrlType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    connection: Optional[ConnectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
