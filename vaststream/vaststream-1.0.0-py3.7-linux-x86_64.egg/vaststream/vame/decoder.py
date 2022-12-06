"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "DECODE_MODE", "DecChannelParamters", "DecStreamInfo", "DecJpegInfo", "DecStatus",
    "DecOutputOptions", "DecVideoInfo", "JpegDecCapability", "VideoDecCapability", "DEC_MAX_PIX_FMT_NUM",
    "DEC_MAX_CODING_MODE_NUM", "DEC_JPEG_MAX_WIDTH", "DEC_JPEG_MAX_HEIGHT", "DEC_JPEG_MIN_WIDTH", "DEC_JPEG_MIN_HEIGHT",
    "DEC_VIDEO_MAX_WIDTH", "DEC_VIDEO_MAX_HEIGHT", "DEC_VIDEO_MIN_WIDTH", "DEC_VIDEO_MIN_HEIGHT", "DEC_MAX_STREAM_BUFFER_SIZE",
    "createDecoderChannel", "destoryDecoderChannel", "startDecoder", "resetDecoder", "stopDecoder",
    "sendStreamToDecoder", "receiveFrameFromDecoder", "jpegSyncDecoder", "transferFrameFromDecoder",
    "decReleaseFrame", "getJpegInfo", "getVideoInfo", "getStreamInfoFromDecoder", "getDecoderStatus",
    "jpegDecGetCaps", "videoDecGetCaps", "getDecoderAvailableChannels", "Decoder", "H264Reader"
]

import os
import warnings
from _vaststream_pybind11 import vame as _vame
from typing import List, Optional, Tuple
from .common import *
from .utils import *

# =========================== ENUM =============================
class DECODE_MODE():
    """
    vame decode mode.\n
    ----------\n
    @enum NORMAL: normal mode for decode.\n
    @enum INTRA_ONLY: intral_only mode for decode.\n
    """
    NORMAL: int = _vame.decodeMode.VAME_DEC_NORMAL
    INTRA_ONLY: int = _vame.decodeMode.VAME_DEC_INTRA_ONLY

# =========================== STRUCT =============================
class DecChannelParamters(_vame.decChannelParamters):
    """
    Decode Channel Paramters.
    """
    codecType: CODEC_TYPE
    sourceMode: SOURCE_MODE
    decodeMode: DECODE_MODE
    pixelFormat: PIXEL_FORMAT
    extraBufferNumber: int

class DecStreamInfo(_vame.decStreamInfo):
    """
    Decode Stream Information.
    """
    width: int
    height: int
    fps: int
    pixelSize: int

class DecJpegInfo(_vame.decJpegInfo):
    """
    Decode Jpeg Information.
    """
    width: int
    height: int
    x_density: int
    y_density: int
    outputFormat: CHROMA_FORMAT
    codingMode: JPEG_CODING_MODE


class DecStatus(_vame.decStatus):
    """
    Decode status.
    """
    state: STATE
    hardwareID: HardwareID
    result: int
    runningFrames: int
    reorderedFrames: int
    bufferedFrames: int
    droppedFrames: int

class DecOutputOptions(_vame.decOutputOptions):
    """
    Decode Output Options.
    """
    memoryType: MEMORY_TYPE
    enableCrop: int

class DecVideoInfo(_vame.decVideoInfo):
    """
    Decode Video Infomation.
    """
    width: int
    height: int
    cropFlag: int
    cropWidth: int
    cropHeight: int
    xOffset: int
    yOffset: int
    fps: int
    pixelFormat: PIXEL_FORMAT

class JpegDecCapability(_vame.jpegDecCapability):
    """
    Jpeg Decode Capability.
    """
    maxWidth: int
    maxHeight: int
    minWidth: int
    minHeight: int
    codingMode: List[JPEG_CODING_MODE]
    pixelFormats: List[PIXEL_FORMAT]

