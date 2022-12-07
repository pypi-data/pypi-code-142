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
"""PAD
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
    "pad",
]


def pad(inputs, left, top, right, bottom, fill_value=0, mode='constant'):
  """_summary_

  Args:
      inputs (_type_): _description_
      left (_type_): _description_
      top (_type_): _description_
      right (_type_): _description_
      bottom (_type_): _description_
      fill_value (int, optional): _description_. Defaults to 0.
  """
  if isinstance(inputs, np.ndarray):
    if inputs.ndim == 3:
      inputs = np.pad(inputs, ((top, bottom), (left, right), (0, 0)), mode=mode, constant_values=fill_value)
    elif inputs.ndim == 2:
      inputs = np.pad(inputs, ((top, bottom), (left, right)), mode=mode, constant_values=fill_value)
    return inputs

  elif isinstance(inputs, Image.Image):
    return tvf.pad(inputs, [left, top, right, bottom], mode=mode, value=fill_value)

  elif isinstance(inputs, torch.Tensor):
    return tvf.pad(inputs, [left, top, right, bottom], mode=mode, value=fill_value)

  else:
    raise NotImplementedError
