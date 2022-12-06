"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "DEVICE_TYPE", "DeviceInfo", "createDataBuffer", "createDataBufferFromContext", "destroyDataBuffer",
    "getDataBufferAddr", "getDataBufferSize", "getDataBufferDeviceInfo", "updateDataBuffer"
    ]

from typing import Any
from _vaststream_pybind11 import vacm as _vacm
from .common import *
from .utils import *


# =========================== ENUM =============================
class DEVICE_TYPE():
    """
    vacm device type.\n
    ----------\n
    @enum CPU: in CPU.\n
    @enum VACC: in VACC\n
    """
    CPU: int = _vacm.deviceType.vacmDE_CPU
    VACC: int = _vacm.deviceType.vacmDE_VACC

# =========================== STRUCT =============================

class DeviceInfo(_vacm.deviceInfo):
    """
    device information
    """
    deviceType: DEVICE_TYPE
    deviceIdx: int

# =========================== API =============================
def createDataBuffer(devInfo: DeviceInfo, handle: DataHandle, size: int) -> DataBuffer:
    """
    Create a data buffer.\n
    ------------\n
    devInfo [in]: device information.\n
    handle [in]: handle of data buffer.\n
    size [in]: buffer size.\n
    """
    return DataBuffer(_vacm.createDataBuffer(devInfo, handle.ptr, size))

def createDataBufferFromContext(devType: DEVICE_TYPE, handle: DataHandle, size: int) -> DataBuffer:
    """
    Create a data buffer from device context.\n
    ------------\n
    devType [in]: device type.\n
    handle [in]: handle of data buffer.\n
    size [in]: buffer size.\n
    """
    return DataBuffer(_vacm.createDataBufferFromContext(devType, handle.ptr, size))

@err_check
def destroyDataBuffer(buffer: DataBuffer) -> int:
    """
    Destroy a data buffer.\n
    ------------\n
    buffer [in]: data buffer.\n
    """
    return _vacm.destroyDataBuffer(buffer.ptr)

def getDataBufferAddr(buffer: DataBuffer) -> DataHandle:
    """
    Get the buffer address for a data buffer.\n
    ------------\n
    buffer [in]: data buffer.\n
    """ 
    
    return DataHandle(_vacm.getDataBufferAddr(buffer.ptr))

def getDataBufferSize(buffer: DataBuffer) -> int:
    """
    Get the buffer size for a data buffer.\n
    ------------\n
    buffer [in]: data buffer.\n
    """ 
    return _vacm.getDataBufferSize(buffer.ptr)

def getDataBufferDeviceInfo(buffer: DataBuffer) -> DeviceInfo:
    """
    Get the device information for a data buffer.\n
    ------------\n
    buffer [in]: data buffer.\n
    """ 
    deviceInfo = _vacm.deviceInfo()
    ret = _vacm.getDataBufferDeviceInfo(buffer.ptr, deviceInfo)
    if ret != _vacm.ER_SUCCESS:
        raise Exception(f"getDataBufferDeviceInfo return error {ret}.")
    return deviceInfo

@err_check
def updateDataBuffer(buffer: DataBuffer, devInfo: DeviceInfo, handle: DataHandle, size: int) -> int:
    """
    Update a data buffer.\n
    ------------\n
    buffer [in]: data buffer.\n
    devInfo [in]: device information.\n
    handle [in]: handle of data buffer.\n
    size [in]: data buffer size.\n
    """ 
    return _vacm.updateDataBuffer(buffer.ptr, devInfo, handle.ptr, size)