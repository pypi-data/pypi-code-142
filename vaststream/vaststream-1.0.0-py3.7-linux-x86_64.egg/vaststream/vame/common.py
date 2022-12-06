"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8

__all__ = [
    "CODEC_TYPE", "SOURCE_MODE", "MEMORY_TYPE", "PIXEL_FORMAT", "STATE",
    "VIDEO_FIELD", "FRAME_TYPE", "CHROMA_FORMAT", "JPEG_CODING_MODE", "VIDEO_PROFILE",
    "VIDEO_LEVEL", "Stream", "CropInfo", "Frame", "HardwareID",
    "Rational", "systemInitialize", "systemUninitialize", "getVersion", "ER_RSLT_WARN_MORE_DATA", "ER_RSLT_WARN_EOS"
]

from _vaststream_pybind11 import vame as _vame
import numpy as np
from .utils import *
from typing import List, Any

# =========================== ENUM =============================


class CODEC_TYPE():
    """
    vame codec type.\n
    ----------\n
    @enum DEC_JPEG\n
    @enum DEC_H264\n
    @enum DEC_HEVC\n
    @enum ENC_JPEG\n
    @enum ENC_H264\n
    @enum ENC_HEVC\n
    """
    DEC_JPEG: int = _vame.codecType.VAME_CODEC_DEC_JPEG
    DEC_H264: int = _vame.codecType.VAME_CODEC_DEC_H264
    DEC_HEVC: int = _vame.codecType.VAME_CODEC_DEC_HEVC
    ENC_JPEG: int = _vame.codecType.VAME_CODEC_ENC_JPEG
    ENC_H264: int = _vame.codecType.VAME_CODEC_ENC_H264
    ENC_HEVC: int = _vame.codecType.VAME_CODEC_ENC_HEVC


class SOURCE_MODE():
    """
    vame source mode.\n
    ----------\n
    @enum SRC_FRAME\n
    """
    SRC_FRAME: int = _vame.sourceMode.VAME_SRC_FRAME


class MEMORY_TYPE():
    """
    vame memory type.\n
    ----------\n
    @enum DEVICE\n
    @enum HOST\n
    @enum FLUSH\n
    """
    DEVICE: int = _vame.memoryType.VAME_MEM_DEVICE
    HOST: int = _vame.memoryType.VAME_MEM_HOST
    FLUSH: int = _vame.memoryType.VAME_MEM_FLUSH


class PIXEL_FORMAT():
    """
    vame pixel format
    ----------\n
    @enum NONE\n
    @enum YUV420P\n
    @enum YUV444P\n
    @enum YUV422P\n
    @enum YUV420P9\n
    @enum YUV422P9\n
    @enum YUV444P9\n
    @enum YUV420P10\n
    @enum YUV422P10\n
    @enum YUV444P10\n
    @enum YUV420P12\n
    @enum YUV422P12\n
    @enum YUV444P12\n
    @enum NV12\n
    @enum NV21\n
    @enum GRAY8\n
    @enum GRAY9\n
    @enum GRAY10\n
    @enum GRAY12\n
    @enum RGB24\n
    @enum BGR24\n
    @enum ARGB\n
    @enum RGBA\n
    @enum ABGR\n
    @enum BGRA\n
    """
    NONE: int = _vame.pixelFormat.VAME_PIX_FMT_NONE
    YUV420P: int = _vame.pixelFormat.VAME_PIX_FMT_YUV420P
    YUV444P: int = _vame.pixelFormat.VAME_PIX_FMT_YUV444P
    YUV422P: int = _vame.pixelFormat.VAME_PIX_FMT_YUV422P
    YUV420P9: int = _vame.pixelFormat.VAME_PIX_FMT_YUV420P9
    YUV422P9: int = _vame.pixelFormat.VAME_PIX_FMT_YUV422P9
    YUV444P9: int = _vame.pixelFormat.VAME_PIX_FMT_YUV444P9
    YUV420P10: int = _vame.pixelFormat.VAME_PIX_FMT_YUV420P10
    YUV422P10: int = _vame.pixelFormat.VAME_PIX_FMT_YUV422P10
    YUV444P10: int = _vame.pixelFormat.VAME_PIX_FMT_YUV444P10
    YUV420P12: int = _vame.pixelFormat.VAME_PIX_FMT_YUV420P12
    YUV422P12: int = _vame.pixelFormat.VAME_PIX_FMT_YUV422P12
    YUV444P12: int = _vame.pixelFormat.VAME_PIX_FMT_YUV444P12
    NV12: int = _vame.pixelFormat.VAME_PIX_FMT_NV12
    NV21: int = _vame.pixelFormat.VAME_PIX_FMT_NV21
    GRAY8: int = _vame.pixelFormat.VAME_PIX_FMT_GRAY8
    GRAY9: int = _vame.pixelFormat.VAME_PIX_FMT_GRAY9
    GRAY10: int = _vame.pixelFormat.VAME_PIX_FMT_GRAY10
    GRAY12: int = _vame.pixelFormat.VAME_PIX_FMT_GRAY12
    RGB24: int = _vame.pixelFormat.VAME_PIX_FMT_RGB24
    BGR24: int = _vame.pixelFormat.VAME_PIX_FMT_BGR24
    ARGB: int = _vame.pixelFormat.VAME_PIX_FMT_ARGB
    RGBA: int = _vame.pixelFormat.VAME_PIX_FMT_RGBA
    ABGR: int = _vame.pixelFormat.VAME_PIX_FMT_ABGR
    BGRA: int = _vame.pixelFormat.VAME_PIX_FMT_BGRA


