#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""
from mindspore import context, nn
import troubleshooter as ts


class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()

    def construct(self, x):
        return x + self.y


@ts.proposal(write_file_path="/tmp/")
def main():
    net = Net()
    out = net(1)


if __name__ == '__main__':
    main()
