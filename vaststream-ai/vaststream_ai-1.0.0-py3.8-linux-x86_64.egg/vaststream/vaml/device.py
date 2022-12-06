"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "AiDevInfo", "CodecDevInfo", "getAiDeviceCount", "getAiDevInfo", 
    "getCodecDeviceCount", "getCodecDevInfo", "getCardCount", "VastaiDevice"
]

from _vaststream_pybind11 import vaml as _vaml
from .utils import *
from .card import *
from typing import List

# =========================== STRUCT =============================
class AiDevInfo(_vaml.aiDevInfo):
    """
    Ai Device Infomation.\n
    """
    dieIndex: DieIndex
    aiBaseInfo: NodeBaseInfo

class CodecDevInfo(_vaml.codecDevInfo):
    """
    Codec Device Infomation.\n
    """
    dieIndex: DieIndex
    videoBaseInfo: NodeBaseInfo

# =========================== API =============================
def getCardCount() -> int:
    """
    get the count of card.\n
    """
    return _vaml.getCardCount()
    
def getAiDeviceCount() -> int:
    """
    get the count of ai device.\n
    """
    return _vaml.getAiDeviceCount()

def getAiDevInfo(count:int) -> List[AiDevInfo]:
    """
    get the information of ai device.\n
    ----------\n
    count [in]: the count of ai device .\n
    """
    return _vaml.getAiDevInfo(count)

def getCodecDeviceCount() -> int:
    """
    get the count of codec device.\n
    """
    return _vaml.getCodecDeviceCount()

def getCodecDevInfo(count:int) -> List[CodecDevInfo]:
    """
    get the information of codec device.\n
    ----------\n
    count [in]: the count of codec device.\n
    """
    return _vaml.getCodecDevInfo(count)

class VastaiDevice():
    """
    Device tool class.
    """
    def __init__(self):
        """
        Get information related to the device tool class.\n
        """
        self._instance = True

    @property
    def cardCount(self):
        return self.getCardCount()

    @property
    def aiDeviceCount(self):
        return self.getAiDeviceCount()

    @property
    def codecDeviceCount(self):
        return self.getCodecDeviceCount()

    @property
    def aiDevInfo(self):
        return self.getAiDevInfo()

    @property
    def codecDevInfo(self):
        return self.getCodecDevInfo()

    def getCardCount(self):
        """
        get the count of card.
        """
        assert self._instance, "Please create VastaiCard."
        return getCardCount()
        
    def getAiDeviceCount(self):
        """
        get the count of ai device.
        """
        assert self._instance, "Please create VastaiDevice."
        return getAiDeviceCount()

    def getAiDevInfo(self):
        """
        get the information of ai device.
        """
        assert self._instance, "Please create VastaiDevice."
        aiDeviceCount = self.getAiDeviceCount()
        return getAiDevInfo(aiDeviceCount)

    def getCodecDeviceCount(self):
        """
        get the count of codec device.
        """
        assert self._instance, "Please create VastaiDevice."
        return getCodecDeviceCount()

    def getCodecDevInfo(self):
        """
        get the information of codec device.
        """
        assert self._instance, "Please create VastaiDevice."
        aiDeviceCount = self.getAiDeviceCount()
        return getCodecDevInfo(aiDeviceCount)
    
    # def __getitem__(self,index):
    #     return "hello"
    
