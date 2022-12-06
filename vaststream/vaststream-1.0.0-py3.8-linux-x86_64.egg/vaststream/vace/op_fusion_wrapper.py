"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = ["RgbCropResizeCvtcolor", "RgbCvtcolorNormal", "RgbLetterboxCvtcolor", 
           "RgbResizeCvtColorCropNormal", "RgbResizeCvtcolor", 
           "YuvCvtcolorLetterboxNorm", "YuvNV12CropCvtColorResizeNorm", "YuvNV12CvtColorResizeCropNorm",
           "YuvCvtColorResizeNorm", "YuvLetterbox2RgbNorm", "YuvNv12Resize2RgbNorm", "YuvNv12ResizeCvtcolorCropNorm"]

from .common import *
from .op_attr_desc import *
from .op_base import OpBase

class RgbCropResizeCvtcolor(OpBase):
    """
    RgbCropResizeCvtcolor class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc, 
        crop_desc: CropDesc,
        resize_desc: ResizeDesc, 
        cvt_color_desc: CvtColorDesc, 
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TensorDesc,
    ):
        """
        RgbCropResizeCvtcolor class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        crop_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc=iimage_desc,
            oimage_desc=oimage_desc,
            crop_desc = crop_desc,
            cvt_color_desc=cvt_color_desc,
            normal_desc=normal_desc,
            scale_desc=scale_desc,
            resize_desc=resize_desc,
            tensor_desc=tensor_desc,
        )
        self.setInutFormat()
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.RGB_CROP_RESIZE_CVTCOLOR_NORM_TENSOR

class RgbCvtcolorNormal(OpBase):
    """
    RgbCvtcolorNormal class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        cvt_color_desc: CvtColorDesc, 
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc,
        tensor_desc: TensorDesc
    ):
        """
        RgbCvtcolorNormal class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc=iimage_desc,
            cvt_color_desc=cvt_color_desc,
            normal_desc=normal_desc,
            scale_desc=scale_desc,
            tensor_desc=tensor_desc,
        )
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.RGB_CVTCOLOR_NORM_TENSOR    

class RgbLetterboxCvtcolor(OpBase):
    """
    RgbLetterboxCvtcolor class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc, 
        resize_desc: ResizeDesc, 
        cvt_color_desc: CvtColorDesc, 
        padding_desc: PaddingDesc, 
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TensorDesc
    ):
        """
        RgbLetterboxCvtcolor class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        padding_desc[in]: padding descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc=iimage_desc,
            oimage_desc=oimage_desc,
            resize_desc=resize_desc,
            cvt_color_desc=cvt_color_desc,
            padding_desc=padding_desc,
            normal_desc=normal_desc,
            scale_desc=scale_desc,
            tensor_desc=tensor_desc
        )
        self.setInutFormat()

    def type(self) -> OP_TYPE:
        return OP_TYPE.RGB_LETTERBOX_CVTCOLOR_NORM_TENSOR 

class RgbResizeCvtColorCropNormal(OpBase):
    """
    RgbResizeCvtColorCropNormal class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc, 
        resize_desc: ResizeDesc, 
        cvt_color_desc: CvtColorDesc, 
        crop_desc: CropDesc,
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TensorDesc
    ):
        """
        RgbResizeCvtColorCropNormal class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        crop_desc[in]: crop descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc=iimage_desc,
            oimage_desc=oimage_desc,
            resize_desc=resize_desc,
            cvt_color_desc=cvt_color_desc,
            crop_desc=crop_desc,
            normal_desc=normal_desc,
            scale_desc=scale_desc,
            tensor_desc=tensor_desc
        )
        self.setInutFormat()

    def type(self) -> OP_TYPE:
        return OP_TYPE.RGB_RESIZE_CVTCOLOR_CROP_NORM_TENSOR 

class RgbResizeCvtcolor(OpBase):
    """
    RgbResizeCvtcolor class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc, 
        resize_desc: ResizeDesc, 
        cvt_color_desc: CvtColorDesc, 
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TensorDesc
    ):
        """
        RgbResizeCvtcolor class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc=iimage_desc,
            oimage_desc=oimage_desc,
            resize_desc=resize_desc,
            cvt_color_desc=cvt_color_desc,
            normal_desc=normal_desc,
            scale_desc=scale_desc,
            tensor_desc=tensor_desc
        )
        self.setInutFormat()

    def type(self) -> OP_TYPE:
        return OP_TYPE.RGB_RESIZE_CVTCOLOR_NORM_TENSOR 

class YuvCvtcolorLetterboxNorm(OpBase):
    """
    YuvCvtcolorLetterboxNorm class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc, 
        cvt_color_desc: CvtColorDesc, 
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        padding_desc: PaddingDesc, 
        resize_desc: ResizeDesc, 
        tensor_desc: TensorDesc
    ):
        """
        YuvCvtcolorLetterboxNorm class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        padding_desc[in]: padding descrition.\n
        resize_desc[in]: resize descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc=iimage_desc,
            oimage_desc=oimage_desc,
            cvt_color_desc=cvt_color_desc,
            normal_desc=normal_desc,
            scale_desc=scale_desc,
            padding_desc=padding_desc,
            resize_desc=resize_desc,
            tensor_desc=tensor_desc
        )
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.YUV_NV12_CVTCOLOR_LETTERBOX_NORM_TENSOR

