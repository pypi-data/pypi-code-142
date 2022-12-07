"""The base of the classes."""


from dataclasses import dataclass, field
from typing import Callable, Union, Dict, List, Type
from pyguarantees import severity


@dataclass
class Guarantee:
    parameter_name: str
    where: str = field(init=False)
    guarantee_name: str = field(init=False)
    guaranteed_type: Type = field(init=False)
    qualname: str = field(init=False)
    module: str = field(init=False)

    def enforce(self, arg):
        pass


@dataclass
class TypeGuarantee(Guarantee):
    error_severity: int = severity.ERROR
    force_conversion: bool = False
    error_callback: Callable = None
    check_functions: \
        Union[
            List[Callable],
            Dict[Callable, str],
            Dict[str, Callable]
        ] = None
