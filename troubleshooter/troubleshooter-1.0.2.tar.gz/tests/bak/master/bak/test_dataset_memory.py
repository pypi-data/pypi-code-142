#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import os
import troubleshooter as ts


@ts.proposal(write_file_path="/tmp/")
def main():
    print("Test dataset memory not enough.")
    raise RuntimeError(f"Memory not enough: current free memory size")


if __name__ == '__main__':
    main()
