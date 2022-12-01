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
[ 常量索引 ]

"""
from . import const_api
from . import const_common
from . import const_interpreter
from . import const_name
from . import const_path
from . import const_state
from . import const_type


# --------------------------------------------------------------------------
class AwakenConst:
    """ 
    [ 常量索引 ]

    """


    # ----------------------------------------------------------------------
    @property
    def Api(self) -> const_api:
        """ 
        [ 接口常量 ]

        """
        return const_api


    # ----------------------------------------------------------------------
    @property
    def Common(self) -> const_common:
        """ 
        [ 通用常量 ]

        """
        return const_common


    # ----------------------------------------------------------------------
    @property
    def Interpreter(self) -> const_interpreter:
        """ 
        [ 解释器常量 ]

        """
        return const_interpreter


    # ----------------------------------------------------------------------
    @property
    def Name(self) -> const_name:
        """ 
        [ 名称常量 ]

        """
        return const_name


    # ----------------------------------------------------------------------
    @property
    def Path(self) -> const_path:
        """ 
        [ 路径常量 ]

        """
        return const_path


    # ----------------------------------------------------------------------
    @property
    def State(self) -> const_state:
        """ 
        [ 状态常量 ]

        """
        return const_state


    # ----------------------------------------------------------------------
    @property
    def Type(self) -> const_type:
        """ 
        [ 类型常量 ]

        """
        return const_type


# --------------------------------------------------------------------------
G_CONST: AwakenConst  = AwakenConst()
""" 常量索引全局实例 """
