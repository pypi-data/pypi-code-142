from dataclasses import dataclass

from ._base import TypeGuarantee
from pyguarantees.functional_guarantees.classes.util.common_checks import \
    enforce_check_functions, check_type


@dataclass
class IsBool(TypeGuarantee):
    def __post_init__(self):
        self.guarantee_name = "IsBool"
        self.guaranteed_type = bool

    def enforce(self, arg):
        arg = check_type(arg, self)
        enforce_check_functions(arg, self)
        return arg
