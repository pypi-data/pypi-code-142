import glob
import os
import sys
import typing

import click
import numpy as np
import pandas as pd

from ..logging import print, print_dict, print_series
from . import plot_params_distribution


@click.command(name="param-dis")
@click.option(
    "--input-dir", show_default=True, type=click.Path(), default="results/params/cdf"
)
@click.option(
    "--output-dir",
    show_default=True,
    type=click.Path(),
    default="results/param_dis/cdf",
)
@click.option(
    "--threshold-percentage",
    show_default=True,
    type=click.FloatRange(min=0, max=100),
    default=None,
)
@click.option(
    "--threshold", show_default=True, type=click.FloatRange(min=0, max=1), default=0.9
)
def main(
    input_dir: str = "results/cdf/params",
    output_dir: str = "results/cdf/param-dis",
    threshold_percentage: typing.Optional[float] = None,
    threshold: float = 0.9,
):
    files = glob.glob(pathname=f"{input_dir}/*.csv")
    dfs: dict[str, pd.DataFrame] = dict()
    for filepath in files:
        name, _ = os.path.splitext(os.path.basename(filepath))
        df = pd.read_csv(filepath)
        df["model"] = name
        dfs[name] = df
    r2_score = pd.concat(
        [df[["id", "model", "r2_score"]] for df in dfs.values()], ignore_index=True
    )
    print_series(r2_score["r2_score"].describe(), title="R2 Score Describe (All)")
    if threshold_percentage:
        threshold = float(np.percentile(a=r2_score["r2_score"], q=threshold_percentage))
        print_dict(
            {"r2_score": threshold},
            title="R2 Score Threshold",
        )
    else:
        print_dict(
            {"percentage": threshold_percentage, "r2_score": threshold},
            title="R2 Score Threshold",
        )
    r2_score = r2_score[r2_score["r2_score"] > threshold]
    print_series(r2_score["r2_score"].describe(), title="R2 Score Describe (Selected)")
    print_series(r2_score["model"].value_counts(), title="Catchment Counts (Selected)")
    for name, df in dfs.items():
        df = df[df["r2_score"] > threshold]
        if df.empty:
            continue
        os.makedirs(name=output_dir, exist_ok=True)
        plot_params_distribution(data=df, fname=os.path.join(output_dir, f"{name}.png"))


if __name__ == "__main__":
    sys.exit(main())
