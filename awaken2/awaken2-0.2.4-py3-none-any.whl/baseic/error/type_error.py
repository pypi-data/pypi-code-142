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
类型相关异常

"""
from .baseic import AwakenBaseError


# --------------------------------------------------------------------------
class AwakenTypeDetectionFailedError(AwakenBaseError):
    """ [ 类型检测异常 ] """

    def __init__(
        self, 
        expect: str, 
        result: str,
    ):
        self.expect = expect
        self.result = result
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'期望类型:: {self.expect}, 意外得到:: {self.result} !'
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenBrowserDriverNotSupportError(AwakenBaseError):
    """ [ 浏览器驱动不支持 ] """
