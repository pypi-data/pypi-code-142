"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "init", "shutDown", "getVersion", "vamlER_SUCCESS"
    # "API_VERSION_SRT",
    # "MAX_DIE_PER_DEVICE", "MAX_DEVICE_UUID_BUFFER_SIZE", "MAX_SYSTEM_VERSION_BUFFER_SIZE",
    # "VAML_16_BUF_SIZE", "VAML_32_BUF_SIZE", "VAML_64_BUF_SIZE","VAML_128_BUF_SIZE", "VAML_256_BUF_SIZE"
]

from _vaststream_pybind11 import vaml as _vaml
from .utils import *

# =========================== DEFINE =============================
vamlER_SUCCESS = _vaml.vamlER_SUCCESS

# =========================== API =============================
@err_check
def init() -> int:
    """
    initialize the environment for vaml api.\n
    """
    return _vaml.init()

@err_check
def shutDown() -> int:
    """
    release the environment for vaml api.\n
    """
    return _vaml.shutDown()

def getVersion() -> str:
    """
    get the vaml api version information.\n
    """
    return _vaml.getVersion()
