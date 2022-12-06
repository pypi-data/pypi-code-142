"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["OpBase"]

from abc import ABCMeta, abstractmethod
from .common import *
from .op_attr_desc import *
from .op_fusion import *
from typing import Union
from vaststream.vacm import Dataset


class OpBase(metaclass=ABCMeta):
    def __init__(
        self,
        iimage_desc: ImageDesc = None,
        oimage_desc: ImageDesc = None,
        cvt_color_desc: CvtColorDesc = None,
        normal_desc: NormalDesc = None,
        scale_desc: ScaleDesc = None,
        padding_desc: PaddingDesc = None,
        resize_desc: ResizeDesc = None,
        tensor_desc: TensorDesc = None,
        crop_desc: CropDesc = None,
    ):
        self.iimage_desc = iimage_desc
        self.oimage_desc = oimage_desc
        self.cvt_color_desc = cvt_color_desc
        self.normal_desc = normal_desc
        self.scale_desc = scale_desc
        self.padding_desc = padding_desc
        self.resize_desc = resize_desc
        self.tensor_desc = tensor_desc
        self.crop_desc = crop_desc
        
        self._op = None
    
    @abstractmethod
    def type(self) -> OP_TYPE:
        pass

    @property
    def op(self):
        if self._op is None:
            self.create()
        return self._op

    def create(self) -> None:
        """
        Create a vaceOp instance.
        """
        if self._op is None:
            self._op = createOp(self.type())
            self._setOpAttr()
            
    def setInutFormat(self) -> None:
        """
        Set a vaceOp input Format.
        """
        if self.iimage_desc is None:
            raise("Input image desc is None")
        
        if self._op is None:
            self.create()
            
        assert setOpAttr(self._op, "iimage_format", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.iimage_desc.format) == 0

        
    def destroy(self) -> None:
        """
        Destroy a vaceOp instance.
        """
        assert self._op is not None, "Please create op."
        destroyOp(self._op)
        self._op = None
 
    def _setOpAttr(self) -> None:
        assert self._op is not None, "Please create op."
        if self.iimage_desc:
            assert setOpAttr(self._op, "iimage_width", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.iimage_desc.width) == 0
            assert setOpAttr(self._op, "iimage_height", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.iimage_desc.height) == 0
            assert setOpAttr(self._op, "iimage_width_pitch", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.iimage_desc.widthPitch) == 0
            assert setOpAttr(self._op, "iimage_height_pitch", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.iimage_desc.heightPitch) == 0  
       
        if self.oimage_desc:      
            assert setOpAttr(self._op, "oimage_width", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.oimage_desc.width) == 0
            assert setOpAttr(self._op, "oimage_height", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.oimage_desc.height) == 0
                
        if self.cvt_color_desc:
            assert setOpAttr(self._op, "color_cvt_code", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.cvt_color_desc.color_cvt_code) == 0
            assert setOpAttr(self._op, "color_space", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.cvt_color_desc.color_space) == 0
        
        if self.resize_desc:
            assert setOpAttr(self._op, "resize_type", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.resize_desc.type) == 0
            if self.resize_desc.width and self.resize_desc.height:
                assert setOpAttr(self._op, "resize_width", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.resize_desc.width) == 0
                assert setOpAttr(self._op, "resize_height", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.resize_desc.height) == 0
        
        if self.padding_desc:
            assert setOpAttr(self._op, "padding0", DATA_TYPE.UINT_8, PARAM_TYPE.ELEMENT, self.padding_desc.padding[0]) == 0
            assert setOpAttr(self._op, "padding1", DATA_TYPE.UINT_8, PARAM_TYPE.ELEMENT, self.padding_desc.padding[1]) == 0
            assert setOpAttr(self._op, "padding2", DATA_TYPE.UINT_8, PARAM_TYPE.ELEMENT, self.padding_desc.padding[2]) == 0
            assert setOpAttr(self._op, "edge_padding_type", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.padding_desc.type) == 0
       
        if self.normal_desc:
            assert setOpAttr(self._op, "mean0", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.normal_desc.mean[0]) == 0
            assert setOpAttr(self._op, "mean1", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.normal_desc.mean[1]) == 0
            assert setOpAttr(self._op, "mean2", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.normal_desc.mean[2]) == 0
            assert setOpAttr(self._op, "std0", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.normal_desc.std[0]) == 0
            assert setOpAttr(self._op, "std1", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.normal_desc.std[1]) == 0
            assert setOpAttr(self._op, "std2", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.normal_desc.std[2]) == 0     
            assert setOpAttr(self._op, "norma_type", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.normal_desc.type) == 0     

        if self.scale_desc:
            assert setOpAttr(self._op, "scale0", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.scale_desc.scale[0]) == 0
            assert setOpAttr(self._op, "scale1", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.scale_desc.scale[1]) == 0
            assert setOpAttr(self._op, "scale2", DATA_TYPE.FLOAT, PARAM_TYPE.ELEMENT, self.scale_desc.scale[2]) == 0  

        if self.crop_desc:
            assert setOpAttr(self._op, "crop_x", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.crop_desc.start_x) == 0
            assert setOpAttr(self._op, "crop_y", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.crop_desc.start_y) == 0
            if self.crop_desc.width and self.crop_desc.height:
                assert setOpAttr(self._op, "crop_width", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.crop_desc.width) == 0
                assert setOpAttr(self._op, "crop_height", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.crop_desc.height) == 0

        if self.tensor_desc:
            assert setOpAttr(self._op, "tensor_type0", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, self.tensor_desc.type) == 0  
        
    def setAttr(self, attrName: str, attrDType: DATA_TYPE, attrGType: PARAM_TYPE, value: Union[int, float]) -> int:
        """
        Set attributes of a specified op.\n
        ----------\n
        attrName [in]: the attribute name.\n
        attrDType [in]: data type of attribute.\n
        attrGType [in]: the attribute type (PARAM_ELEMENT | PARAM_ARRAY).\n
        value [in]: the value of attribute.\n
        return: vaceER_SUCCESS if succeed, otherwise other error code.\n
        """
        assert self._op is not None, "Please create op."
        return setOpAttr(self._op, attrName, attrDType, attrGType, value)
    
    def setAttrArray( 
            self,
            attrName: str, 
            attrDType: DATA_TYPE,
            attrGType: PARAM_TYPE,
            value: Union[int, float],
            index: int
        ) -> int:
        """
        Set attributes of a specified op.\n
        ----------\n
        attrName [in]: the attribute name.\n
        attrDType [in]: data type of attribute.\n
        attrGType [in]: the attribute type (PARAM_ELEMENT | PARAM_ARRAY).\n
        value [in]: the value of attribute.\n
        return: vaceER_SUCCESS if succeed, otherwise other error code.\n
        """
        assert self._op is not None, "Please create op."
        return setOpAttrArray(self._op, attrName, attrDType, attrGType, value, index)

    def getAttr(
        self,
        attrName: str, 
        attrDType: DATA_TYPE
    ) -> Union[int, float]:
        """
        Get attributes of a specified op.\n
        ----------\n
        attrName [in]: the attribute name.\n
        attrDType [in]: data type of attribute.\n
        """ 
        assert self._op is not None, "Please create op."
        return getOpAttr(self._op, attrName, attrDType)
    
    def getAttrArray(
        self,
        attrName: str, 
        attrDType: DATA_TYPE, 
        index: int
    ) -> Union[int, float]:
        """
        Get attributes of a specified op.\n
        ----------\n
        attrName [in]: the attribute name.\n
        attrDType [in]: data type of attribute.\n
        attrGType [in]:  the index of array element.\n
        """
        assert self._op is not None, "Please create op."
        return getOpAttrArray(self._op, attrName, attrDType, index)
    
    def execute(
        self,
        input: Dataset, 
        output: Dataset
    ) -> int:
        """
        ExecuteOp op with input dataset.\n
        ----------\n
        input [in]: vacmDataset of input data.\n
        output [out]: vacmDataset of output data.\n
        """
        assert self._op is not None, "Please create op."
        return executeOp(self._op, input, output)

    def resetInImageDesc(self, iimage_desc: ImageDesc) -> None:
        """
        reset Input ImageDesc.\n
        ----------\n
        iimage_desc [in]: new iimage_desc.\n
        """
        assert self._op is not None, "Please create op."
        assert setOpAttr(self._op, "iimage_width", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, iimage_desc.width) == 0
        assert setOpAttr(self._op, "iimage_height", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, iimage_desc.height) == 0
        assert setOpAttr(self._op, "iimage_width_pitch", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, iimage_desc.widthPitch) == 0
        assert setOpAttr(self._op, "iimage_height_pitch", DATA_TYPE.INT, PARAM_TYPE.ELEMENT, iimage_desc.heightPitch) == 0 
    
    def __del__(self):
        self.destroy()