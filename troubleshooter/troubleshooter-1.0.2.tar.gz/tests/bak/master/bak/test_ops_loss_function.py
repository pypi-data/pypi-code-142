#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import os
from mindspore import Tensor, nn
import numpy as np

import troubleshooter as ts


@ts.proposal(write_file_path="/tmp/")
def main():
    logits = Tensor(np.array([[-0.8, 1.2], [-0.1, -0.4]]).astype(np.float32))
    labels = Tensor(np.array([[0.3, 0.8, 1.2], [-0.6, 0.1, 2.2]]).astype(np.float32))
    # loss = nn.BCEWithLogitsLoss()
    loss = nn.MSELoss()
    output = loss(logits, labels)
    print(output)


if __name__ == '__main__':
    main()
