from typing import List, Optional, Mapping

from kognic.io.model.input.abstract.base_input import BaseInput
from kognic.io.model.input.cameras_sequence.frame import Frame
from kognic.io.model.input.metadata.metadata import MetaData
from kognic.io.model.input.resources import Image
from kognic.io.model.input.sensor_specification import SensorSpecification


class CamerasSequence(BaseInput):
    external_id: str
    frames: List[Frame]
    sensor_specification: Optional[SensorSpecification] = None
    metadata: MetaData = dict()

    @property
    def resources(self) -> Mapping[str, Image]:
        mappings = [frame.resources for frame in self.frames]
        superset = {}
        for mapping in mappings:
            superset = {**superset, **mapping}
        return superset
