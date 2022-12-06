#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, Dict

import numpy as np
from simulariumio import AgentData, MetaData, TrajectoryData, UnitData

from simularium_metrics_calculator import PLOT_TYPE

simple_test_traj_data = TrajectoryData(
    meta_data=MetaData(),
    agent_data=AgentData(
        times=0.5 * np.array(list(range(3))),
        n_agents=np.array(3 * [3]),
        viz_types=np.array(3 * [3 * [1000.0]]),
        unique_ids=np.array([[0.0, 1.0, 2.0], [0.0, 1.0, 2.0], [0.0, 1.0, 2.0]]),
        types=[["C", "U", "C"], ["U", "L", "S"], ["O", "Y", "W"]],
        positions=np.zeros((3, 3, 3)),
        radii=np.ones((3, 3)),
    ),
    time_units=UnitData("ns"),
    spatial_units=UnitData("nm"),
)

nearest_neighbor_positions = np.array(
    [
        [
            [0, 0, 0],
            [0, 1, 0],
            [1.73, 0, 0],
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        [
            [10, 0, 0],
            [0, 17.3, 0],
            [0, 0, 0],
        ],
    ]
)


def assert_traces_equal(
    test_traces: Dict[str, np.ndarray], expected_traces: Dict[str, np.ndarray]
) -> None:
    assert test_traces.keys() == expected_traces.keys()
    for type_name in expected_traces:
        assert False not in np.isclose(
            test_traces[type_name], expected_traces[type_name]
        )


def assert_plot_data_equal(
    test_plot_data: Dict[str, Any],
    expected_plot_data: Dict[str, Any],
    plot_type: PLOT_TYPE,
) -> None:
    assert test_plot_data["layout"]["title"] == expected_plot_data["layout"]["title"]
    assert (
        test_plot_data["layout"]["xaxis"]["title"]
        == expected_plot_data["layout"]["xaxis"]["title"]
    )
    if plot_type != PLOT_TYPE.HISTOGRAM:
        assert (
            test_plot_data["layout"]["yaxis"]["title"]
            == expected_plot_data["layout"]["yaxis"]["title"]
        )
    assert len(test_plot_data["data"]) == len(expected_plot_data["data"])
    for expected_trace in expected_plot_data["data"]:
        found = False
        trace_name = expected_trace["name"]
        for test_trace in test_plot_data["data"]:
            if test_trace["name"] == trace_name:
                assert False not in np.isclose(
                    np.array(test_trace["x"]), np.array(expected_trace["x"])
                )
                if plot_type != PLOT_TYPE.HISTOGRAM:
                    assert False not in np.isclose(
                        np.array(test_trace["y"]), np.array(expected_trace["y"])
                    )
                    assert test_trace["mode"] == expected_trace["mode"]
                found = True
                break
        if not found:
            raise AssertionError(f"Did not find {trace_name} in plot traces.")
