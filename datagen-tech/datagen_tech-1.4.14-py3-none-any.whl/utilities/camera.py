from dataclasses import dataclass
from typing import TypeVar, Union, ClassVar, NamedTuple

import numpy as np

from datagen.api import assets
from datagen.utilities.arrays import to_arrays
from datagen.utilities.extrinsics import Extrinsics

Resolution = NamedTuple('Resolution', x=int, y=int)

Sensor = NamedTuple("Sensor", width=float, height=float)


@dataclass
class Focus:
    focal_length: float
    fov: float

    @classmethod
    def from_focal_length(cls, focal_length: float, sensor_width: float) -> "Focus":
        fov = 2 * np.arctan2(0.5 * sensor_width, focal_length)
        return cls(fov=fov, focal_length=focal_length)

    @classmethod
    def from_fov(cls, fov: float, sensor_width: float) -> "Focus":
        focal_length = sensor_width / (np.tan(fov / 2) * 2)
        return cls(fov=fov, focal_length=focal_length)


@dataclass
class Intrinsics:
    resolution: Resolution
    sensor: Sensor
    focus: Focus
    pxl_aspect_ratio: float

    @property
    def matrix(self):
        pixels_per_mm_h = self.resolution.x / self.sensor.height
        pixels_per_mm_w = self.resolution.y / self.sensor.width
        f_x, f_y = self.focus.focal_length * pixels_per_mm_h, self.focus.focal_length * pixels_per_mm_w
        return np.array(
            [
                [f_x, 0, self.resolution.x / 2],
                [0.0, f_y * self.pxl_aspect_ratio, self.resolution.y / 2],
                [0.0, 0.0, 1.0],
            ]
        )


P = TypeVar("P", bound=Union[assets.Point, np.array])


class CameraUtils:
    PLUGINS_GROUP_NAME: ClassVar[str] = "datagen.plugins.utils.camera"

    def calculate_yaw_pitch_roll(self, camera: Union[assets.Camera, P] = None, look_at_point: P = None) -> np.array:
        camera_location = self._get_camera_location(camera)
        camera_location, look_at_point = to_arrays(camera_location, look_at_point)
        extrinsics = Extrinsics.from_look_at(camera_location, look_at_point)
        return extrinsics.rotation.to_ypr()

    def rotate(self, camera: assets.Camera, look_at_point: P) -> None:
        ypr = self.calculate_yaw_pitch_roll(camera, look_at_point=look_at_point)
        camera.extrinsics.rotation = assets.Rotation.from_ypr(ypr)

    def _get_camera_location(self, camera: Union[assets.Camera, P]) -> P:
        return camera if isinstance(camera, (assets.Point, np.ndarray)) else camera.extrinsics.location

    def get_extrinsic_matrix(self, camera: assets.Camera) -> np.array:
        extrinsics = self._get_extrinsics_from_camera_asset(camera)
        return extrinsics.matrix

    def get_rotation_matrix(self, camera: assets.Camera) -> np.array:
        extrinsics = self._get_extrinsics_from_camera_asset(camera)
        return extrinsics.rotation.matrix

    def _get_extrinsics_from_camera_asset(self, camera: assets.Camera) -> Extrinsics:
        camera_location, yaw_pitch_roll = to_arrays(camera.extrinsics.location, camera.extrinsics.rotation)
        extrinsics = Extrinsics.from_yaw_pitch_roll(camera_location, yaw_pitch_roll)
        return extrinsics
