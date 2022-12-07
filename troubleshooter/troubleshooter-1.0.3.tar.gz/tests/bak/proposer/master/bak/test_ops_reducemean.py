#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import mindspore
from mindspore import ops
from mindspore import Tensor, nn, context
import numpy as np
context.set_context(mode=context.GRAPH_MODE)

import troubleshooter as ts


class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()
        self.reduce_mean = ops.ReduceMean(keep_dims=True)

    def construct(self, x):
        out = self.reduce_mean(x, axis=(2, 3))
        return out


with ts.proposal(write_file_path="/tmp/"):
    net = Net()
    x = Tensor(np.ones((3, 4, 5, 6), dtype=np.float32), mindspore.float32)
    out = net(x)
    print('out', out.shape)
