from enum import Enum
import ipaddress
from typing import List, Union

IPAddr = Union[ipaddress.IPv4Address, ipaddress.IPv6Address]
IPAddrList = List[IPAddr]


class MRTTypes(Enum):
    RIBS = 1
    UPDATES = 2
