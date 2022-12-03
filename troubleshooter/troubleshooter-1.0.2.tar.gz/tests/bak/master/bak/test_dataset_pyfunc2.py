#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""

import os
import numpy as np
import mindspore.dataset as ds
import mindspore.dataset.vision.c_transforms as C
import mindspore.dataset.vision.py_transforms as P
from mindspore.dataset.vision import Inter

import random
from PIL import Image
import troubleshooter as ts
import numpy as np

imagenet_path = "../../../data"


class GetDatasetGenerator:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.seg_name = os.listdir(os.path.join(root_dir, "n02095570"))
        self.img_name = os.listdir(os.path.join(root_dir, "n02095570"))

    def __getitem__(self, index):
        segment_name = self.seg_name[index]
        img_name = self.seg_name[index]
        segment_path = os.path.join(self.root_dir, "n02095570", segment_name)
        img_path = os.path.join(self.root_dir, "n02095570", img_name)
        image_img = Image.open(img_path)
        segment_img = Image.open(segment_path)

        image_np = np.array(image_img)
        segment_np = np.array(segment_img)

        return image_np, segment_np

    def __len__(self):
        return len(self.img_name)


class pyfunc_crop_error():
    def __init__(self, scale, patch):
        self.s = scale
        self.patch = patch

    def __call__(self, image, label):
        print(type(image))
        data, label = image, label
        h, w = data.shape[:2]

        ix = random.randrange(0, w - self.patch + 1)
        iy = random.randrange(0, h - self.patch + 1)

        data_patch = data[..., iy: iy + self.patch, ix: ix + self.patch]
        label_patch = label[..., iy: iy + self.patch, ix: ix + self.patch]

        return {'data': data_patch, 'label': label_patch}


@ts.proposal(write_file_path="/tmp/")
def test_pyfunc_crop_error():
    generator = GetDatasetGenerator(imagenet_path)
    dataset = ds.GeneratorDataset(generator, ["data", "label"], shuffle=False)

    resize_op = C.Resize(size=(388, 388))
    # c_trans = [resize_op, py_func_crop(2, 24)]
    c_trans = [resize_op]
    dataset = dataset.map(operations=c_trans, input_columns=["data"])
    dataset = dataset.map(operations=c_trans, input_columns=["label"])
    dataset = dataset.map(operations=[pyfunc_crop_error(2, 24)], input_columns=["data", "label"])

    for data in dataset.create_dict_iterator():
        print(data["data"].shape, data["label"].shape)


if __name__ == '__main__':
    test_pyfunc_crop_error()