class STATE():
    """
    vame state.\n
    ----------\n
    @enum NONE\n
    @enum READY\n
    @enum RUNNING\n
    @enum ERROR\n
    @enum STOPPING\n
    @enum STOPPED\n
    """
    ST_NONE: int = _vame.state.VAME_ST_NONE
    ST_READY: int = _vame.state.VAME_ST_READY
    ST_RUNNING: int = _vame.state.VAME_ST_RUNNING
    ST_ERROR: int = _vame.state.VAME_ST_ERROR
    ST_STOPPING: int = _vame.state.VAME_ST_STOPPING
    ST_STOPPED: int = _vame.state.VAME_ST_STOPPED


class VIDEO_FIELD():
    """
    vame video field.\n
    ----------\n
    @enum FLD_FRAME\n
    """
    FLD_FRAME: int = _vame.videoField.VAME_FLD_FRAME


class FRAME_TYPE():
    """
    vame frame type.\n
    ----------\n
    @enum I\n
    @enum P\n
    @enum B\n
    """
    I: int = _vame.frameType.VAME_FRM_I
    P: int = _vame.frameType.VAME_FRM_P
    B: int = _vame.frameType.VAME_FRM_B


class CHROMA_FORMAT():
    """
    vame chroma format.\n
    ----------\n
    @enum FMT_NONE\n
    @enum FMT_400\n
    @enum FMT_411\n
    @enum FMT_420\n
    @enum FMT_422\n
    @enum FMT_440\n
    @enum FMT_444\n
    """
    FMT_NONE: int = _vame.chromaFormat.VAME_CHROMA_FMT_NONE
    FMT_400: int = _vame.chromaFormat.VAME_CHROMA_FMT_400
    FMT_411: int = _vame.chromaFormat.VAME_CHROMA_FMT_411
    FMT_420: int = _vame.chromaFormat.VAME_CHROMA_FMT_420
    FMT_422: int = _vame.chromaFormat.VAME_CHROMA_FMT_422
    FMT_440: int = _vame.chromaFormat.VAME_CHROMA_FMT_440
    FMT_444: int = _vame.chromaFormat.VAME_CHROMA_FMT_444


class JPEG_CODING_MODE():
    """
    vame jpeg coding mode.\n
    ----------\n
    @enum NONE\n
    @enum BASELINE\n
    @enum PROGRESSIVE\n
    @enum NONINTERLEAVED\n
    """
    NONE: int = _vame.jpegCodingMode.VAME_JPEG_NONE
    BASELINE: int = _vame.jpegCodingMode.VAME_JPEG_BASELINE
    PROGRESSIVE: int = _vame.jpegCodingMode.VAME_JPEG_PROGRESSIVE
    NONINTERLEAVED: int = _vame.jpegCodingMode.VAME_JPEG_NONINTERLEAVED


class VIDEO_PROFILE():
    """
    vame video profile.\n
    ----------\n
    @enum HEVC_MAIN_STILL_PICTURE\n
    @enum HEVC_MAIN\n
    @enum HEVC_MAIN_10\n
    @enum HEVC_MAIN_REXT\n
    @enum H264_BASELINE\n
    @enum H264_MAIN\n
    @enum H264_HIGH\n
    @enum H264_HIGH_10\n
    @enum AV1_MAIN\n
    @enum AV1_HIGH\n
    @enum AV1_PROFESSIONAL\n
    """
    HEVC_MAIN_STILL_PICTURE: int = _vame.videoProfile.VAME_VIDEO_PRFL_HEVC_MAIN_STILL_PICTURE
    HEVC_MAIN: int = _vame.videoProfile.VAME_VIDEO_PRFL_HEVC_MAIN
    HEVC_MAIN_10: int = _vame.videoProfile.VAME_VIDEO_PRFL_HEVC_MAIN_10
    HEVC_MAIN_REXT: int = _vame.videoProfile.VAME_VIDEO_PRFL_HEVC_MAIN_REXT
    H264_BASELINE: int = _vame.videoProfile.VAME_VIDEO_PRFL_H264_BASELINE
    H264_MAIN: int = _vame.videoProfile.VAME_VIDEO_PRFL_H264_MAIN
    H264_HIGH: int = _vame.videoProfile.VAME_VIDEO_PRFL_H264_HIGH
    H264_HIGH_10: int = _vame.videoProfile.VAME_VIDEO_PRFL_H264_HIGH_10
    AV1_MAIN: int = _vame.videoProfile.VAME_VIDEO_PRFL_AV1_MAIN
    AV1_HIGH: int = _vame.videoProfile.VAME_VIDEO_PRFL_AV1_HIGH
    AV1_PROFESSIONAL: int = _vame.videoProfile.VAME_VIDEO_PRFL_AV1_PROFESSIONAL


