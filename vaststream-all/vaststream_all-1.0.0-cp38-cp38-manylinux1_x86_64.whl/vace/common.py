"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["IMAGE_TYPE", "OP_TYPE", "RESIZE_TYPE", "COLOR_CVT_CODE", "COLOR_SPACE", "FLIP_TYPE", "PADDING_TYPE",
           "WARP_AFFINE_MODE", "DATA_TYPE", "PARAM_TYPE", "NORM_TYPE", "TENSORIZATION_TYPE", "ImageDesc",
           "CropRect", "PaddingValues", "PaddingEdges", "AffineMatrix", "getVersion", "Op", "CustomizedOpInfo"]

from _vaststream_pybind11 import vace as _vace
from typing import List
from typing import Any
from .utils import *

class PointerContainer():
    """
    Pointer Container
    """
    def __init__(self, _ptr: Any):
        self._ptr = _ptr
        
    @property
    def ptr(self):
        return self._ptr

class Op(PointerContainer):
    """
    Vace Op Container
    """
    pass

class CustomizedOpInfo(PointerContainer):
    """
    Customized OpInfo Container
    """
    pass


# =========================== ENUM =============================
class IMAGE_TYPE():
    """
    vace codec type. \n
    @enum YUV_NV12. \n
    @enum YUV_I420. \n
    @enum RGB_PLANAR. \n
    @enum RGB888. \n
    @enum BGR888. \n
    @enum GRAY. \n
    @enum FORMAT_BUTT. \n
    """
    YUV_NV12:int = _vace.imageType.vaceIMG_YUV_NV12
    YUV_I420:int = _vace.imageType.vaceIMG_YUV_I420
    RGB_PLANAR:int = _vace.imageType.vaceIMG_RGB_PLANAR
    RGB888:int = _vace.imageType.vaceIMG_RGB888
    BGR888:int = _vace.imageType.vaceIMG_BGR888
    GRAY:int = _vace.imageType.vaceIMG_RGB888
    FORMAT_BUTT:int = _vace.imageType.vaceIMG_FORMAT_BUTT

class OP_TYPE():
    """
    vace op type. \n
    @enum MEM_COPY_OP. \n
    @enum CUSTOMIZED_OP. \n
    @enum CROP. \n
    @enum CVT_COLOR. \n
    @enum BATCH_CROP_RESIZE. \n
    @enum WARP_AFFINE. \n
    @enum FLIP. \n
    @enum SCALE. \n
    @enum COPY_MAKE_BOARDER. \n
    @enum YUV_NV12_RESIZE_2RGB_NORM_TENSOR. \n
    @enum YUV_NV12_CVTCOLOR_RESIZE_NORM_TENSOR. \n
    @enum YUV_NV12_RESIZE_CVTCOLOR_CROP_NORM_TENSOR. \n
    @enum YUV_NV12_CROP_CVTCOLOR_RESIZE_NORM_TENSOR. \n
    @enum YUV_NV12_CVTCOLOR_RESIZE_CROP_NORM_TENSOR. \n
    @enum YUV_NV12_CVTCOLOR_LETTERBOX_NORM_TENSOR. \n
    @enum YUV_NV12_LETTERBOX_2RGB_NORM_TENSOR. \n
    @enum RGB_CVTCOLOR_NORM_TENSOR. \n
    @enum RGB_RESIZE_CVTCOLOR_NORM_TENSOR. \n
    @enum RGB_RESIZE_CVTCOLOR_CROP_NORM_TENSOR. \n
    @enum RGB_CROP_RESIZE_CVTCOLOR_NORM_TENSOR. \n
    @enum RGB_LETTERBOX_CVTCOLOR_NORM_TENSOR. \n
    @enum MAX_NUM. \n
    """
    MEM_COPY_OP:int = _vace.opType.vaceOP_MEM_COPY_OP
    CUSTOMIZED_OP:int = _vace.opType.vaceOP_CUSTOMIZED_OP
    RESIZE:int = _vace.opType.vaceOP_RESIZE
    CROP:int = _vace.opType.vaceOP_CROP
    CVT_COLOR:int = _vace.opType.vaceOP_CVT_COLOR
    BATCH_CROP_RESIZE:int = _vace.opType.vaceOP_BATCH_CROP_RESIZE
    WARP_AFFINE:int = _vace.opType.vaceOP_WARP_AFFINE
    FLIP:int = _vace.opType.vaceOP_FLIP
    SCALE:int = _vace.opType.vaceOP_SCALE
    COPY_MAKE_BOARDER:int = _vace.opType.vaceOP_COPY_MAKE_BOARDER
    YUV_NV12_RESIZE_2RGB_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_YUV_NV12_RESIZE_2RGB_NORM_TENSOR
    YUV_NV12_CVTCOLOR_RESIZE_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_YUV_NV12_CVTCOLOR_RESIZE_NORM_TENSOR
    YUV_NV12_RESIZE_CVTCOLOR_CROP_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_YUV_NV12_RESIZE_CVTCOLOR_CROP_NORM_TENSOR
    YUV_NV12_CROP_CVTCOLOR_RESIZE_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_YUV_NV12_CROP_CVTCOLOR_RESIZE_NORM_TENSOR
    YUV_NV12_CVTCOLOR_RESIZE_CROP_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_YUV_NV12_CVTCOLOR_RESIZE_CROP_NORM_TENSOR
    YUV_NV12_CVTCOLOR_LETTERBOX_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_YUV_NV12_CVTCOLOR_LETTERBOX_NORM_TENSOR
    YUV_NV12_LETTERBOX_2RGB_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_YUV_NV12_LETTERBOX_2RGB_NORM_TENSOR
    RGB_CVTCOLOR_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_RGB_CVTCOLOR_NORM_TENSOR
    RGB_RESIZE_CVTCOLOR_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_RGB_RESIZE_CVTCOLOR_NORM_TENSOR
    RGB_RESIZE_CVTCOLOR_CROP_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_RGB_RESIZE_CVTCOLOR_CROP_NORM_TENSOR
    RGB_CROP_RESIZE_CVTCOLOR_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_RGB_CROP_RESIZE_CVTCOLOR_NORM_TENSOR
    RGB_LETTERBOX_CVTCOLOR_NORM_TENSOR:int = _vace.opType.vaceOP_FUSION_OP_RGB_LETTERBOX_CVTCOLOR_NORM_TENSOR
    MAX_NUM:int = _vace.opType.vaceOP_FUSION_OP_MAX_NUM

