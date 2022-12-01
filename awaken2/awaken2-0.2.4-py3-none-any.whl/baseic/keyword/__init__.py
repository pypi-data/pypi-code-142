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
关键字索引

"""
from . import keyword_api
from . import keyword_common
from . import keyword_database
from . import keyword_script
from . import keyword_sqlite


# --------------------------------------------------------------------------
class AwakenKeyword:
    """
    [ 关键字索引 ]

    """


    # ----------------------------------------------------------------------
    @property
    def Api(self) -> keyword_api:
        """
        [ 接口关键字 ]

        """
        return keyword_api


    # ----------------------------------------------------------------------
    @property
    def Common(self) -> keyword_common:
        """
        [ 通用关键字 ]

        """
        return keyword_common


    # ----------------------------------------------------------------------
    @property
    def DataBase(self) -> keyword_database:
        """
        [ 数据库关键字 ]

        """
        return keyword_database


    # ----------------------------------------------------------------------
    @property
    def Script(self) -> keyword_script:
        """
        [ 脚本关键字 ]

        """
        return keyword_script


    # ----------------------------------------------------------------------
    @property
    def Sqlite(self) -> keyword_sqlite:
        """
        [ SQLite 语句关键字 ]

        """
        return keyword_sqlite


# --------------------------------------------------------------------------
G_KEYWORD: AwakenKeyword  = AwakenKeyword()
""" 关键字索引全局实例 """
