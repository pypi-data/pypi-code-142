#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import os
from mindspore import Tensor, nn, ops
import mindspore
import numpy as np
import troubleshooter as ts


@ts.proposal(write_file_path="/tmp/")
def main():
    x = Tensor(np.array([1.0, 2.0, 3.0]), mindspore.float32)
    y = np.array([4.0, 5.0, 6.0])
    output = x * y
    print(output)


if __name__ == '__main__':
    main()
