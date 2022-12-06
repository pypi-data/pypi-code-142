"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8
__all__ = ["LOG_CHANNEL", "LOG_LEVEL", "initLogger", "logMessage"]


from typing import Any
from _vaststream_pybind11 import vacm as _vacm
from .common import *
from .utils import *

# =========================== ENUM =============================


class LOG_CHANNEL():
    """
    vacm log channel.\n
    ----------\n
    @enum APP: app log channel.\n
    @enum CM: vacm log channel.\n
    @enum CE: vace log channel.\n
    @enum CL: vacl log channel.\n
    @enum ME: vame log channel.\n
    @enum ML: vaml log channel.\n
    @enum RT: runtime log channel.\n
    @enum NN: vacm log channel.\n
    @enum TM: vacm log channel.\n
    """
    APP: int = _vacm.logChannel.vacmLC_APP
    CM: int = _vacm.logChannel.vacmLC_CM
    CE: int = _vacm.logChannel.vacmLC_CE
    CL: int = _vacm.logChannel.vacmLC_CL
    ME: int = _vacm.logChannel.vacmLC_ME
    ML: int = _vacm.logChannel.vacmLC_ML
    RT: int = _vacm.logChannel.vacmLC_RT
    NN: int = _vacm.logChannel.vacmLC_NN
    TM: int = _vacm.logChannel.vacmLC_TM


class LOG_LEVEL():
    """
    vacm log level.\n
    ----------\n
    @enum TRACE: trace log level.\n
    @enum DEBUG: debug log level.\n
    @enum INFO: info log level.\n
    @enum WARN: warn log level.\n
    @enum ERROR: error log level.\n
    @enum ALARM: alarm log level.\n
    @enum FATAL: fatal log level.\n
    """
    TRACE: int = _vacm.logLevel.vacmLL_TRACE
    DEBUG: int = _vacm.logLevel.vacmLL_DEBUG
    INFO: int = _vacm.logLevel.vacmLL_INFO
    WARN: int = _vacm.logLevel.vacmLL_WARN
    ERROR: int = _vacm.logLevel.vacmLL_ERROR
    ALARM: int = _vacm.logLevel.vacmLL_ALARM
    FATAL: int = _vacm.logLevel.vacmLL_FATAL

# =========================== API =============================


def initLogger() -> int:
    """
    Initialize logger system for message logging.\n
    ------------\n
    """
    return _vacm.initLogger()


def logMessage(logChannel: LOG_CHANNEL, logLevel: LOG_LEVEL, fmt: str) -> int:
    """
    Write a message to the log file.\n
    ------------\n
    logChannel [in]: The log channel, which is pre-configured in the log configuration file.\n
    logLevel [in]: The log level.
    """
    return _vacm.logMessage(logChannel, logLevel, fmt)
