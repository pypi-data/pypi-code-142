#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class METRIC_TYPE(Enum):
    """
    The type of a metric, for determining
    which metrics can be plotted against one another.
    """

    OTHER = "OTHER"
    PER_TIME = "PER_TIME"
    PER_AGENT = "PER_AGENT"


class PLOT_TYPE(Enum):
    """
    The type of a plot.
    """

    SCATTER = "scatter"
    HISTOGRAM = "histogram"


class SCATTER_PLOT_MODE(Enum):
    """
    Mode for how to draw points on a scatter plot.
    """

    MARKERS = "markers"
    LINES = "lines"


class PLOT_AXIS(Enum):
    """
    Axes for a 2D plot.
    """

    X = "x"
    Y = "y"
