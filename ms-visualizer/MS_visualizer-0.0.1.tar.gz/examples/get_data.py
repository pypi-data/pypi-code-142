from MS_visualizer.controller.func import memoize

import numpy as np
import pandas as pd
import pathlib

pd.set_option('display.max_columns', None)
import opentimspy


def get_bounds(data_path: pathlib.Path):
    """Get bounds on selection variables."""
    rawdata = opentimspy.OpenTIMS(data_path)
    min_max_mz = np.array([rawdata.min_mz, rawdata.max_mz])
    return {
        "frame": (rawdata.min_frame, rawdata.max_frame),
        "retention_time": (rawdata.min_retention_time, rawdata.max_retention_time),
        "scan": (rawdata.min_scan, rawdata.max_scan),
        "inv_ion_mobility": (rawdata.min_inv_ion_mobility, rawdata.max_inv_ion_mobility),
        "tof": tuple(rawdata.handle.mz_to_tof(1, min_max_mz)),  # this might be an approximation.
        "mz": tuple(min_max_mz),
        "min_intensity": (0, float("inf")),
    }


# TODO:
# this should also have the capability to extract more dimensions if we want to.
# and it should be an iterator: for this it would make sense to do it in C++
def get_opentims_data(
        data_path: pathlib.Path,
        level="MS1",
        min_intensity: int = 0,
        constraint: str = "",
        **extents
) -> pd.DataFrame:
    """Get data.

    Arguments:
        data_path (pathlib.Path): Path to data.
        level (str): If 'MS1', will extract only MS1, if 'MS2', only MS2, otherwise all of frames.
        other_contraints (str): Other query contstraints (pandas expression string).
        **extents (dict): tuples with minimal and maximal values assigned to names of dimensions. These must include 'frame' or 'retention_time'. They can include 'scan' xor 'inv_ion_mobility', and 'tof' xor 'mz'. These will be then used to build up the query. The extents do not follow the pythonic ranges convention, in as much maximal value is not maximal+1 in terms of integer variables. On the contrary, these are translated into "variable <= max_variable_value" expressions. 

    Returns:
        pd.DataFrame: A dataframe with raw data. 
    """
    # ^ == XOR
    assert ("frame" in extents) ^ (
                "retention_time" in extents), "You need to specify selection in terms of either frames or retention times. Cross specification ain't allowed as well."
    assert not (("scan" in extents) and (
                "inv_ion_mobility" in extents)), "You have provided simultaneously scan and inv_ion_mobility values. You need to specify selection in terms of either scans or inverse ion mobilities, or provide none of them."
    assert not (("tof" in extents) and (
                "mz" in extents)), "You have provided simultaneously tof and mz values. You need to specify selection in terms of either time of flights (tof) or mass to charge ratios (mz), or provide none of them."
    for var_name, (var_min, var_max) in extents.items():
        assert var_min < var_max, f"For variable '{var_name}', supplied minimal value, {var_min}, was greater or equal to the maximal value, {var_max}. "

    rawdata = opentimspy.OpenTIMS(data_path)
    variables_to_extract = list(extents)

    if "frame" in extents:
        min_frame, max_frame = extents.pop("frame")
        Frames = pd.DataFrame(rawdata.frames).query(f"Id >= {min_frame} and Id <= {max_frame}")
    else:
        min_retention_time, max_retention_time = extents.pop("retention_time")
        Frames = pd.DataFrame(rawdata.frames).query(f"Time >= {min_retention_time} and Time <= {max_retention_time}")

    if level == "MS1":
        Frames = Frames.query("MsMsType == 0")
    if level == "MS2":
        Frames = Frames.query("MsMsType != 0")

    constraints = []
    if constraint:
        constraints.append(constraint)
    if min_intensity > 0:
        constraints.append(f"intensity >= {min_intensity}")
    for var_name, (var_min, var_max) in extents.items():
        constraints.append(f"{var_name} >= {var_min} and {var_name} <= {var_max}")
    constraints_expr = " and ".join(constraints)

    result_df = pd.concat(
        pd.DataFrame(rawdata.query(frames=[frame])).query(constraints_expr)
        for frame in Frames.Id
    )
    return result_df


# cached functions
memoized_get_opentims_data = memoize(get_opentims_data)
memoized_get_bounds = memoize(get_bounds)

if __name__ == "__main__":
    data_path = pathlib.Path("../data/data.d")
    MS1 = get_opentims_data(
        data_path=data_path,
        min_intensity=10,
        constraint="inv_ion_mobility <= 0.4467452 + 0.00101627*mz and inv_ion_mobility <= 0.5301116 + 0.000849*mz",
        frame=(10, 40),
        tof=(1, 500),
        scan=(300, 800),
    )

    print(MS1)

    # just to test: Thilo, do not use 'level'.
    MS2 = get_opentims_data(
        data_path=data_path,
        level='MS2',
        min_intensity=10,
        constraint="inv_ion_mobility <= 0.4467452 + 0.00101627*mz and inv_ion_mobility <= 0.5301116 + 0.000849*mz",
        frame=(10, 40),
        mz=(500, 560),
        scan=(300, 800),
    )
