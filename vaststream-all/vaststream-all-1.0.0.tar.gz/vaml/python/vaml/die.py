"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["getDieIndexByDevIndex", "getDieHandleByIndex", "getDieHandleByDieIndex"]

from _vaststream_pybind11 import vaml as _vaml
from .utils import *
from .card import *

# =========================== API =============================
def getDieIndexByDevIndex(devIndex:int) -> DieIndex:
    """
    get the physical index of die by logical index.\n
    ----------\n
    devIndex [in]: the logical index.\n
    """
    return _vaml.getDieIndexByDevIndex(devIndex)

def getDieHandleByIndex(cardHandle:int,index:int) -> int:
    """
    get the handle of die by card handle and index.\n
    ----------\n
    cardHandle [in]: the card handle.\n
    index [in]: the index.\n
    """
    return _vaml.getDieHandleByIndex(cardHandle,index)

def getDieHandleByDieIndex(dieIndex:DieIndex) -> int:
    """
    get the handle of die by its index.\n
    ----------\n
    dieIndex [in]: the die index.\n
    """
    return _vaml.getDieHandleByDieIndex(dieIndex)

# class VastaiDevice():
#     """
#     Device tool class.
#     """
#     def __init__(self, cardHandle:int):
#         """
#         Get information related to the device tool class.\n
#         """
#         self._instance = True
#         self.cardHandle = cardHandle
    
#     def __enter__(self):
#         self.__init__(self.cardHandle)
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return self
    
#     # def getCount(self,AiDevice=False,CodecDevice=False,Die=False):
#     #     """
#     #     get the count of ai device or codec device or the die of the specified handle of card.
#     #     """
#     #     assert self._instance, "Please create VastaiDevice."
#     #     if AiDevice:
#     #             count = getAiDeviceCount()
#     #     elif CodecDevice:
#     #         count = getCodecDeviceCount()
#     #     elif Die:
#     #         count = getDieCount(self.cardHandle)
#     #     return count
    
#     def getAiDeviceCount(self):
#         """
#         get the count of ai device.
#         """
#         assert self._instance, "Please create VastaiDevice."
#         return getAiDeviceCount()

#     def getAiDevInfo(self):
#         """
#         get the information of ai device.
#         """
#         assert self._instance, "Please create VastaiDevice."
#         aiDeviceCount = self.getAiDeviceCount()
#         return getAiDevInfo(aiDeviceCount)

#     def getCodecDeviceCount(self):
#         """
#         get the count of codec device.
#         """
#         assert self._instance, "Please create VastaiDevice."
#         return getCodecDeviceCount()

#     def getCodecDevInfo(self):
#         """
#         get the information of codec device.
#         """
#         assert self._instance, "Please create VastaiDevice."
#         aiDeviceCount = self.getAiDeviceCount()
#         return getCodecDevInfo(aiDeviceCount)
    
#     def getDieCount(self):
#         """
#         get the count of die of the specified handle of card.
#         """
#         assert self._instance, "Please create VastaiDevice."
#         return getDieCount(self.cardHandle)

#     def getDieInfo(self):
#         """
#         get the information of die of the specified handle of card.
#         """
#         assert self._instance, "Please create VastaiDevice."
#         return getDieInfo(self.cardHandle)
    
#     def getDieIndexByDevIndex(self):
#         """
#         get the physical index of die by logical index.
#         """
#         assert self._instance, "Please create VastaiDevice."
#         dieIndexs = []
#         dieCount = self.getDieCount()
#         for dieIdx in range(dieCount):
#             dieIndex = getDieIndexByDevIndex(dieIdx)
#             dieIndexs.append(dieIndex)
#         return dieIndexs
    
#     def getDieHandle(self, use_dieIndex=False, use_devIndex=False):
#         """
#         get the handle of die by some ways.
#         """
#         assert self._instance, "Please create VastaiDevice."
#         dieInfos = self.getDieInfo()
#         for dieIdx in range(len(dieInfos)):
#             if use_dieIndex:
#                 dieHandle = getDieHandleByDieIndex(dieInfos[dieIdx].dieIndex)
#             elif use_devIndex:
#                 dieHandle = getDieIndexByDevIndex(dieIdx)
#             else:
#                 dieHandle = getDieHandleByIndex(self.cardHandle,dieIdx)
#         return dieHandle
