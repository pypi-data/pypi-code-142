"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["createOp", "destroyOp", "setOpAttr", "setOpAttrArray",
           "getOpAttr", "getOpAttrArray", "executeOp"]

from _vaststream_pybind11 import vace as _vace
from typing import Union
from .common import *
from .utils import *
from vaststream.vacm.common import Dataset

# =========================== API =============================
def createOp(opType: OP_TYPE) -> Op:
    """
    Create a vaceOp instance.\n
    ----------\n
    opType [in]: the type of operator.\n
    return: the pointer to vaceOp pointer.\n
    """
    ptr_ = _vace.createOp(opType)
    return Op(ptr_)

@err_check
def destroyOp(op: Op) -> int:
    """
    Destroy a vaceOp instance.\n
    ----------\n
    op [in]: the pointer of the specified op.\n
    return :vaceER_SUCCESS if succeed, otherwise other error code.\n
    """
    ptr_ = op.ptr
    return _vace.destroyOp(ptr_)

def setOpAttr(
    op: Op, 
    attrName: str, 
    attrDType: DATA_TYPE,
    attrGType: PARAM_TYPE,
    value: Union[int, float]
    ) -> int:
    """
    Set attributes of a specified op.\n
    ----------\n
    op [in]: the pointer of the specified op.\n
    attrName [in]: the attribute name.\n
    attrDType [in]: data type of attribute.\n
    attrGType [in]: the attribute type (PARAM_ELEMENT | PARAM_ARRAY).\n
    value [in]: the value of attribute.\n
    return: vaceER_SUCCESS if succeed, otherwise other error code.\n
    """
    ptr_ = op.ptr
    return _vace.setVaceOPAttr(ptr_, attrName, attrDType, attrGType, value)

def setOpAttrArray(
    op: Op, 
    attrName: str, 
    attrDType: DATA_TYPE,
    attrGType: PARAM_TYPE,
    value: Union[int, float],
    index: int
    ) -> int:
    """
    Set attributes of a specified op.\n
    ----------\n
    op [in]: the pointer of the specified op.\n
    attrName [in]: the attribute name.\n
    attrDType [in]: data type of attribute.\n
    attrGType [in]: the attribute type (PARAM_ELEMENT | PARAM_ARRAY).\n
    value [in]: the value of attribute.\n
    return: vaceER_SUCCESS if succeed, otherwise other error code.\n
    """
    ptr_ = op.ptr
    return _vace.setVaceOPAttrArray(ptr_, attrName, attrDType, attrGType, value, index)

def getOpAttr(
    op: Op, 
    attrName: str, 
    attrDType: DATA_TYPE
    ) -> Union[int, float]:
    """
    Get attributes of a specified op.\n
    ----------\n
    opPy [in]: the pointer of the specified op.\n
    attrName [in]: the attribute name.\n
    attrDType [in]: data type of attribute.\n
    return: the value of attribute.\n
    """ 
    if attrDType == DATA_TYPE.INT:
        return _vace.getVaceOPAttrInt(op.ptr, attrName, attrDType)
    
    elif attrDType == DATA_TYPE.UINT_8:
        return _vace.getVaceOPAttrUint8(op.ptr, attrName, attrDType)
    
    # elif attrDType == DATA_TYPE.UINT_16:
    #     return _vace.getVaceOPAttrUint16(op.ptr, attrName, attrDType)
    
    # elif attrDType == DATA_TYPE.UINT_32:
    #     return _vace.getVaceOPAttrUint32(op.ptr, attrName, attrDType)
    
    # elif attrDType == DATA_TYPE.UINT_64:
    #     return _vace.getVaceOPAttrUint64(op.ptr, attrName, attrDType)
    
    elif attrDType == DATA_TYPE.FLOAT:
        return _vace.getVaceOPAttrFloat(op.ptr, attrName, attrDType)
    
    # elif attrDType == DATA_TYPE.DOUBLE:
    #     return _vace.getVaceOPAttrDouble(op.ptr, attrName, attrDType)
    else:
        print("Not support format", attrDType)
        return _vace.vaceER_BASE

def getOpAttrArray(
    op: Op, 
    attrName: str, 
    attrDType: DATA_TYPE, 
    index: int
    ) -> Union[int, float]:
    """
    Get attributes of a specified op.\n
    ----------\n
    op [in]: the pointer of the specified op.\n
    attrName [in]: the attribute name.\n
    attrDType [in]: data type of attribute.\n
    attrGType [in]:  the index of array element.\n
    return: the value of attribute.\n
    """
    if attrDType == DATA_TYPE.INT:
        return _vace.getVaceOPAttrArrayInt(op.ptr, attrName, attrDType, index)
    
    elif attrDType == DATA_TYPE.UINT_8:
        return _vace.getVaceOPAttrArrayUint8(op.ptr, attrName, attrDType, index)
    
    # elif attrDType == DATA_TYPE.UINT_16:
    #     return _vace.getVaceOPAttrArrayUint16(op.ptr, attrName, attrDType, index)
    
    # elif attrDType == DATA_TYPE.UINT_32:
    #     return _vace.getVaceOPAttrArrayUint32(op.ptr, attrName, attrDType, index)
    
    # elif attrDType == DATA_TYPE.UINT_64:
    #     return _vace.getVaceOPAttrArrayUint64(op.ptr, attrName, attrDType, index)
    
    elif attrDType == DATA_TYPE.FLOAT:
        return _vace.getVaceOPAttrArrayFloat(op.ptr, attrName, attrDType, index)
    
    # elif attrDType == DATA_TYPE.DOUBLE:
    #     return _vace.getVaceOPAttrArrayDouble(op.ptr, attrName, attrDType, index)

    else:
        print("Not support format", attrDType)
        return _vace.vaceER_BASE

@err_check
def executeOp(
    op: Op, 
    input: Dataset, 
    output: Dataset
    ) -> int:
    """
     ExecuteOp op with input dataset.\n
    ----------\n
    op [in]: the pointer of the specified op.\n
    input [in]: vacmDataset of input data.\n
    output [out]: vacmDataset of output data.\n
    return: vaceER_SUCCESS if succeed, otherwise other error code.\n
    """
    return _vace.executeOp(op.ptr, input.ptr, output.ptr)
