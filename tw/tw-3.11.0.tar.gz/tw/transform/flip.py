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
"""FLIP
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
    "vflip",
    "hflip",
    "random_vflip",
    "random_hflip",
]


def vflip(inputs, **kwargs):
  """vertical flip
  """
  if isinstance(inputs, np.ndarray):
    return np.ascontiguousarray(inputs[::-1, ...])

  elif isinstance(inputs, Image.Image):
    return tvf.vflip(inputs)

  elif isinstance(inputs, torch.Tensor):
    return tvf.vflip(inputs)

  else:
    raise NotImplementedError


def hflip(inputs, **kwargs):
  """horizontal flip
  """
  if isinstance(inputs, np.ndarray):
    return np.ascontiguousarray(inputs[:, ::-1, ...])

  elif isinstance(inputs, Image.Image):
    return tvf.hflip(inputs)

  elif isinstance(inputs, torch.Tensor):
    return tvf.hflip(inputs)

  else:
    raise NotImplementedError


def random_vfilp(inputs, p=0.5, **kwargs):
  if random.random() > p:
    return vflip(inputs, **kwargs)
  return inputs


def random_hfilp(inputs, p=0.5, **kwargs):
  if random.random() > p:
    return hflip(inputs, **kwargs)
  return inputs
