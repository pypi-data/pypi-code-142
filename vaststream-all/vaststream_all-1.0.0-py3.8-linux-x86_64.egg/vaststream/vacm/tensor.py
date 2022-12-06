"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "Shape", "createTensor", "createTensorWithDataHandle", "destroyTensor", "getTensorDataHandle",
    "setTensorDataHandle", "getTensorDeviceInfo", "getTensorShape", "setTensorShape", "getTensorDataType",
    "setTensorDataType", "getTensorSize"
    ]

from typing import Any, List
from _vaststream_pybind11 import vacm as _vacm
from .databuffer import DeviceInfo
from .common import *
from .utils import *


# =========================== STRUCT =============================
class Shape(_vacm.shape):
    ndims: int
    shapes: List[int]


# =========================== API =============================

def createTensor(devInfo: DeviceInfo, shape: Shape, dType: D_TYPE) -> Tensor:
    """
    Create a tensor for a device with specific shapes and data type.\n
    ------------\n
    devInfo [in]: Device information for the tensor.\n
    shape [in]: shape of the tensor.\n
    dType [in]: data type of the tensor.\n
    """
    return Tensor(_vacm.createTensor(devInfo, shape, dType))

def createTensorWithDataHandle(devInfo: DeviceInfo, shape: Shape, dType: D_TYPE, handle: DataHandle, detach: bool = True) -> Tensor:
    """
    Create a tensor with data handle for a device with specific shapes and data type.\n
    ------------\n
    devInfo [in]: Device information for the tensor.\n
    shape [in]: shape of the tensor.\n
    dType [in]: data type of the tensor.\n
    handle [in]: a vacmDataHandle with the data handle.\n
    detach [in] whether the handle will be detached or not. If detached, the handle will be released by tensor.\n
    """
    return Tensor(_vacm.createTensorWithDataHandle(devInfo, shape, dType, handle.ptr, detach))

@err_check
def destroyTensor(tensor: Tensor) -> int:
    """
    Destroy a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.
    """
    return _vacm.destroyTensor(tensor.ptr)

def getTensorDataHandle(tensor: Tensor) -> DataHandle:
    """
    Get the data handle of a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.
    """
    return DataHandle(_vacm.getTensorDataHandle(tensor.ptr))

@err_check
def setTensorDataHandle(tensor: Tensor, handle: DataHandle, detach: bool = True) -> int:
    """
    Set the data handle for a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.\n
    handle [in]: a vacmDataHandle with the data handle to the tensor.\n
    detach [in] whether the handle will be detached or not. If detached, the handle will be released by tensor.\n
    """
    return _vacm.setTensorDataHandle(tensor.ptr, handle.ptr, detach)

def getTensorDeviceInfo(tensor: Tensor) -> DeviceInfo:
    """
    Get the device information of a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.\n
    """
    deviceInfo = _vacm.deviceInfo()
    ret = _vacm.getTensorDeviceInfo(tensor.ptr, deviceInfo)
    if ret != _vacm.ER_SUCCESS:
        raise Exception(f"getTensorDeviceInfo return error {ret}.")
    return deviceInfo

def getTensorShape(tensor: Tensor) -> Shape:
    """
    Get the data shape of a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.\n
    """
    shape = _vacm.shape()
    ret = _vacm.getTensorShape(tensor.ptr, shape)
    if ret != _vacm.ER_SUCCESS:
        raise Exception(f"getTensorShape return error {ret}.")
    return shape

@err_check
def setTensorShape(tensor: Tensor, shape: Shape) -> int:
    """
    Set the data shape of a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.\n
    shape [in]: a Shape to with the data shape.\n
    """
    return _vacm.setTensorShape(tensor.ptr, shape)

def getTensorDataType(tensor: Tensor) -> D_TYPE:
    """
    Get the data type of a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.\n
    """
    return _vacm.getTensorDataType(tensor.ptr)

@err_check
def setTensorDataType(tensor: Tensor, dType: D_TYPE) -> int:
    """
    Set the data type of a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.\n
    dType [in]: Data type to set.\n
    """
    return _vacm.setTensorDataType(tensor.ptr, dType)

def getTensorSize(tensor: Tensor) -> int:
    """
    Get the size of a tensor.\n
    ------------\n
    tensor [in]: the tensor instance.\n
    """
    return _vacm.getTensorSize(tensor.ptr)