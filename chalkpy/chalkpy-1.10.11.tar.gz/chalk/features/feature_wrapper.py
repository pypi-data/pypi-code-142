from __future__ import annotations

import copy
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Optional, TypeVar, cast

from chalk.features.filter import Filter
from chalk.serialization.parsed_annotation import ParsedAnnotation
from chalk.streams import Windowed
from chalk.streams._windows import _stream_fqn_from_duration
from chalk.utils.collections import ensure_tuple

if TYPE_CHECKING:
    from chalk.features.feature_field import Feature

T = TypeVar("T")

__all__ = ["FeatureWrapper", "unwrap_feature"]


class FeatureWrapper:
    """
    FeatureWrapper emulates DataFrames and
    nested has-one relationships when used
    as a type annotation or within a filter.
    """

    def __init__(self, feature: Feature) -> None:
        # Binding as a private variable as not to have naming conflicts user's use of __getattr__
        self._chalk_feature = feature

    def __hash__(self):
        return hash(self._chalk_feature)

    def __gt__(self, other: object):
        return Filter(self._chalk_feature, ">", other)

    def __ge__(self, other: object):
        return Filter(self._chalk_feature, ">=", other)

    def __lt__(self, other: object):
        return Filter(self._chalk_feature, "<", other)

    def __le__(self, other: object):
        return Filter(self._chalk_feature, "<=", other)

    def _cmp(self, op: str, other: object):
        from chalk.features.feature_field import Feature

        if isinstance(other, Feature):
            # If comparing against a feature directly, then we know it's not being used in a join condition
            # Since join conditions would be against another FeatureWrapper or a literal value
            is_eq = self._chalk_feature == other
            # They are the same feature. Short-circuit and return a boolean
            if op == "==" and is_eq:
                return True
            if op == "!=" and not is_eq:
                return False
            return NotImplemented  # GT / LT doesn't really make sense otherwise
        return Filter(self._chalk_feature, op, other)

    def __ne__(self, other: object):
        return self._cmp("!=", other)

    def __eq__(self, other: object):
        return self._cmp("==", other)

    def __and__(self, other: object):
        return self._cmp("and", other)

    def __or__(self, other: object):
        if other is None:
            return Optional[self]
        return self._cmp("or", other)

    def __repr__(self):
        return f"FeatureWrapper(fqn={self._chalk_feature.namespace}.{self._chalk_feature.name}, typ={self._chalk_feature.typ})"

    def __str__(self):
        return str(self._chalk_feature)

    def in_(self, examples: Iterable):
        return self._cmp("in", examples)

    def __call__(self, *args, **kwargs):
        if isinstance(self._chalk_feature.typ.underlying, Windowed):
            arg = None

            if len(args) == 0 and len(kwargs) == 1:
                keyword, arg = kwargs.popitem()
                if keyword != "window":
                    raise TypeError(f"Unsupported keyword argument for windowed feature: '{keyword}'")

            elif len(args) == 1 and len(kwargs) == 0:
                arg = args[0]

            elif len(args) + len(kwargs) > 1:
                raise TypeError(
                    f"Only one window can be specified for requesting window features, "
                    f"but {args=} and {kwargs=} were specified for '{self._chalk_feature.root_fqn}'."
                )

            wind: Windowed = cast(Windowed, self._chalk_feature.typ.underlying)
            if arg is None:
                raise TypeError(
                    f"Missing window duration for '{self._chalk_feature.root_fqn}'. "
                    f"{', '.join(wind._buckets)} are supported."
                )

            from chalk.features import FeatureSetBase

            parent = (
                FeatureSetBase.registry[self._chalk_feature.namespace]
                if len(self._chalk_feature.path) == 0
                else FeatureWrapper(self._chalk_feature.path[-1].parent)
            )
            desired_feature_name = _stream_fqn_from_duration(self._chalk_feature.name, arg)
            if not hasattr(parent, desired_feature_name):
                raise TypeError(
                    f"Unsupported window duration '{arg}' for '{self._chalk_feature.root_fqn}'. "
                    f"{', '.join(wind._buckets)} are supported."
                )
            return getattr(parent, desired_feature_name)

        return self

    def __getitem__(self, item: Any):
        from chalk.features.dataframe import DataFrame

        if isinstance(self._chalk_feature.typ.underlying, Windowed):
            return self.__call__(*ensure_tuple(item))

        if self._chalk_feature.typ is not None and issubclass(self._chalk_feature.typ.parsed_annotation, DataFrame):
            f_copy = FeatureWrapper(copy.copy(self._chalk_feature))

            f_copy._chalk_feature.typ = ParsedAnnotation(underlying=self._chalk_feature.typ.parsed_annotation[item])

            return f_copy

        raise TypeError(f"Feature {self} does not support subscripting")

    def __getattr__(self, item: str):
        from chalk.features.feature_field import Feature
        from chalk.features.feature_set import Features

        # Passing through __getattr__ on has_one features, as users can use getattr
        # notation in annotations for resolvers
        if item.startswith("__"):
            # Short-circuiting on the dunders to be compatible with copy.copy
            raise AttributeError(item)

        if self._chalk_feature.typ is not None and issubclass(self._chalk_feature.typ.underlying, Features):
            for f in self._chalk_feature.typ.underlying.features:
                assert isinstance(f, Feature), f"HasOne feature {f} does not inherit from FeaturesBase"
                if f.attribute_name == item:
                    return FeatureWrapper(self._chalk_feature.copy_with_path(f))
        raise AttributeError(f"'{self}' has no attribute '{item}'")


def unwrap_feature(maybe_feature_wrapper: Any) -> Feature:
    """Unwrap a class-annotated FeatureWrapper instance into the underlying feature.

    For example:

    .. code-block::

        @features
        class FooBar:
            foo: str
            bar: int

        type(FooBar.foo) is FeatureWrapper
        type(unwrap_feature(FooBar.foo)) is Feature
    """
    from chalk.features.feature_field import Feature

    if isinstance(maybe_feature_wrapper, FeatureWrapper):
        maybe_feature_wrapper = maybe_feature_wrapper._chalk_feature
    if isinstance(maybe_feature_wrapper, Feature):
        return maybe_feature_wrapper
    raise TypeError(
        f"{maybe_feature_wrapper} is of type {type(maybe_feature_wrapper).__name__}, expecting type FeatureWrapper"
    )
