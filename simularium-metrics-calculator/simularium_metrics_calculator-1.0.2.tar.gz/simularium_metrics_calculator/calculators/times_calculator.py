#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

import numpy as np
from simulariumio import TrajectoryData

from .calculator import Calculator


class TimesCalculator(Calculator):
    def __init__(self, stride: int = 1):
        """
        Calculates the times over the course of the trajectory.

        Parameters
        ----------
        stride: int (optional)
            use every nth time step.
            Default: 1
        """
        self.stride = stride

    def traces(self, traj_data: TrajectoryData) -> Dict[str, np.ndarray]:
        """
        Return the time at each time step.

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate metrics.

        Returns
        -------
        Dict[str, np.ndarray]
            The name of each trace mapped
            to an array of the data for that trace.
        """
        return {"Time": traj_data.agent_data.times[:: self.stride]}

    def units(self, traj_data: TrajectoryData) -> str:
        """
        Return a string label for the units to use on the axis title.

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate the metric.

        Returns
        -------
        str
            A label for the units.
        """
        return str(traj_data.time_units)
