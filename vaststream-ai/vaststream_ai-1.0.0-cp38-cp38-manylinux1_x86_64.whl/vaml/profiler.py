# """
# Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
# The information contained herein is confidential property of the company.
# The user, copying, transfer or disclosure of such information is prohibited
# except by express written agreement with VASTAI Technologies Co., Ltd.
# """
# # coding: utf-8

# __all__ = [
#     "PROF_EXPORT_FILE_TYPE", "ProfConfig", "profStart", "profStop"
# ]

# from _vaststream_pybind11 import vaml as _vaml
# from .utils import *

# # =========================== ENUM ============================
# class PROF_EXPORT_FILE_TYPE():
#     """
#     Profiler Export File Type.\n
#     ----------\n
#     @enum CSV_TYPE.\n
#     @enum TRACEVIEW_TYPE.\n
#     @enum BOTH_CSV_AND_TRACEVIEW_TYPE.\n
#     @enum UNSPECIFIED_TYPE.\n
#     """
#     CSV_TYPE: int = _vaml.profExportFileType.CSV_TYPE
#     TRACEVIEW_TYPE: int = _vaml.profExportFileType.TRACEVIEW_TYPE
#     BOTH_CSV_AND_TRACEVIEW_TYPE: int = _vaml.profExportFileType.BOTH_CSV_AND_TRACEVIEW_TYPE
#     UNSPECIFIED_TYPE: int = _vaml.profExportFileType.UNSPECIFIED_TYPE

# # =========================== STRUCT =============================
# class ProfConfig(_vaml.profConfig):
#     """
#     Profiler Config.\n
#     """
#     fileType: PROF_EXPORT_FILE_TYPE
#     retPath: str
#     exeCommand: str

# # =========================== API =============================
# @err_check
# def profStart(profConfig:ProfConfig) -> int:
#     """
#     start profiler and begin to monitor the profiler.\n
#     ----------\n
#     profConfig [in]: performance monitoring config.\n
#     """
#     return _vaml.profStart(profConfig)
    
# @err_check
# def profStop() -> int:
#     """
#     stop profiler.\n
#     """
#     return _vaml.profStop()