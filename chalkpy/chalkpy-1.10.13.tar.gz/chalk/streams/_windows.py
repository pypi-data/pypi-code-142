from datetime import timedelta
from typing import Any, Callable, Generic, List, Mapping, Optional, Set, Type, TypeVar, Union

import polars as pl

from chalk._validation.feature_validation import FeatureValidation
from chalk.utils.collections import ensure_tuple
from chalk.utils.duration import Duration, parse_chalk_duration, timedelta_to_duration

T = TypeVar("T")


class WindowedInstance:
    def __init__(self, values: Mapping[str, T]):
        self.values = values

    def __call__(self, period: str):
        return self.values[period]


class WindowedMeta(type):
    _kind: Type[T]

    def __getitem__(cls, underlying: Type[T]) -> "Windowed[Type[T]]":
        cls._kind = underlying
        return Windowed(
            buckets=[],
            mode=None,
            description=None,
            owner=None,
            tags=None,
            name=None,
            max_staleness=None,
            version=None,
            etl_offline_to_online=None,
            encoder=None,
            decoder=None,
            min=None,
            max=None,
            min_length=None,
            max_length=None,
            contains=None,
            dtype=None,
        )  # noqa


JsonValue = TypeVar("JsonValue")


def _stream_fqn_from_seconds(name: str, seconds: int) -> str:
    return f"{name}__{seconds}__"


def _stream_fqn_from_duration(name: str, duration: str) -> str:
    seconds = int(parse_chalk_duration(duration).total_seconds())
    return f"{name}__{seconds}__"


class Windowed(Generic[T], metaclass=WindowedMeta):
    _kind: Type[T]
    _buckets: List[str]
    _mode: Optional[str]
    _description: Optional[str]
    _owner: Optional[str]
    _tags: Optional[Any]
    _name: Optional[str]
    _version: Optional[int]
    _etl_offline_to_online: Optional[bool]
    _encoder: Optional[Callable[[T], JsonValue]]
    _decoder: Optional[Callable[[JsonValue], T]]
    _min: Optional[T]
    _max: Optional[T]
    _min_length: Optional[int]
    _max_length: Optional[int]
    _contains: Optional[T]
    _dtype: Optional[Union[Type[pl.DataType], pl.DataType]]

    @property
    def buckets_seconds(self) -> Set[int]:
        return set(int(parse_chalk_duration(bucket).total_seconds()) for bucket in self._buckets)

    def _get_feature(
        self,
        bucket: str,
        default_name: str,
    ):
        from chalk.features import Feature

        fqn = _stream_fqn_from_duration(self._name or default_name, bucket)

        return Feature(
            name=fqn,
            version=self._version,
            owner=self._owner,
            tags=None if self._tags is None else list(ensure_tuple(self._tags)),
            description=self._description,
            primary=False,
            max_staleness=timedelta_to_duration(self._max_staleness)
            if isinstance(self._max_staleness, timedelta)
            else self._max_staleness,
            etl_offline_to_online=self._etl_offline_to_online,
            encoder=self._encoder,
            decoder=self._decoder,
            polars_dtype=self._dtype,
            validations=FeatureValidation(
                min=self._min,
                max=self._max,
                min_length=self._min_length,
                max_length=self._max_length,
                contains=self._contains,
            ),
        )

    def __init__(
        self,
        buckets: List[str],
        mode: Optional[str],
        description: Optional[str],
        owner: Optional[str],
        tags: Optional[Any],
        name: Optional[str],
        max_staleness: Optional[Duration],
        version: Optional[int],
        etl_offline_to_online: Optional[bool],
        encoder: Optional[Callable[[T], JsonValue]],
        decoder: Optional[Callable[[JsonValue], T]],
        min: Optional[T],
        max: Optional[T],
        min_length: Optional[int],
        max_length: Optional[int],
        contains: Optional[T],
        dtype: Optional[Union[Type[pl.DataType], pl.DataType]],
    ):
        self._buckets = buckets
        self._mode = mode
        self._description = description
        self._owner = owner
        self._tags = tags
        self._name = name
        self._max_staleness = max_staleness
        self._description = description
        self._version = version
        self._etl_offline_to_online = etl_offline_to_online
        self._encoder: Optional[Callable[[T], JsonValue]] = encoder
        self._decoder: Optional[Callable[[JsonValue], T]] = decoder
        self._min: Optional[T] = min
        self._max: Optional[T] = max
        self._min_length: Optional[int] = min_length
        self._max_length: Optional[int] = max_length
        self._contains: Optional[T] = contains
        self._dtype: Optional[Union[Type[pl.DataType], pl.DataType]] = dtype

    def __getitem__(self, window: str) -> Type[T]:
        return self._get_feature(window, self._name)

        return SelectedWindow(kind=self, selected=window)  # noqa

    def __call__(self, window: str) -> Type[T]:
        return self[window]


class SelectedWindow:
    def __init__(self, kind: Windowed, selected: str):
        self.windowed = kind
        self.selected = selected


def windowed(
    *buckets: str,
    mode: Optional[str] = None,
    description: Optional[str] = None,
    owner: Optional[str] = None,
    tags: Optional[Any] = None,
    name: Optional[str] = None,
    max_staleness: Optional[Duration] = None,
    version: Optional[int] = None,
    etl_offline_to_online: Optional[bool] = None,
    encoder: Optional[Callable[[T], JsonValue]] = None,
    decoder: Optional[Callable[[JsonValue], T]] = None,
    min: Optional[T] = None,
    max: Optional[T] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    contains: Optional[T] = None,
    dtype: Optional[Union[Type[pl.DataType], pl.DataType]] = None,
) -> Windowed[T]:
    return Windowed(
        list(buckets),
        mode=mode,
        description=description,
        owner=owner,
        tags=tags,
        name=name,
        max_staleness=max_staleness,
        version=version,
        etl_offline_to_online=etl_offline_to_online,
        encoder=encoder,
        decoder=decoder,
        min=min,
        max=max,
        min_length=min_length,
        max_length=max_length,
        contains=contains,
        dtype=dtype,
    )
