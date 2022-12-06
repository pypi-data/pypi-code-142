"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "ENC_QUALITY_MODE", "ENC_TUNE_TYPE", "ENC_QP_TYPE", "ENC_SEI_NAL_TYPE", "EncExternalSEI",
    "EncPictureArea", "EncPictureROI", "EncExtendedParams", "EncVideoConfiguration", "EncJPEGConfiguration",
    "EncChannelParamters", "EncOutputOptions", "ENC_MAX_STRM_BUF_NUM", "ENC_MAX_REF_FRAMES", "ENC_MAX_GOP_SIZE",
    "ENC_MAX_LTR_FRAMES", "ENC_MAX_ROI_NUM", "ENC_DEFAULT_PAR", "ENC_VIDEO_MAX_HEIGHT", "ENC_VIDEO_MAX_WIDTH",
    "ENC_VIDEO_MIN_HEIGHT", "ENC_VIDEO_MIN_WIDTH", "ENC_JPEG_MAX_HEIGHT", "ENC_JPEG_MAX_WIDTH", "ENC_JPEG_MIN_HEIGHT",
    "ENC_JPEG_MIN_WIDTH", "ENC_MAX_OUTBUF_NUM", "createEncoderChannel", "destoryEncoderChannel", "startEncoder",
    "resetEncoder", "stopEncoder", "sendFrameToEncoder", "receiveStreamFromEncoder", "jpegSyncEncoder", "encReleaseStream",
    "getEncoderAvailableChannels", "YUVReader", "Encoder"
]

import os
import numpy as np
import warnings
from _vaststream_pybind11 import vame as _vame
from typing import Any, Union, Tuple, Optional
from .common import *
from .utils import *

# =========================== ENUM =============================
class ENC_QUALITY_MODE():
    """
    vame encode quality mode.\n
    ----------\n
    @enum GOLD.\n
    @enum SILVER.\n
    @enum SILVER2.\n
    @enum BRONZE.\n
    """
    GOLD: int = _vame.encQualityMode.VAME_GOLD_QUALITY
    SILVER: int = _vame.encQualityMode.VAME_SILVER_QUALITY
    SILVER2: int = _vame.encQualityMode.VAME_SILVER2_QUALITY
    BRONZE: int = _vame.encQualityMode.VAME_BRONZE_QUALITY


class ENC_TUNE_TYPE():
    """
    vame encode tune type.\n
    ----------\n
    @enum PSNR.\n
    @enum SSIM.\n
    @enum VISUAL.\n
    @enum SHARP_VISUAL.\n
    """
    PSNR: int = _vame.encTuneType.VAME_ENC_TUNE_PSNR
    SSIM: int = _vame.encTuneType.VAME_ENC_TUNE_SSIM
    VISUAL: int = _vame.encTuneType.VAME_ENC_TUNE_VISUAL
    SHARP_VISUAL: int = _vame.encTuneType.VAME_ENC_TUNE_SHARP_VISUAL


class ENC_QP_TYPE():
    """
    vame encode qp type.\n
    ----------\n
    @enum QP.\n
    @enum QP_DELTA.\n
    """
    QP: int = _vame.encQPType.VAME_ENC_QP
    QP_DELTA: int = _vame.encQPType.VAME_ENC_QP_DELTA


class ENC_SEI_NAL_TYPE():
    """
    vame encode sei nal type.\n
    ----------\n
    @enum SEI_PREFIX.\n
    @enum SEI_SUFFIX.\n
    """
    SEI_PREFIX: int = _vame.encSEINalType.VAME_ENC_SEI_PREFIX
    SEI_SUFFIX: int = _vame.encSEINalType.VAME_ENC_SEI_SUFFIX


# =========================== STRUCT =============================
class EncExternalSEI(_vame.encExternalSEI):
    """
    Encode External SEI.
    """
    nalType: ENC_SEI_NAL_TYPE
    payloadType: int
    payloadDataSize: int
    payloadData: Any


class EncPictureArea(_vame.encPictureArea):
    """
    Encode Picture Area.
    """
    enable: int
    top: int
    left: int
    bottom: int
    right: int


class EncPictureROI(_vame.encPictureROI):
    """
    Encode Picture ROI.
    """
    area: EncPictureArea
    qpType: ENC_QP_TYPE
    qpValue: int


class EncExtendedParams(_vame.encExtendedParams):
    """
    Encode Extended Params.
    """
    forceIDR: int
    roi: EncPictureROI


