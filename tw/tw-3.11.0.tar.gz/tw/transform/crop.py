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
    "crop",
    "random_crop",
    "center_crop",
    "center_crop_and_pad"
]


def crop(inputs, top, left, height, width, **kwargs):
  """Crop the given image at specified location and output size.
  If the image is torch Tensor, it is expected to have [..., H, W] shape, where ... means an arbitrary number of leading dimensions.
  If image size is smaller than output size along any edge, image is padded with 0 and then cropped.

  Args:
      inputs: Image to be cropped. (0,0) denotes the top left corner of the image.
      top (int): Vertical component of the top left corner of the crop box.
      left (int): Horizontal component of the top left corner of the crop box.
      height (int): Height of the crop box.
      width (int): Width of the crop box.

  """
  if isinstance(inputs, np.ndarray):
    return inputs[top: top + height, left: left + width]

  elif isinstance(inputs, Image.Image):
    return tvf.crop(inputs, top, left, height, width)

  elif isinstance(inputs, torch.Tensor):
    return tvf.crop(inputs, top, left, height, width)

  else:
    raise NotImplementedError


def _get_crop_coords(img_h, img_w, crop_h, crop_w, rh, rw):
  y1 = int((img_h - crop_h) * rh)
  y2 = y1 + crop_h
  x1 = int((img_w - crop_w) * rw)
  x2 = x1 + crop_w
  return x1, y1, x2, y2


def random_crop(inputs, height, width, **kwargs):
  """random crop, require width and height less than image

  Args:
      inputs ([type]): [description]
      height (int or float): output height, or keep ratio (0 ~ 1)
      width (int or float): output width, or keep ratio (0 ~ 1)

  Returns:
      [type]: [description]
  """
  rh = random.random()
  rw = random.random()

  if isinstance(inputs, np.ndarray):
    h, w = inputs.shape[:2]
    new_width = int(w * width) if width < 1 else width
    new_height = int(h * height) if height < 1 else height
    x1, y1, x2, y2 = _get_crop_coords(h, w, new_height, new_width, rh, rw)
    return inputs[y1:y2, x1:x2]

  elif isinstance(inputs, Image.Image):
    h, w = inputs.height, inputs.width
    new_width = int(w * width) if width < 1 else width
    new_height = int(h * height) if height < 1 else height
    x1, y1, x2, y2 = _get_crop_coords(h, w, new_height, new_width, rh, rw)
    inputs = tvf.crop(inputs, y1, x1, y2 - y1 + 1, x2 - x1 + 1)
    return inputs

  elif isinstance(inputs, torch.Tensor):
    h, w = inputs.shape[-2:]
    new_width = int(w * width) if width < 1 else width
    new_height = int(h * height) if height < 1 else height
    x1, y1, x2, y2 = _get_crop_coords(h, w, new_height, new_width, rh, rw)
    inputs = tvf.crop(inputs, y1, x1, y2 - y1 + 1, x2 - x1 + 1)
    return inputs

  else:
    raise NotImplementedError


def _get_center_crop_coords(height, width, crop_height, crop_width):
  y1 = (height - crop_height) // 2
  y2 = y1 + crop_height
  x1 = (width - crop_width) // 2
  x2 = x1 + crop_width
  return x1, y1, x2, y2


def center_crop(inputs, height, width, **kwargs):
  """crop inputs to target height and width.

  Args:
      inputs ([type]): [description]
      height (int or float): output height
      width (int or float): output width

  Returns:
      [type]: [description]
  """
  if isinstance(inputs, np.ndarray):
    h, w = inputs.shape[:2]
    x1, y1, x2, y2 = _get_center_crop_coords(h, w, height, width)
    return inputs[y1:y2, x1:x2]

  elif isinstance(inputs, Image.Image):
    h, w = inputs.height, inputs.width
    x1, y1, x2, y2 = _get_center_crop_coords(h, w, height, width)
    inputs = tvf.crop(inputs, y1, x1, y2 - y1 + 1, x2 - x1 + 1)
    return inputs

  elif isinstance(inputs, torch.Tensor):
    h, w = inputs.shape[-2:]
    x1, y1, x2, y2 = _get_center_crop_coords(h, w, height, width)
    inputs = tvf.crop(inputs, y1, x1, y2 - y1 + 1, x2 - x1 + 1)
    return inputs

  elif isinstance(inputs, (list, tuple, T.MetaBase)):
    raise NotImplementedError

  else:
    raise NotImplementedError


