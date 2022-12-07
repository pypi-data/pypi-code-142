#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import numpy as np
import mindspore as ms
import mindspore.ops as ops
from mindspore import nn, Tensor, context
import troubleshooter as ts

context.set_context(mode=context.GRAPH_MODE)


class Net(nn.Cell):
    def __init__(self):
        super().__init__()
        self.relu = ops.ReLU()
        self.reducesum = ops.ReduceSum()

    def construct(self, x, a, b):
        if a > b:
            return self.relu(x)  # shape: (2, 3, 4, 5), dtype:Float32
        else:
            return self.reducesum(x)  # shape:(), dype: Float32


@ts.proposal(write_file_path="/tmp/")
def main():
    input_x = Tensor(np.random.rand(2, 3, 4, 5).astype(np.float32))
    input_a = Tensor(2, ms.float32)
    input_b = Tensor(6, ms.float32)
    net = Net()
    out = net(input_x, input_a, input_b)


if __name__ == '__main__':
    main()
