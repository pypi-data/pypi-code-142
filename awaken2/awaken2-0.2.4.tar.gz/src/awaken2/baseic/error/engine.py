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
引擎模块相关异常

"""
from .baseic import AwakenBaseError


# --------------------------------------------------------------------------
class AwakenWebEngineError(AwakenBaseError):
    """ [ WEB引擎异常 ] """


# --------------------------------------------------------------------------
class AwakenTaskPretreatmentError(AwakenBaseError):
    """ [ 任务预处理异常 ] """
