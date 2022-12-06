#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

import numpy as np
import pytest
from simulariumio import TrajectoryData

from simularium_metrics_calculator.calculators import NearestNeighborCalculator
from simularium_metrics_calculator.tests import (
    assert_traces_equal,
    nearest_neighbor_positions,
    simple_test_traj_data,
)


@pytest.mark.parametrize(
    "traj_data, expected_traces, expected_units",
    [
        (
            simple_test_traj_data,
            {
                "t = 0.0 ns": np.array([1.0, 1.0, 1.73]),
                "t = 1.0 ns": np.array([10.0, 17.3, 10.0]),
            },
            " (nm)",
        )
    ],
)
def test_nearest_neighbor(
    traj_data: TrajectoryData,
    expected_traces: Dict[str, np.ndarray],
    expected_units: str,
) -> None:
    calculator = NearestNeighborCalculator()
    traj_data.agent_data.positions = nearest_neighbor_positions
    traces, units = calculator.calculate(traj_data)
    assert_traces_equal(traces, expected_traces)
    assert units == expected_units
