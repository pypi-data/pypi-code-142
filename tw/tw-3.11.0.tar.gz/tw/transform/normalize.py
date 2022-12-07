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
"""NORMALIZE
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
    "to_float",
    "to_tensor",
    "to_pil",
]


def to_float(inputs, **kwargs):
  if isinstance(inputs, np.ndarray):
    return inputs.astype('float')

  elif isinstance(inputs, Image.Image):
    raise NotImplementedError

  elif isinstance(inputs, torch.Tensor):
    return inputs.float()

  else:
    raise NotImplementedError


def to_tensor(inputs, scale=None, mean=None, std=None, **kwargs):
  """to tensor: (x / scale - mean) / std and from HWC to CHW

  Args:
      inputs ([type]): [description]
      scale ([type], optional): [description]. Defaults to None.
      mean ([type], optional): [description]. Defaults to None.
      std ([type], optional): [description]. Defaults to None.

  Raises:
      NotImplementedError: [description]

  Returns:
      [type]: [description]
  """
  if isinstance(inputs, np.ndarray):
    if inputs.ndim == 3:
      m = torch.from_numpy(np.ascontiguousarray(inputs.transpose((2, 0, 1))))
    elif inputs.ndim == 2:
      m = torch.from_numpy(inputs)[None]
    elif inputs.ndim == 4:
      m = torch.from_numpy(np.ascontiguousarray(inputs.transpose((0, 3, 1, 2))))
    else:
      raise NotImplementedError(inputs.ndim)
    m = m.type(torch.FloatTensor)
    if scale is not None:
      m = m.float().div(scale)
    if mean is not None:
      m.sub_(torch.tensor(mean)[:, None, None])
    if std is not None:
      m.div_(torch.tensor(std)[:, None, None])
    return m

  elif isinstance(inputs, Image.Image):
    m = tvf.pil_to_tensor(inputs)
    m = m.float()
    if scale is not None:
      m = m.float().div(scale)
    if mean is not None:
      m.sub_(torch.tensor(mean)[:, None, None])
    if std is not None:
      m.div_(torch.tensor(std)[:, None, None])
    return m

  elif isinstance(inputs, torch.Tensor):
    return inputs

  else:
    raise NotImplementedError


def to_pil(inputs, **kwargs):
  if isinstance(inputs, np.ndarray):
    return Image.fromarray(np.uint8(inputs))

  elif isinstance(inputs, Image.Image):
    return inputs

  elif isinstance(inputs, torch.Tensor):
    raise NotImplementedError

  else:
    raise NotImplementedError
