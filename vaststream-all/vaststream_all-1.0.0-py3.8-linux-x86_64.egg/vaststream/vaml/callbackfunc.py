# """
# Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
# The information contained herein is confidential property of the company.
# The user, copying, transfer or disclosure of such information is prohibited
# except by express written agreement with VASTAI Technologies Co., Ltd.
# """
# # coding: utf-8

# __all__ = ["registerErrorCallBack", "unRegisterErrorCallBack"]

# from _vaststream_pybind11 import vaml
# from typing import Any
# from .utils import *
# from .card import *

# # =========================== API =============================
# def registerErrorCallBack(errorCallbackPy:Any, userData:str) -> int:
#     """
#     register error call back function.\n
#     errorCallbackPy [in]: The callback function of type vamlRegisterErrorCallBack.\n
#     userData [in]: The user defined data to be passed into the callback function.\n
#     """
#     return vaml.registerErrorCallBack(errorCallbackPy, userData)

# @err_check
# def unRegisterErrorCallBack() -> int:
#     """
#     unregister error call back function.\n
#     """
#     return vaml.unRegisterErrorCallBack()