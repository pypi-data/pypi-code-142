from typing import Dict, List, Optional, Tuple, Type

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


def plot_segments(
    segments,
    capture=None,
    capture_name=None,
    labels=None,
    current_start=0,
    ylim=None,
    figsize: Tuple = (30, 8),
    currentAxis=None,
):

    if currentAxis is None:
        if capture is not None:
            currentAxis = capture.plot(figsize=figsize)
        else:
            plt.figure(figsize=figsize)
            currentAxis = plt.gca()

    cmap = plt.cm.rainbow

    if capture is not None:
        y_min = capture.describe().loc["min"].min()
        y_max = capture.describe().loc["max"].max()
        x_min = 0
        x_max = capture.shape[0]
    else:
        y_min = 0
        y_max = 1
        x_min = 0
        x_max = segments[-1].end

    if ylim:
        y_min = ylim[0]
        y_max = ylim[1]

    if labels is None:
        labels = segments.label_values

    delta = 1 / len(labels)
    label_float = np.arange(0, 1, delta)
    label_float[-1] = 1.0

    label_colors = {labels[index]: cmap(x) for index, x in enumerate(label_float)}
    label_legend = [Line2D([0], [0], color=cmap(x), lw=4) for x in label_float] + [
        Line2D([0], [0], color="white", lw=4)
    ]

    for index, seg in segments.iterrows():
        y_origin = y_min

        x_origin = seg["capture_sample_sequence_start"] + current_start
        x_final = (
            seg["capture_sample_sequence_end"] - seg["capture_sample_sequence_start"]
        )
        y_final = y_max - y_min

        currentAxis.add_artist(
            plt.Rectangle(
                (x_origin, y_origin),
                x_final,
                y_final,
                alpha=0.2,
                color=label_colors[seg["label_value"]],
            )
        )

    currentAxis.legend(label_legend, labels + [""], loc=1)

    if capture_name:
        currentAxis.text(
            current_start,
            y_max,
            capture_name,
            style="italic",
        )

    currentAxis.set_xlim(left=x_min, right=x_max)
