"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["DataHandle", "Dataset", "DataBuffer", "Tensor", "Context", "D_TYPE", "SUCCESS", "NOT_IMPLEMENT"]
from _vaststream_pybind11 import vacm as _vacm
from .utils import *

class DataHandle(PointerContainer):
    """
    DataHandle Container
    """
    pass

class Dataset(PointerContainer):
    """
    Dataset Container
    """
    pass

class DataBuffer(PointerContainer):
    """
    DataBuffer Container
    """
    pass

class Tensor(PointerContainer):
    """
    Tensor Container
    """
    pass

class Context(PointerContainer):
    """
    Context Container
    """
    pass


# =========================== ENUM =============================


class D_TYPE():
    """
    vacm data type.\n
    ----------\n
    @enum UINT8\n
    @enum INT8\n
    @enum UINT16\n
    @enum INT16\n
    @enum UINT32\n
    @enum INT32\n
    @enum FLOAT16\n
    @enum FLOAT32\n
    @enum BFLOAT\n
    @enum ANY\n
    """
    UINT8: int = _vacm.dType.vacmDT_UINT8
    INT8: int = _vacm.dType.vacmDT_INT8
    UINT16: int = _vacm.dType.vacmDT_UINT16
    INT16: int = _vacm.dType.vacmDT_INT16
    UINT32: int = _vacm.dType.vacmDT_UINT32
    INT32: int = _vacm.dType.vacmDT_INT32
    FLOAT16: int = _vacm.dType.vacmDT_FLOAT16
    FLOAT32: int = _vacm.dType.vacmDT_FLOAT32
    BFLOAT: int = _vacm.dType.vacmDT_BFLOAT
    ANY: int = _vacm.dType.vacmDT_ANY


# =========================== DEFINE =============================
SUCCESS = _vacm.ER_SUCCESS
NOT_IMPLEMENT = _vacm.ER_NOT_IMPLEMENT
