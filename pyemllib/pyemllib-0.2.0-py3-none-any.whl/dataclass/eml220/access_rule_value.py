from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/access-2.2.0"


class AccessRuleValue(Enum):
    READ = "read"
    WRITE = "write"
    CHANGE_PERMISSION = "changePermission"
    ALL = "all"
