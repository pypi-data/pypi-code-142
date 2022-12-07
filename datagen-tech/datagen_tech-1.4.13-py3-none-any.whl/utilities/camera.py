from typing import TypeVar, Union, ClassVar, Optional

import numpy as np

from datagen.dev import mutually_exclusive
from datagen.api import assets
from datagen.utilities.arrays import to_ndarrays
from datagen.utilities.extrinsics import Extrinsics

P = TypeVar("P", bound=Union[assets.Point, np.array])


class CameraUtils:
    PLUGINS_GROUP_NAME: ClassVar[str] = "utils.api.camera"

    @mutually_exclusive("camera", "camera_location")
    def calculate_yaw_pitch_roll(
        self, camera: assets.Camera = None, camera_location: P = None, look_at_point: P = None
    ) -> np.array:
        camera_location = self._get_camera_location(camera, camera_location)
        camera_coords, look_at_coords = to_ndarrays(camera_location, look_at_point)
        extrinsics = Extrinsics.from_look_at(camera_coords, look_at_coords)
        return extrinsics.rotation.to_ypr()

    def set_rotation(self, camera: assets.Camera, look_at_point: P) -> None:
        ypr = self.calculate_yaw_pitch_roll(camera, look_at_point=look_at_point)
        camera.extrinsic_params.rotation = assets.Rotation.from_ypr(ypr)

    def _get_camera_location(self, camera: Optional[assets.Camera], camera_location: Optional[P]) -> P:
        return camera_location if camera_location is not None else camera.extrinsic_params.location