def _get_center_crop_and_pad_coords(h, w, height, width):
  crop_x = max([0, (width - w) // 2])
  crop_y = max([0, (height - h) // 2])
  crop_w = min([width, w])
  crop_h = min([height, h])
  src_x = max([0, (w - width) // 2])
  src_y = max([0, (h - height) // 2])
  crop_y1 = crop_y
  crop_y2 = max(min(crop_y + crop_h, height), 0)
  crop_x1 = max(crop_x, 0)
  crop_x2 = max(min(crop_x + crop_w, width), 0)
  src_y1 = max(src_y, 0)
  src_y2 = max(min(src_y + crop_h, h), 0)
  src_x1 = max(src_x, 0)
  src_x2 = max(min(src_x + crop_w, w), 0)
  return crop_y1, crop_y2, crop_x1, crop_x2, src_y1, src_y2, src_x1, src_x2


def center_crop_and_pad(inputs, height, width, fill_value=0, **kwargs):
  """center crop and padding image to target_height and target_width

    if image width or height is smaller than target size, it will prefer to pad
      to max side and then implement center crop.

    if image width or height is less than target size, it will center paste image
      to target size.

  Args:
      inputs ([type]): [description]
      height ([int]): target height
      width ([int]): target width
      fill_value ([float]): default to 0
  """
  assert height > 0 and width > 0, "height or width should larger than 0."

  if isinstance(inputs, np.ndarray):
    h, w, c = inputs.shape[:3]
    cy1, cy2, cx1, cx2, sy1, sy2, sx1, sx2 = _get_center_crop_and_pad_coords(h, w, height, width)
    new_img = np.ones([height, width, c], dtype=meta.bin.dtype) * fill_value
    new_img[cy1:cy2, cx1:cx2] = meta.bin[sy1:sy2, sx1:sx2]
    return new_img

  elif isinstance(inputs, Image.Image):
    raise NotImplementedError

  elif isinstance(inputs, torch.Tensor):
    new_shape = list(inputs.shape)
    h, w = new_shape[-2:]
    new_shape[-2] = height
    new_shape[-1] = width
    new_image = torch.ones(*new_shape).to(inputs) * fill_value
    cy1, cy2, cx1, cx2, sy1, sy2, sx1, sx2 = _get_center_crop_and_pad_coords(h, w, height, width)
    new_image[..., cy1:cy2, cx1:cx2] = inputs[..., sy1:sy2, sx1:sx2]
    return new_image

  elif isinstance(inputs, (list, tuple, T.MetaBase)):
    for meta in inputs:

      if isinstance(meta, T.ImageMeta):
        assert meta.bin.ndim == 3, "current require input to be 3-channel."
        h, w, c = meta.bin.shape
        cy1, cy2, cx1, cx2, sy1, sy2, sx1, sx2 = _get_center_crop_and_pad_coords(h, w, height, width)
        new_img = np.ones([height, width, c], dtype=meta.bin.dtype) * fill_value
        new_img[cy1:cy2, cx1:cx2] = meta.bin[sy1:sy2, sx1:sx2]
        meta.bin = new_img

      elif isinstance(meta, T.BoxListMeta):
        assert meta.is_affine_size
        h, w = meta.max_y, meta.max_x
        cy1, cy2, cx1, cx2, sy1, sy2, sx1, sx2 = _get_center_crop_and_pad_coords(h, w, height, width)
        meta.bboxes -= [sx1, sy1, sx1, sy1]
        meta.bboxes += [cx1, cy1, cx1, cy1]
        meta.set_affine_size(max_h=height, max_w=width)
        meta.clip_with_affine_size()

    return inputs

  else:
    raise NotImplementedError
