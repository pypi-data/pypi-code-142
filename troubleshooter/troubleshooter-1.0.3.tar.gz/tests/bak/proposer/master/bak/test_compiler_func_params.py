#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""
import mindspore.context as context
import mindspore.nn as nn
from mindspore import Tensor
from mindspore.nn import Cell
from mindspore import ops
from mindspore import dtype as mstype
import mindspore
import troubleshooter as ts

context.set_context(mode=mindspore.GRAPH_MODE, pynative_synchronize=False)


class Net(nn.Cell):
    def __init__(self):
        super().__init__()
        self.add = ops.Add()
        self.sub = ops.Sub()
        self.mul = ops.Mul()
        self.div = ops.Div()

    def func(x, y):
        return self.div(x, y)

    def construct(self, x, y):
        a = self.sub(x, 1)
        b = self.add(a, y)
        c = self.mul(b, self.func(a, a, b))
        return c


@ts.proposal(write_file_path="/tmp/")
def main():
    input1 = Tensor(3, mstype.float32)
    input2 = Tensor(2, mstype.float32)
    net = Net()
    out = net(input1, input2)
    print(out)


if __name__ == '__main__':
    main()
