#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""
from mindspore import Tensor, nn, ops
import mindspore
import numpy as np

import troubleshooter as ts


@ts.proposal(write_file_path="/tmp/")
def main():
    x = Tensor(np.array([2, 3]), mindspore.int32)
    y = Tensor(np.array([4, 5, 6]), mindspore.int32)
    output = x - y
    print(output)


if __name__ == '__main__':
    main()
