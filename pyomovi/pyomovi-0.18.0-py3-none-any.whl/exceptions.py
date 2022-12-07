from typing import Any, Dict, Iterable, List, Optional, Type, Union, cast

class OMOVIException(Exception):
    _registered_exceptions: List[Type["OMOVIException"]] = []
    default_message = ""

    def __init__(self, *args: Any) -> None:
        super().__init__(*args or [self.default_message])

    def __init_subclass__(cls) -> None:
        cls._registered_exceptions.append(cls)

class InvalidAtomType(OMOVIException):
    def __init__(self, atom_type: str) -> None:
        super().__init__(f"Atom type '{atom_type}' is invalid. See valid atom types with pyomovi.atom_types.keys().")