class EncVideoConfiguration(_vame.encVideoConfiguration):
    """
    Encode Video Configuration
    """
    profile: VIDEO_PROFILE
    level: VIDEO_LEVEL
    width: int
    height: int
    frameRate: Rational
    bitDepthLuma: int
    bitDepthChroma: int
    gopSize: int
    gdrDuration: int
    lookaheadDepth: int
    qualityMode: ENC_QUALITY_MODE
    tune: ENC_TUNE_TYPE
    keyInt: int
    crf: int
    cqp: int
    llRc: int
    bitRate: int
    initQp: int
    vbvBufSize: int
    vbvMaxRate: int
    intraQpDelta: int
    qpMinI: int
    qpMaxI: int
    qpMinPB: int
    qpMaxPB: int
    vbr: int
    aqStrength: float
    enableROI: int
    P2B: int
    bBPyramid: int
    maxFrameSizeMultiple: float


class EncJPEGConfiguration(_vame.encJPEGConfiguration):
    """
    Encode JPEG Configuration.
    """
    codingWidth: int
    codingHeight: int
    frameType: PIXEL_FORMAT
    userData: str
    losslessEn: int


class EncChannelParamters():
    """
    Encode Channel Paramters.
    """
    codecType: CODEC_TYPE
    outbufNum: int
    enProfiling: int
    config: Union[EncVideoConfiguration, EncJPEGConfiguration]


class EncOutputOptions(_vame.encOutputOptions):
    """
    Encode Output Options
    """
    reserved: int

# =========================== DEFINE =============================
ENC_MAX_STRM_BUF_NUM = _vame.VAME_ENC_MAX_STRM_BUF_NUM
ENC_MAX_REF_FRAMES = _vame.VAME_ENC_MAX_REF_FRAMES
ENC_MAX_GOP_SIZE = _vame.VAME_ENC_MAX_GOP_SIZE
ENC_MAX_LTR_FRAMES = _vame.VAME_ENC_MAX_LTR_FRAMES
ENC_MAX_ROI_NUM = _vame.VAME_ENC_MAX_ROI_NUM
ENC_DEFAULT_PAR = _vame.VAME_ENC_DEFAULT_PAR
ENC_VIDEO_MAX_HEIGHT = _vame.VAME_ENC_VIDEO_MAX_HEIGHT
ENC_VIDEO_MAX_WIDTH = _vame.VAME_ENC_VIDEO_MAX_WIDTH
ENC_VIDEO_MIN_HEIGHT = _vame.VAME_ENC_VIDEO_MIN_HEIGHT
ENC_VIDEO_MIN_WIDTH = _vame.VAME_ENC_VIDEO_MIN_WIDTH
ENC_JPEG_MAX_HEIGHT = _vame.VAME_ENC_JPEG_MAX_HEIGHT
ENC_JPEG_MAX_WIDTH = _vame.VAME_ENC_JPEG_MAX_WIDTH
ENC_JPEG_MIN_HEIGHT = _vame.VAME_ENC_JPEG_MIN_HEIGHT
ENC_JPEG_MIN_WIDTH = _vame.VAME_ENC_JPEG_MIN_WIDTH
ENC_MAX_OUTBUF_NUM = _vame.VAME_ENC_MAX_OUTBUF_NUM

# =========================== API =============================
@err_check
def createEncoderChannel(channelId: int, params: EncChannelParamters) -> int:
    """
    Create an encoder channel.\n
    ----------\n
    channelId [in]: Encoder channel index.\n\n
    params [in]: The init parameter for create encoder channel.\n
    """
    # 类型兼容
    paramsPybind = _vame.encChannelParamters()
    paramsPybind.codecType = params.codecType
    paramsPybind.outbufNum = params.outbufNum
    paramsPybind.enProfiling = params.enProfiling
    if isinstance(params.config, EncJPEGConfiguration):
        paramsPybind.jpegConfig = params.config
    else:
        paramsPybind.videoConfig = params.config
    return _vame.createEncoderChannel(paramsPybind, channelId)

@err_check
def destoryEncoderChannel(channelId: int) -> int:
    """
    Destory an encoder channel.\n
    ----------\n
    channelId [in]: Encoder channel index.\n\n
    """
    return _vame.destoryEncoderChannel(channelId)

@err_check
def startEncoder(channelId: int) -> int:
    """
    Start the encoder.\n
    ----------\n
    channelId [in]: Encoder channel index.\n\n
    """
    return _vame.startEncoder(channelId)

