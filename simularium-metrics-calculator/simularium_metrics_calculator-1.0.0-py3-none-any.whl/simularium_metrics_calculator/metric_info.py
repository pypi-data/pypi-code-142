#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, Dict, List, Type

from .calculators.calculator import Calculator
from .constants import METRIC_TYPE, PLOT_AXIS


class MetricInfo:
    display_name: str
    metric_type: METRIC_TYPE
    calculator: Type[Calculator]
    exclude_axes: List[str]

    def __init__(
        self,
        display_name: str,
        metric_type: METRIC_TYPE,
        calculator: Type[Calculator],
        exclude_axes: List[PLOT_AXIS] = None,
    ):
        """
        Data about a metric that can be calculated.

        Parameters
        ----------
        display_name: str
            The name for this metric to display on a plot axis.
        metric_type: METRIC_TYPE
            The type of metric, for determining which metrics
            can be plotted against one another.
        calculator: Type[Calculator]
            The calculator class for this metric.
        exclude_axes: List[PLOT_AXIS] (optional)
            A list of plot axes where this metric doesn't make sense, if any.
            Default: [] (don't exclude any axes)
        """
        self.display_name = display_name
        self.metric_type = metric_type
        self.calculator = calculator
        self.exclude_axes = []
        if exclude_axes is not None:
            self.exclude_axes = [axis.value for axis in exclude_axes]

    def to_dict(self) -> Dict[str, Any]:
        """
        Get a dict with info about the metric that a client needs to know.

        Returns
        -------
        Dict[str, Any]
            A dict of the metric info, including
            display name, metric type, and excluded axes.
        """
        return {
            "display_name": self.display_name,
            "metric_type": self.metric_type.value,
            "exclude_axes": self.exclude_axes,
        }
