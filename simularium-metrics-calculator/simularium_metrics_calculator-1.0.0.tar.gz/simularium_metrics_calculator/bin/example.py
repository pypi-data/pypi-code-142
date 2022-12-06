#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, Dict, List

from simulariumio import FileConverter, InputFileData

from simularium_metrics_calculator import (
    PLOT_TYPE,
    SCATTER_PLOT_MODE,
    MetricsService,
    PlotInfo,
)


def log_available_metrics(metrics: List[Dict[str, Any]]) -> None:
    print("\nAvailable metrics:")
    for index, metric in enumerate(metrics):
        uid = metric["uid"]
        display_name = metric["display_name"]
        metric_type = metric["metric_type"]
        print(f"  {index} : {display_name}, uid = {uid} ({metric_type})")
    print("")


def main() -> None:
    # create main class
    metrics_service = MetricsService()

    # get the metrics that are available to plot
    metrics = metrics_service.available_metrics()
    log_available_metrics(metrics)

    # load simularium trajectory data using simulariumio
    traj_data = FileConverter(
        input_file=InputFileData(
            file_path=(
                "simularium_metrics_calculator/tests/data/"
                "aster_pull3D_couples_actin_solid_3_frames_small.json"
            )
        )
    )._data

    # configure some plots
    plot1 = PlotInfo(  # Number of agents vs time scatterplot
        plot_type=PLOT_TYPE.SCATTER,
        metric_id_x=metrics[0]["uid"],
        metric_id_y=metrics[2]["uid"],
        scatter_plot_mode=SCATTER_PLOT_MODE.LINES,
    )
    plot2 = PlotInfo(  # Nearest neighbor distance histogram
        plot_type=PLOT_TYPE.HISTOGRAM,
        metric_id_x=metrics[3]["uid"],
        title="Nearest Neighbor Distance",  # optional
    )

    # calculate plot data
    result = metrics_service.plot_data(
        traj_data,
        plots=[
            plot1,
            plot2,
        ],
    )
    print(f"\nTo plot:\n- {plot1}\n- {plot2}")
    print(f"\nRESULT = \n{result}\n")


if __name__ == "__main__":
    main()
