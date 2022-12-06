"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8
__all__ = ["createContext", "destroyContext",
           "setCurrentContext", "getCurrentContext"]

from _vaststream_pybind11 import vacm as _vacm
from .common import *
from .utils import *


def createContext(devIdx: int) -> Context:
    """
    Create a context in the device.\n
    ------------\n
    devIdx [in]: Device index in which the context will be created.\n
    ctx [out]: Pointer to the address of vacmContext to receive the context instance.\n
    """
    return Context(_vacm.createContext(devIdx))


@err_check
def destroyContext(ctx: Context) -> int:
    """
    Destroy a context in the device.\n
    ------------\n
    ctx [in]: Pointer to a vacmContext with the context instance.
    """
    return _vacm.destroyContext(ctx.ptr)


@err_check
def setCurrentContext(ctx: Context) -> int:
    """
    Set the current context for the calling thread.\n
    ------------\n
    ctx [in]: Pointer to a vacmContext with the context instance.
    """
    return _vacm.setCurrentContext(ctx.ptr)


def getCurrentContext() -> Context:
    """
    Get the current context for the calling thread.\n
    ------------\n
    ctx [out]: Pointer to the address of vacmContext to receive the context instance.
    """
    return Context(_vacm.getCurrentContext())
