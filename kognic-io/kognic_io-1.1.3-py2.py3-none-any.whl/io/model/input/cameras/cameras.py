from typing import Optional, Mapping

from kognic.io.model.input.abstract.base_input import BaseInput
from kognic.io.model.input.cameras.frame import Frame
from kognic.io.model.input.metadata.metadata import MetaData
from kognic.io.model.input.resources import Image
from kognic.io.model.input.sensor_specification import SensorSpecification


class Cameras(BaseInput):
    external_id: str
    frame: Frame
    sensor_specification: Optional[SensorSpecification] = None
    metadata: MetaData = dict()

    @property
    def resources(self) -> Mapping[str, Image]:
        return self.frame.resources
