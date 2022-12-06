#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict

import numpy as np
import pytest
from simulariumio import TrajectoryData

from simularium_metrics_calculator.calculators import NumberOfAgentsCalculator
from simularium_metrics_calculator.tests import (
    assert_traces_equal,
    simple_test_traj_data,
)


@pytest.mark.parametrize(
    "traj_data, expected_traces, expected_units",
    [
        (
            simple_test_traj_data,
            {
                "C": np.array([2.0, 0.0, 0.0]),
                "U": np.array([1.0, 1.0, 0.0]),
                "L": np.array([0.0, 1.0, 0.0]),
                "S": np.array([0.0, 1.0, 0.0]),
                "O": np.array([0.0, 0.0, 1.0]),
                "Y": np.array([0.0, 0.0, 1.0]),
                "W": np.array([0.0, 0.0, 1.0]),
            },
            "",
        )
    ],
)
def test_num_agents(
    traj_data: TrajectoryData,
    expected_traces: Dict[str, np.ndarray],
    expected_units: str,
) -> None:
    calculator = NumberOfAgentsCalculator()
    traces, units = calculator.calculate(traj_data)
    assert_traces_equal(traces, expected_traces)
    assert units == expected_units
