#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import mindspore
from mindspore import ops
from mindspore import Tensor, nn
import numpy as np

from mindspore import context

import troubleshooter as ts

device_type = "Ascend"
context.set_context(device_target=device_type)


@ts.proposal(write_file_path="/tmp/")
def main():
    input_x = Tensor(np.array([[1.0], [2.0], [-4.0]]), mindspore.float32)
    input_y = 0.5
    _pow = ops.Pow()
    out = _pow(input_x, input_y)

    print(out)
    print(out.dtype)


if __name__ == '__main__':
    main()