class VideoDecCapability(_vame.videoDecCapability):
    """
    Video Decode Capability.
    """
    bitDepth: int
    maxWidth: int
    maxHeight: int
    minWidth: int
    minHeight: int
    maxProFile: VIDEO_PROFILE
    maxLevel: VIDEO_LEVEL
    pixelFormats: List[PIXEL_FORMAT]

# =========================== DEFINE =============================
DEC_MAX_PIX_FMT_NUM = _vame.VAME_DEC_MAX_PIX_FMT_NUM
DEC_MAX_CODING_MODE_NUM = _vame.VAME_DEC_MAX_CODING_MODE_NUM
DEC_JPEG_MAX_WIDTH = _vame.VAME_DEC_JPEG_MAX_WIDTH
DEC_JPEG_MAX_HEIGHT = _vame.VAME_DEC_JPEG_MAX_HEIGHT
DEC_JPEG_MIN_WIDTH = _vame.VAME_DEC_JPEG_MIN_WIDTH
DEC_JPEG_MIN_HEIGHT = _vame.VAME_DEC_JPEG_MIN_HEIGHT
DEC_VIDEO_MAX_WIDTH = _vame.VAME_DEC_VIDEO_MAX_WIDTH
DEC_VIDEO_MAX_HEIGHT = _vame.VAME_DEC_VIDEO_MAX_HEIGHT
DEC_VIDEO_MIN_WIDTH = _vame.VAME_DEC_VIDEO_MIN_WIDTH
DEC_VIDEO_MIN_HEIGHT = _vame.VAME_DEC_VIDEO_MIN_HEIGHT
DEC_MAX_STREAM_BUFFER_SIZE = _vame.VAME_DEC_MAX_STREAM_BUFFER_SIZE

# =========================== API =============================
@err_check
def createDecoderChannel(channelId: int, params: DecChannelParamters) -> int:
    """
    Create an decoder channel.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    param [in]: The init parameter for create decoder channel.\n
    """
    return _vame.createDecoderChannel(params, channelId)

@err_check
def destoryDecoderChannel(channelId: int) -> int:
    """
    Destory the system.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    return _vame.destoryDecoderChannel(channelId)

@err_check
def startDecoder(channelId: int) -> int:
    """
    Start the decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    return _vame.startDecoder(channelId)

@err_check
def resetDecoder(channelId: int) -> int:
    """
    Restart the decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    return _vame.resetDecoder(channelId)

@err_check
def stopDecoder(channelId: int) -> int:
    """
    Stop the decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    return _vame.stopDecoder(channelId)

def sendStreamToDecoder(channelId: int, stream: Stream, timeout: int = 4000) -> int:
    """
    Send a stream to decoder to decode.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    stream [in]: Stream data for decoder.\n
    timeout [in]: timeout value.\n
    """
    ret = _vame.sendStreamToDecoder(channelId, stream, timeout)
    if ret >= _vame.vameER_RSLT_ERR_START:
        raise Exception(f"sendStreamToDecoder return error {ret}.")
    if ret != _vame.vameER_SUCCESS:
        warnings.warn(f"sendStreamToDecoder waring: {ret}")
    return ret

def receiveFrameFromDecoder(channelId: int, decOutOptions: DecOutputOptions, timeout: int = 4000) -> Tuple[int, Optional[Frame]]:
    """
    Receive a frame from Decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    decOutOptions [in]: Decoder output options.\n
    timeout [in]: timeout value.\n
    """
    frame = _vame.frame()
    ret = _vame.receiveFrameFromDecoder(channelId, frame, decOutOptions, timeout)
    if ret >= _vame.vameER_RSLT_ERR_START:
         raise Exception(f"receiveFrameFromDecoder return error {ret}.")
    if ret == _vame.vameER_SUCCESS:
        return (ret, frame)
    return (ret, None)

def jpegSyncDecoder(channelId: int, imagePath: str, timeout: int = 4000) -> Frame:
    """
    Decode jpeg, sync api.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    imagePath [in]: The image path.\n
    """
    if not os.path.exists(imagePath):
        raise Exception(f"Can not find file: {imagePath}")
    frame = _vame.frame()
    ret = _vame.jpegSyncDecoder(channelId, imagePath, frame, timeout)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"jpegSyncDecoder return error {ret}.")
    return frame

