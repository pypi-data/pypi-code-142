#!/usr/bin/env python3
# coding=utf-8
import mindspore
from mindspore import Tensor, nn
from mindspore import context
import numpy as np

import troubleshooter as ts

#@ts.tracking(depth=25, filter={"not_in_func": ["construct"], "path": ["primitive.py"]})
@ts.tracking(level=2)
def main():
    context.set_context(mode=context.PYNATIVE_MODE)
    conv = nn.Conv2d(3, 2, 3, pad_mode='valid', weight_init="ones")
    relu = nn.ReLU()
    seq = nn.SequentialCell([conv, relu])
    x = Tensor(np.ones([1, 3, 4, 4]), dtype=mindspore.float32)
    output = seq(x)
    print(output)

if __name__ == '__main__':
        main()

