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
通用字段关键字
    
"""


# --------------------------------------------------------------------------
class Config:
    """
    [ 配置关键字 ]
        
    """
    Debug = 'debug'
    """ 调试模式 """

    IsWriteDatabase = 'is_write_database'
    """ 是否写入数据库 """

    EngineQueueMaxCount = 'engine_queue_max_count'
    """ 引擎队列最大数量 """

    TaskQueueMaxCount = 'task_queue_max_count'
    """ 任务队列最大数量 """

    CpuPropertyTime = 'cpu_property_time'
    """ CPU资源检索时隔 """

    CpuPropertyCeiling = 'cpu_property_ceiling'
    """ CPU资源检索阈值 """


# --------------------------------------------------------------------------
class TransactionFieldKey:
    """
    [ 事务处理字段名关键字 ]

    """
    Result = 'result'
    """ 结果 """

    Items = 'items'
    """ 项目 """

    Data = 'data'
    """ 数据 """

    Totai = 'total'
    """ 合计 """

    Count = 'count'
    """ 数量 """


# --------------------------------------------------------------------------
class PagingDataFieldKey:
    """
    [ 分页数据字段名关键字 ]

    """
    Page = 'page'
    """ 页数 """

    Number = 'number'
    """ 数据量 """
