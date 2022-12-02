from typing import List, Mapping

from kognic.io.model import PointCloud
from kognic.io.model.input.abstract import BaseInputWithIMUData
from kognic.io.model.input.lidars_sequence.frame import Frame
from kognic.io.model.input.metadata.metadata import MetaData


class LidarsSequence(BaseInputWithIMUData):
    external_id: str
    frames: List[Frame]
    metadata: MetaData = dict()

    @property
    def resources(self) -> Mapping[str, PointCloud]:
        mappings = [frame.resources for frame in self.frames]
        superset = {}
        for mapping in mappings:
            superset = {**superset, **mapping}
        return superset
