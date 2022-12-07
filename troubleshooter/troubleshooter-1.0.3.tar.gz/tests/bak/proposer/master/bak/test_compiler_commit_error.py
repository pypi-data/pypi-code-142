#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""
import mindspore
from mindspore import context, nn
import troubleshooter as ts

context.set_context(mode=mindspore.GRAPH_MODE)
class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()
        self.n = 5.0

    def construct(self, x):
#       x + 2.0
        return x + self.n  # commit after code


@ts.proposal(write_file_path="/tmp/")
def main():
    net = Net()
    out = net(1)
    print(out)


if __name__ == '__main__':
    main()
