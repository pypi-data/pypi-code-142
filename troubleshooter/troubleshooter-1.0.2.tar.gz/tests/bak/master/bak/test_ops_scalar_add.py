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
    x = False
    y = True
    output = ops.scalar_add(x, y)
    print('output', output)


if __name__ == '__main__':
    main()
