from typing import List, Optional, Mapping

from kognic.io.model.input.abstract import BaseInputWithIMUData
from kognic.io.model.input.lidars_and_cameras_sequence.frame import Frame
from kognic.io.model.input.metadata.metadata import MetaData
from kognic.io.model.input.resources.resource import Resource
from kognic.io.model.input.sensor_specification import SensorSpecification


class LidarsAndCamerasSequence(BaseInputWithIMUData):
    external_id: str
    frames: List[Frame]
    calibration_id: str
    sensor_specification: Optional[SensorSpecification] = None
    metadata: MetaData = dict()

    @property
    def resources(self) -> Mapping[str, Resource]:
        mappings = [frame.resources for frame in self.frames]
        superset = {}
        for mapping in mappings:
            superset = {**superset, **mapping}
        return superset
