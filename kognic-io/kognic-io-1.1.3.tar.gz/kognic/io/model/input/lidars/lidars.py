from typing import Mapping

from kognic.io.model import PointCloud
from kognic.io.model.input.abstract import BaseInputWithIMUData
from kognic.io.model.input.lidars.frame import Frame
from kognic.io.model.input.metadata.metadata import MetaData


class Lidars(BaseInputWithIMUData):
    external_id: str
    frame: Frame
    metadata: MetaData = dict()

    @property
    def resources(self) -> Mapping[str, PointCloud]:
        return self.frame.resources
