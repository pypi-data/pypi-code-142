#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import os
from mindspore import context, nn, Tensor, ops
import mindspore
import numpy as np

from troubleshooter import proposal

context.set_context(mode=context.GRAPH_MODE, device_target="CPU")


class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()
        self.concat = ops.Concat()

    def construct(self, x):
        n = 1000
        input_x = ()
        for i in range(n):
            input_x += (x,)
        output = self.concat(input_x)
        return output


@proposal(write_file_path="/tmp/")
def demo():
    net = Net()
    x = Tensor(np.random.rand(1, 4, 16, 16), mindspore.float32)
    output = net(x)


if __name__ == '__main__':
    demo()
