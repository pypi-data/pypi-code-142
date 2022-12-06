#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .calculators import (
    AgentsCalculator,
    NearestNeighborCalculator,
    NumberOfAgentsCalculator,
    TimesCalculator,
)
from .constants import METRIC_TYPE, PLOT_AXIS
from .metric_info import MetricInfo

metrics_list = [
    MetricInfo(
        display_name="Time",
        metric_type=METRIC_TYPE.PER_TIME,
        calculator=TimesCalculator,
        exclude_axes=[PLOT_AXIS.Y],
    ),
    MetricInfo(
        display_name="Agent IDs",
        metric_type=METRIC_TYPE.PER_AGENT,
        calculator=AgentsCalculator,
        exclude_axes=[PLOT_AXIS.Y],
    ),
    MetricInfo(
        display_name="Number of agents",
        metric_type=METRIC_TYPE.PER_TIME,
        calculator=NumberOfAgentsCalculator,
    ),
    MetricInfo(
        display_name="Nearest neighbor distance",
        metric_type=METRIC_TYPE.PER_AGENT,
        calculator=NearestNeighborCalculator,
    ),
]
