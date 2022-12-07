#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

from mindspore import Tensor, context
import numpy as np
import mindspore as ms
import mindspore.nn as nn
from mindspore.common.initializer import Normal
import troubleshooter as ts
from mindspore import load_checkpoint, load_param_into_net
import functools

class LeNet5(nn.Cell):
    def __init__(self, num_class=10, num_channel=1):
        super(LeNet5, self).__init__()
        # 定义所需要的运算
        self.conv1 = nn.Conv2d(num_channel, 6, 5, pad_mode='valid')
        self.conv2 = nn.Conv2d(6, 16, 5, pad_mode='valid')
        self.fc1 = nn.Dense(16 * 5 * 5, 120, weight_init=Normal(0.02))
        self.fc2 = nn.Dense(120, 84, weight_init=Normal(0.02))
        self.fc3 = nn.Dense(84, num_class, weight_init=Normal(0.02))
        self.relu = nn.ReLU()
        self.max_pool2d = nn.MaxPool2d(kernel_size=2, stride=2)
        self.flatten = nn.Flatten()

    #@exception_wrap()
    def construct(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.max_pool2d(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.max_pool2d(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

#@ts.proposal(print_clear_stack=True)
def test_lent():
    context.set_context(mode=context.PYNATIVE_MODE, device_target="CPU")
    x = np.arange(1 * 24 * 24).reshape(1, 1, 24, 24)
    x = Tensor(x, ms.float32)
    net = LeNet5()
    out = net(x)


# @ts.proposal(write_file_path="/tmp/")
def test_load_ckpt1():
    net = LeNet5()
    filename = "./data/"
    pdict = load_checkpoint(filename)


# @ts.proposal(write_file_path="/tmp/")
def test_load_ckpt2():
    net = LeNet5()
    filename = "data/lenet_7-2.ckpt"
    pdict = load_checkpoint(filename)


#@ts.proposal()
def test_load_param_into_net():
    net = LeNet5()
    filename = "data/resnet-10_78.ckpt"
    pdict = load_checkpoint(filename, filter_prefix="conv1")
    load_param_into_net(net, pdict)


if __name__ == "__main__":
    test_lent()