class VIDEO_LEVEL():
    """
    vame video level.\n
    ----------\n
    @enum HEVC_1\n
    @enum HEVC_2\n
    @enum HEVC_2_1\n
    @enum HEVC_3\n
    @enum HEVC_3_1\n
    @enum HEVC_4\n
    @enum HEVC_4_1\n
    @enum HEVC_5\n
    @enum HEVC_5_1\n
    @enum HEVC_5_2\n
    @enum HEVC_6\n
    @enum HEVC_6_1\n
    @enum HEVC_6_2\n
    @enum H264_1\n
    @enum H264_1_b\n
    @enum H264_1_1\n
    @enum H264_1_2\n
    @enum H264_1_3\n
    @enum H264_2\n
    @enum H264_2_1\n
    @enum H264_2_2\n
    @enum H264_3\n
    @enum H264_3_1\n
    @enum H264_3_2\n
    @enum H264_4\n
    @enum H264_4_1\n
    @enum H264_4_2\n
    @enum H264_5\n
    @enum H264_5_1\n
    @enum H264_5_2\n
    @enum H264_6\n
    @enum H264_6_1\n
    @enum H264_6_2\n
    """
    HEVC_1: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_1
    HEVC_2: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_2
    HEVC_2_1: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_2_1
    HEVC_3: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_3
    HEVC_3_1: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_3_1
    HEVC_4: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_4
    HEVC_4_1: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_4_1
    HEVC_5: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_5
    HEVC_5_1: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_5_1
    HEVC_5_2: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_5_2
    HEVC_6: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_6
    HEVC_6_1: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_6_1
    HEVC_6_2: int = _vame.videoLevel.VAME_VIDEO_LVL_HEVC_6_2
    H264_1: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_1
    H264_1_b: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_1_b
    H264_1_1: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_1_1
    H264_1_2: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_1_2
    H264_1_3: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_1_3
    H264_2: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_2
    H264_2_1: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_2_1
    H264_2_2: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_2_2
    H264_3: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_3
    H264_3_1: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_3_1
    H264_3_2: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_3_2
    H264_4: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_4
    H264_4_1: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_4_1
    H264_4_2: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_4_2
    H264_5: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_5
    H264_5_1: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_5_1
    H264_5_2: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_5_2
    H264_6: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_6
    H264_6_1: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_6_1
    H264_6_2: int = _vame.videoLevel.VAME_VIDEO_LVL_H264_6_2

# =========================== STRUCT =============================


class Stream(_vame.stream):
    """
    Video Stream.
    """
    stream: np.ndarray
    pts: int
    inputBusAddress: int


class CropInfo(_vame.cropInfo):
    """
    Crop infomation in Frame.
    """
    flag: int
    width: int
    height: int
    xOffset: int
    yOffset: int


class Frame(_vame.frame):
    """
    Video Frame.
    """
    data: np.ndarray
    busAddress: List[int]
    stride: List[int]
    dataSize: int
    width: int
    height: int
    pts: int
    memoryType: MEMORY_TYPE
    field: VIDEO_FIELD
    pixelFormat: PIXEL_FORMAT
    frameType: FRAME_TYPE
    cropInfo: CropInfo


# class Version(_vame.version):
#     major: int
#     minor: int
#     build: int
ER_RSLT_WARN_MORE_DATA = _vame.vameER_RSLT_WARN_MORE_DATA
ER_RSLT_WARN_EOS = _vame.vameER_RSLT_WARN_EOS


class HardwareID(_vame.hardwareID):
    """
    Hardware ID.
    """
    dieID: int
    coreID: int


class Rational(_vame.rational):
    """
    FPS Rational.
    """
    numerator: int
    denominator: int

# =========================== API =============================


@err_check
def systemInitialize() -> int:
    """
    Initialize the vame system.\n
    """
    return _vame.systemInitialize()


@err_check
def systemUninitialize() -> int:
    """
    Uninitialize the vame system.\n
    """
    return _vame.systemUninitialize()


def getVersion() -> str:
    """
    Get the VAME API version information.\n
    """
    return _vame.getVersion()
