#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Dict, Tuple

import numpy as np
from simulariumio import TrajectoryData


class Calculator(ABC):
    def calculate(self, traj_data: TrajectoryData) -> Tuple[Dict[str, np.ndarray], str]:
        """
        Return the calculated traces and the units label to use.

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate metrics.

        Returns
        -------
        Dict[str, np.ndarray]
            The name of each trace mapped to an array
            of the data for that trace.
        str
            A label for the units, formatted as " (units)".
        """
        return self.traces(traj_data), self.formatted_units(traj_data)

    @abstractmethod
    def traces(self, traj_data: TrajectoryData) -> Dict[str, np.ndarray]:
        pass

    def formatted_units(self, traj_data: TrajectoryData) -> str:
        units = self.units(traj_data)
        return f" ({units})" if units else ""

    @abstractmethod
    def units(self, traj_data: TrajectoryData) -> str:
        pass
