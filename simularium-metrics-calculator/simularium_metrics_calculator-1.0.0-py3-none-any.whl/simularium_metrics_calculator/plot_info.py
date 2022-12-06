#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional

from .constants import PLOT_TYPE, SCATTER_PLOT_MODE
from .exceptions import IncompatibleMetricsError, InconsistentPlotTypeError
from .metric_info import MetricInfo


class PlotInfo:
    plot_type: PLOT_TYPE
    metric_id_x: int
    metric_id_y: int
    scatter_plot_mode: SCATTER_PLOT_MODE
    title: str

    def __init__(
        self,
        plot_type: PLOT_TYPE,
        metric_id_x: int,
        metric_id_y: int = -1,
        scatter_plot_mode: SCATTER_PLOT_MODE = SCATTER_PLOT_MODE.MARKERS,
        title: str = "",
    ):
        """
        This object takes Simularium trajectory data
        and calculates metrics that can be plotted
        in the Simularium Viewer.

        Parameters
        ----------
        plot_type: PLOT_TYPE
            What type of plot to make.
        metric_id_x : int
            ID for the metric to plot on the x-axis.
        metric_id_y : int (Optional)
            ID for the metric to plot on the y-axis.
            If not provided, the plot will be a histogram.
        scatter_plot_mode : SCATTER_PLOT_MODE (Optional)
            If the plot is a scatterplot, how to draw the points.
            Default: SCATTER_PLOT_MODE.MARKERS (draw as dots)
        title: str
            Title to display above plot.
        """
        self.plot_type = plot_type
        self.metric_id_x = metric_id_x
        self.metric_id_y = metric_id_y
        self.scatter_plot_mode = scatter_plot_mode
        self.title = title
        self.display_title = title

    def validate_plot_configuration(
        self, metric_info_x: MetricInfo, metric_info_y: Optional[MetricInfo]
    ) -> None:
        """
        Check that the plot type and number of metrics are consistent,
        and that the X and Y metrics are of the same type
        if this is not a histogram.

        Parameters
        ----------
        metric_info_x: MetricInfo
            Info about the metric to plot on the x-axis.
        metric_info_y: MetricInfo (optional)
            Info about the metric to plot on the y-axis.
            Default: None (only for histograms)
        """
        self._check_plot_type_is_consistent()
        self._check_metrics_are_compatible(metric_info_x, metric_info_y)

    def _check_plot_type_is_consistent(self) -> None:
        """
        Make sure the number of metrics is consistent with the plot type,
        1 metric for histogram and 2 for scatter.
        """
        if not (self.metric_id_y < 0) == (self.plot_type == PLOT_TYPE.HISTOGRAM):
            raise InconsistentPlotTypeError(self.plot_type)

    def _check_metrics_are_compatible(
        self, metric_info_x: MetricInfo, metric_info_y: Optional[MetricInfo]
    ) -> None:
        """
        Check that the X and Y metrics are of the same type,
        if this is not a histogram.
        """
        if metric_info_y is None:
            return
        x_metric_type = metric_info_x.metric_type
        y_metric_type = metric_info_y.metric_type
        if x_metric_type != y_metric_type:
            x_metric_name = metric_info_x.display_name
            y_metric_name = metric_info_y.display_name
            raise IncompatibleMetricsError(x_metric_name, y_metric_name)

    def set_display_title(
        self, metric_info_x: MetricInfo, metric_info_y: Optional[MetricInfo]
    ) -> None:
        """
        Return the title to display above the plot.
        If no title is provided, default to "Y metric name vs. X metric name".

        Parameters
        ----------
        metric_info_x: MetricInfo
            Info about the metric to plot on the x-axis.
        metric_info_y: MetricInfo (optional)
            Info about the metric to plot on the y-axis.
            Default: None (only for histograms)
        """
        if self.title:
            # use custom title
            self.display_title = self.title
            return
        x_metric_name = metric_info_x.display_name
        if metric_info_y is None:
            # histogram
            self.display_title = f"{x_metric_name}"
            return
        # scatter plot
        y_metric_name = metric_info_y.display_name
        self.display_title = f"{y_metric_name} vs. {x_metric_name.lower()}"

    def __str__(self) -> str:
        """
        Get the title and type of this plot.

        Returns
        -------
        str
            "[title] [type of plot]"
        """
        title = f"{self.display_title} " if self.display_title else ""
        pt = "histogram" if self.plot_type == PLOT_TYPE.HISTOGRAM else "scatter plot"
        return f"{title}{pt}"