class YuvNV12CropCvtColorResizeNorm(OpBase):
    """
    YuvNV12CropCvtColorResizeNorm class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc,
        crop_desc: CropDesc,
        resize_desc: ResizeDesc, 
        cvt_color_desc: CvtColorDesc,
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TENSORIZATION_TYPE
    ):
        """
        YuvNV12CropCvtColorResizeNorm class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        crop_desc[in]: crop Descrption.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc = iimage_desc,
            oimage_desc = oimage_desc,
            crop_desc = crop_desc,
            resize_desc = resize_desc,
            cvt_color_desc=cvt_color_desc,
            normal_desc = normal_desc,
            scale_desc = scale_desc,          
            tensor_desc = tensor_desc
        )
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.YUV_NV12_CROP_CVTCOLOR_RESIZE_NORM_TENSOR

class YuvNV12CvtColorResizeCropNorm(OpBase):
    """
    YuvNV12CvtColorResizeCropNorm class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc,
        resize_desc: ResizeDesc, 
        cvt_color_desc: CvtColorDesc,
        crop_desc: CropDesc,  
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TENSORIZATION_TYPE
    ):
        """
        YuvNV12CvtColorResizeCropNorm class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        crop_desc[in]: crop Descrption.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc = iimage_desc,
            oimage_desc = oimage_desc,
            resize_desc = resize_desc,
            cvt_color_desc=cvt_color_desc,
            crop_desc = crop_desc,
            normal_desc = normal_desc,
            scale_desc = scale_desc,          
            tensor_desc = tensor_desc
        )
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.YUV_NV12_CVTCOLOR_RESIZE_CROP_NORM_TENSOR

class YuvCvtColorResizeNorm(OpBase):
    """
    YuvCvtColorResizeNorm class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc,
        resize_desc: ResizeDesc, 
        cvt_color_desc: CvtColorDesc,  
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TENSORIZATION_TYPE
    ):
        """
        YuvCvtColorResizeNormTensor class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc = iimage_desc,
            oimage_desc = oimage_desc,
            resize_desc = resize_desc,
            cvt_color_desc=cvt_color_desc,
            normal_desc = normal_desc,
            scale_desc = scale_desc,          
            tensor_desc = tensor_desc
        )
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.YUV_NV12_CVTCOLOR_RESIZE_NORM_TENSOR

class YuvLetterbox2RgbNorm(OpBase):
    """
    YuvLetterbox2RgbNorm class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc,
        resize_desc: ResizeDesc, 
        cvt_color_desc: CvtColorDesc, 
        padding_desc: PaddingDesc, 
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TENSORIZATION_TYPE
    ):
        """
        YuvLetterbox2RgbNormTensor class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        padding_desc[in]: padding descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc = iimage_desc,
            oimage_desc = oimage_desc,
            resize_desc = resize_desc,
            cvt_color_desc=cvt_color_desc,
            padding_desc=padding_desc,
            normal_desc = normal_desc,
            scale_desc = scale_desc,          
            tensor_desc = tensor_desc
        )
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.YUV_NV12_LETTERBOX_2RGB_NORM_TENSOR

class YuvNv12Resize2RgbNorm(OpBase):
    """
    YuvNv12Resize2RgbNorm class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc,
        resize_desc: ResizeDesc,  
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TENSORIZATION_TYPE
    ):
        """
        YuvNv12Resize2RgbNormTensor class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc = iimage_desc,
            oimage_desc = oimage_desc,
            resize_desc = resize_desc,
            normal_desc = normal_desc,
            scale_desc = scale_desc,          
            tensor_desc = tensor_desc
        )
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.YUV_NV12_RESIZE_2RGB_NORM_TENSOR

class YuvNv12ResizeCvtcolorCropNorm(OpBase):
    """
    YuvNv12ResizeCvtcolorCropNorm class.
    """
    def __init__(
        self, 
        iimage_desc: ImageDesc, 
        oimage_desc: ImageDesc,
        resize_desc: ResizeDesc,  
        cvt_color_desc: CvtColorDesc, 
        crop_desc: CropDesc,
        normal_desc: NormalDesc, 
        scale_desc: ScaleDesc, 
        tensor_desc: TENSORIZATION_TYPE
    ):
        """
        YuvNv12ResizeCvtcolorCropNorm class.\n
        ----------\n
        iimage_desc[in]: input image descrition.\n
        oimage_desc[in]: output image descrition.\n
        resize_desc[in]: resize descrition.\n
        cvt_color_desc[in]: cvt color descrition.\n
        crop_desc[in]: crop Descrption.\n
        normal_desc[in]: normal descrition.\n
        scale_desc[in]: scale descrition.\n
        tensor_desc[in]: tensor descrition.\n
        """
        super().__init__(
            iimage_desc = iimage_desc,
            oimage_desc = oimage_desc,
            resize_desc = resize_desc,
            cvt_color_desc = cvt_color_desc,
            crop_desc = crop_desc,
            normal_desc = normal_desc,
            scale_desc = scale_desc,          
            tensor_desc = tensor_desc
        )
    
    def type(self) -> OP_TYPE:
        return OP_TYPE.YUV_NV12_RESIZE_CVTCOLOR_CROP_NORM_TENSOR

