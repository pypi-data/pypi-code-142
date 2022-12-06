"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8
__all__ = ["OpGraph", "Stream", "Model", "StreamInput","getVersion"]

from _vaststream_pybind11 import vacl as _vacl
from .utils import PointerContainer

class OpGraph(PointerContainer):
    """
    OpGraph Container.
    """
    pass

class Stream(PointerContainer):
    """
    Stream Container.
    """
    pass

class Model(PointerContainer):
    """
    Model Container.
    """
    pass

class StreamInput(PointerContainer):
    """
    Stream Input Container.
    """
    pass
    
def getVersion() -> str:
    """
    get the vacl version.\n
    """
    return _vacl.getVersion()
