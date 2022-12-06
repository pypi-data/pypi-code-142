"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "NodeMajorMinor", "DieIndex", "PciCardId", "PciSubSystemId","NodeBaseInfo", 
    "DieBaseInfo", "Capability","PciInfo", "CardInfo", "FanSpeedInfo", "getCardInfo",
    "getCardHandleByUUID", "getCardHandleByPciBusId", "getCardHandleByIndex", "getCardHandleByCardId", 
    "getUUID","getPciInfo", "getCapability", "getFanSpeedInfo", "getManageNodeAttribute", "getDriverSWVersion", 
    "getDieCount", "getDieInfo"
]

from _vaststream_pybind11 import vaml as _vaml
from .utils import *
from typing import List

# =========================== UNION =============================
class NodeMajorMinor(_vaml.nodeMajorMinor):
    """
    Node Major Minor.\n
    """
    minor: int
    major: int

class DieIndex(_vaml.dieIndex):
    """
    Die Index.\n
    """
    dieId: int
    cardId: int
    seqNum: int

class PciCardId(_vaml.pciCardId):
    """
    Pci Card Id.\n
    """
    venderId: int
    cardId: int

class PciSubSystemId(_vaml.pciSubSystemId):
    """
    Pci Subsystem Id.\n
    """
    subVenderId: int
    subCardId: int

# =========================== STRUCT =============================
class NodeBaseInfo(_vaml.nodeBaseInfo):
    """
    Node Base Infomation.\n
    """
    name: str
    majorMinor: NodeMajorMinor

class DieBaseInfo(_vaml.dieBaseInfo):
    """
    Die Base Infomation.\n
    """
    dieIndex: DieIndex
    vaccBaseInfo: NodeBaseInfo
    renderBaseInfo: NodeBaseInfo
    videoBaseInfo: NodeBaseInfo

class Capability(_vaml.capability):
    """
    Vaml Capability.\n
    """
    aiCapability: int
    videoCapability: int

class PciInfo(_vaml.pciInfo):
    """
    Pci Infomation.\n
    """
    busId: str
    domain: int
    bus: int
    card: int
    pciId: PciCardId
    pciSubId: PciSubSystemId
    pcieCardBaseInfo: NodeBaseInfo
    pcieCardVersionBaseInfo: NodeBaseInfo
    pcieCardCtlBaseInfo: NodeBaseInfo

class CardInfo(_vaml.cardInfo):
    """
    Card Infomation.\n
    """
    cardId: int
    uuid: str
    cardTypeName: str
    pciInfo: PciInfo
    cardCapability: Capability
    manNodeBaseInfo: NodeBaseInfo
    dieNum: int
    dieInfo: List[DieBaseInfo]
 
class FanSpeedInfo(_vaml.fanSpeedInfo):
    """
    The Fan Speed Infomation.\n
    """
    fanSpeedLevel: int

# =========================== API =============================

def getCardInfo() -> List[CardInfo]:
    """
    get the information of card.\n
    """
    cardInfo = []
    return _vaml.getCardInfo(cardInfo)

def getCardHandleByUUID(uuid:str) -> int:
    """
    get the card handle by uuid.\n
    ----------\n
    uuid [in]: uuid.\n
    """
    return _vaml.getCardHandleByUUID(uuid)

def getCardHandleByPciBusId(pciBusId:str) -> int:
    """
    get the card handle by pciBus id.\n
    ----------\n
    pciBusId [in]: pciBus id.\n
    """
    return _vaml.getCardHandleByPciBusId(pciBusId)

def getCardHandleByIndex(index:int) -> int:
    """
    get the card handle by index of card.\n
    ----------\n
    index [in]: index of card.\n
    """
    return _vaml.getCardHandleByIndex(index)

def getCardHandleByCardId(cardId:int) -> int:
    """
    get the card handle by card id.\n
    ----------\n
    cardId [in]: card id.\n
    """
    return _vaml.getCardHandleByCardId(cardId)

def getUUID(cardHandle:int) -> str:
    """
    get the uuid by the specified handle of card.\n
    ----------\n
    cardHandle [in]: the card handle.\n
    """
    return _vaml.getUUID(cardHandle)

def getPciInfo(cardHandle:int) -> PciInfo:
    """
    get the pci information by the specified handle of card.\n
    ----------\n
    cardHandle [in]: the card handle.\n
    """
    return _vaml.getPciInfo(cardHandle)

