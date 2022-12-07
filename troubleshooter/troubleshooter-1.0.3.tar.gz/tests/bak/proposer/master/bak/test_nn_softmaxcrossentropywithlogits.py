#!/usr/bin/env python3
# coding=utf-8

import mindspore
from mindspore import ops
from mindspore import Tensor, nn
import numpy as np

import troubleshooter as ts


class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()
        self.loss = nn.SoftmaxCrossEntropyWithLogits(sparse=False)

    def construct(self, logits, labels):
        output = self.loss(logits, labels)
        return output


@ts.proposal(write_file_path="/tmp/")
def main():
    net = Net()
    logits = Tensor(np.array([[[2, 4, 1, 4, 5], [2, 1, 2, 4, 3]]]), mindspore.float32)
    labels = Tensor(np.array([[[0, 0, 0, 0, 1], [0, 0, 0, 1, 0]]]).astype(np.float32))
    print(logits.shape, labels.shape)
    out = net(logits, labels)
    print('out', out)


if __name__ == "__main__":
    main()
