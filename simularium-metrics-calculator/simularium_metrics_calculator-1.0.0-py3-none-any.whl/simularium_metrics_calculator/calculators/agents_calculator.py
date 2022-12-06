#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List

import numpy as np
from simulariumio import TrajectoryData

from .calculator import Calculator


class AgentsCalculator(Calculator):
    def __init__(self, time_indices: List[int] = None):
        """
        Calculates the agent IDs at the given timestep.

        Parameters
        ----------
        time_indices: List[int]
            Which time step(s) to use.
            Default: first step
        """
        self.time_indices = time_indices

    def traces(self, traj_data: TrajectoryData) -> Dict[str, np.ndarray]:
        """
        Return the agent IDs at the given time step.

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate metrics.

        Returns
        -------
        Dict[str, np.ndarray]
            The name of each trace mapped
            to an array of the data for that trace
        """
        time_units = str(traj_data.time_units)
        if self.time_indices is None:
            self.time_indices = [0]
        traces = {}
        for time_index in self.time_indices:
            time = traj_data.agent_data.times[time_index]
            trace_name = f"t = {time} {time_units}"
            traces[trace_name] = traj_data.agent_data.unique_ids[time_index]
        return traces

    def units(self, traj_data: TrajectoryData) -> str:
        """
        Return a string label for the units to use on the axis title

        Parameters
        ----------
        traj_data: TrajectoryData
            Trajectory data for which to calculate the metric

        Returns
        -------
        str
            A label for the units
        """
        return ""
