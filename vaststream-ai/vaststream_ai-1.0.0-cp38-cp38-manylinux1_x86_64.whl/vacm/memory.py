"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "COPY_MEM_TYPE", "mallocDevice", "freeDevice", "mallocModelInOut", "freeModelInOut",
    "memcpy", "getNumpyFromHandle", "getHandleFromNumpy", "memcpyDevices"
    ]


from typing import Any
from _vaststream_pybind11 import vacm as _vacm
from .common import *
from .utils import *
import numpy as np

# =========================== ENUM =============================
class COPY_MEM_TYPE():
    """
    vacm copy memory type.\n
    -----------\n
    @enum FROM_DEVICE: copy memory from device\n
    @enum TO_DEVICE: copy memory to device\n
    @enum DEVICE_TO_DEVICE: copy memory from device to device\n
    """
    FROM_DEVICE: int = _vacm.copyMemType.vacmCT_COPY_FROM_DEVICE
    TO_DEVICE: int = _vacm.copyMemType.vacmCT_COPY_TO_DEVICE
    DEVICE_TO_DEVICE: int = _vacm.copyMemType.vacmCT_COPY_DEVICE_TO_DEVICE


# =========================== API =============================
def mallocDevice(memSize: int) -> DataHandle:
    """
    Allocate memory from device.\n
    ------------\n
    memSize [in]: Size of memory in bytes.\n
    """
    return DataHandle(_vacm.malloc(memSize))

@err_check
def freeDevice(handle: DataHandle) -> int:
    """
    Free a memory in device.\n
    ------------\n
    handle [in]: the data handle with the memory information.\n
    """
    return _vacm.free(handle.ptr)

def mallocModelInOut(memSize: int) -> DataHandle:
    """
    Allocate memory for model input or output from device.\n
    ------------\n
    memSize [in]: Size of memory in bytes.\n
    """
    return DataHandle(_vacm.mallocModelInOut(memSize))

@err_check
def freeModelInOut(handle: DataHandle) -> int:
    """
    Free a model input or output memory in device.\n
    ------------\n
    handle [in]: the data handle with the memory information.\n
    """
    return _vacm.freeModelInOut(handle.ptr)

@err_check
def memcpy(handleSrc: DataHandle, handleDst: DataHandle, memSize: int, cmType: COPY_MEM_TYPE) -> int:
    """
    Copy a memory between host and device according to copy type. Synchronous interface.\n
    ------------\n
    handleSrc [in]: the data handle with the source memory.\n
    handleDst [in]: the data handle with the destination memory.\n
    memSize [in]: Size of memory in bytes to copy.\n
    cmType [in]: Type of copy.\n
    """
    return _vacm.memcpy(handleSrc.ptr, handleDst.ptr, memSize, cmType)

def getNumpyFromHandle(dataHandle: DataHandle, memSize: int) -> np.ndarray:
    """
    get the numpy array from data handle.\n
    ------------\n
    dataHandle [in]: the data handle of numpy array.\n
    memSize [in]: Size of memory in bytes to copy.\n
    """
    return _vacm.getNumpyFromHandle(dataHandle.ptr, memSize)
    
def getHandleFromNumpy(numpyData: np.ndarray) -> DataHandle:
    """
    get data handle from the numpy array.\n
    ------------\n
    numpyData [in]: the numpy array.\n
    """
    if numpyData.dtype != np.uint8:
        raise Exception("getHandleFromNumpy only support numpy.uint8 data type")
    np.ascontiguousarray(numpyData)
    return DataHandle(_vacm.getHandleFromNumpy(numpyData))
    
# @err_check
# def memcpyAsync(handleSrc: DataHandle, handleDst: DataHandle, memSize: int, cmType: COPY_MEM_TYPE, evt: Any) -> int:
#     """
#     Copy a memory between host and device according to copy type. Asynchronous interface.\n
#     ------------\n
#     handleSrc [in]: the data handle with the source memory.\n
#     handleDst [in]: the data handle with the destination memory.\n
#     memSize [in]: Size of memory in bytes to copy.\n
#     cmType [in]: Type of copy.\n
#     evt [in]: a vacmEvent object which can be waited for operation to complete.\n
#     """
#     return _vacm.memcpyAsync(handleSrc.ptr, handleDst.ptr, memSize, cmType, evt)

@err_check
def memcpyDevices(handleSrc: DataHandle, devIdxSrc: int, handleDst: DataHandle, devIdxDst: int, memSize: int) -> int:
    """
    Copy a memory between two devices. Synchronous interface.\n
    ------------\n
    handleSrc [in]: the data handle with the source memory.\n
    devIdxSrc [in]: Device index for the source memory.\n
    handleDst [in]: the data handle with the destination memory.\n
    devIdxDst [in]: Device index for the destination memory.\n
    memSize [in]: Size of memory in bytes to copy.\n
    """
    return _vacm.memcpyDevices(handleSrc.ptr, devIdxSrc, handleDst.ptr, devIdxDst, memSize)

# @err_check
# def memcpyDevicesAsync(handleSrc: DataHandle, devIdxSrc: int, handleDst: DataHandle, devIdxDst: int, memSize: int, evt: Any) -> int:
#     """
#     Copy a memory between two devices. Asynchronous interface.\n
#     ------------\n
#     handleSrc [in]: the data handle with the source memory.\n
#     devIdxSrc [in]: Device index for the source memory.\n
#     handleDst [in]: the data handle with the destination memory.\n
#     devIdxDst [in]: Device index for the destination memory.\n
#     memSize [in]: Size of memory in bytes to copy.\n
#     evt [in]: a vacmEvent object which can be waited for operation to complete.\n
#     """
#     return _vacm.memcpyDevicesAsync(handleSrc.ptr, devIdxSrc, handleDst.ptr, devIdxDst, memSize, evt)

# @err_check
# def memset(handle: DataHandle, value: int, count: int) -> int:
#     """
#     Set a memory block with a specific value. Synchronous interface.\n
#     ------------\n
#     handle [in]: the data handle with the memory.\n
#     value [in]: Value to be set.\n
#     count [in]: Count of memory size to be set.\n
#     """
#     return _vacm.memset(handle.ptr, value, count)

# @err_check
# def memsetAsync(handle: DataHandle, value: int, count: int, evt: Any) -> int:
#     """
#     Set a memory block with a specific value. Asynchronous interface.\n
#     ------------\n
#     handle [in]: the data handle with the memory.\n
#     value [in]: Value to be set.\n
#     count [in]: Count of memory size to be set.\n
#     evt [in]: a vacmEvent object which can be waited for operation to complete.\n
#     """
#     return _vacm.memsetAsync(handle.ptr, value, count, evt)
