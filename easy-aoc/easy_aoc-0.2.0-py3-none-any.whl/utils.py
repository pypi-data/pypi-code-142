"""Internal utils for easy-aoc."""
import functools
from collections import abc
from typing import Any, TypeAlias, Union

import attrs

RecursiveDict: TypeAlias = abc.Mapping[str, Union[str, int, "RecursiveDict"]]


def serialize(instance: Any) -> dict[str, int | str]:
    """Serialize the instance into a flattened dict.

    :param instance: The `attrs` instance to serialize
    :return: A flattened, serialized dict
    """
    return _flatten(attrs.asdict(instance))


def _flatten(base_dict: RecursiveDict) -> dict[str, int | str]:
    """Flatten the recursive dict into a flat dict.

    Note: If duplicate keys exist, only one key->value pair will remain.

    :param base_dict: The base dict to flatten
    :return: The flattened dict
    """
    flat_dict = {}
    for key, value in base_dict.items():
        if isinstance(value, abc.Mapping):
            flat_dict.update(_flatten(value))
        else:
            flat_dict[key] = value
    return flat_dict


def flat_repr(instance: Any) -> str:
    """Create a user-friendly, flat wrapper for the end user.

    :param instance: The instance to represent
    :return: A flat representation of the instance
    """
    cls_name = type(instance).__name__
    attributes = " ".join(f"{k}={v!r}" for k, v in serialize(instance).items())
    return f"<{cls_name} {attributes}>"


class FlatAttributeMixin:
    """A mixin for flat attribute access on domain models."""

    @functools.cache
    def _as_flatten_dict(self) -> dict[str, int | str]:
        """Get this instance as a flattened dict.

        :return: A flattened dict of the instance.
        """
        return serialize(self)

    def __getattr__(self, attr: str) -> Any:
        """Try accessing the attribute from a flattened representation.

        :param attr: The attribute to get
        :return: The value, if found
        :raises AttributeError: if the attr was not found
        """
        try:
            return self._as_flatten_dict()[attr]
        except KeyError:
            raise AttributeError(
                f"{type(self).__name__!r} has no attribute {attr!r}"
            ) from None
