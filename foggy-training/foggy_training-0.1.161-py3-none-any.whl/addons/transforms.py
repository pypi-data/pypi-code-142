from typing import Union

import numpy as np
import pandas as pd
from sklearn import pipeline, preprocessing
from torch import nn


class CallableFunctionTransformer(pipeline.FunctionTransformer):
    def __call__(self, X):
        return super(CallableFunctionTransformer, self).transform(X)


def make_transformer(f, *args, **kwargs):
    return CallableFunctionTransformer(f, *args, **kwargs)


@make_transformer
def read_tifffile(filename: str):
    try:
        from tifffile import imread
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f'You must install tifffile (pip install tifffile) for this to work.')
    return imread(filename)


def _scale(array):
    shape = array.shape
    array = preprocessing.minmax_scale(array.reshape(-1, 1), feature_range=(0, 255)).astype(np.uint8)
    return array.reshape(*shape)


@make_transformer
def tiff_to_rgb(image):
    rgb = image[:, :, 2], image[:, :, 1], image[:, :, 0]
    rgb = [_scale(i) for i in rgb]
    return np.stack(rgb, axis=-1)


def read_file(file: str):
    return read_tifffile(file)


def pad_input(sample):
    required = 12 - sample.shape[0]
    if required:
        size = sample[0].shape[:-1]
        padding = np.zeros((required, *size, 11))
        sample = np.concatenate((sample, padding))
    assert sample.shape[0] == 12
    return sample


def read_datapoint(datapoint: Union[pd.Series, dict], read_y=True, padding=True):
    x = [read_file(f) for f in datapoint['filename']]
    x = np.array(x)

    if padding:
        x = pad_input(x)

    sample = dict(x=x)

    if read_y:
        y = read_file(datapoint['corresponding_agbm'])
        sample['y'] = y

    return sample


class TiffFileReader(nn.Module):
    """Scale Sentinel 2 optical channels"""

    def __init__(self, read_y: bool = True, padding: bool = True) -> None:
        super().__init__()
        self.read_y = read_y
        self.padding = padding

    def forward(self, data):
        if isinstance(data, pd.DataFrame):
            data = [read_datapoint(row[1], read_y=self.read_y, padding=self.padding) for row in data.iterrows()]
            xs = np.stack([d['x'] for d in data])
            ys = np.stack([d['y'] for d in data])
            data = dict(x=xs, y=ys)

        elif isinstance(data, (pd.Series, dict)):
            data = read_datapoint(data, read_y=self.read_y, padding=self.padding)
        else:
            raise ValueError(f'Expected data to be either pd.DataFrame, pd.Series or dict. You passed {type(data)}')
        return data


class Sentinel2Scale(nn.Module):
    """Scale Sentinel 2 optical channels"""

    def __init__(self) -> None:
        super().__init__()

    def forward(self, data):
        x = data['x']
        scale_val = 4000.  # True scaling is [0, 10000], most info is in [0, 4000] range
        x = x / scale_val

        # CLP values in band 10 are scaled differently than optical bands, [0, 100]
        x[..., 10] = x[..., 10] * scale_val / 100.

        try:
            x = x.clamp(0, 1.)
        except AttributeError:
            x = np.clip(x, 0, 1)

        data['x'] = x

        return data


class Sentinel1Scale(nn.Module):
    """Scale Sentinel 1 SAR channels"""

    def __init__(self) -> None:
        super().__init__()

    def forward(self, data):
        x = data['x']
        s1_max = 20.  # S1 db values range mostly from -50 to +20 per empirical analysis
        s1_min = -50.
        x = (x - s1_min) / (s1_max - s1_min)

        try:
            x = x.clamp(0, 1.)
        except AttributeError:
            x = np.clip(x, 0, 1)

        data['x'] = x

        return data


class ExtractRGB(nn.Module):
    def __init__(self, key: str = 'RGB') -> None:
        super().__init__()
        self.key = key

    def forward(self, data):
        x = data['x']
        rgb_channels = x[..., (2, 1, 0)]
        data[self.key] = rgb_channels
        return data
