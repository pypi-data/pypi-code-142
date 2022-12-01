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
[ 单元测试装饰器 ]

"""
from ..broadcast.awaken_log import G_LOG


# --------------------------------------------------------------------------
def deco_test_capture_exception(cls):
    """ 
    [ 捕获运行异常装饰器 ]

    ---
    描述
    - 冠以该装饰器的函数在执行异常时返回断言, 用以单元测试。

    """
    def _deco_test_capture_exception(*args, **kwargs):
        try:
            cls(*args, **kwargs)
            assert True
        except BaseException as error:
            G_LOG.error(str(error))
            assert False
    return _deco_test_capture_exception
