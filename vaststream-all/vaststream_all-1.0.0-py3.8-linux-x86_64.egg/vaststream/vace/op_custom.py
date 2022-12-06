"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["loadCustomizedOp", "destroyCustomizedOpInfo", "unloadCustomizedOps", 
           "getCustomizedOpCount", "getCustomizedOpName", "createCustomizedOp"]

from _vaststream_pybind11 import vace as _vace
from .common import *
from .utils import *

# =========================== API =============================
def loadCustomizedOp(elfFilePath: str) -> CustomizedOpInfo:
    """
    Load the custom op.\n
    ----------\n
    elfFilePath [in]: Path of the elf file.\n
    return: An object that contains elf file information.\n
    """
    return CustomizedOpInfo(_vace.loadCustomizedOp(elfFilePath))
      

@err_check
def destroyCustomizedOpInfo(opInfo: CustomizedOpInfo) -> int:
    """
    Destroy customized opInfo.\n
    ----------\n
    opInfo [in]: An object that contains elf file information, created by loadCustomizedOp.\n
    return :vaceER_SUCCESS if succeed, otherwise other error code.\n
    """
    _ptr = opInfo.ptr
    return _vace.destroyCustomizedOpInfo(_ptr)

@err_check
def unloadCustomizedOps(opInfo: CustomizedOpInfo) -> int:
    """
    Unload customized opInfo.\n
    ----------\n
    opInfo [in]: An object that contains elf file information, created by loadCustomizedOp.\n
    return :vaceER_SUCCESS if succeed, otherwise other error code.\n
    """
    _ptr = opInfo.ptr
    return _vace.unloadCustomizedOps(_ptr)

def getCustomizedOpCount(opInfo: CustomizedOpInfo) -> int:
    """
    getCustomizedOpCount.\n
    ----------\n
    opInfo [in]: An object that contains elf file information, created by loadCustomizedOp.\n
    return: OpInfo count.\n
    """
    _ptr = opInfo.ptr
    return _vace.getCustomizedOpCount(_ptr)

def getCustomizedOpName(opInfo: CustomizedOpInfo, 
                        index: int) -> str:
    """
    Get customized op name.\n
    ----------\n
    opInfo [in]: An object that contains elf file information, created by loadCustomizedOp.\n
    index [in]: Get the op name at the index position\n
    return: return opname at the index position
    """
    _ptr = opInfo.ptr
    return _vace.getCustomizedOpName(_ptr, index)

def createCustomizedOp(opInfo: CustomizedOpInfo,
                       opname: str) -> Op:

    """
    createCustomizedOp.\n
    ----------\n
    opInfo [in]: Get from invoke loadCustomizedOp api, include one or more customzied op information\n
    opname [in]: op name in opInfo.\n
    return: the pointer to vaceOp pointer.\n
    """
    op_info_ptr_ = opInfo.ptr
    op_ptr_ = _vace.createCustomizedOp(op_info_ptr_, opname)
    return Op(op_ptr_)
