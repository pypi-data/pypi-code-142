"""
Operations
----------
This module defines basic operations of the functions in AILCA.
"""


import numpy
import json
import itertools
from typing import Union


def sublist(data_list: list,
            idx: Union[list, numpy.ndarray]) -> list:
    """
    Make a sub-list of ``data_list`` by selecting elements in the given ``idx``.

    :param data_list: (*list*) The original list.
    :param idx: (*Union[list, numpy.ndarray]*) Set of indices for the selected items in the original list.
    :return: (*list*) A sub-list of the original list.
    """

    return [data_list[i] for i in idx]


def split_list(data_list: list,
               n_sub_lists: int,
               idx_rand: numpy.ndarray = None) -> list:
    """
    Split a given ``data_list`` into ``n_sub_lists`` sub-lists.

    :param data_list: (*list*) An original lists to be split.
    :param n_sub_lists: (*int*) The number of sub-lists.
    :param idx_rand: (*numpy.ndarray, optional*) A random indices to split the list (*default* = ``None``).
    :return: (*list*) A list of the sub-lists.
    """

    if idx_rand is None:
        idx_rand = numpy.array_split(numpy.random.permutation(len(data_list)), n_sub_lists)

    sub_lists = list()

    for i in range(0, n_sub_lists):
        sub_lists.append([data_list[idx] for idx in idx_rand[i]])

    return sub_lists


def merge_lists(l1: list,
                l2: list) -> list:
    """
    Merge two lists ``l1`` and ``l2``.

    :param l1: (*list*) A list to be merged.
    :param l2: (*list*) A list to be merged to ``l1``.
    :return: (*list*) A merged list of ``l1`` and ``l2``.
    """

    return list(itertools.chain.from_iterable(l1 + l2))


def flatten_lists(lists: list):
    """
    Convert a list of lists to a list of values.

    :param lists: (*list*) A list of lists.
    :return: (*list*) A list of values.
    """

    return list(itertools.chain(*lists))


def print_dict(obj_dict: dict):
    """
    Print contents of the given dictionary ``obj_dict`` with indentations.

    :param obj_dict: (*dict*) A dictionary object to be printed.
    """

    print(json.dumps(obj_dict, indent=4))
