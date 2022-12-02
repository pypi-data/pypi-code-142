import opentimspy
import pathlib
from functools import wraps
from pathlib import Path
from typing import Callable
import collections

import numpy as np
import pandas as pd


def memoize(fun):
    """A simple memoize decorator for functions supporting positional args."""

    @wraps(fun)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(sorted(kwargs.items())))
        try:
            return cache[key]
        except KeyError:
            ret = cache[key] = fun(*args, **kwargs)
        return ret
    cache = {}
    return wrapper


def get_min_max_values(path):
    """returns min max values for the dataset"""

    data_path = pathlib.Path(path)
    rawdata = opentimspy.OpenTIMS(data_path)

    data = {
        "min_mz": rawdata.min_mz,
        "max_mz": rawdata.max_mz,
        "min_rt": rawdata.min_retention_time,
        "max_rt": rawdata.max_retention_time,
        "min_frame": rawdata.min_frame,
        "max_frame": rawdata.max_frame,
        "min_scan": rawdata.min_scan,
        "max_scan": rawdata.max_scan,
        "min_iim": rawdata.min_inv_ion_mobility,
        "max_iim": rawdata.max_inv_ion_mobility,
    }

    return data


# create a memoized version of the get_min_max_values function
memoized_min_max_values = memoize(get_min_max_values)


def get_data_path_options(base_path):
    """
    searches for .d files in a given base path
    :return a list with paths from the base path
    """

    options = []
    path = Path(base_path)
    for e in path.glob("**/*.d"):
        options.append(str(e))

    return options


def create_table_df(df):
    list_ = list(df["cluster"])
    result = pd.DataFrame(columns=['cluster', 'number'])

    for x in range(-1, max(list_)+1):
        count = list_.count(x)
        result.loc[x+1] = [x, count]

    return result


def max_vote(xx):
    _argmax, _max = max(collections.Counter(xx).items(), key=lambda x: x[1])
    return _argmax


def bin_3D_points(
        df: pd.DataFrame,
        digits,
        summary_ops={
            'intensity': np.sum,  # total intensity in a voxel
            'cluster': max_vote,  # max vote on the voxel's cluster label
            'probability': max_vote
        },
) -> pd.DataFrame:
    """Bin 3D points sparsely represented into sparser bins.

    Arguments:
        df (pd.DataFrame): A data frame. Needs to contain columns 'intensity' and 'cluster' and all of the keys of the digits dictionary input.
        digits (dict): A mapping between the column and the rounding.
        summary_ops (dict): A dictionary mapping summary operations to perform on the columns. Note that for a given column you can either provide a Callable, or a list of Callables.
    Returns:
        pd.DataFrame: Binned data.
    """
    for col in [*digits, "intensity", "cluster"]:
        assert col in df.columns, f"Missing column '{col}' in the provided data frame."

    rounded_cols = [
        df[col].round(col_digits)
        for col, col_digits in digits.items()
    ]
    return df.groupby(rounded_cols).agg(summary_ops).reset_index()
