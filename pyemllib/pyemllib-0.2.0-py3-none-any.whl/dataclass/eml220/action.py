from enum import Enum

__NAMESPACE__ = "https://eml.ecoinformatics.org/software-2.2.0"


class Action(Enum):
    INSTALL = "install"
    ASSERT = "assert"
