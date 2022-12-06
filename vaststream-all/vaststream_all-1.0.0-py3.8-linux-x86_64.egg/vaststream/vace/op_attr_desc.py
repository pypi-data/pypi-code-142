"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["ImgDesc", "CvtColorDesc", "NormalDesc", "ScaleDesc", 
           "PaddingDesc", "ResizeDesc", "TensorDesc", "CropDesc"]

from .common import *
from typing import List

class ImgDesc(ImageDesc):
    def __init__(self, imgShape: List[int], format:IMAGE_TYPE = IMAGE_TYPE.YUV_NV12):
        """
        Img Descrption.\n
        ----------\n
        imgShape [in]: image shape, shoule be [w, h] or [w, h, w_pitch, h_pitch].\n
        format [in]: image format.\n
        """
        super().__init__()
        if len(imgShape) == 2:
            self.width = self.widthPitch = imgShape[0]
            self.height = self.heightPitch = imgShape[1]      
        elif len(imgShape) == 4:
            self.width, self.height, self.widthPitch, self.heightPitch = imgShape
        else:
            raise Exception("imgShape should be [w, h] or [w, h, w_pitch, h_pitch].")
        self.format = format
        
class CvtColorDesc():
    def __init__(self, color_cvt_code: COLOR_CVT_CODE, color_space: COLOR_SPACE):
        """
        Cvt Color Descrption.\n
        ----------\n
        color_cvt_code [in]: coloe cvt code.\n
        color_space [in]: color space.\n
        """
        self.color_cvt_code = color_cvt_code
        self.color_space = color_space

class ResizeDesc():
    def __init__(self, type: RESIZE_TYPE, dsize: List[int] = None):
        """
        Resize Descrption.\n
        ----------\n
        type [in]: resize type.\n
        dsize [in]: reisze dst shape, should be [w, h], default None.\n
        """
        self.width, self.height = [0, 0]
        if dsize is not None:
            assert len(dsize) == 2, "dsize should be [w, h]."
            self.width, self.height = dsize
        self.type = type


class NormalDesc():
    def __init__(self, mean: List[float], std: List[float], type: NORM_TYPE = NORM_TYPE.DIV255):
        """
        Normal Descrption.\n
        ----------\n
        mean [in]: mean values, should be [mean0, mean1, mean2].\n
        std [in]: std values, should be [std0, std1, std2].\n
        """
        assert len(mean) == len(std) == 3, "input should have 3 channels's value"
        self.mean = mean
        self.std = std
        self.type = type

class ScaleDesc():
    def __init__(self, scale: List[float]):
        """
        Scale Descrption.\n
        ----------\n
        scale [in]: scale values, should be [scale0, scale1, scale2].\n
        """
        assert len(scale) == 3, "scale should have 3 channels's value"
        self.scale = scale

class PaddingDesc():
    def __init__(self, padding: List[int], type: PADDING_TYPE = PADDING_TYPE.CONSTANT):
        """
        Padding Descrption.\n
        ----------\n
        padding [in]: padding values, should be [padding0, padding1, padding2].\n
        type [in]: padding type.\n
        """
        assert len(padding) == 3, "padding_values should have 3 channels's value"
        self.padding = padding
        self.type = type

class TensorDesc():
    def __init__(self, type: TENSORIZATION_TYPE):
        """
        Tensor Descrption.\n
        ----------\n
        type [in]: tensorization type.\n
        """
        self.type = type


class CropDesc(CropRect):
    def __init__(
        self, 
        start_x: int, 
        start_y: int, 
        width: int = None,
        height: int = None
        ):
        """
        Crop Descrption.\n
        ----------\n
        start_x [in]: Image Crop start x, should be int value \n
        start_y [in]: Image Crop start y, should be int value \n
        width [in]: Image Crop width, should be int value \n
        height [in]: Image Crop height , should be int value \n

        """
        super().__init__()
        self.start_x = start_x
        self.start_y = start_y  
        self.width, self.height = [0, 0]
        if width is not None and height is not None:  
            self.width = width        
            self.height = height