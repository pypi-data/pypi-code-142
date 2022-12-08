from typing import Type
from unittest.mock import Mock

# From unittest.mock
_unsupported_magics = {
    "__getattr__",
    "__setattr__",
    "__init__",
    "__new__",
    "__prepare__",
    "__instancecheck__",
    "__subclasscheck__",
    "__del__",
}


class AccessedError(Exception):
    pass


def inaccessable_mock(cls: Type) -> Type:
    inaccessable_attrs = {
        attr: Mock(side_effect=AccessedError)
        for attr in set(dir(cls)) - _unsupported_magics
    }
    return Mock(cls, **inaccessable_attrs)
