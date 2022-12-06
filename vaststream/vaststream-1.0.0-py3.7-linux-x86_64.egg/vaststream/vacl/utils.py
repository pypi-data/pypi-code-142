"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

import numpy as np
from typing import Any
from _vaststream_pybind11 import vacl as _vacl, vacm as _vacm
from vaststream.vacm import DataHandle

__all__ = ["PointerContainer", "err_check", "loadImage"]

class PointerContainer():
    """
    Pointer Container
    """
    def __init__(self, _ptr: Any):
        self._ptr = _ptr
        
    @property
    def ptr(self):
        return self._ptr

# 返回值校验
def err_check(func):
    def wrapper(*args,**kwargs):
        ret = func(*args,**kwargs)
        if ret != _vacl.vaclER_SUCCESS:
            raise Exception(f"{func.__name__} return error {ret}.")
        return ret
    return wrapper

def loadImage(imageFile:str, imageWidth:int, imageHeight:int) -> DataHandle:
    """
    load the test image\n
    --------------\n
     imageFile [in]: the image file.\n
     imageWidth [in]: the image width.\n
     imageHeight [in]: the image height.\n
    """
    return DataHandle(_vacl.loadImage(imageFile, imageWidth, imageHeight))