@err_check
def resetEncoder(channelId: int) -> int:
    """
    Restart the encoder.\n
    ----------\n
    channelId [in]: Encoder channel index.\n\n
    """
    return _vame.resetEncoder(channelId)

@err_check
def stopEncoder(channelId: int) -> int:
    """
    Stop the encoder.\n
    ----------\n
    channelId [in]: Encoder channel index.\n\n
    """
    return _vame.stopEncoder(channelId)

def sendFrameToEncoder(channelId: int, frame: Frame, extParams: EncExtendedParams = None, timeout: int = 4000) -> int:
    """
    Send a frame to Encoder to encode.\n
    ----------\n
    channelId [in]: Encoder channel index.\n
    frame[in]: The frame which send to encoder.\n
    extParams[in]: Ext params for encoder.\n
    timeout[in]: timeout value.\n
    """
    ret = _vame.sendFrameToEncoder(channelId, frame, extParams, timeout)
    if ret >= _vame.vameER_RSLT_ERR_START:
        raise Exception(f"sendFrameToEncoder return error {ret}.")
    if ret != _vame.vameER_SUCCESS:
        warnings.warn(f"sendFrameToEncoder waring: {ret}")
    return ret

def receiveStreamFromEncoder(channelId: int, timeout: int = 4000) -> Tuple[int, Optional[Stream]]:
    """
    Receive a stream from Encoder.\n
    ----------\n
    channelId [in]: Encoder channel index.\n
    timeout [in]: timeout value.\n
    """
    stream = _vame.stream()
    ret = _vame.receiveStreamFromEncoder(channelId, stream, timeout)
    if ret >= _vame.vameER_RSLT_ERR_START:
         raise Exception(f"receiveStreamFromEncoder return error {ret}.")
    if ret == _vame.vameER_SUCCESS:
        return (ret, stream)
    return (ret, None)

def jpegSyncEncoder(channelId: int, frame: Frame, extParams: EncExtendedParams = None, timeout: int = 4000) -> Stream:
    """
    Jpeg Encode Sync api.\n
    ----------\n
    channelId [in]: Encoder channel index.\n
    frame [in]: YUV frame data.\n
    extParams[in]: Ext params for encoder.\n
    timeout [in]: timeout value.\n
    """
    stream = _vame.stream()
    ret = _vame.jpegSyncEncoder(channelId, frame, stream, extParams, timeout)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"jpegSyncEncoder return error {ret}.")
    return stream

def encReleaseStream(channelId: int, stream: Stream, timeout: int = 4000) -> int:
    """
    Release the vame stream whose content filled by vameReceiveStreamFromEncoder.\n
    ----------\n
    channelId [in]: Encoder channel index.\n
    stream [in]: Stream to release.\n
    timeout [in]: timeout value.\n
    """
    return _vame.encReleaseStream(channelId, stream, timeout)

def getEncoderAvailableChannels() -> int:
    """
    Get the Encoder available channels.
    """
    return _vame.getEncoderAvailableChannels()