def transferFrameFromDecoder(channelId: int, frame: Frame, crop: bool) -> Frame:
    """
    Tranfer frame data from device to host.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    frame [in]: Frame to transfer.\n
    crop [in]: Whether to crop.\n
    """
    ret = _vame.transferFrameFromDecoder(channelId, frame, crop)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"transferFrameFromDecoder return error {ret}.")
    return frame

@err_check
def decReleaseFrame(channelId: int, frame: Frame, timeout: int = 4000) -> int:
    """
    Receive a frame from Decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    frame [in]: Frame to release.\n
    timeout [in]: timeout value.\n
    """
    return _vame.decReleaseFrame(channelId, frame, timeout)

def getJpegInfo(imagePath: str) -> DecJpegInfo:
    """
    Get input jpeg information.\n
    ----------\n
    imagePath [in]: The image path.\n
    """
    jpegInfo = _vame.decJpegInfo()
    ret = _vame.getJpegInfo(imagePath, jpegInfo)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"getJpegInfo return error {ret}.")
    return jpegInfo

def getVideoInfo(stream: Stream, codecType: CODEC_TYPE) -> DecVideoInfo:
    """
    Get input video information.\n
    ----------\n
    stream [in]: Stream to parse.\n
    codecType [int]: codec type.\n
    """
    decVideoInfo = _vame.decVideoInfo()
    ret = _vame.getVideoInfo(stream, codecType, decVideoInfo)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"getVideoInfo return error {ret}.")
    return decVideoInfo

def getStreamInfoFromDecoder(channelId: int) -> DecStreamInfo:
    """
    Get the Stream information by Decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    decStreamInfo = _vame.decStreamInfo()
    ret = _vame.getStreamInfoFromDecoder(channelId, decStreamInfo)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"getStreamInfoFromDecoder return error {ret}.")
    return decStreamInfo

def getDecoderStatus(channelId: int) -> DecStatus:
    """
    Get the Decoder status information.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    decStatus = _vame.decStatus()
    ret = _vame.getDecoderStatus(channelId, decStatus)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"getDecoderStatus return error {ret}.")
    return decStatus

def jpegDecGetCaps() -> JpegDecCapability:
    """
    Get the ability of the jpeg decoder on the device.
    """
    jpegDecCapability = _vame.jpegDecCapability()
    ret = _vame.jpegDecGetCaps(jpegDecCapability)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"jpegDecGetCaps return error {ret}.")
    return jpegDecCapability

def videoDecGetCaps(codec: CODEC_TYPE) -> VideoDecCapability:
    """
    Get the ability of the video decoder on the device.\n
    ----------\n
    codec [in]: codec type.\n
    """
    videoDecCapability = _vame.videoDecCapability()
    ret = _vame.videoDecGetCaps(codec, videoDecCapability)
    if ret != _vame.vameER_SUCCESS:
        raise Exception(f"videoDecGetCaps return error {ret}.")
    return videoDecCapability

def getDecoderAvailableChannels() -> int:
    """
    Get the Decoder available channels.
    """
    return _vame.getDecoderAvailableChannels()

