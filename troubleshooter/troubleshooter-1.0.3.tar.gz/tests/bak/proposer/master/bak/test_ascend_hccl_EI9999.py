#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""
from mindspore import Tensor, nn, ops
import mindspore
import numpy as np

import troubleshooter as ts


@ts.proposal(write_file_path="/tmp/")
def main():
    raise ValueError("EI9999: XXXX")


if __name__ == '__main__':
    from tests.util import delete_file, file_and_key_match
    delete_file("/tmp/")
    main()
    assert file_and_key_match("/tmp/", "vm_id_1")

