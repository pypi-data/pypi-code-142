#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

from mindspore import Tensor, nn
import mindspore.context as context
import mindspore as ms
import mindspore.ops as ops
import numpy as np

import troubleshooter as ts

context.set_context(mode=context.PYNATIVE_MODE)


# context.set_context(save_graphs=True, save_graphs_path="./graphs")

# @ts.snooping(depth=20, filter={"not_in_func": ["construct"], "path": ["site-packages/mindspore"]})
class avgPoolDemo(nn.Cell):
    def __init__(self):
        super(avgPoolDemo, self).__init__()
        self.conv3d = nn.Conv3d(in_channels=2, out_channels=2, kernel_size=(1, 1, 1))
        self.pool = ops.AvgPool3D(kernel_size=(2, 2, 3), strides=1, pad_mode="valid")
        self.squeeze2 = ops.Squeeze(2)

    def construct(self, inputs):
        x = self.conv3d(inputs)
        x = self.pool(x)
        x = self.squeeze2(x)
        x = self.squeeze2(x)
        x = self.squeeze2(x)
        return x


@ts.tracking(depth=4)
def main():
    test_net = avgPoolDemo()
    # predict
    x = Tensor(np.arange(1 * 2 * 2 * 2 * 3).reshape((1, 2, 2, 2, 3)), ms.float32)
    out = test_net(x)
    print("out = ", out)


if __name__ == "__main__":
    main()
