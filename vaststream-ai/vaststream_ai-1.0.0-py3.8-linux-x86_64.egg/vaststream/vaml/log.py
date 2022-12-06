"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "OP_STATUS", "LOG_LEVEL", "setLogLevel", "logMsg", "errorString"
]

from _vaststream_pybind11 import vaml as _vaml
from .utils import *

# =========================== ENUM =============================

class OP_STATUS():
    """
    vaml op status.\n
    ----------\n
    @enum SUCCESS\n
    @enum UNINITIALIZED\n
    @enum INITIALIZED\n
    @enum CARD_EMPTY\n
    @enum INITI_FAIL\n
    @enum CARD_NOTFOUND\n
    @enum INPUT_PARAMETER_NULL\n
    @enum INPUT_PARAMETER_ERROR\n
    @enum PCIE_MAJOR_ERROR\n
    @enum USER_BUF_INSUFFICIENT\n
    @enum CALLBACK_INITIALIZED\n
    @enum CALLBACK_UNINITIALIZED\n
    @enum PROFILER_ALREADY_RUNNING\n
    @enum PROFILER_ALREADY_STOP:\n
    @enum PROFILER_EXPORT_FILE_TYPE_INVALID\n
    @enum PROFILER_EXPORT_FOLDER_PATH_INVALID\n
    @enum AI_SCRIPT_PATH_INVALID\n
    @enum AI_SCRIPT_ROOT_PERMISSION\n
    @enum MAX\n
    """
    SUCCESS: int = _vaml.opStatus.VAML_SUCCESS
    UNINITIALIZED: int = _vaml.opStatus.VAML_ERROR_UNINITIALIZED
    INITIALIZED: int = _vaml.opStatus.VAML_ERROR_INITIALIZED
    CARD_EMPTY: int = _vaml.opStatus.VAML_ERROR_CARD_EMPTY
    INITI_FAIL: int = _vaml.opStatus.VAML_ERROR_INITI_FAIL
    CARD_NOTFOUND: int = _vaml.opStatus.VAML_ERROR_CARD_NOTFOUND
    INPUT_PARAMETER_NULL: int = _vaml.opStatus.VAML_ERROR_INPUT_PARAMETER_NULL
    INPUT_PARAMETER_ERROR: int = _vaml.opStatus.VAML_ERROR_INPUT_PARAMETER_ERROR
    PCIE_MAJOR_ERROR: int = _vaml.opStatus.VAML_ERROR_PCIE_MAJOR_ERROR
    USER_BUF_INSUFFICIENT: int = _vaml.opStatus.VAML_USER_BUF_INSUFFICIENT
    CALLBACK_INITIALIZED: int = _vaml.opStatus.VAML_ERROR_CALLBACK_INITIALIZED
    CALLBACK_UNINITIALIZED: int = _vaml.opStatus.VAML_ERROR_CALLBACK_UNINITIALIZED
    PROFILER_ALREADY_RUNNING: int = _vaml.opStatus.VAML_ERROR_PROFILER_ALREADY_RUNNING
    PROFILER_ALREADY_STOP: int = _vaml.opStatus.VAML_ERROR_PROFILER_ALREADY_STOP
    PROFILER_EXPORT_FILE_TYPE_INVALID: int = _vaml.opStatus.VAML_ERROR_PROFILER_ALREADY_STOP
    PROFILER_EXPORT_FOLDER_PATH_INVALID: int = _vaml.opStatus.VAML_ERROR_PROFILER_EXPORT_FOLDER_PATH_INVALID
    AI_SCRIPT_PATH_INVALID: int = _vaml.opStatus.VAML_ERROR_AI_SCRIPT_PATH_INVALID
    AI_SCRIPT_ROOT_PERMISSION: int = _vaml.opStatus.VAML_ERROR_AI_SCRIPT_ROOT_PERMISSION
    MAX: int = _vaml.opStatus.VAML_ERROR_MAX

class LOG_LEVEL():
    """
    vaml log level.\n
    ----------\n
    @enum TRACE\n
    @enum DEBUG\n
    @enum INFO\n
    @enum WARN\n
    @enum ERROR\n
    @enum FATAL\n
    @enum NONE\n
    """
    TRACE: int = _vaml.logLevel.VAML_LOG_TRACE
    DEBUG: int = _vaml.logLevel.VAML_LOG_DEBUG
    INFO: int = _vaml.logLevel.VAML_LOG_INFO
    WARN: int = _vaml.logLevel.VAML_LOG_WARN
    ERROR: int =_vaml.logLevel.VAML_LOG_ERROR
    FATAL: int = _vaml.logLevel.VAML_LOG_FATAL
    NONE: int = _vaml.logLevel.VAML_LOG_NONE

# =========================== API =============================
@err_check
def setLogLevel(logLevel:LOG_LEVEL) -> int:
    """
    set logger system for message logging.\n
    ----------\n
    logLevel [in]: the log Level type.\n
    """
    return _vaml.setLogLevel(logLevel)

@err_check
def logMsg(logLevel:LOG_LEVEL,fmt:str,*args) -> int:
    """
    write a message to the console or file.\n
    ----------\n
    logLevel [in]: the log Level type.\n
    fmt [in]: the string format.\n
    args [in]: the log information associated with fmt.\n
    """
    return _vaml.logMsg(logLevel,fmt,args[0],args[1])

def errorString(opStatus:OP_STATUS) -> str:
    """
    convert the description of an error code from error code.\n
    ----------\n
    opStatus [in]: the error code.\n
    """
    return _vaml.errorString(opStatus)