class RESIZE_TYPE():
    """
    vace resize type. \n
    @enum NO_RESIZE. \n
    @enum BILINEAR. \n
    @enum NEAREST. \n
    @enum BICUBIC. \n
    @enum LANCOZ. \n
    @enum BILINEAR_PILLOW. \n
    @enum BILINEAR_CV. \n
    @enum LANCZOS_PILLOW. \n
    @enum LANCZOS_CV. \n
    @enum BOX_PILLOW. \n
    @enum HAMMING_PILLOW. \n
    @enum BICUBIC_PILLOW. \n
    @enum BUTT. \n
    """
    NO_RESIZE:int = _vace.resizeType.vaceRESIZE_NO_RESIZE
    BILINEAR:int = _vace.resizeType.vaceRESIZE_BILINEAR
    NEAREST:int = _vace.resizeType.vaceRESIZE_NEAREST
    BICUBIC:int = _vace.resizeType.vaceRESIZE_BICUBIC
    LANCOZ:int = _vace.resizeType.vaceRESIZE_LANCOZ
    BILINEAR_PILLOW:int = _vace.resizeType.vaceRESIZE_BILINEAR_PILLOW
    BILINEAR_CV:int = _vace.resizeType.vaceRESIZE_BILINEAR_CV
    LANCZOS_PILLOW:int = _vace.resizeType.vaceRESIZE_LANCZOS_PILLOW
    LANCZOS_CV:int = _vace.resizeType.vaceRESIZE_LANCZOS_CV
    BOX_PILLOW:int = _vace.resizeType.vaceRESIZE_BOX_PILLOW
    HAMMING_PILLOW:int = _vace.resizeType.vaceRESIZE_HAMMING_PILLOW
    BICUBIC_PILLOW:int = _vace.resizeType.vaceRESIZE_BICUBIC_PILLOW
    BUTT:int = _vace.resizeType.vaceRESIZE_BUTT

