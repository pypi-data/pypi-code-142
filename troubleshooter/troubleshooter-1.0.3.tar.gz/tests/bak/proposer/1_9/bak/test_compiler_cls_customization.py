#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import os
import mindspore
import mindspore.nn as nn
import mindspore.ops as ops
import numpy as np
from mindspore import Tensor

import troubleshooter as ts
from mindspore.common.initializer import initializer, XavierUniform
from mindspore import context


context.set_context(mode=mindspore.GRAPH_MODE)
class LayerParams:
    def __init__(self, dtype: str):
        self._type = dtype

    def get_weights(self, shape):
        nn_param = initializer(XavierUniform(), shape, mindspore.float32)
        nn_param = mindspore.Parameter(nn_param)
        return nn_param


class MyCell(nn.Cell):
    def __init__(self):
        super().__init__()
        self._fc_params = LayerParams("fc")
        self.matmul = ops.MatMul()

    def _fc(self, inputs, output_size):
        width = inputs.shape[-1]
        weight = self._fc_params.get_weights((width, output_size))
        return weight

    def construct(self, x, output_size):
        weight = self._fc(x, output_size)
        output = self.matmul(x, weight)
        return output


@ts.proposal(write_file_path="/tmp/")
def test_cls_customization():
    net = MyCell()
    inputs = Tensor(np.ones((2, 4), dtype=np.float32))
    outputs = net(inputs, 5)
    print(outputs.shape)


if __name__ == '__main__':
    test_cls_customization()
