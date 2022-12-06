"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "PllClock", "Temperature", "TempThreshold", "PinVolt", "Power","PowerCur", 
    "PowerVolt", "MemUtilizationRate", "UtilizationRate", "McuUtilizationRate",
    "ProcessInfo", "getPllClocks", "getTemperature","getPower", "getPinVolt", 
    "getPowerCur", "getPowerVolt", "getTempThreshold", "getMemUtilizationRate", 
    "getMcuUtilizationRate", "getUtilizationRate", "getRunningProcesses", 
    "getNetWorkRunningInfo", "MAX_PLL_CLOCK_SUBMODULE", "MAX_TEMPERATURE_SUBMODULE",
    "MAX_TEMP_THRESHOLD_SUBMODULE", "MAX_POWER_SUMMODULE", "MAX_POWER_CURRENT_SUMMODULE", 
    "MAX_POWER_VOLTAGE_SUMMODULE", "MAX_PIN_VOLT_SUMMODULE", "MAX_PVT_VOLT_SUMMODULE", 
    "MAX_DIE_CMCU_NUM", "MAX_DIE_VDSP_NUM", "MAX_DIE_VDMCU_NUM", "MAX_DIE_VEMCU_NUM" 
]

from _vaststream_pybind11 import vaml as _vaml
from .utils import *
from typing import List

# =========================== DEFINE =============================
MAX_PLL_CLOCK_SUBMODULE = _vaml.MAX_PLL_CLOCK_SUBMODULE
MAX_TEMPERATURE_SUBMODULE = _vaml.MAX_TEMPERATURE_SUBMODULE
MAX_TEMP_THRESHOLD_SUBMODULE = _vaml.MAX_TEMP_THRESHOLD_SUBMODULE
MAX_POWER_SUMMODULE = _vaml.MAX_POWER_SUMMODULE
MAX_POWER_CURRENT_SUMMODULE = _vaml.MAX_POWER_CURRENT_SUMMODULE
MAX_POWER_VOLTAGE_SUMMODULE = _vaml.MAX_POWER_VOLTAGE_SUMMODULE
MAX_PIN_VOLT_SUMMODULE = _vaml.MAX_PIN_VOLT_SUMMODULE
MAX_PVT_VOLT_SUMMODULE = _vaml.MAX_PVT_VOLT_SUMMODULE
MAX_DIE_CMCU_NUM = _vaml.MAX_DIE_CMCU_NUM
MAX_DIE_VDSP_NUM = _vaml.MAX_DIE_VDSP_NUM
MAX_DIE_VDMCU_NUM = _vaml.MAX_DIE_VDMCU_NUM
MAX_DIE_VEMCU_NUM = _vaml.MAX_DIE_VEMCU_NUM

# =========================== STRUCT =============================
class PllClock(_vaml.pllClock):
    """
    PllClock.\n
    """
    unit: int
    clockArray: List[int]

class Temperature(_vaml.temperature):
    """
    Temperature.\n
    """
    unit: int
    temperature: List[int]

class TempThreshold(_vaml.tempThreshold):
    """
    Temperature Threshold.\n
    """
    unit: int
    tempThreshold: List[int]

class PinVolt(_vaml.pinVolt):
    """
    Pin Voltage.\n
    """
    unit: int
    pinVolt: List[int]

class Power(_vaml.power):
    """
    Power.\n
    """
    unit: int
    power: List[int]

class PowerCur(_vaml.powerCur):
    """
    Power Current.\n
    """
    unit: int
    powerCur: List[int]

class PowerVolt(_vaml.powerVolt):
    """
    power Voltage.\n
    """
    unit: int
    powerVolt: List[int]
 
class MemUtilizationRate(_vaml.memUtilizationRate):
    """
    The Memory Utilization Rate.\n
    """
    total: int
    free: int
    used: int
    utilizationRate: int

class UtilizationRate(_vaml.utilizationRate):
    """
    The Utilization Rate.\n
    """
    ai: int
    vdsp: int
    vemcu: int
    vdmcu: int

class McuUtilizationRate(_vaml.mcuUtilizationRate):
    """
    The Mcu Utilization Rate.\n
    """
    ai: int
    vdsp: List[int]
    vemcu: List[int]
    vdmcu: List[int]

class ProcessInfo(_vaml.processInfo):
    """
    The Process Infomation.\n
    """
    pid: int
    memused: int
    name: str

# =========================== API =============================

def getPllClocks(dieHandle:int) -> PllClock:
    """
    get the pll clocks information by the specified handle of die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    pllClock = _vaml.pllClock()
    ret = _vaml.getPllClocks(dieHandle, pllClock)
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get PllClocks error {ret}.")
    return pllClock

def getTemperature(dieHandle:int) -> Temperature:
    """
    get the temperature information of its die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    temperature = _vaml.temperature()
    ret = _vaml.getTemperature(dieHandle,temperature)
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get temperature error {ret}.")
    return temperature

def getPower(dieHandle:int) -> Power:
    """
    get the power information of its die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    power = _vaml.power()
    ret = _vaml.getPower(dieHandle,power)
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get power error {ret}.")
    return power

def getPinVolt(dieHandle:int) -> PinVolt:
    """
    get the pin voltage information of its die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    pinVolt = _vaml.pinVolt()
    ret = _vaml.getPinVolt(dieHandle,pinVolt)
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get pin voltage error {ret}.")
    return pinVolt

def getPowerCur(dieHandle:int) -> PowerCur:
    """
    get the power current information of its die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    powerCur = _vaml.powerCur()
    ret = _vaml.getPowerCur(dieHandle,powerCur) 
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get power current error {ret}.")
    return powerCur

def getPowerVolt(dieHandle:int) -> PowerVolt:
    """
    get the power voltage information of its die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    powerVolt = _vaml.powerVolt()
    ret = _vaml.getPowerVolt(dieHandle,powerVolt)
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get power voltage error {ret}.")
    return powerVolt

def getTempThreshold(dieHandle:int) -> TempThreshold:
    """
    get the temperature threshold of its die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    tempThreshold = _vaml.tempThreshold()
    ret = _vaml.getTempThreshold(dieHandle,tempThreshold) 
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get temperature threshold error {ret}.")
    return tempThreshold

def getMemUtilizationRate(dieHandle:int) -> MemUtilizationRate:
    """
    get the memory utilization rate of die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    return _vaml.getMemUtilizationRate(dieHandle)

def getMcuUtilizationRate(dieHandle:int) -> McuUtilizationRate:
    """
    get the mcu utilization rate of die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    mcuUtilizationRate = _vaml.mcuUtilizationRate()
    ret = _vaml.getMcuUtilizationRate(dieHandle,mcuUtilizationRate)
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get mcu utilization rate error {ret}.")
    return mcuUtilizationRate

def getUtilizationRate(dieHandle:int) -> UtilizationRate:
    """
    get the utilization rate of die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    return _vaml.getUtilizationRate(dieHandle)

def getRunningProcesses(dieHandle:int) -> List[ProcessInfo]:
    """
    get the process information of die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    processInfo = []
    return _vaml.getRunningProcesses(dieHandle,processInfo)

def getNetWorkRunningInfo(dieHandle:int) -> List[ProcessInfo]:
    """
    get the net process information of die.\n
    ----------\n
    dieHandle [in]: the die handle.\n
    """
    modelProcessInfo = []
    return _vaml.getNetWorkRunningInfo(dieHandle,modelProcessInfo)