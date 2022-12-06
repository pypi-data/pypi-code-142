#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .constants import PLOT_TYPE


class MetricNotFoundError(Exception):
    def __init__(self, metric_id: int, **kwargs: int):
        """
        This exception is intended to communicate that the requested metric ID
        does not exist in the metrics registry.
        """
        super().__init__(**kwargs)
        self.metric_id = metric_id

    def __str__(self) -> str:
        return (
            f"Cannot create plot: Metric ID = {self.metric_id} not found in registry."
        )


class InconsistentPlotTypeError(Exception):
    def __init__(self, plot_type: PLOT_TYPE, **kwargs: int):
        """
        This exception is intended to communicate that the type of a plot
        is not consistent with the number of metrics provided.
        """
        super().__init__(**kwargs)
        self.plot_type = plot_type

    def __str__(self) -> str:
        if self.plot_type == PLOT_TYPE.HISTOGRAM:
            error = "Plot type is histogram and more than one metric was provided"
        else:
            error = "Plot type is scatter and only one metric was provided"
        return f"Cannot create plot: {error}."


class IncompatibleMetricsError(Exception):
    def __init__(self, x_metric_name: str, y_metric_name: str, **kwargs: int):
        """
        This exception is intended to communicate that the requested metrics
        have incompatible metric types and can't be plotted against each other.
        """
        super().__init__(**kwargs)
        self.x_metric_name = x_metric_name
        self.y_metric_name = y_metric_name

    def __str__(self) -> str:
        return (
            f"Cannot create plot: {self.y_metric_name} and "
            f"{self.x_metric_name} are incompatible."
        )
