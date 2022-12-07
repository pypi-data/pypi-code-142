#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code for testing load dataset
"""

import mindspore.dataset as ds
import mindspore.dataset.vision.c_transforms as CV
import mindspore.dataset.transforms.c_transforms as C
from mindspore.dataset.vision import Inter
from mindspore.common import dtype as mstype
import troubleshooter as ts

from mindspore import context

context.set_context(mode=context.PYNATIVE_MODE)


def is_dataset_obj(obj):
    # print("type:", type(obj))
    return isinstance(obj, ds.engine.datasets_vision.MnistDataset)


def print_dataset(ds):
    mnist_it = ds.create_dict_iterator()
    data = next(mnist_it)
    #    'Image shape: {}'.format(data["image"].shape), 'Label: {}'.format(data["label"])
    #    for _, data in enumerate(mnist_dt):
    #        train_x = Tensor(data['image'].astype(np.float32))
    #        label = Tensor(data['label'].astype(np.int32))
    #        print("train image,", train_x.shape)
    #        print("train label,", label)
    #        image_shape = train_x.shape
    #        break
    return 'Image shape={}, Label: {}'.format(data["image"].shape, data["label"])


def create_dataset(data_path, batch_size=32, num_parallel_workers=1):
    """
    create dataset for train or test
    """
    # define dataset
    mnist_ds = ds.MnistDataset(data_path)
    print("type:", type(mnist_ds))
    resize_height, resize_width = 32, 32
    rescale = 1.0 / 255.0
    rescale_nml = 1 / 0.3081
    shift_nml = -1 * 0.1307 / 0.3081

    # define map operations
    resize_op = CV.Resize((resize_height, resize_width), interpolation=Inter.LINEAR)  # Bilinear mode
    rescale_nml_op = CV.Rescale(rescale_nml * rescale, shift_nml)
    hwc2chw_op = CV.HWC2CHW()
    type_cast_op = C.TypeCast(mstype.int32)

    # apply map operations on images
    # mnist_ds = mnist_ds.map(operations=type_cast_op, input_columns="label", num_parallel_workers=num_parallel_workers)
    # mnist_ds = mnist_ds.map(operations=resize_op, input_columns="image", num_parallel_workers=num_parallel_workers)
    # mnist_ds = mnist_ds.map(operations=rescale_nml_op, input_columns="image", num_parallel_workers=num_parallel_workers)
    # mnist_ds = mnist_ds.map(operations=hwc2chw_op, input_columns="image", num_parallel_workers=num_parallel_workers)
    mnist_ds = mnist_ds.map(operations=[rescale_nml_op, hwc2chw_op], input_columns="image",
                            num_parallel_workers=num_parallel_workers)
    mnist_ds = mnist_ds.map(operations=type_cast_op, input_columns="label", num_parallel_workers=num_parallel_workers)
    # apply DatasetOps
    mnist_ds = mnist_ds.shuffle(buffer_size=1024)
    mnist_ds = mnist_ds.batch(batch_size)

    return mnist_ds


# @ts.snooping(depth=3, prefix="", custom_repr=(is_dataset_obj, print_dataset), filter={"path": ["cell.py", "validators.py"]})
# @ts.snooping(depth=3, filter={"path": ["cell.py", "validators.py"]})
@ts.proposal(write_file_path="/tmp/")
def main():
    dataset = create_dataset("/opt/nvme0n1/dataset/MNIST_Data/train")

    print("\n create dict iterator")
    mnist_it = dataset.create_dict_iterator()
    data = next(mnist_it)
    print('Image shape: {}'.format(data["image"].shape), 'Label: {}'.format(data["label"]))


if __name__ == '__main__':
    main()
