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
[ WebApi装饰器 ]

"""
from ...server.api.server_request_handler import ServerRequestHandler


# --------------------------------------------------------------------------
def deco_webapi_error_capture(cls):
    """ 
    [ WebApi错误捕捉装饰器 ]

    ---
    描述
    - 冠以该装饰器的接口在请求异常时将返回错误请求响应。

    """
    def _deco_webapi_error_capture(*args, **kwargs):
        try:
            return cls(*args, **kwargs)
        except BaseException as error:
            return ServerRequestHandler.unsuccessful(str(error))
    return _deco_webapi_error_capture
