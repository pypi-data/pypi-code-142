from __future__ import annotations

import copy
import re
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Optional, TypeVar

from chalk.features.filter import Filter
from chalk.serialization.parsed_annotation import ParsedAnnotation
from chalk.streams import Windowed
from chalk.streams._windows import _stream_fqn_from_duration

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

    def __call__(self, *args, **kwargs):
        # We need to be callable to write `Optional[FeatureClass.x]`
        # if isinstance(self._chalk_feature.typ.underlying, Windowed):
        #     return self._chalk_feature.typ.underlying(*args, **kwargs)
        if isinstance(self._chalk_feature.typ.underlying, Windowed):
            desired_feature_name = _stream_fqn_from_duration(self._chalk_feature.name, args[0])
            from chalk.features import FeatureSetBase

            if len(self._chalk_feature.path) == 0:
                return getattr(FeatureSetBase.registry[self._chalk_feature.namespace], desired_feature_name)
            else:
                return getattr(FeatureWrapper(self._chalk_feature.path[-1].parent), desired_feature_name)

        return self

    # def __call__(self, *args, **kwargs):
    #     # Only Windowed[T] should invoke call
    #     #   class User:
    #     #     logins: Windowed[int] = windowed("10m")
    #     #
    #     #   def fn(x: User.logins("10m")) -> ...
    #     return self._chalk_feature.typ.underlying(*args, **kwargs)

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

    def __getitem__(self, item: Any):
        from chalk.features.dataframe import DataFrame

        if self._chalk_feature.typ is not None and issubclass(self._chalk_feature.typ.parsed_annotation, DataFrame):
            f_copy = FeatureWrapper(copy.copy(self._chalk_feature))

            f_copy._chalk_feature.typ = ParsedAnnotation(underlying=self._chalk_feature.typ.parsed_annotation[item])

            return f_copy

        if self._chalk_feature.typ is not None and issubclass(self._chalk_feature.typ.parsed_annotation, Windowed):
            # TODO: Support this syntax
            base_name = re.sub(r"__[0-9a-zA-Z]+__$", "", str(self))
            raise AttributeError(
                f"Windows should be accessed via " f"{base_name}('{str(item)}'), not {base_name}['{str(item)}']"
            )

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
