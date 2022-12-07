# Copyright 2018 The KaiJIN Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""COLORSPACE
"""
import math
import random
import typing

import cv2
import PIL
from PIL import Image
import numpy as np

import torch
import torchvision.transforms.functional as tvf
import torchvision.transforms as tvt

import tw
from tw import transform as T
from tw.utils.logger import logger

__all__ = [
    "load_image",
    "to_color",
    "to_data_range",
    "rgb_to_yuv_bt709_videorange",
    "rgb_to_yuv_bt709_fullrange",
    "yuv_bt709_videorange_to_rgb",
    "yuv_bt709_fullrange_to_rgb",
    "rgb_to_bgr",
    "bgr_to_rgb",
    "rgb_to_yuv_bt601",
    "yuv_bt601_to_rgb",
    "rgb_to_yiq",
    "rgb_to_lhm",
    "rgb_to_xyz",
    "xyz_to_lab",
    "rgb_to_lab",
]


def load_image(path, format='cv2'):
  """loading

  Args:
      path (str): _description_
      format (str, optional): _description_. Defaults to 'cv2'.

  Returns:
      _type_: _description_
  """
  if format == 'cv2':
    return cv2.imread(path, cv2.IMREAD_UNCHANGED)
  elif format == 'pil':
    return Image.open(path)


def to_data_range(image, src_data_range, dst_data_range):
  if src_data_range == dst_data_range:
    return image
  if isinstance(image, np.ndarray):
    return image * (dst_data_range / src_data_range)
  elif isinstance(image, torch.Tensor):
    return image * (dst_data_range / src_data_range)
  else:
    raise NotImplementedError


def rgb_to_yuv_bt709_videorange(image, data_range=255.0):
  """image in [0, 255]
  """
  image = to_data_range(image, data_range, 255.0)

  if isinstance(image, np.ndarray):
    R, G, B = np.split(image, 3, axis=2)
    Y = 0.1826 * R + 0.6142 * G + 0.0620 * B + 16  # [16, 235]
    U = -0.1007 * R - 0.3385 * G + 0.4392 * B + 128  # [16, 240]
    V = 0.4392 * R - 0.3990 * G - 0.0402 * B + 128  # [16, 240]
    yuv_image = np.concatenate([Y, U, V], axis=2)

  elif isinstance(image, torch.Tensor):
    R, G, B = torch.split(image, 1, dim=-3)
    Y = 0.1826 * R + 0.6142 * G + 0.0620 * B + 16  # [16, 235]
    U = -0.1007 * R - 0.3385 * G + 0.4392 * B + 128  # [16, 240]
    V = 0.4392 * R - 0.3990 * G - 0.0402 * B + 128  # [16, 240]
    yuv_image = torch.cat([Y, U, V], dim=-3)

  else:
    raise NotImplementedError

  return to_data_range(yuv_image, 255.0, data_range)


def rgb_to_yuv_bt709_fullrange(image, data_range=255.0):
  """image in [0, 255]
  """
  image = to_data_range(image, data_range, 255.0)

  if isinstance(image, np.ndarray):
    R, G, B = np.split(image, 3, axis=2)
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B  # [0, 255]
    U = -0.1146 * R - 0.3854 * G + 0.5000 * B + 128  # [0, 255]
    V = 0.5000 * R - 0.4542 * G - 0.0468 * B + 128  # [0, 255]
    yuv_image = np.concatenate([Y, U, V], axis=2)

  elif isinstance(image, torch.Tensor):
    R, G, B = torch.split(image, 1, dim=-3)
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B  # [0, 255]
    U = -0.1146 * R - 0.3854 * G + 0.5000 * B + 128  # [0, 255]
    V = 0.5000 * R - 0.4542 * G - 0.0468 * B + 128  # [0, 255]
    yuv_image = torch.cat([Y, U, V], dim=-3)

  else:
    raise NotImplementedError

  return to_data_range(yuv_image, 255.0, data_range)


def yuv_bt709_videorange_to_rgb(image, data_range=255.0):
  """image in [0, 255]
  """
  image = to_data_range(image, data_range, 255.0)

  if isinstance(image, np.ndarray):
    Y, U, V = np.split(image, 3, axis=2)
    Y = Y - 16
    U = U - 128
    V = V - 128
    R = 1.1644 * Y + 1.7927 * V
    G = 1.1644 * Y - 0.2132 * U - 0.5329 * V
    B = 1.1644 * Y + 2.1124 * U
    image = np.concatenate([R, G, B], axis=2)

  elif isinstance(image, torch.Tensor):
    Y, U, V = torch.split(image, 1, dim=-3)
    Y = Y - 16
    U = U - 128
    V = V - 128
    R = 1.1644 * Y + 1.7927 * V
    G = 1.1644 * Y - 0.2132 * U - 0.5329 * V
    B = 1.1644 * Y + 2.1124 * U
    image = torch.cat([R, G, B], dim=-3)

  else:
    raise NotImplementedError

  return to_data_range(image, 255.0, data_range)


def yuv_bt709_fullrange_to_rgb(image, data_range=255.0):
  """image in [0, 255]
  """
  image = to_data_range(image, data_range, 255.0)

  if isinstance(image, np.ndarray):
    Y, U, V = np.split(image, 3, axis=2)
    Y = Y
    U = U - 128
    V = V - 128
    R = 1.000 * Y + 1.570 * V
    G = 1.000 * Y - 0.187 * U - 0.467 * V
    B = 1.000 * Y + 1.856 * U
    image = np.concatenate([R, G, B], axis=2)

  elif isinstance(image, torch.Tensor):
    Y, U, V = torch.split(image, 1, dim=-3)
    Y = Y
    U = U - 128
    V = V - 128
    R = 1.000 * Y + 1.570 * V
    G = 1.000 * Y - 0.187 * U - 0.467 * V
    B = 1.000 * Y + 1.856 * U
    image = torch.cat([R, G, B], dim=-3)

  else:
    raise NotImplementedError

  return to_data_range(image, 255.0, data_range)


def rgb_to_bgr(image):
  """image in [0, 255]
  """
  if isinstance(image, np.ndarray):
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

  elif isinstance(image, torch.Tensor):
    r, g, b = torch.split(image, 1, dim=-3)
    return torch.cat([b, g, r], dim=-3)

  else:
    raise NotImplementedError


def bgr_to_rgb(image):
  """image in [0, 255]
  """
  if isinstance(image, np.ndarray):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  elif isinstance(image, torch.Tensor):
    b, g, r = torch.split(image, 1, dim=-3)
    return torch.cat([r, g, b], dim=-3)

  else:
    raise NotImplementedError


def rgb_to_yuv_bt601(image, data_range=255.0):
  """Convert a batch of RGB images to a batch of YCbCr images

  It implements the ITU-R BT.601 conversion for standard-definition
  television. See more details in
  https://en.wikipedia.org/wiki/YCbCr#ITU-R_BT.601_conversion.

  Args:
      x: Batch of images with shape (N, 3, H, W). RGB color space, range [0, 255].

  Returns:
      Batch of images with shape (N, 3, H, W). YCbCr color space.
  """
  image = to_data_range(image, data_range, 1.0)

  if isinstance(image, np.ndarray):
    raise NotImplementedError

  elif isinstance(image, torch.Tensor):
    assert image.ndim == 4 and image.size(1) == 3
    weigth = torch.tensor([
        [65.481, -37.797, 112.0],
        [128.553, -74.203, -93.786],
        [24.966, 112.0, -18.214]]).to(image.device)
    bias = torch.tensor([16, 128, 128]).view(1, 3, 1, 1).to(image.device)
    yuv_image = torch.matmul(image.permute(0, 2, 3, 1), weigth).permute(0, 3, 1, 2) + bias

  else:
    raise NotImplementedError

  return to_data_range(yuv_image, 1.0, data_range)


def yuv_bt601_to_rgb(image, data_range=255.0):
  """Convert a batch of YCbCr images to a batch of RGB images

  It implements the inversion of the above rgb2ycbcr function.

  Args:
      x: Batch of images with shape (N, 3, H, W). YCbCr color space, range [0, 255].

  Returns:
      Batch of images with shape (N, 3, H, W). RGB color space.
  """
  image = to_data_range(image, data_range, 1.0)

  if isinstance(image, np.ndarray):
    raise NotImplementedError

  elif isinstance(image, torch.Tensor):
    assert image.ndim == 4 and image.size(1) == 3
    weight = 255. * torch.tensor([
        [0.00456621, 0.00456621, 0.00456621],
        [0, -0.00153632, 0.00791071],
        [0.00625893, -0.00318811, 0]]).to(image)
    bias = torch.tensor([-222.921, 135.576, -276.836]).view(1, 3, 1, 1).to(image)
    image = torch.matmul(image.permute(0, 2, 3, 1), weight).permute(0, 3, 1, 2) + bias

  else:
    raise NotImplementedError

  return to_data_range(image, 1.0, data_range)


def to_color(inputs, **kwargs):
  """gray to color

  Note:
    np.ndarray: [h, w, 1] or [h, w] -> [h, w, 3]
    torch.Tensor: [1, h, w] or [h, w] -> [3, h, w]
    PIL.Image:

  """
  if isinstance(inputs, np.ndarray):
    if inputs.ndim == 3 and inputs.shape[2] == 3:
      return inputs

    h, w = inputs.shape[:2]
    inputs = inputs.reshape([h, w, 1])
    return np.repeat(inputs, 3, axis=2)

  elif isinstance(inputs, Image.Image):
    return inputs.convert(mode='RGB')

  elif isinstance(inputs, torch.Tensor):
    if inputs.ndim == 3 and inputs.shape[0] == 3:
      return inputs

    h, w = inputs.shape[-2:]
    inputs = inputs.reshape(1, h, w)
    return inputs.repeat(3, 1, 1)

  else:
    raise NotImplementedError


def rgb_to_yiq(x: torch.Tensor, data_range=255.0) -> torch.Tensor:
  """Convert a batch of RGB images to a batch of YIQ images

  Args:
      x: Batch of images with shape (N, 3, H, W). RGB colour space.

  Returns:
      Batch of images with shape (N, 3, H, W). YIQ colour space.
  """
  x = to_data_range(x, data_range, 255.0)

  if isinstance(x, np.ndarray):
    raise NotImplementedError

  elif isinstance(x, torch.Tensor):
    yiq_weights = torch.tensor([[0.299, 0.587, 0.114], [0.5959, -0.2746, -0.3213], [0.2115, -0.5227, 0.3112]]).t().to(x)
    x = torch.matmul(x.permute(0, 2, 3, 1), yiq_weights).permute(0, 3, 1, 2)

  else:
    raise NotImplementedError

  return to_data_range(x, 255.0, data_range)


def rgb_to_lhm(x: torch.Tensor, data_range=255.0) -> torch.Tensor:
  """Convert a batch of RGB images to a batch of LHM images

  Args:
      x: Batch of images with shape (N, 3, H, W). RGB colour space.

  Returns:
      Batch of images with shape (N, 3, H, W). LHM colour space.

  Reference:
      https://arxiv.org/pdf/1608.07433.pdf
  """
  x = to_data_range(x, data_range, 255.0)

  if isinstance(x, np.ndarray):
    raise NotImplementedError

  elif isinstance(x, torch.Tensor):
    lhm_weights = torch.tensor([[0.2989, 0.587, 0.114], [0.3, 0.04, -0.35], [0.34, -0.6, 0.17]]).t().to(x)
    x = torch.matmul(x.permute(0, 2, 3, 1), lhm_weights).permute(0, 3, 1, 2)

  else:
    raise NotImplementedError

  return to_data_range(x, 255.0, data_range)


def _safe_frac_pow(x: torch.Tensor, p) -> torch.Tensor:
  EPS = torch.finfo(x.dtype).eps
  return torch.sign(x) * torch.abs(x + EPS).pow(p)


def rgb_to_xyz(x: torch.Tensor, data_range=255.0) -> torch.Tensor:
  """Convert a batch of RGB images to a batch of XYZ images

  Args:
      x: Batch of images with shape (N, 3, H, W). RGB colour space.

  Returns:
      Batch of images with shape (N, 3, H, W). XYZ colour space.
  """
  x = to_data_range(x, data_range, 1.0)

  if isinstance(x, np.ndarray):
    raise NotImplementedError

  elif isinstance(x, torch.Tensor):
    mask_below = (x <= 0.04045).to(x)
    mask_above = (x > 0.04045).to(x)

    tmp = x / 12.92 * mask_below + torch.pow((x + 0.055) / 1.055, 2.4) * mask_above

    weights_rgb_to_xyz = torch.tensor([[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750],
                                       [0.0193339, 0.1191920, 0.9503041]]).to(x)

    xyz = torch.matmul(tmp.permute(0, 2, 3, 1), weights_rgb_to_xyz.t()).permute(0, 3, 1, 2)

  else:
    raise NotImplementedError

  return xyz


def xyz_to_lab(x: torch.Tensor, illuminant: str = 'D50', observer: str = '2') -> torch.Tensor:
  """Convert a batch of XYZ images to a batch of LAB images

  Args:
      x: Batch of images with shape (N, 3, H, W). XYZ colour space.
      illuminant: {“A”, “D50”, “D55”, “D65”, “D75”, “E”}, optional. The name of the illuminant.
      observer: {“2”, “10”}, optional. The aperture angle of the observer.

  Returns:
      Batch of images with shape (N, 3, H, W). LAB colour space.
  """
  if isinstance(x, np.ndarray):
    raise NotImplementedError

  elif isinstance(x, torch.Tensor):
    epsilon = 0.008856
    kappa = 903.3
    illuminants = {
        'A': {'2': (1.098466069456375, 1, 0.3558228003436005),
              '10': (1.111420406956693, 1, 0.3519978321919493)},
        'D50': {'2': (0.9642119944211994, 1, 0.8251882845188288),
                '10': (0.9672062750333777, 1, 0.8142801513128616)},
        'D55': {'2': (0.956797052643698, 1, 0.9214805860173273),
                '10': (0.9579665682254781, 1, 0.9092525159847462)},
        'D65': {'2': (0.95047, 1., 1.08883),  # This was: `lab_ref_white`
                '10': (0.94809667673716, 1, 1.0730513595166162)},
        'D75': {'2': (0.9497220898840717, 1, 1.226393520724154),
                '10': (0.9441713925645873, 1, 1.2064272211720228)},
        'E': {'2': (1.0, 1.0, 1.0),
              '10': (1.0, 1.0, 1.0)}}

    illuminants_to_use = torch.tensor(illuminants[illuminant][observer]).to(x).view(1, 3, 1, 1)

    tmp = x / illuminants_to_use

    mask_below = tmp <= epsilon
    mask_above = tmp > epsilon
    tmp = _safe_frac_pow(tmp, 1. / 3.) * mask_above + (kappa * tmp + 16.) / 116. * mask_below

    weights_xyz_to_lab = torch.tensor([[0, 116., 0], [500., -500., 0], [0, 200., -200.]]).to(x)
    bias_xyz_to_lab = torch.tensor([-16., 0., 0.]).to(x).view(1, 3, 1, 1)

    x_lab = torch.matmul(tmp.permute(0, 2, 3, 1), weights_xyz_to_lab.t()).permute(0, 3, 1, 2) + bias_xyz_to_lab
    return x_lab

  else:
    raise NotImplementedError


def rgb_to_lab(x: torch.Tensor, data_range=255) -> torch.Tensor:
  """Convert a batch of RGB images to a batch of LAB images

  Args:
      x: Batch of images with shape (N, 3, H, W). RGB colour space.
      data_range: dynamic range of the input image.

  Returns:
      Batch of images with shape (N, 3, H, W). LAB colour space.
  """
  if isinstance(x, np.ndarray):
    raise NotImplementedError

  elif isinstance(x, torch.Tensor):
    lab = xyz_to_lab(rgb_to_xyz(x, data_range=float(data_range)))

  else:
    raise NotImplementedError

  return lab
