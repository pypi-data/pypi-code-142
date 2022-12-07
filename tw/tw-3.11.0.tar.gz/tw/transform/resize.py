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
"""RESIZE
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
    "resize",
    "shortside_resize",
    "random_resize",
    "adaptive_resize",
]

INTER_MAPPING = {
    cv2.INTER_LINEAR: tvf.InterpolationMode.BILINEAR,
    cv2.INTER_NEAREST: tvf.InterpolationMode.NEAREST,
    cv2.INTER_CUBIC: tvf.InterpolationMode.BICUBIC,
    cv2.INTER_LANCZOS4: tvf.InterpolationMode.LANCZOS,
    #   tvf.InterpolationMode.BOX,
    #   tvf.InterpolationMode.HAMMING,
}


def _get_shortside_shape(h, w, min_size):
  if (w <= h and w == min_size) or (h <= w and h == min_size):
    ow, oh = w, h
  # resize
  if w < h:
    ow = min_size
    oh = int(min_size * h / w)
  else:
    oh = min_size
    ow = int(min_size * w / h)
  return oh, ow


def resize(inputs, height, width, interpolation=cv2.INTER_LINEAR, **kwargs):
  """inputs will be aspect sized by short side to min_size.

  Args:
      inputs ([type]): [description]
      min_size (int): image will aspect resize according to short side size.
      interpolation ([type], optional): [description]. Defaults to cv2.INTER_LINEAR.

  Returns:
      [type]: [description]
  """
  if isinstance(inputs, np.ndarray):
    return cv2.resize(inputs, dsize=(width, height), interpolation=interpolation)

  elif isinstance(inputs, Image.Image):
    return tvf.resize(inputs, (height, width), interpolation=INTER_MAPPING[interpolation])

  elif isinstance(inputs, torch.Tensor):
    return tvf.resize(inputs, (height, width), interpolation=INTER_MAPPING[interpolation])

  elif isinstance(inputs, (list, tuple, T.MetaBase)):
    for meta in inputs:
      if meta.source == T.COLORSPACE.HEATMAP:
        interpolation = cv2.INTER_NEAREST
      if isinstance(meta, T.ImageMeta):
        h, w = meta.bin.shape[:2]
        meta.bin = cv2.resize(meta.bin, dsize=(width, height), interpolation=interpolation)
        meta.transform.append(('resize', h, height, w, width))
      if isinstance(meta, T.VideoMeta):
        h, w = meta.bin.shape[1:3]
        meta.bin = np.array([cv2.resize(meta.bin[i], dsize=(width, height), interpolation=interpolation)
                            for i in range(meta.n)])
        meta.transform.append(('resize', h, height, w, width))
      if isinstance(meta, T.BoxListMeta):
        assert meta.is_affine_size
        scale_w = float(width) / meta.max_x
        scale_h = float(height) / meta.max_y
        if len(meta.bboxes) > 0:
          meta.bboxes *= np.array([scale_w, scale_h, scale_w, scale_h])
        meta.transform.append(('resize', meta.max_y, height, meta.max_x, width))
        meta.set_affine_size(height, width)
      if isinstance(meta, T.KpsListMeta):
        assert meta.is_affine_size
        scale_w = float(width) / meta.max_x
        scale_h = float(height) / meta.max_y
        if len(meta.keypoints):
          meta.keypoints *= [scale_w, scale_h]
        meta.transform.append(('resize', meta.max_y, height, meta.max_x, width))
        meta.set_affine_size(height, width)
    return inputs

  else:
    raise NotImplementedError


def _get_shortside_shape(h, w, min_size):
  if (w <= h and w == min_size) or (h <= w and h == min_size):
    ow, oh = w, h
  # resize
  if w < h:
    ow = min_size
    oh = int(min_size * h / w)
  else:
    oh = min_size
    ow = int(min_size * w / h)
  return oh, ow


def shortside_resize(inputs, min_size=256, interpolation=cv2.INTER_LINEAR, **kwargs):
  """inputs will be aspect sized by short side to min_size.

  Args:
      inputs ([type]): [description]
      min_size (int): image will aspect resize according to short side size.
      interpolation ([type], optional): [description]. Defaults to cv2.INTER_LINEAR.

  Returns:
      [type]: [description]
  """
  if isinstance(inputs, np.ndarray):
    h, w = inputs.shape[:2]
    oh, ow = _get_shortside_shape(h, w, min_size)
    return cv2.resize(inputs, dsize=(ow, oh), interpolation=interpolation)

  elif isinstance(inputs, Image.Image):
    return tvt.Resize(size=min_size, interpolation=INTER_MAPPING[interpolation])(inputs)

  elif isinstance(inputs, torch.Tensor):
    return tvt.Resize(size=min_size, interpolation=INTER_MAPPING[interpolation])(inputs)

  elif isinstance(inputs, (tuple, list, T.MetaBase)):
    for meta in inputs:
      if meta.source == T.COLORSPACE.HEATMAP:
        interpolation = cv2.INTER_NEAREST
      if isinstance(meta, T.ImageMeta):
        h, w = meta.bin.shape[:2]
        oh, ow = _get_shortside_shape(h, w, min_size)
        meta.bin = cv2.resize(meta.bin, dsize=(ow, oh), interpolation=interpolation)
      if isinstance(meta, T.VideoMeta):
        h, w = meta.bin.shape[1:3]
        oh, ow = _get_shortside_shape(h, w, min_size)
        meta.bin = np.array([cv2.resize(meta.bin[i], dsize=(ow, oh), interpolation=interpolation)
                            for i in range(meta.n)])
      if isinstance(meta, T.BoxListMeta):
        assert meta.is_affine_size
        oh, ow = _get_shortside_shape(meta.max_y, meta.max_x, min_size)
        scale_w = float(ow) / meta.max_x
        scale_h = float(oh) / meta.max_y
        meta.bboxes *= [scale_w, scale_h, scale_w, scale_h]
        meta.set_affine_size(oh, ow)
      if isinstance(meta, T.KpsListMeta):
        assert meta.is_affine_size
        oh, ow = _get_shortside_shape(meta.max_y, meta.max_x, min_size)
        scale_w = float(ow) / meta.max_x
        scale_h = float(oh) / meta.max_y
        meta.keypoints *= [scale_w, scale_h]
        meta.set_affine_size(oh, ow)
    return inputs

  else:
    raise NotImplementedError


def random_resize(inputs, scale_range=(1, 4), interpolation=cv2.INTER_LINEAR, **kwargs):
  """random resize inputs with aspect ratio.

  Args:
      inputs ([type]): [description]
      scale_range (tuple, optional): [description]. Defaults to (1, 4).
      interpolation ([type], optional): [description]. Defaults to cv2.INTER_LINEAR.

  Returns:
      [type]: [description]
  """
  _min, _max = scale_range
  scale = random.random() * (_max - _min) + _min

  if isinstance(inputs, np.ndarray):
    h, w = inputs.shape[:2]
    return cv2.resize(inputs, dsize=(int(w * scale), int(h * scale)), interpolation=interpolation)

  elif isinstance(inputs, Image.Image):
    h, w = inputs.height, inputs.width
    return tvf.resize(inputs, (int(h * scale), int(w * scale)), interpolation=INTER_MAPPING[interpolation])

  elif isinstance(inputs, torch.Tensor):
    h, w = inputs.shape[-2:]
    return tvf.resize(inputs, (int(h * scale), int(w * scale)), interpolation=INTER_MAPPING[interpolation])

  elif isinstance(inputs, (list, tuple, T.MetaBase)):
    scale_h, scale_w = scale, scale
    for meta in inputs:
      if meta.source == T.COLORSPACE.HEATMAP:
        interpolation = cv2.INTER_NEAREST
      if isinstance(meta, T.ImageMeta):
        h, w = meta.bin.shape[:2]
        height, width = int(h * scale_h), int(w * scale_w)
        meta.bin = cv2.resize(meta.bin, dsize=(width, height), interpolation=interpolation)
        meta.transform.append(('resize_scale', scale_h, scale_w))
      if isinstance(meta, T.VideoMeta):
        h, w = meta.bin[0].shape[:2]
        height, width = int(h * scale_h), int(w * scale_w)
        meta.bin = np.array([cv2.resize(meta.bin[i], dsize=(width, height), interpolation=interpolation)
                            for i in range(meta.n)])
        meta.transform.append(('resize_scale', scale_h, scale_w))
      if isinstance(meta, T.BoxListMeta):
        assert meta.is_affine_size
        if len(meta.bboxes):
          meta.bboxes *= [scale_w, scale_h, scale_w, scale_h]
        meta.set_affine_size(height, width)
        meta.transform.append(('resize_scale', scale_h, scale_w))
      if isinstance(meta, T.KpsListMeta):
        assert meta.is_affine_size
        if len(meta.keypoints):
          meta.keypoints *= [scale_w, scale_h]
        meta.set_affine_size(height, width)
        meta.transform.append(('resize_scale', scale_h, scale_w))
    return inputs

  else:
    raise NotImplementedError


def adaptive_resize(inputs, height, width, interpolation=cv2.INTER_LINEAR, **kwargs):
  """_summary_

  Args:
      inputs (_type_): _description_
      height (_type_): _description_
      width (_type_): _description_
      interpolation (_type_, optional): _description_. Defaults to cv2.INTER_LINEAR.

  Raises:
      NotImplementedError: _description_

  Returns:
      _type_: _description_
  """
  if isinstance(inputs, np.ndarray):
    h, w = inputs.shape[:2]
    if h < height or w < width:
      return inputs
    return shortside_resize(inputs, min(height, width), interpolation=interpolation)

  elif isinstance(inputs, Image.Image):
    h, w = inputs.height, inputs.width
    if h < height or w < width:
      return inputs
    return tvf.resize(inputs, (height, width), interpolation=INTER_MAPPING[interpolation])

  elif isinstance(inputs, torch.Tensor):
    h, w = inputs.shape[-2:]
    if h < height or w < width:
      return inputs
    return tvf.resize(inputs, (height, width), interpolation=INTER_MAPPING[interpolation])

  elif isinstance(inputs, (list, tuple, T.MetaBase)):
    raise NotImplementedError

  else:
    raise NotImplementedError
