"""
Image
-----
It provides functions to process and load the image data for machine learning.
"""


import torch
import numpy
import pandas
from tqdm import tqdm
from PIL import Image
from ailca.core.env import *
from ailca.data.base import Data, Dataset


def get_image_data(path_img_file: str) -> torch.Tensor:
    """
    Read an image data from a given image file in ``path_img_file``.

    :param path_img_file: (*str*) Path of the image file.
    :return: (*torch.Tensor*) A tensor object of the image file.
    """

    img = torch.tensor(numpy.array(Image.open(path_img_file).convert('RGB')), dtype=torch.float)

    return torch.swapaxes(img, 0, 2)


def load_dataset(path_metadata_file: str,
                 path_imgs: str,
                 idx_img_id: int,
                 idx_target: int = None,
                 verbose: bool = True) -> Dataset:
    """
    Load the dataset containing the numerical features.
    If ``idx_target`` is given, the dataset is loaded with the target values.

    :param path_metadata_file: (*str*) The path of the metadata file of the image data.
    :param path_imgs: (*str*) A directory of the image files.
    :param idx_img_id: (*int*) An index of the image identifiers in the metadata file.
    :param idx_target: (*int, optional*) An index of the target values in the data file (*default* = ``None``).
    :param verbose: (*bool*) A flag variable to present the system log in data loading (*default* = ``True``).
    :return: (*Dataset*) A dataset object.
    """

    metadata_file = pandas.read_excel(path_metadata_file)
    metadata = numpy.array(metadata_file)
    names_feats = [metadata_file.columns.values[idx_img_id]]
    name_target = None if idx_target is None else metadata_file.columns.values[idx_target]
    iter_range = range(0, metadata.shape[0])
    list_data = list()

    # If ``verbose`` is ``True``, the loading bar is presented through the standard I/O.
    if verbose:
        iter_range = tqdm(iter_range)

    # Read images in the dataset.
    for i in iter_range:
        img = get_image_data(path_imgs + '/' + metadata[i, idx_img_id])

        if idx_target is None:
            list_data.append(Data(x=img, idx=i, dtype=DTYPE_IMG))
        else:
            list_data.append(Data(x=img, y=metadata[i, idx_target], idx=i, dtype=DTYPE_IMG))

    return Dataset(list_data,
                   idx_img_id=idx_img_id,
                   idx_target=idx_target,
                   names_feats=names_feats,
                   name_target=name_target,
                   types_feats=[DTYPE_IMG for i in range(0, len(names_feats))])
