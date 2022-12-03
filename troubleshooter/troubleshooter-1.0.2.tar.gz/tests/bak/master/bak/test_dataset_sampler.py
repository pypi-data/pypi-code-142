#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import mindspore.dataset as ds

import troubleshooter as ts


class MySampler(ds.Sampler):
    def __init__(self):
        # self.num_samples = 10
        self.dataset_size = 0
        self.child_sampler = None

    def __iter__(self):
        for i in range(0, 10, 2):
            yield i


@ts.proposal(write_file_path="/tmp/")
def main():
    DATA_DIR = "../../../data/cifar-10-batches/"
    dataset = ds.Cifar10Dataset(DATA_DIR, sampler=MySampler())
    for data in dataset.create_dict_iterator():
        print("Image shape:", data['image'].shape, ", Label:", data['label'])


if __name__ == '__main__':
    main()
