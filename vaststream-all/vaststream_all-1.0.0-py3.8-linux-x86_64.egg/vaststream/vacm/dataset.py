"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "DATASET_MODE", "createDataset", "destroyDataset", "addDatasetBuffer", "getDatasetBufferCount",
    "getDatasetBuffer", "addDatasetTensor", "getDatasetTensorCount", "getDatasetTensor", "getDatasetMode",
    "getDatasetUserCtx", "setDatasetUserCtx", "clearDataset"
    ]

from typing import Any
from _vaststream_pybind11 import vacm as _vacm
from .tensor import *
from .common import *
from .utils import *

# =========================== ENUM =============================
class DATASET_MODE():
    """
    vacm dataset mode.\n
    ----------\n
    @enum BUFFER: buffer dataset mode.\n
    @enum TENSOR: tensor dataset mode.\n
    """
    BUFFER: int = _vacm.datasetMode.vacmDM_BUFFER
    TENSOR: int = _vacm.datasetMode.vacmDM_TENSOR


# =========================== API =============================
def createDataset(mode: DATASET_MODE) -> Dataset:
    """
    Create a dataset.\n
    ------------\n
    mode [in]: dataset mode.\n
    """
    return Dataset(_vacm.createDataset(mode))

@err_check
def destroyDataset(dataset: Dataset) -> int:
    """
    Destroy a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    """
    return _vacm.destroyDataset(dataset.ptr)

@err_check
def addDatasetBuffer(dataset: Dataset, buffer: DataBuffer) -> int:
    """
    Add a dataset buffer.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    buffer [in]: the data buffer instance to be added.\n 
    """
    return _vacm.addDatasetBuffer(dataset.ptr, buffer.ptr)

def getDatasetBufferCount(dataset: Dataset) -> int:
    """
    Get the data buffer count for a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    """
    return _vacm.getDatasetBufferCount(dataset.ptr)

def getDatasetBuffer(dataset: Dataset, index: int) -> DataBuffer:
    """
    Get the data buffer by index for a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    index [in]: Index of data buffer.\n
    """
    return DataBuffer(_vacm.getDatasetBuffer(dataset.ptr, index))

@err_check
def addDatasetTensor(dataset: Dataset, tensor: Tensor) -> int:
    """
    Add a tensor into a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    tensor [in]: the tensor instance to be added.\n
    """
    return _vacm.addDatasetTensor(dataset.ptr, tensor.ptr)

def getDatasetTensorCount(dataset: Dataset) -> int:
    """
    Get the tensor count for a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    """
    return _vacm.getDatasetTensorCount(dataset.ptr)

def getDatasetTensor(dataset: Dataset, index: int) -> Tensor:
    """
    Get the tensor by index for a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    index [in]: Index of the tensor.\n
    """
    return Tensor(_vacm.getDatasetTensor(dataset.ptr, index))

def getDatasetMode(dataset: Dataset) -> DATASET_MODE:
    """
    Get the mode for a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    """
    return _vacm.getDatasetMode(dataset.ptr)

def getDatasetUserCtx(dataset: Dataset) -> DataHandle:
    """
    Get the user context data for a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    """
    return DataHandle(_vacm.getDatasetUserCtx(dataset.ptr))

@err_check
def setDatasetUserCtx(dataset: Dataset, userCtx: DataHandle) -> int:
    """
    Set the user context data for a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    userCtx [in]: User defined context data for the dataset.\n
    """
    return _vacm.setDatasetUserCtx(dataset.ptr, userCtx.ptr)

@err_check
def clearDataset(dataset: Dataset) -> int:
    """
    Clear a dataset.\n
    ------------\n
    dataset [in]: a dataset instance.\n
    """
    return _vacm.clearDataset(dataset.ptr)
