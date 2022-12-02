from typing import List, Optional, Mapping

from kognic.io.model import UnixTimestampNs
from kognic.io.model.input.abstract.base_frame import BaseFrame
from kognic.io.model.input.resources.point_cloud import PointCloud


class Frame(BaseFrame):
    point_clouds: List[PointCloud]
    unix_timestamp: Optional[UnixTimestampNs] = None

    @property
    def resources(self) -> Mapping[str, PointCloud]:
        return {p.resource_id: p for p in self.point_clouds}
