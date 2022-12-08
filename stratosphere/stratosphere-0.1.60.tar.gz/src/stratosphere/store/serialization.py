from functools import partial
import json
from typing import List
import uuid
import zlib
from pickle import PickleError

import cloudpickle
import numpy as np
import pandas as pd
from stratosphere import config


def compress(data: bytes, enable_compression=config.serialization.enable_compression) -> bytes:
    if enable_compression:
        return zlib.compress(data)
    else:
        return data


def decompress(data: bytes) -> bytes:
    if isinstance(data, memoryview):
        data = data.tobytes()

    try:
        data = zlib.decompress(data)
    except zlib.error:
        pass

    return data


# Introduced with Python 3.0, https://peps.python.org/pep-3154/
# Unpickling might fail: on different architectures, different python version, in case of missing packages.
PICKLE_DEFAULT_PROTOCOL = 4


def pickle_dumps(obj: object) -> bytes:
    """It returns the compressed (zlib) pickled object. The Pickle DEFAULT_PROTOCOL is used
    for maximum compatibility.

    Args:
        obj (object): Object to serialize.

    Returns:
        bytes: Compressed serialized object.
    """
    return compress(cloudpickle.dumps(obj, protocol=PICKLE_DEFAULT_PROTOCOL))


def pickle_loads(data: bytes) -> object:
    """It returns the loaded object, afer uncompressing and unpickling it.

    Args:
        data (bytes): Serialized object.

    Returns:
        object: Unserialized object.
    """
    try:
        return cloudpickle.loads(decompress(data))
    except Exception:  # noqa # we do want to catch all errors here
        raise PickleError()


def pickle_size(obj: object, unit: str = "b") -> int:
    """It returns the size of the object once serialised (including compression).

    Args:
        obj (object): Object to analyse.
        unit (str, optional): Unit of measure, b (Bytes), kb (KiloBytes), mb (MegaBytes). Defaults to "b".

    Returns:
        int: Size of the serialized object.
    """
    size_object = len(pickle_dumps(obj))
    if unit == "b":
        return int(size_object * 1e2) / 1e2
    elif unit == "kb":
        return int(size_object * 1e-3 * 1e2) / 1e2
    elif unit == "mb":
        return int(size_object * 1e-6 * 1e2) / 1e2
    else:
        return None


serialized_types = [pd.DataFrame, pd.Series, np.ndarray, uuid.UUID, dict, list]


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, pd.DataFrame):
            return {"__type": "pandas.DataFrame", "data": obj.to_dict(orient="list"), "index": obj.index.tolist()}
        elif isinstance(obj, pd.Series):
            return {"__type": "pandas.Series", "data": obj.tolist(), "index": obj.index.tolist()}
        elif isinstance(obj, np.ndarray):
            return {"__type": "numpy.ndarray", "data": obj.tolist()}
        elif isinstance(obj, uuid.UUID):
            return {"__type": "uuid.UUID", "data": str(obj)}
        else:
            return json.JSONEncoder.default(self, obj)


def serialize(obj: object, enable_compression=config.serialization.enable_compression) -> bytes:
    return compress(json.dumps(obj, cls=JSONEncoder).encode("UTF-8"), enable_compression=enable_compression)


def deserialize(obj: bytes) -> object:
    def f(d):
        if isinstance(d, dict) and "__type" in d:
            # This ia a value to deserialize
            if d["__type"] == "pandas.DataFrame":
                df = pd.DataFrame.from_dict(d["data"], orient="columns")
                df.index = pd.Index(d["index"])
                return df
            elif d["__type"] == "pandas.Series":
                return pd.Series(d["data"], index=d["index"])
            elif d["__type"] == "numpy.ndarray":
                return np.asarray(d["data"])
            elif d["__type"] == "uuid.UUID":
                return uuid.UUID(d["data"])
            else:
                # We don't know how to deserialize it, return it as a dictionary.
                return d

        if isinstance(d, list):
            # Walk thru the list, trying to decode values.
            return [f(v) for v in d]

        if isinstance(d, dict):
            # Walk thru the dict, trying to decode values.
            return {kv[0]: f(kv[1]) for kv in d.items()}

        else:
            # Nothing to do, return value.
            return d

    return json.loads(decompress(obj).decode("UTF-8"), object_hook=f)


def serialize_df(
    df: pd.DataFrame, ignore_columns: list = None, enable_compression=config.serialization.enable_compression
):
    consider_columns = [col_name for col_name in df.columns if col_name not in ignore_columns]

    # Identify columns to serialize
    serialized_cols = []
    for col_name in consider_columns:
        for serialized_type in serialized_types:
            # We assume that the types in the first row are the same of the other rows.
            if isinstance(df[col_name].iloc[0], serialized_type):
                serialized_cols.append(col_name)
                break

    if len(serialized_cols) > 0:
        # If there are columns to serialize, work on a frame copy.
        df = df.copy()
        for col_name in serialized_cols:
            df[col_name] = df[col_name].map(partial(serialize, enable_compression=enable_compression))

    # Identify columns that haven't been serialized, among the ones to be considered.
    non_serialized_cols = [col_name for col_name in consider_columns if col_name not in serialized_cols]

    columns = {"serialized": serialized_cols, "non_serialized": non_serialized_cols, "compression": enable_compression}
    return df, columns


def deserialize_df(df: pd.DataFrame, columns: List[str]):
    if len(columns) == 0:
        return df

    df = df.copy()
    for col_name in columns:
        df[col_name] = df[col_name].map(deserialize)

    return df


def explode_json_column(df: pd.DataFrame, col_name: str, prefix: str = None, suffix: str = None) -> pd.DataFrame:
    """Explode a column in the Pandas dataframe containing a dict to a list of columns.
    Useful to handle the "attributes" column in the "Experiments" table, which contains
    the serialized values as JSON.
    Args:
        df (pd.DataFrame): Pandas dataframe
        col_name (str): Column to process.
        prefix (str, optional): Prefix to consider for all exploded columns.
        suffix (str, optional): In case exploded columns already exist, use this suffix.
        Defaults to _{col_name}.
    Returns:
        pd.DataFrame: Resulting Pandas dataframe.
    """

    if suffix is None:
        suffix = f"_{col_name}"

    # Explode column containing json to multiple columns, in a dataframe.
    df_exploded = pd.json_normalize(df[col_name])

    if prefix is not None:
        df_exploded.columns = [f"{prefix}{col_name}" for col_name in df_exploded.columns]

    return df.drop(columns=[col_name]).merge(
        df_exploded,
        how="left",
        left_index=True,
        right_index=True,
        suffixes=(None, suffix),
    )
