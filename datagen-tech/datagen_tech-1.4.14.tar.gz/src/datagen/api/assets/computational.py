import abc
from typing import TypeVar, Type

import numpy as np
from pydantic import BaseModel, Field

from datagen.config import assets as assets_conf

T = TypeVar("T", bound="ComputationalAsset")


class ComputationalAsset(BaseModel, abc.ABC):
    @abc.abstractmethod
    def to_ndarray(self) -> np.ndarray:
        ...

    @classmethod
    @abc.abstractmethod
    def from_ndarray(cls: Type[T], arr: np.ndarray) -> T:
        ...


class Point(ComputationalAsset):
    x: float = Field(ge=-5.0, le=5.0)
    y: float = Field(ge=-5.0, le=5.0)
    z: float = Field(ge=-5.0, le=5.0)

    def to_ndarray(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z])

    @classmethod
    def from_ndarray(cls, arr: np.ndarray):
        return Point(x=arr[0], y=arr[1], z=arr[2])


class Vector(ComputationalAsset):
    x: float = Field(ge=-5.0, le=5.0)
    y: float = Field(ge=-5.0, le=5.0)
    z: float = Field(ge=-5.0, le=5.0)

    def to_ndarray(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z])

    @classmethod
    def from_ndarray(cls, arr: np.ndarray):
        return Vector(x=arr[0], y=arr[1], z=arr[2])


class Rotation(ComputationalAsset):
    yaw: float
    roll: float
    pitch: float

    def to_ndarray(self) -> np.ndarray:
        return self.to_ypr()

    def to_ypr(self) -> np.ndarray:
        return np.array([self.yaw, self.pitch, self.roll])

    @classmethod
    def from_ndarray(cls, arr: np.ndarray):
        return cls.from_ypr(arr)

    @classmethod
    def from_ypr(cls, arr: np.ndarray):
        return Rotation(yaw=arr[0], pitch=arr[1], roll=arr[2])
