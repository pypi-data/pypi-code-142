#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

from mindspore.nn import Cell
import mindspore
from mindspore import context
import troubleshooter as ts


class Net(Cell):
    def construct(x):
        return x

@ts.proposal(write_file_path="/tmp/")
def main():
    net = Net()
    out = net(2)
    print("out=", out)


class Net_LessInput(Cell):
    def construct(self, x, y):
        return x + y


@ts.proposal(write_file_path="/tmp/")
def less_input_case():
    context.set_context(mode=mindspore.PYNATIVE_MODE, pynative_synchronize=True)
    net = Net_LessInput()
    out = net(1)
    print(out)


class Net_MoreInput(Cell):
    def construct(self, x):
        return x

@ts.proposal(write_file_path="/tmp/")
def more_input_case():
    context.set_context(mode=mindspore.PYNATIVE_MODE, pynative_synchronize=True)
    net = Net_MoreInput()
    out = net(1, 2)
    print(out)





if __name__ == '__main__':
    more_input_case()
