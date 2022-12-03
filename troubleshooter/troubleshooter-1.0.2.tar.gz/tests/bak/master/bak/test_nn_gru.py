#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import os
import mindspore
from mindspore import Tensor
from mindspore import nn, context
import numpy as np

import troubleshooter as ts

context.set_context(mode=context.GRAPH_MODE)


class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()
        self.gru = nn.GRU(10, 16, 1000, has_bias=True, batch_first=True, bidirectional=False)

    def construct(self, x, h0):
        output = self.gru(x, h0)
        return output


with ts.proposal(write_file_path="/tmp/") as ts:
    net = Net()
    x = Tensor(np.ones([3, 5, 10]).astype(np.float32))
    h0 = Tensor(np.ones([1 * 1000, 3, 16]).astype(np.float32))
    output, hn = net(x, h0)
    print('output', output.shape)
