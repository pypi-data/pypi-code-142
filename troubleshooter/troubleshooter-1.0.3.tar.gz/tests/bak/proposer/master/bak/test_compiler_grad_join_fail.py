#!/usr/bin/env python3
# coding=utf-8
import numpy as np
import mindspore as ms
import mindspore.ops as ops
from mindspore import nn, Tensor, context
import troubleshooter as ts

from mindspore import ms_function


def func(a, b):
    return a, b


grad = ops.GradOperation(get_by_list=False, sens_param=True)


@ms_function()
def test_grad(x, y, sens):
    sens_i = ops.Fill()(ops.DType()(x), ops.Shape()(x), sens)
    a = grad(func)(x, y, sens_i)
    return a


@ts.proposal(write_file_path="/tmp/")
def grad_join_fail():
    x = Tensor([1.0])
    y = Tensor([2.0])
    test_grad(x, y, 1.0)


if __name__ == "__main__":
    grad_join_fail()
