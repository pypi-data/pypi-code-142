# Copyright 2022 quinn.7@foxmail.com All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
[ 接口常量 ]

"""


# --------------------------------------------------------------------------
class StateCode:
    """ 
    [ 接口状态标识码常量 ]

    ---
    描述
    - 定义 WebApi 接口返回的接口错误状态标识。

    """
    Success = 0
    """ 请求成功 """

    Error   = -1
    """ 请求异常 """

    Warning = -2
    """ 服务器异常 """


# --------------------------------------------------------------------------
class StateMessage:
    """
    [ 接口状态提示语常量 ]

    """
    Success = 'success'
    """ 请求成功 """

    Error   = 'error'
    """ 请求异常 """

    Warning = 'warning'
    """ 服务器异常 """
