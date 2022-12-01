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
SQLite 语句关键字
    
"""


# --------------------------------------------------------------------------
class Event:
    """
    [ SQLite 事件关键字 ]

    """
    CreateTable = 'CREATE TABLE'
    """ 建表事件 """


# --------------------------------------------------------------------------
class SelectEvent:
    """
    [ SQLite 查表事件相关 ]

    """
    Count = 'COUNT'
    """ 计算数量 """

    Sum   = 'SUM'
    """ 计算全额 """


# --------------------------------------------------------------------------
class SelectEvent:
    """
    [ SQLite 查表事件相关 ]

    """
    Count = 'COUNT'
    """ 计算数量 """

    Sum   = 'SUM'
    """ 计算全额 """

    Distinct = 'DISTINCT'
    """ 去重 """


# --------------------------------------------------------------------------
class SortType:
    """
    [ SQLite 排序类型 ]

    """
    Asc = 'ASC'
    """ 从小到大, 升序排列 """

    Desc = 'DESC'
    """ 从大到小, 降序排列 """


# --------------------------------------------------------------------------
class CreateTable:
    """
    [ SQLite 建表事件相关 ]

    """
    IfNotExists = 'IF NOT EXISTS'
    """ 建表时如果不存在则创建 """


# --------------------------------------------------------------------------
class DataType:
    """
    [ SQLite 数据类型相关 ]

    """
    IdKey = 'INTEGER PRIMARY KEY'
    """ 整数主键 """

    Int = 'INT'
    IntNotNull = 'INT NOT NULL'

    Text = 'TEXT'
    TextNotNull = 'TEXT NOT NULL'

    Date = 'DATE'
    DateNotNull = 'DATE NOT NULL'