class Decoder():
    """
    Decoder tool class.
    """
    def __init__(self, channelId: int, params: DecChannelParamters, auto_start: bool = False, auto_init: bool = True) -> None:
        """
        Decoder tool class.\n
        ----------\n
        channelId [in]: Decoder channel index.\n
        param [in]: The init parameter for create decoder channel.\n
        auto_start [in]: Whether to start and end channel automatically.\n
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
        Create the decoder.
        """
        if not self._instance:
            if self.auto_init: systemInitialize()
            createDecoderChannel(self.channelId, self.params)
            self._instance = True
            if self.auto_start: startDecoder(self.channelId)
    
    def destory(self) -> None:
        """
        Destory the decoder.
        """
        assert self._instance, "Please create decoder."
        if self.auto_start: stopDecoder(self.channelId)
        destoryDecoderChannel(self.channelId)
        self._instance = False
        if self.auto_init: systemUninitialize()
    
    def start(self):
        """
        Start the decoder.
        """
        assert self._instance, "Please create decoder."
        return startDecoder(self.channelId)
    
    def stop(self):
        """
        Stop the decoder.
        """
        assert self._instance, "Please create decoder."
        return stopDecoder(self.channelId)
    
    def reset(self):
        """
        Reset the decoder.
        """
        assert self._instance, "Please create decoder."
        return resetDecoder(self.channelId)
    
    def sendStream(self, stream: Stream, timeout: int = 4000) -> int:
        """
        Send a stream to decoder to decode.\n
        ----------\n
        stream [in]: Stream data for decoder.\n
        timeout [in]: timeout value.\n
        """
        assert self._instance, "Please create decoder."
        return sendStreamToDecoder(self.channelId, stream, timeout)
    
    def receiveFrame(self, decOutOptions: DecOutputOptions, timeout: int = 4000) -> Tuple[int, Optional[Frame]]:
        """
        Receive a frame from Decoder.\n
        ----------\n
        decOutOptions [in]: Decoder output options.\n
        timeout [in]: timeout value.\n
        """
        assert self._instance, "Please create decoder."
        return receiveFrameFromDecoder(self.channelId, decOutOptions, timeout)
    
    def jpegSync(self, imagePath: str) -> Frame:
        """
        Decode jpeg, sync api.\n
        ----------\n
        imagePath [in]: The image path.\n
        """
        assert self._instance, "Please create decoder."
        return jpegSyncDecoder(self.channelId, imagePath)
    
    def transferFrame(self, frame: Frame, crop: bool) -> Frame:
        """
        Tranfer frame data from device to host.\n
        ----------\n
        frame [in]: Frame to transfer.\n
        crop [in]: Whether to crop.\n
        """
        assert self._instance, "Please create decoder."
        return transferFrameFromDecoder(self.channelId, frame, crop)
    
    def releaseFrame(self, frame: Frame, timeout: int = 4000) -> int:
        """
        Receive a frame from Decoder.\n
        ----------\n
        frame [in]: Frame to release.\n
        timeout [in]: timeout value.\n
        """
        assert self._instance, "Please create decoder."
        return decReleaseFrame(self.channelId, frame, timeout)
    
    def getStreamInfo(self) -> DecStreamInfo:
        """
        Get the Stream information by Decoder.\n
        """
        assert self._instance, "Please create decoder."
        return getStreamInfoFromDecoder(self.channelId)
    
    def getStatus(self) -> DecStatus:
        """
        Get the Decoder status information.\n
        """
        assert self._instance, "Please create decoder."
        return getDecoderStatus(self.channelId)


class H264Reader():
    """
    H264/HEVC Reader tool class.
    """
    def __init__(self, filePath: str):
        """
        H264/HEVC Reader tool class.\n
        ----------\n
        filePath [in]: H264/HEVC file path.\n
        """
        if not os.path.exists(filePath):
            raise Exception(f"Can not find H264/HEVC file {filePath}.")
        self.filePath = filePath
        self._h264Reader = None
        self.cnt = 0
    
    def __enter__(self):
        self.init()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
    
    def init(self) -> None:
        """
        Init the reader.
        """
        if self._h264Reader is None:
            self._h264Reader = _vame.H264Reader(self.filePath)
            self._h264Reader.init()
        
    def release(self) -> None:
        """
        Release the reader.
        """
        assert self._h264Reader is not None, "please init the reader."
        self._h264Reader.release()
        self._h264Reader = None

    def readStream(self) -> Optional[Stream]:
        """
        Read one NALU data from H264/HEVC file.
        """
        assert self._h264Reader is not None, "please init the reader."
        stream = _vame.stream()
        ret = self._h264Reader.getStream(stream)
        if ret == 0:
            return None
        self.cnt += 1
        stream.pts = self.cnt
        return stream