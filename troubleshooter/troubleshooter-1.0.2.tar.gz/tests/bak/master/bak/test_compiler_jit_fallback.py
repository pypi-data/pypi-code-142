#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import numpy as np
from mindspore import Tensor, ms_function

import troubleshooter as ts


@ms_function
def test_np_add():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 2, 3, 4, 5])
    # z = Tensor(np.add(x, y))
    return np.add(x, y)


@ts.proposal(write_file_path="/tmp/")
def main():
    np_add_res = test_np_add()
    print(np_add_res)


if __name__ == '__main__':
    main()
