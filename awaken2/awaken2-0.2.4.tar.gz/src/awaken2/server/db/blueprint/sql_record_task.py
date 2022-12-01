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
[ SQL蓝图 - 任务记录相关 ]

"""
from typing import Any

from ..sqlite_statement_handle import G_SQLITE_STATEMENT_HANDLE
from ....baseic.const import G_CONST
from ....baseic.keyword import G_KEYWORD


# --------------------------------------------------------------------------
class SqlTaskRecord(object):
    """
    [ SQL蓝图 - 任务记录相关 ]

    """


    # ----------------------------------------------------------------------
    @staticmethod
    def get_count(paras: dict = {}) -> Any:
        """
        [ 查询任务记录数量 ]

        ---
        可选参数
        - trid         : { str } - 任务记录编号。
        - tid          : { str } - 关联任务编号。
        - name         : { str } - 任务记录名称。
        - type         : { str } - 任务记录类型。
        - created_date : { str } - 任务记录创建日期, 例如 2022-02-02。
        - state        : { str } - 任务记录状态。
        - start_time   : { str } - 任务记录开始时间。
        - end_time     : { str } - 任务记录结束时间。

        """
        selecter = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.TaskRecord)
        selecter.get(G_KEYWORD.DataBase.TaskRecordFieldKey.TRid, G_KEYWORD.Sqlite.SelectEvent.Count)
        selecter.filter_equal_batch(paras)
        return selecter


    # ----------------------------------------------------------------------
    @staticmethod
    def get_list(paras: dict = {}) -> Any:
        """
        [ 查询任务记录列表 ]

        ---
        可选参数
        - trid         : { str } - 任务记录编号。
        - tid          : { str } - 关联任务编号。
        - name         : { str } - 任务记录名称。
        - type         : { str } - 任务记录类型。
        - created_date : { str } - 任务记录创建日期, 例如 2022-02-02。
        - state        : { str } - 任务记录状态。
        - start_time   : { str } - 任务记录开始时间。
        - end_time     : { str } - 任务记录结束时间。
        - page         : { str } - 当前页数。
        - number       : { str } - 单页数据量。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.TaskRecord)
        sql_handler.filter_equal_batch(paras)
        sql_handler.set_sort_desc(G_KEYWORD.DataBase.TaskRecordFieldKey.TRid)
        page   = paras.get(G_KEYWORD.Common.PagingDataFieldKey.Page)
        number = paras.get(G_KEYWORD.Common.PagingDataFieldKey.Number)
        sql_handler.set_data_limit(page, number)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def get_spend_time(paras: dict = {}) -> Any:
        """
        [ 查询任务记录的消耗时间 ]

        ---
        可选参数
        - trid         : { str } - 任务记录编号。
        - tid          : { str } - 关联任务编号。
        - name         : { str } - 任务记录名称。
        - type         : { str } - 任务记录类型。
        - created_date : { str } - 任务记录创建日期, 例如 2022-02-02。
        - state        : { str } - 任务记录状态。
        - start_time   : { str } - 任务记录开始时间。
        - end_time     : { str } - 任务记录结束时间。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.TaskRecord)
        sql_handler.get(G_KEYWORD.DataBase.TaskRecordFieldKey.SpendTime, G_KEYWORD.Sqlite.SelectEvent.Sum)
        sql_handler.filter_equal_batch(paras)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def creation(
        tid: int,
        name: str,
        docs: str,
        type: str,
        created_date: str,
        start_time: str,
        state: str = G_CONST.State.Result.Null
    ) -> Any:
        """
        [ 创建任务记录 ]

        ---
        参数
        - tid          : { str } - 关联任务编号。
        - name         : { str } - 任务记录名称。
        - docs         : { str } - 任务记录备注。
        - type         : { str } - 任务记录类型。
        - created_date : { str } - 任务记录创建日期, 例如 2022-02-02。
        - start_time   : { str } - 任务记录开始时间。
        - state        : { str } - 任务记录状态。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.insert(G_KEYWORD.DataBase.TableName.TaskRecord)
        sql_handler.deduction([
            'NULL', tid, name, docs, type, created_date, state, start_time, 
            'NULL', 'NULL', 'NULL'
        ])
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def update(
        trid: int,
        state: str,
        end_time: str,
        spend_time: int,
        process: str
    ) -> Any:
        """
        [ 更新任务记录 ]

        ---
        参数
        - trid       : { int } - 任务记录编号。
        - state      : { str } - 任务记录状态。
        - end_time   : { str } - 任务记录结束时间。
        - spend_time : { int } - 任务记录消耗时间。
        - process    : { str } - 任务记录过程。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.update(G_KEYWORD.DataBase.TableName.TaskRecord)
        sql_handler.push(G_KEYWORD.DataBase.TaskRecordFieldKey.State, state)
        sql_handler.push(G_KEYWORD.DataBase.TaskRecordFieldKey.EndTime, end_time)
        sql_handler.push(G_KEYWORD.DataBase.TaskRecordFieldKey.SpendTime, spend_time)
        sql_handler.push(G_KEYWORD.DataBase.TaskRecordFieldKey.Process, process)
        sql_handler.filter_equal(G_KEYWORD.DataBase.TaskRecordFieldKey.TRid, trid)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def delete(paras: dict = {}) -> Any:
        """
        [ 删除任务记录 ] 

        ---
        可选参数
        - tid          : { str } - 关联任务编号。
        - name         : { str } - 任务记录名称。
        - type         : { str } - 任务记录类型。
        - created_date : { str } - 任务记录创建日期, 例如 2022-02-02。
        - start_time   : { str } - 任务记录开始时间。
        - state        : { str } - 任务记录状态。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.delete(G_KEYWORD.DataBase.TableName.TaskRecord)
        sql_handler.filter_equal_batch(paras)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def delete_all() -> Any:
        """
        [ 删除全部项目 ]

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.delete(G_KEYWORD.DataBase.TableName.TaskRecord)
        return sql_handler
