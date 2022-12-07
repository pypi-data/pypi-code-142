#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""
from mindspore import context, nn
import troubleshooter as ts

from mindspore import context

context.set_context(device_target="CPU")


class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()

    def construct(self, x):
        return x + self.y


def main():
    net = Net()
    out = net(1)


if __name__ == '__main__':
    main()