class COLOR_CVT_CODE():
    """
    vace color cvtdoce type. \n
    @enum YUV2RGB_NV12. \n
    @enum YUV2BGR_NV12. \n
    @enum NO_CHANGE. \n
    @enum BGR2RGB. \n
    @enum RGB2BGR. \n
    @enum BGR2RGB_INTERLEAVE2PLANAR. \n
    @enum RGB2BGR_INTERLEAVE2PLANAR. \n
    @enum BGR2BGR_INTERLEAVE2PLANAR. \n
    @enum RGB2RGB_INTERLEAVE2PLANAR. \n
    @enum YUV2GRAY_NV12. \n
    @enum BGR2GRAY_INTERLEAVE. \n
    @enum RGB2GRAY_PLANAR. \n
    @enum BGR2YUV_NV12_PLANAR. \n
    @enum CVT_CODE_BUTT. \n
    """

    YUV2RGB_NV12:int = _vace.colorCvtCode.vaceCOLOR_YUV2RGB_NV12
    YUV2BGR_NV12:int = _vace.colorCvtCode.vaceCOLOR_YUV2BGR_NV12
    NO_CHANGE:int = _vace.colorCvtCode.vaceCOLOR_NO_CHANGE
    BGR2RGB:int = _vace.colorCvtCode.vaceCOLOR_BGR2RGB
    RGB2BGR:int = _vace.colorCvtCode.vaceCOLOR_RGB2BGR
    BGR2RGB_INTERLEAVE2PLANAR:int = _vace.colorCvtCode.vaceCOLOR_BGR2RGB_INTERLEAVE2PLANAR
    RGB2BGR_INTERLEAVE2PLANAR:int = _vace.colorCvtCode.vaceCOLOR_RGB2BGR_INTERLEAVE2PLANAR
    BGR2BGR_INTERLEAVE2PLANAR:int = _vace.colorCvtCode.vaceCOLOR_BGR2BGR_INTERLEAVE2PLANAR
    RGB2RGB_INTERLEAVE2PLANAR:int = _vace.colorCvtCode.vaceCOLOR_RGB2RGB_INTERLEAVE2PLANAR
    YUV2GRAY_NV12:int = _vace.colorCvtCode.vaceCOLOR_YUV2GRAY_NV12
    BGR2GRAY_INTERLEAVE:int = _vace.colorCvtCode.vaceCOLOR_BGR2GRAY_INTERLEAVE
    BGR2GRAY_PLANAR:int = _vace.colorCvtCode.vaceCOLOR_BGR2GRAY_PLANAR
    RGB2GRAY_INTERLEAVE:int = _vace.colorCvtCode.vaceCOLOR_RGB2GRAY_INTERLEAVE
    RGB2GRAY_PLANAR:int = _vace.colorCvtCode.vaceCOLOR_RGB2GRAY_PLANAR
    RGB2YUV_NV12_PLANAR:int = _vace.colorCvtCode.vaceCOLOR_RGB2YUV_NV12_PLANAR
    BGR2YUV_NV12_PLANAR:int = _vace.colorCvtCode.vaceCOLOR_BGR2YUV_NV12_PLANAR  
    CVT_CODE_BUTT:int = _vace.colorCvtCode.vaceCOLOR_CVT_CODE_BUTT

class COLOR_SPACE():
    """
    vace color space. \n
    @enum SPACE_BT709. \n
    @enum SPACE_BT601. \n
    @enum SPACE_BUTT. \n
    """

    BT709:int = _vace.colorSpace.vaceCOLOR_SPACE_BT709
    BT601:int = _vace.colorSpace.vaceCOLOR_SPACE_BT601
    BUTT:int = _vace.colorSpace.vaceCOLOR_SPACE_BUTT

class FLIP_TYPE():
    """
    vace flip type. \n
    @enum X_AXIS. \n
    @enum Y_AXIS. \n
    @enum BOTH_AXES. \n
    """
    
    X_AXIS:int = _vace.flipType.vaceFLIP_X_AXIS
    Y_AXIS:int = _vace.flipType.vaceFLIP_Y_AXIS
    BOTH_AXES:int = _vace.flipType.vaceFLIP_BOTH_AXES

class PADDING_TYPE():
    """
    vace padding type. \n
    @enum CONSTANT. \n
    @enum REPLICATE. \n
    @enum REFLECT. \n
    @enum BUTT. \n
    """

    CONSTANT:int = _vace.paddingType.vaceEDGE_PADDING_TYPE_CONSTANT
    REPLICATE:int = _vace.paddingType.vaceEDGE_PADDING_REPLICATE
    REFLECT:int = _vace.paddingType.vaceEDGE_PADDING_TYPE_REFLECT
    BUTT:int = _vace.paddingType.vaceEDGE_PADDING_TYPE_BUTT

class WARP_AFFINE_MODE():
    """
    vace warp affine mode. \n
    @enum NEAREST. \n
    @enum BILINEAR. \n
    @enum BUTT. \n
    """

    NEAREST:int = _vace.warpAffineMode.vaceWARP_AFFINE_MODE_NEAREST
    BILINEAR:int = _vace.warpAffineMode.vaceWARP_AFFINE_MODE_BILINEAR
    BUTT:int = _vace.warpAffineMode.vaceWARP_AFFINE_MODE_BUTT

