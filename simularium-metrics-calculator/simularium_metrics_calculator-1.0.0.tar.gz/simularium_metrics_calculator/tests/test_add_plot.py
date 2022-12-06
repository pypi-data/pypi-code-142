#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import pytest
from simulariumio import FileConverter, HistogramPlotData, InputFileData

from simularium_metrics_calculator import (
    PLOT_TYPE,
    SCATTER_PLOT_MODE,
    MetricsService,
    PlotInfo,
)
from simularium_metrics_calculator.exceptions import (
    IncompatibleMetricsError,
    InconsistentPlotTypeError,
    MetricNotFoundError,
)
from simularium_metrics_calculator.tests import assert_plot_data_equal

metrics_service = MetricsService()
traj_data = FileConverter(
    input_file=InputFileData(
        file_path=(
            "simularium_metrics_calculator/tests/data/"
            "aster_pull3D_couples_actin_solid_3_frames_small.json"
        )
    )
)._data


@pytest.mark.parametrize(
    "plot_metrics, expected_plot_data",
    [
        # histogram
        (
            [
                PlotInfo(
                    title="NN Distance",
                    plot_type=PLOT_TYPE.HISTOGRAM,
                    metric_id_x=3,
                ),
            ],
            {
                "layout": {
                    "title": "NN Distance",
                    "xaxis": {"title": "Nearest neighbor distance (\u00b5m)"},
                    "yaxis": {"title": "frequency"},
                },
                "data": [
                    {
                        "name": "t = 0.0 s",
                        "type": "histogram",
                        "x": [89.48637941050023, 89.48637941050023],
                    },
                    {
                        "name": "t = 0.1 s",
                        "type": "histogram",
                        "x": [87.40050629143975, 87.40050629143975],
                    },
                ],
            },
        ),
        # scatterplot
        (
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.SCATTER,
                    metric_id_x=0,
                    metric_id_y=2,
                    scatter_plot_mode=SCATTER_PLOT_MODE.LINES,
                ),
            ],
            {
                "layout": {
                    "title": "Number of agents vs. time",
                    "xaxis": {"title": "Time (s)"},
                    "yaxis": {"title": "Number of agents"},
                },
                "data": [
                    {
                        "name": "microtubule",
                        "type": "scatter",
                        "x": [0.0, 0.05, 0.1],
                        "y": [1, 1, 1],
                        "mode": "lines",
                    },
                    {
                        "name": "motor complex",
                        "type": "scatter",
                        "x": [0.0, 0.05, 0.1],
                        "y": [1, 1, 1],
                        "mode": "lines",
                    },
                ],
            },
        ),
        # metric ID does not exist
        pytest.param(
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.HISTOGRAM,
                    metric_id_x=-1,
                ),
            ],
            {},
            marks=pytest.mark.raises(exception=MetricNotFoundError),
        ),
        # plot type and metrics are inconsistent
        pytest.param(
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.SCATTER,
                    metric_id_x=0,
                ),
            ],
            {},
            marks=pytest.mark.raises(exception=InconsistentPlotTypeError),
        ),
        # metrics have incompatible type
        pytest.param(
            [
                PlotInfo(
                    plot_type=PLOT_TYPE.SCATTER,
                    metric_id_x=0,
                    metric_id_y=1,
                ),
            ],
            {},
            marks=pytest.mark.raises(exception=IncompatibleMetricsError),
        ),
    ],
)
def test_add_plot(
    plot_metrics: List[PlotInfo],
    expected_plot_data: HistogramPlotData,
) -> None:
    test_plot_data = metrics_service._plot_dicts(traj_data, plot_metrics)
    assert len(test_plot_data) == 1
    assert_plot_data_equal(
        test_plot_data[0], expected_plot_data, plot_type=plot_metrics[0].plot_type
    )
