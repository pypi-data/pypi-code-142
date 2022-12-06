"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["resize", "crop", "yuvFlip", "warpAffine", "cvtColor",
           "resizeCopyMakeBorder", "batchCropResize", "scale"]

from _vaststream_pybind11 import vace as _vace
from typing import List
from .common import *
from .utils import *
from vaststream.vacm.common import DataHandle

# =========================== API =============================

@err_check
def resize(
    resizeType: RESIZE_TYPE,
    inputImageDesc: ImageDesc,
    inputHandle: DataHandle,
    outputImageDesc: ImageDesc,
    outputHandle: DataHandle
    ) -> int:
    """
    Resize the input image to the output image size.\n
    ----------\n
    resizeType [in]: resize type.\n
    inputImageDesc [in]: the description of input image.\n
    inputHandle [in]: data handle of the input image.\n
    outputImageDesc [in]: the description of output image.\n
    outputHandle[out] data handle of the output image.\n
    return vaceER_SUCCESS if succeed, otherwise other error code.\n
    """    
    input_ptr_ = inputHandle.ptr
    output_ptr_ = outputHandle.ptr
    return _vace.resize(resizeType, inputImageDesc, input_ptr_,
                        outputImageDesc, output_ptr_)    

@err_check
def crop(
    cropRect: CropRect,
    inputImageDesc: ImageDesc,
    inputHandle: DataHandle,
    outputImageDesc: ImageDesc,
    outputHandle: DataHandle
    ) -> int:
    """
    Crop from the input image to get the output image.\n
    ----------\n
    cropRect [in]: crop rectangle.\n
    inputImageDesc [in]: the description of input image.\n
    inputHandle [in]: data handle of the input image.\n
    outputImageDesc [in]: the description of output image.\n
    outputHandle [out]: data handle of the output image.\n
    return vaceER_SUCCESS if succeed, otherwise other error code.\n
    """        
    input_ptr_ = inputHandle.ptr
    output_ptr_ = outputHandle.ptr
    return _vace.crop(cropRect, inputImageDesc, input_ptr_,
                      outputImageDesc, output_ptr_)     

@err_check
def yuvFlip(
    flipType: FLIP_TYPE,
    inputImageDesc: ImageDesc,
    inputHandle: DataHandle,
    outputImageDesc: ImageDesc,
    outputHandle: DataHandle
    ) -> int:
    """
    Flip the input image..\n
    ----------\n
    flipType [in]: flip type.\n
    inputImageDesc [in]: the description of input image.\n
    inputHandle [in]: data handle of the input image.\n
    outputImageDesc [in]: the description of output image.\n
    outputHandle [out]: data handle of the output image.\n
    return vaceER_SUCCESS if succeed, otherwise other error code.\n
    """       
    input_ptr_ = inputHandle.ptr
    output_ptr_ = outputHandle.ptr
    return _vace.yuvFlip(flipType, inputImageDesc, input_ptr_,
                        outputImageDesc, output_ptr_)        

@err_check
def warpAffine(
    affineMatrixPy: AffineMatrix, 
    warpAffineMode: WARP_AFFINE_MODE,
    borderMode: PADDING_TYPE, 
    borderValuesPy: PaddingValues,
    inputImageDesc: ImageDesc,
    inputHandle: DataHandle,
    outputImageDesc: ImageDesc,
    outputHandle: DataHandle
    ) -> int:
    """
    Affine transformation of the input image.\n
    ----------\n
    affineMatrixPy [in]: affine transformation matrix.\n
    warpAffineMode [in]: warp affine mode.\n
    inputImageDesc [in]: border type.\n
    borderMode [in]: border value.\n
    borderValuesPy [in]: the description of input image.\n
    inputHandle [in]: data handle of the input image.\n
    outputImageDesc [in]: the description of output image.\n
    outputHandle [out]: data handle of the output image.\n
    return vaceER_SUCCESS if succeed, otherwise other error code.\n
    """    
    input_ptr_ = inputHandle.ptr
    output_ptr_ = outputHandle.ptr
    return _vace.warpAffine(affineMatrixPy, warpAffineMode, borderMode, borderValuesPy,
                           inputImageDesc, input_ptr_, outputImageDesc, output_ptr_)  

