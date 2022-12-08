"""
Feature Vector
--------------
It provides functions to process and load the vector-shaped data for machine learning.
"""


import numpy
import pandas
import torch
from typing import Union
from tqdm import tqdm
from ailca.core.env import *
from ailca.data.base import Data, Dataset


def load_dataset(path_data_file: str,
                 idx_feat: Union[int, list],
                 idx_target: int = None,
                 verbose: bool = True) -> Dataset:
    """
    Load the dataset containing the numerical features.
    If ``idx_target`` is given, the dataset is loaded with the target values.

    :param path_data_file: (*str*) The path of the data file.
    :param idx_feat: (*Union[int, list]*) An index (or indices) of the numerical features.
    :param idx_target: (*int, optional*) An index of the target values in the data file (*default* = ``None``).
    :param verbose: (*bool*) A flag variable to present the system log in data loading (*default* = ``True``).
    :return: (*Dataset*) A dataset object.
    """

    _idxf = numpy.atleast_1d(idx_feat)
    data_file = pandas.read_excel(path_data_file)
    data = numpy.array(data_file)
    names_feats = data_file.columns.values[_idxf].tolist()
    name_target = None if idx_target is None else data_file.columns.values[idx_target]
    iter_range = range(0, data.shape[0])
    list_data = list()

    if verbose:
        iter_range = tqdm(iter_range)

    for i in iter_range:
        feat_vec = torch.tensor(data[i, _idxf].tolist(), dtype=torch.float)

        if idx_target is None:
            list_data.append(Data(x=feat_vec, idx=i, dtype=DTYPE_FVEC))
        else:
            list_data.append(Data(x=feat_vec, y=data[i, idx_target], idx=i, dtype=DTYPE_FVEC))

    return Dataset(list_data,
                   idx_feat=idx_feat,
                   idx_target=idx_target,
                   names_feats=names_feats,
                   types_feats=[DTYPE_FVEC for i in range(0, len(names_feats))],
                   name_target=name_target)
