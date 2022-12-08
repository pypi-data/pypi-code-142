"""`Adict` is an attribute-accessible dynamic dict wrapper, which allows to access dict items in
attribute notation (".") and allows friendly checks for non-existing items.
"""

from collections.abc import MutableMapping
import json
from typing import Any, Dict, Iterator, Optional, TYPE_CHECKING


__NONE__ = object()


# only py>=39 supports correct type hinting MutableMapping[Any, Any]
class Adict(MutableMapping):  # type: ignore
    """Attribute-accessible implementation of a dictionary."""

    def __init__(self, base: Optional[Dict[Any, Any]] = None, **kwargs: Any):
        """Construct a dynamic dictionary from an existing or an empty base dictionary.

        Args:
            base (dict): The dictionary from which the dynamic dict is constructed from.
        """
        self.__dict: Dict[Any, Any] = base if base is not None else {}
        self.__dict.update(kwargs)

    # dict function overrides

    def __getitem__(self, key: Any) -> Any:
        """Return items using the [] notation from the contained dict. """
        item = self.__getattr__(key)
        if item is None:
            raise KeyError(key)
        return item

    def __setitem__(self, key: Any, value: Any) -> None:
        """Write items using the [] notation into the contained dict."""
        self.__dict[key] = value

    def __delitem__(self, key: Any) -> None:
        del self.__dict[key]

    def __iter__(self) -> Iterator[Any]:
        return iter(self.__dict)

    def __len__(self) -> int:
        return len(self.__dict)

    # object overrides to make the attribute accessible

    def __getattr__(self, item: Any) -> Any:
        """Retrieve the value for the given attribute name from the dict.

        When the value is a dictionary, it is wrapped in another Adict instance.

        Note: __getattr__ is only for the attributes, not defined by the class,
        __getattribute__ catches all atrtibutes.
        """
        if item in self.__dict:
            value = self.__dict[item]
            if isinstance(value, dict):
                return Adict(value)
            return value
        return None

    def __setattr__(self, key: str, value: Any) -> None:
        """Store all attributes in the dictionary, except the explicit attributes.

        Note: Different from __getattr__(), __setattr__() overwrites _all_ attributes setting,
              not only the ones which don't have an object member. So __setattr__() is the
              counterpart of __getattribute__().
        """
        if key.startswith(f'_{type(self).__name__}__'):
            super().__setattr__(key, value)
        else:
            if isinstance(value, dict):
                self.__dict[key] = Adict(value)
            else:
                self.__dict[key] = value

    def __delattr__(self, key: str) -> None:
        if key in self.__dict:
            del self.__dict[key]

    # bool and str overrides

    def __bool__(self) -> bool:
        return bool(self.__dict)

    def __str__(self) -> str:
        """String is the dictionoary as string."""
        return self.__dict.__str__()

    def __repr__(self) -> str:
        """Representation is the dictionaries representation."""
        return self.__dict.__repr__()

    if TYPE_CHECKING:  # pragma: no cover
        __dict__ = {}  # type: Dict[Any, Any]
    else:
        @property
        def __dict__(self) -> Dict[Any, Any]:
            """Dict representation is the contained dictonary."""
            return self.__dict

    # safe accessing
    def __call__(self, key: str, default: Any = __NONE__) -> Any:
        value = self.__getattr__(key)
        if value is not None:
            return value

        if default is not __NONE__:
            if isinstance(default, dict):
                return Adict(default)
            return default
        return Adict()


class JsonEncoder(json.encoder.JSONEncoder):
    """Basic Json Encoder, which transforms any Adict elements into back into their __dict__
       representation. Additionally, we transform any other types into their str()
       representation."""

    def default(self, o: object) -> Any:
        if isinstance(o, Adict):
            return o.__dict__
        return str(o)
