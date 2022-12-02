from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/access-2.2.0"


class AccessTypeOrder(Enum):
    ALLOW_FIRST = "allowFirst"
    DENY_FIRST = "denyFirst"
