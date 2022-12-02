from typing import List, Mapping

from kognic.io.model.input.abstract.base_frame import BaseFrame
from kognic.io.model.input.resources.image import Image


class Frame(BaseFrame):
    images: List[Image]

    @property
    def resources(self) -> Mapping[str, Image]:
        return {i.resource_id: i for i in self.images}
