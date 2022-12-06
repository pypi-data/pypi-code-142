#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List

import numpy as np
from simulariumio import TrajectoryData

from .calculator import Calculator


class NumberOfAgentsCalculator(Calculator):
    def __init__(self, stride: int = 1, exclude_types: List[str] = None):
        """
        Calculates the number of agents of each type over time.

        Parameters
        ----------
        stride: int (optional)
            Include every nth timestep.
            Default: 1
        exclude_types : List[str] (optional)
            Type names for agents to ignore.
            Default: include all type names found in the trajectory
        """
        self.exclude_types = exclude_types if exclude_types is not None else []
        self.stride = stride

    def traces(self, traj_data: TrajectoryData) -> Dict[str, np.ndarray]:
        """
        Return the number of agents of each type over time.

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
        type_names_array = np.array(traj_data.agent_data.types)
        unique_types = np.unique(type_names_array)
        ytraces = {}
        for type_name in unique_types:
            if type_name in self.exclude_types:
                continue
            ytraces[type_name] = np.count_nonzero(
                type_names_array == type_name, axis=1
            )[:: self.stride]
        return ytraces

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
        return ""
