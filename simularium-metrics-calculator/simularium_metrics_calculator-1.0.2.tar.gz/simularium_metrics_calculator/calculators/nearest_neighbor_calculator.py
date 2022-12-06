#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List

import numpy as np
import scipy
from simulariumio import TrajectoryData

from .calculator import Calculator


class NearestNeighborCalculator(Calculator):
    def __init__(self, time_indices: List[int] = None):
        """
        Calculates the distance to the nearest neighbor for each agent
        at a given time index.

        Parameters
        ----------
        time_indices: List[int]
            Which time step(s) to use.
            Default: first and last
        """
        self.time_indices = time_indices

    @staticmethod
    def _nearest_neighbor_distances(positions: np.ndarray) -> np.ndarray:
        """
        Distance to nearest neighbor for each position.
        """
        dist_grid = scipy.spatial.distance.cdist(positions, positions)
        masked_grid = np.ma.array(dist_grid, mask=np.eye(len(positions)))
        return np.min(masked_grid, axis=1).data

    def _set_default_time_indices(self, times: np.ndarray) -> List[int]:
        """
        Get a list of the first and last time indices.
        """
        total_steps = len(times)
        if total_steps < 2:
            return [0]
        else:
            return [0, len(times) - 1]

    def traces(self, traj_data: TrajectoryData) -> Dict[str, np.ndarray]:
        """
        Return the distance to the nearest neighbor for each agent
        at the requested time indices (by default first and last).

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
        time_units = str(traj_data.time_units)
        if self.time_indices is None:
            self.time_indices = self._set_default_time_indices(
                traj_data.agent_data.times
            )
        traces = {}
        for time_index in self.time_indices:
            time = traj_data.agent_data.times[time_index]
            trace_name = f"t = {time} {time_units}"
            traces[trace_name] = self._nearest_neighbor_distances(
                traj_data.agent_data.positions[time_index]
            )
        return traces

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
        return str(traj_data.spatial_units)