class DATA_TYPE():
    """
    vace data type. \n
    @enum INT. \n
    @enum UINT_8. \n
    @enum UINT_16. \n
    @enum UINT_32. \n
    @enum UINT_64. \n
    @enum FLOAT. \n
    @enum FLOAT_16. \n
    @enum DOUBLE. \n
    """

    INT:int = _vace.dataType.vaceDT_INT     
    UINT_8:int = _vace.dataType.vaceDT_UINT_8      
    UINT_16:int = _vace.dataType.vaceDT_UINT_16     
    UINT_32:int = _vace.dataType.vaceDT_UINT_32     
    UINT_64:int = _vace.dataType.vaceDT_UINT_64     
    FLOAT:int = _vace.dataType.vaceDT_FLOAT       
    FLOAT_16:int = _vace.dataType.vaceDT_FLOAT_16    
    DOUBLE:int = _vace.dataType.vaceDT_DOUBLE   

class PARAM_TYPE():
    """
    vace param type. \n
    @enum ELEMENT. \n
    @enum ARRAY. \n
    @enum TENSOR. \n
    """

    ELEMENT:int = _vace.paramType.vacePARAM_ELEMENT
    ARRAY:int = _vace.paramType.vacePARAM_ARRAY
    TENSOR:int = _vace.paramType.vacePARAM_TENSOR

class NORM_TYPE():
    """
    vace norm type. \n
    @enum NORMALIZATION_NONE. \n
    @enum EQUAL. \n
    @enum MINUSMEAN. \n
    @enum MINUSMEAN_DIVSTD. \n
    @enum DIV255_MINUSMEAN_DIVSTD. \n
    @enum DIV1275_MINUSONE. \n
    @enum DIV255. \n
    @enum NORMALIZATION_NONE_BUTT. \n
    """

    NORMALIZATION_NONE:int = _vace.normType.vaceNORM_NORMALIZATION_NONE
    EQUAL:int = _vace.normType.vaceNORM_EQUAL
    MINUSMEAN:int = _vace.normType.vaceNORM_MINUSMEAN
    MINUSMEAN_DIVSTD:int = _vace.normType.vaceNORM_MINUSMEAN_DIVSTD
    DIV255_MINUSMEAN_DIVSTD:int = _vace.normType.vaceNORM_DIV255_MINUSMEAN_DIVSTD
    DIV1275_MINUSONE:int = _vace.normType.vaceNORM_DIV1275_MINUSONE
    DIV255:int = _vace.normType.vaceNORM_DIV255
    NORMALIZATION_NONE_BUTT:int = _vace.normType.vaceNORM_NORMALIZATION_NONE_BUTT

class TENSORIZATION_TYPE():
    """
    vace tensorization type. \n
    @enum NONE. \n
    @enum UINT8. \n
    @enum UINT8_INTERLEAVE. \n
    @enum FP16. \n
    @enum FP16_INTERLEAVE. \n
    @enum FP16_INTERLEAVE_RGB. \n
    @enum BUTT. \n
    """

    NONE:int = _vace.tensorizationType.vaceTENSORIZATION_NONE
    UINT8:int = _vace.tensorizationType.vaceTENSORIZATION_UINT8
    UINT8_INTERLEAVE:int = _vace.tensorizationType.vaceTENSORIZATION_UINT8_INTERLEAVE
    FP16:int = _vace.tensorizationType.vaceTENSORIZATION_FP16
    FP16_INTERLEAVE:int = _vace.tensorizationType.vaceTENSORIZATION_FP16_INTERLEAVE
    FP16_INTERLEAVE_RGB:int = _vace.tensorizationType.vaceTENSORIZATION_FP16_INTERLEAVE_RGB
    BUTT:int = _vace.tensorizationType.vaceTENSORIZATION_TYPE_BUTT

# ================================ STRUCT ============================
class ImageDesc(_vace.imageDesc):
    width:int
    height:int
    widthPitch:int
    heightPitch:int
    format:IMAGE_TYPE

class CropRect(_vace.cropRect):
    start_x:int
    start_y:int
    width:int
    height:int

class PaddingValues(_vace.paddingValuesPy):
    value:List[int]

class PaddingEdges(_vace.paddingEdges):
    top: int
    bottom: int
    left: int
    right: int

class AffineMatrix(_vace.affineMatrixPy):
    matrix:List[float]

# ================================ API ============================
def getVersion() -> str:
    """
    Get the VAME API version information.\n
    ------------\n
    version [out]: vace version.\n
    """
    return _vace.getVersion()