def getCapability(cardHandle:int) -> Capability:
    """
    get the capability by the specified handle of card.\n
    ----------\n
    cardHandle [in]: the card handle.\n
    """
    capability = _vaml.capability()
    ret = _vaml.getCapability(cardHandle,capability)
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get the capability by the specified handle of card error {ret}.")
    return capability

def getFanSpeedInfo(cardHandle:int) -> FanSpeedInfo:
    """
    get the fan speed of card.\n
    ----------\n
    cardHandle [in]: the card handle.\n
    """
    speedInfo = _vaml.fanSpeedInfo()
    ret = _vaml.getFanSpeedInfo(cardHandle,speedInfo)
    if ret != _vaml.vamlER_SUCCESS:
        raise Exception(f"get the fan speed error {ret}.")
    return speedInfo
    
def getManageNodeAttribute() -> NodeBaseInfo:
    """
    get the attributes of managed node.\n
    """
    return _vaml.getManageNodeAttribute()

def getDriverSWVersion() -> str:
    """
    get the version information of driver.\n
    """
    return _vaml.getDriverSWVersion()

def getDieCount(cardHandle:int) -> int:
    """
    get the count of die of the specified handle of card.\n'
    ----------\n
    cardHandle [in]: the card handle.\n
    """
    return _vaml.getDieCount(cardHandle)

def getDieInfo(cardHandle:int) -> List[DieBaseInfo]:
    """
    get the information of die of the specified handle of card.\n
    ----------\n
    cardHandle [in]: the card handle.\n
    """
    dieInfo = []
    return _vaml.getDieInfo(cardHandle,dieInfo)

# class VastaiCard():
#     """
#     Card tool class.
#     """
#     def __init__(self):
#         """
#         Get information related to the card tool class.\n
#         """
#         self._instance = True
    
#     def __enter__(self):
#         self.__init__()
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return self
    
#     def getCount(self):
#         """
#         get the count of card.
#         """
#         assert self._instance, "Please create VastaiCard."
#         return getCardCount()

#     def getInfo(self):
#         """
#         get the information of card.
#         """
#         assert self._instance, "Please create VastaiCard."
#         return getCardInfo()

#     def getCardHandle(self,use_uuid=False, use_pciBusId=False, use_cardId=False):
#         """
#         get the handle of card by some ways.
#         """
#         assert self._instance, "Please create VastaiCard."
#         cardsInfo = self.getInfo()
#         cardHandles = []
#         for idx in range(len(cardsInfo)):
#             if use_uuid:
#                 uuid = cardsInfo[idx].uuid
#                 cardHandle = getHandleByUUID(uuid)
#             elif use_pciBusId:
#                 pciBusId = cardsInfo[idx].busId
#                 cardHandle = getHandleByPciBusId(pciBusId)
#             elif use_cardId:
#                 cardId = cardsInfo[idx].cardId
#                 cardHandle = getCardHandleByCardId(cardId)
#             else:
#                 cardHandle = getCardHandleByIndex(idx)
#             cardHandles.append(cardHandle)

#         return cardHandles
    
#     def getUUID(self):
#         """
#         get the uuid by the specified handle of card.
#         """
#         assert self._instance, "Please create VastaiCard."
#         cardHandles = self.getCardHandle()
#         uuids = []
#         for cardHandle in cardHandles:
#             uuid = getUUID(cardHandle)
#             uuids.append(uuid)
#         return uuids
    
#     def getPciInfo(self):
#         """
#         get the pci information by the specified handle of card.
#         """
#         assert self._instance, "Please create VastaiCard."
#         cardHandles = self.getCardHandle()
#         pciInfos = []
#         for cardHandle in cardHandles:
#             pciInfo = getPciInfo(cardHandle)
#             pciInfos.append(pciInfo)
#         return pciInfos

#     def getCapability(self):
#         """
#         get the capability by the specified handle of card.
#         """
#         assert self._instance, "Please create VastaiCard."
#         cardHandles = self.getCardHandle()
#         capabilitys = []
#         for cardHandle in cardHandles:
#             capability = getCapability(cardHandle)
#             capabilitys.append(capability)
#         return capabilitys
    
#     def getFanSpeed(self):
#         """
#         get the fan speed by the specified handle of card.
#         """
#         assert self._instance, "Please create VastaiCard."
#         cardHandles = self.getCardHandle()
#         fanSpeedInfos = []
#         for cardHandle in cardHandles:
#             fanSpeedInfo = getFanSpeedInfo(cardHandle)
#             fanSpeedInfos.append(fanSpeedInfo)
#         return fanSpeedInfos