class YUVReader():
    """
    YUV Reader tool class.
    """
    SUPPORT_PIXEL_FORMAT = (PIXEL_FORMAT.YUV420P, PIXEL_FORMAT.NV12, PIXEL_FORMAT.NV21)

    def __init__(self, filePath: str, format: PIXEL_FORMAT, width: int, height: int, stride: int = None):
        if not os.path.exists(filePath):
            raise Exception(f"Can not find YUV file {filePath}.")
        self.filePath = filePath
        self.format = format
        self.width = width
        self.height = height
        if stride is None:
            stride = width
        self.stride = [width, 0, 0]
        self.busAddress = [0, 0, 0]
        self.luma_size = 0
        self.chroma_size_cb = 0
        self.chroma_size_cr = 0
        self.pic_size = 0
        self._parse()
        self.fileHandle = None

    def _parse(self):
        # 仅支持420
        if self.format not in self.SUPPORT_PIXEL_FORMAT:
            raise Exception(f"The format {self.format} is not supported yet, only support {self.SUPPORT_PIXEL_FORMAT}.")
        self.luma_size = self.stride[0] * self.height
        # 奇数向上取整
        stride_align = ((self.stride[0] + 1) // 2 * 2) // 2
        height_align = ((self.height + 1) // 2 * 2) // 2
        if self.format == PIXEL_FORMAT.YUV420P:
            self.stride[1] = stride_align
            self.stride[2] = stride_align
            self.chroma_size_cb = self.stride[1] * height_align
            self.chroma_size_cr = self.stride[2] * height_align
        else:
            self.stride[1] = (self.stride[0] + 1) // 2 * 2
            self.chroma_size_cb = self.stride[1] * height_align
            self.chroma_size_cr = 0
        self.pic_size = self.luma_size + self.chroma_size_cb + self.chroma_size_cr

    def __enter__(self):
        self.create()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
    
    def create(self) -> None:
        """
        Create reader.
        """
        if self.fileHandle is None:
            self.fileHandle = open(self.filePath, "rb")
    
    def release(self) -> None:
        """
        Release reader.
        """
        assert self.fileHandle is not None, "Please create reader."
        self.fileHandle.close()
        self.fileHandle = None


    def readFrame(self) -> Optional[Frame]:
        """
        Read one frame.\n
        """
        assert self.fileHandle is not None, "Please create reader."
        dataBytes = self.fileHandle.read(self.pic_size)
        if dataBytes == b'':
            return None

        frame = Frame()
        frame.data = np.frombuffer(dataBytes, np.byte)
        frame.dataSize = self.pic_size
        frame.width = self.width
        frame.height = self.height
        frame.stride = self.stride
        frame.busAddress = self.busAddress
        frame.memoryType = MEMORY_TYPE.HOST
        frame.pixelFormat = self.format

        return frame

class Encoder():
    """
    Encoder tool class.
    """
    def __init__(self, channelId: int, params: EncChannelParamters, auto_start: bool = False, auto_init: bool = True) -> None:
        """
        Encoder tool class.\n
        ----------\n
        channelId [in]: Encoder channel index.\n\n
        params [in]: The init parameter for create encoder channel.\n
        auto_start [in]: Whether to start and stop channel automatically.\n
        auto_init [in]: Whether to systemInitialize and systemUninitialize automatically.\n
        """
        self.channelId = channelId
        self.params = params
        self.auto_start = auto_start
        self.auto_init = auto_init
        self._instance = False
    
    def __enter__(self):
        self.create()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destory()
    
    def create(self) -> None:
        """
        Create the encoder.
        """
        if not self._instance:
            if self.auto_init: systemInitialize()
            createEncoderChannel(self.channelId, self.params)
            self._instance = True
            if self.auto_start: startEncoder(self.channelId)
    
    def destory(self) -> None:
        """
        Destory the enconder.
        """
        assert self._instance, "Please create encoder."
        if self.auto_start: stopEncoder(self.channelId)
        destoryEncoderChannel(self.channelId)
        self._instance = False
        if self.auto_init: systemUninitialize()

    def start(self):
        """
        Start the encoder.
        """
        assert self._instance, "Please create encoder."
        return startEncoder(self.channelId)
    
    def stop(self):
        """
        Stop the encoder.
        """
        assert self._instance, "Please create encoder."
        return stopEncoder(self.channelId)
    
    def reset(self):
        """
        Reset the encoder.
        """
        assert self._instance, "Please create encoder."
        return resetEncoder(self.channelId)
    
    def sendFrame(self, frame: Frame, extParams: EncExtendedParams = None, timeout: int = 4000) -> int:
        """
        Send a frame to Encoder to encode.\n
        ----------\n
        frame[in]: The frame which send to encoder.\n
        extParams[in]: Ext params for encoder.\n
        timeout[in]: timeout value.\n
        """
        assert self._instance, "Please create encoder."
        return sendFrameToEncoder(self.channelId, frame, extParams, timeout)
    
    def receiveStream(self, timeout: int = 4000) -> Tuple[int, Optional[Stream]]:
        """
        Receive a stream from Encoder.\n
        ----------\n
        timeout [in]: timeout value.\n
        """
        assert self._instance, "Please create encoder."
        return receiveStreamFromEncoder(self.channelId, timeout)
    
    def jpegSync(self, frame: Frame, extParams: EncExtendedParams = None, timeout: int = 4000) -> Stream:
        """
        Jpeg Encode Sync api.\n
        ----------\n
        frame [in]: YUV frame data.\n
        extParams[in]: Ext params for encoder.\n
        timeout [in]: timeout value.\n
        """
        assert self._instance, "Please create encoder."
        return jpegSyncEncoder(self.channelId, frame, extParams, timeout)
    
    def releaseStream(self, stream: Stream, timeout: int = 4000) -> int:
        """
        Release the vame stream whose content filled by vameReceiveStreamFromEncoder.\n
        ----------\n
        stream [in]: Stream to release.\n
        timeout [in]: timeout value.\n
        """
        assert self._instance, "Please create encoder."
        return encReleaseStream(self.channelId, stream, timeout)