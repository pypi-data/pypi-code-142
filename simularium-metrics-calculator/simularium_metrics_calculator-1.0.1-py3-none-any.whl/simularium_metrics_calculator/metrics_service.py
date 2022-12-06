#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import Any, Dict, List

from simulariumio import HistogramPlotData, ScatterPlotData, TrajectoryData
from simulariumio.constants import CURRENT_VERSION
from simulariumio.plot_readers import HistogramPlotReader, ScatterPlotReader

from .exceptions import MetricNotFoundError
from .metric_info import MetricInfo
from .metrics_registry import metrics_list
from .plot_info import PlotInfo


class MetricsService:
    def __init__(self) -> None:
        """
        This object lists and calculates metrics
        that can be plotted in the Simularium Viewer.
        """
        self._create_metrics_registry()

    def _create_metrics_registry(self) -> None:
        """
        Get a dict mapping metric index (as per-session unique ID)
        to info about each available metric.
        """
        self.metrics_registry = {}
        for index, metric_info in enumerate(metrics_list):
            self.metrics_registry[index] = metric_info

    def metric_info_for_id(self, metric_id: int) -> MetricInfo:
        """
        Get a MetricInfo for a given metric's session id.
        Raise an error if the metric_id is not found in the registry.

        Parameters
        ----------
        metric_id: int
            The session ID for the requested metric.

        Returns
        -------
        MetricInfo
            Info about the requested metric.
        """
        if metric_id not in self.metrics_registry:
            raise MetricNotFoundError(metric_id)
        return self.metrics_registry[metric_id]

    def available_metrics(self) -> List[Dict[str, Any]]:
        """
        Get the IDs and display names for the metrics
        that are compatible with the given type of data.

        Returns
        -------
        List[Dict[str, Any]]
            A list of info about each available metric,
            including session ID, display name, metric type,
            and excluded axes.
        """
        result = []
        for uid, metric_info in self.metrics_registry.items():
            info = metric_info.to_dict()
            info["uid"] = uid
            result.append(info)
        return result

    def plot_data(self, traj_data: TrajectoryData, plots: List[PlotInfo]) -> str:
        """
        Add plots with the given configuration.

        Parameters
        ----------
        traj_data : TrajectoryData,
            A Simularium trajectory.
        plots: List[PlotInfo]
            A list of PlotInfo configuration for each plot.

        Returns
        -------
        str
            A JSON string of the plot(s) in simularium format.
        """
        plot_dicts = self._plot_dicts(traj_data, plots)
        return json.dumps(
            {
                "version": CURRENT_VERSION.PLOT_DATA,
                "data": plot_dicts,
            }
        )

    def _plot_dicts(
        self, traj_data: TrajectoryData, plots: List[PlotInfo]
    ) -> List[Dict[str, Any]]:
        """
        Calculate each plot and get a dict for each.
        """
        result = []
        for plot_info in plots:
            result.append(self._calculate_plot(traj_data, plot_info))
        return result

    def _calculate_plot(
        self, traj_data: TrajectoryData, plot_info: PlotInfo
    ) -> Dict[str, Any]:
        """
        Calculate a plot with the given configuration.
        """
        # get metric info
        x_metric_info = self.metric_info_for_id(plot_info.metric_id_x)
        y_metric_info = None
        if plot_info.metric_id_y >= 0:
            y_metric_info = self.metric_info_for_id(plot_info.metric_id_y)
        # validate and setup title
        plot_info.validate_plot_configuration(x_metric_info, y_metric_info)
        plot_info.set_display_title(x_metric_info, y_metric_info)
        # X axis metric
        x_calculator = x_metric_info.calculator()
        x_traces, x_units = x_calculator.calculate(traj_data)
        x_metric_title = x_metric_info.display_name
        # create and add plots
        if y_metric_info is None:  # HISTOGRAM
            plot_data = HistogramPlotData(
                title=plot_info.display_title,
                xaxis_title=f"{x_metric_title}{x_units}",
                traces=x_traces,
            )
            return HistogramPlotReader().read(plot_data)
        else:  # SCATTER PLOT
            # only use the first trace for X axis since there can only be one
            x_trace = x_traces[list(x_traces.keys())[0]]
            # Y axis metric
            y_calculator = y_metric_info.calculator()
            y_traces, y_units = y_calculator.calculate(traj_data)
            y_metric_title = y_metric_info.display_name
            # create and add scatter plot
            plot_data = ScatterPlotData(
                title=plot_info.display_title,
                xaxis_title=f"{x_metric_title}{x_units}",
                yaxis_title=f"{y_metric_title}{y_units}",
                xtrace=x_trace,
                ytraces=y_traces,
                render_mode=plot_info.scatter_plot_mode.value,
            )
            return ScatterPlotReader().read(plot_data)
