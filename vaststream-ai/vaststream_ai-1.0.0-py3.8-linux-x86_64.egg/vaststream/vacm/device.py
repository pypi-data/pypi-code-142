"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["getDevice", "setDevice", "resetDevice"]

from _vaststream_pybind11 import vacm as _vacm
from .common import *
from .utils import *


def getDevice() -> int:
    """
    Get current device index..\n
    """
    return _vacm.getDevice()


@err_check
def setDevice(devIdx: int) -> int:
    """
    Set the device to be used in the process. All resources will be bound to the device specified.\n
    ----------\n
    devIdx [in]: Device index to be set.\n
    """
    return _vacm.setDevice(devIdx)


@err_check
def resetDevice(devIdx: int) -> int:
    """
    brief Reset the device used in the process. All resources bound to this device will be released.\n
    ----------\n
    devIdx [in]: Device index to be set.\n
    """
    return _vacm.resetDevice(devIdx)