@err_check
def cvtColor(
    cvtType: COLOR_CVT_CODE,
    cvtColorSpace: COLOR_SPACE,
    inputImageDesc: ImageDesc,
    inputHandle: DataHandle,
    outputImageDesc: ImageDesc,
    outputHandle: DataHandle
    ) -> int:
    """
    Covert input image color according to cvt color config.\n
    ----------\n
    cvtType [in]: color code type.\n
    cvtColorSpace [in]: convert color space.\n
    inputImageDesc [in]: the description of input image.\n
    inputHandle [in]: data handle of the input image.\n
    outputImageDesc [in]: the description of output image.\n
    outputHandle [out]: data handle of the output image.\n
    return vaceER_SUCCESS if succeed, otherwise other error code.\n
    """    
    input_ptr_ = inputHandle.ptr
    output_ptr_ = outputHandle.ptr
    return _vace.cvtColor(cvtType, cvtColorSpace, inputImageDesc,
						 input_ptr_, outputImageDesc, output_ptr_)  

@err_check
def resizeCopyMakeBorder(
    resizeType: RESIZE_TYPE,						
    paddingType: PADDING_TYPE,
    paddingValues: List[int],
    paddingEdges:PaddingEdges,
    inputImageDesc: ImageDesc,
    inputHandle: DataHandle,
    outputImageDesc: ImageDesc,
    outputHandle: DataHandle
    ) -> int:
    """
    Resize and make border to the input image..\n
    ----------\n
    resizeType [in]: resize type.\n
    paddingType [in]: padding type.\n
	paddingValues [in]: padding values.\n
    paddingEdges [in]: padding edges: left, right, top, bottom.\n
    inputImageDesc [in]: the description of input image.\n
    inputHandle [in]: data handle of the input image.\n
    outputImageDesc [in]: the description of output image.\n
    outputHandle [out]: data handle of the output image.\n
    return vaceER_SUCCESS if succeed, otherwise other error code.\n
    """    
    input_ptr_ = inputHandle.ptr
    output_ptr_ = outputHandle.ptr
    return _vace.resizeCopyMakeBorder(resizeType, paddingType, paddingValues, 
                                     paddingEdges, inputImageDesc, 
						             input_ptr_, outputImageDesc, output_ptr_)      

@err_check
def batchCropResize(
    cropRects: List[CropRect],						
    resizeType: RESIZE_TYPE,
    inputImageDesc: ImageDesc,
    inputHandle: DataHandle,
    outputImageDesc: ImageDesc,
    outputHandle: List[DataHandle]
    ) -> int:
    """
    Batch crop the input image using cropRects settings, then all resize to the output image size.\n
    ----------\n
    cropRects [in]: list of crop rectangles. size is cropNum.\n
    cropNum [in]: the size of cropRects, also the number of output, the size of outputHandles.\n
    resizeType [in]: resize type.\n
    inputImageDesc [in]: input image description.\n
    inputHandle [in]: data handle for input image. on Device ddr.\n
    outputImageDesc [in]: output image description. All the outputs share the same image description.\n
    outputHandles [out]: data handles for output images. on Device ddr. size is cropNum.\n
    return vaceER_SUCCESS if succeed, otherwise other error code.\n
    """		    
    input_ptr_ = inputHandle.ptr
    output_ptr_list_ = [output_ptr_.ptr for output_ptr_ in outputHandle] 
    return _vace.batchCropResize(cropRects, resizeType, inputImageDesc, 
                                input_ptr_, outputImageDesc, output_ptr_list_)    

@err_check
def scale(
    resizeType: RESIZE_TYPE,						
    inputImageDesc: List[ImageDesc],
    inputHandle: DataHandle,
    outputImageDesc: ImageDesc,
    outputHandle: List[DataHandle]
    ) -> int:
    """
    Scale the input image to output images. Only YUV images are supported at now.\n
    ----------\n
    resizeType [in]: resize type. only vace_RESIZE_BILINEAR is supported at now.\n
    outputCount [in]: output count. Maximum output is 16.\n
    inputImageDesc [in]: input image description.\n
    inputHandle [in]: data handle for input image. on Device ddr.\n
    outputImageDesc [in]: array of output image description. Array size is outputCount.\n
    outputHandles [in]: data handles for output images. on Device ddr. size is outputCount.\n
    return vaceER_SUCCESS if succeed, otherwise other error code.\n
    """		
    input_ptr_ = inputHandle.ptr
    output_ptr_list_ = [output_ptr_.ptr for output_ptr_ in  outputHandle]
    return _vace.scale(resizeType, inputImageDesc, 
                       input_ptr_, outputImageDesc, output_ptr_list_)    




