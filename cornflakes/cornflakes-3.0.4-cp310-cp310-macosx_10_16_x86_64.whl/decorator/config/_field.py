from dataclasses import MISSING
from typing import Any, Callable, List, Optional, Union

from cornflakes.decorator._types import WITHOUT_DEFAULT
from cornflakes.decorator.dataclass import Field

_MISSING_TYPE = type(MISSING)


class ConfigField(Field):
    """Instances of dataclasses Field wrapped for configs."""

    __slots__ = (*getattr(Field, "__slots__", ()), "alias")

    def __init__(
        self,
        default: Union[_MISSING_TYPE, Any] = MISSING,
        default_factory: Union[_MISSING_TYPE, Callable] = MISSING,
        init: Optional[bool] = True,
        repr: Optional[bool] = True,
        hash: Optional[Union[bool, _MISSING_TYPE]] = None,
        compare: Optional[bool] = True,
        metadata: Optional[bool] = None,
        kw_only: Union[_MISSING_TYPE, bool] = MISSING,
        validator: Optional[Union[Callable[[str], Any], _MISSING_TYPE]] = MISSING,
        alias: Optional[Union[List[str], str]] = None,
        ignore: Optional[bool] = False,
    ):
        """Init Field method."""
        super().__init__(
            **{
                key: value
                for key, value in (
                    ("default", default),  # type: ignore
                    ("default_factory", default_factory),
                    ("init", init),
                    ("repr", repr),
                    ("hash", hash),
                    ("compare", compare),
                    ("metadata", metadata),
                    ("kw_only", kw_only),
                )
                if key in Field.__init__.__code__.co_varnames
            }
        )
        self.alias = alias
        self.ignore = ignore
        self.validator = validator

    def __repr__(self):
        """Repr Field method."""
        return f"{Field.__repr__(self)[:-1]}," f"alias={self.alias})"


def config_field(
    *,
    default: Union[_MISSING_TYPE, Any] = MISSING,
    default_factory: Union[_MISSING_TYPE, Callable] = MISSING,
    init: Optional[bool] = True,
    repr: Optional[bool] = True,
    hash: Optional[Union[bool, _MISSING_TYPE]] = None,
    compare: Optional[bool] = True,
    metadata: Optional[bool] = None,
    kw_only: Union[_MISSING_TYPE, bool] = MISSING,
    validator: Optional[Union[Callable[[str], Any], _MISSING_TYPE]] = MISSING,
    alias: Optional[Union[List[str], str]] = None,
    ignore: Optional[bool] = False,
    no_default: Optional[bool] = None,
):
    """This function is used instead of exposing Field creation directly.

    So that a type checker can be told (via overloads) that this is a function whose type depends on its parameters.
    This function is used instead of exposing Field creation directly,
    so that a type checker can be told (via overloads) that this is a
    function whose type depends on its parameters.
    """
    if default is not MISSING and default_factory is not MISSING:
        raise ValueError("cannot specify both default and default_factory")

    if default is MISSING and default_factory is MISSING and no_default:
        default_factory = WITHOUT_DEFAULT

    new_field = ConfigField(
        default, default_factory, init, repr, hash, compare, metadata, kw_only, validator, alias, ignore
    )
    return new_field
