from typing import Dict, List

from kognic.io.model.ego.imu_data import IMUData
from kognic.io.model.input.abstract.base_input import BaseInput


class BaseInputWithIMUData(BaseInput):
    """
    Base class for any input that has IMU data.
    """
    imu_data: List[IMUData] = []

    def to_dict(self, by_alias=True) -> Dict:
        # IMU data is excluded as it's posted separately.
        return self.dict(exclude_none=True,
                         by_alias=by_alias,
                         exclude={'imu_data': True})
