#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

from mindspore import Tensor, nn, ops
import numpy as np
import mindspore

import troubleshooter as ts

with ts.proposal(write_file_path="/tmp/"):
    paddings = ((-1, 1), (2, 2))
    net = nn.Pad(paddings, mode="SYMMETRIC")
    x = Tensor(np.array([[1, 2, 3], [4, 5, 6]]), mindspore.float32)
    print("x=", x.shape)
    y = net(x)
    print(y.shape)
