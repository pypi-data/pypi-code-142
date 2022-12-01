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
[ SQL蓝图 - 用例记录相关 ]

"""
from typing import Any

from ..sqlite_statement_handle import G_SQLITE_STATEMENT_HANDLE
from ....baseic.const import G_CONST
from ....baseic.keyword import G_KEYWORD


# --------------------------------------------------------------------------
class SqlCaseRecord(object):
    """
    [ SQL蓝图 - 用例记录相关 ]

    """


    # ----------------------------------------------------------------------
    @staticmethod
    def get_count(paras: dict = {}) -> Any:
        """
        [ 查询用例编号数量 ]

        ---
        可选参数
        - crid          : { str } - 用例记录编号。
        - trid          : { str } - 任务记录编号。
        - name          : { str } - 用例记录名称。
        - type          : { str } - 用例记录类型。
        - created_date  : { str } - 用例记录创建日期, 例如 2022-02-02。
        - state         : { str } - 用例记录状态。
        - start_time    : { str } - 用例记录开始时间。
        - end_time      : { str } - 用例记录结束时间。

        """
        selecter = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.CaseRecord)
        selecter.get(G_KEYWORD.DataBase.CaseRecordFieldKey.CRid, G_KEYWORD.Sqlite.SelectEvent.Count)
        selecter.filter_equal_batch(paras)
        return selecter


    # ----------------------------------------------------------------------
    @staticmethod
    def get_list(paras: dict = {}) -> Any:
        """
        [ 查询用例记录列表 ]

        ---
        可选参数
        - crid         : { str } - 用例记录编号。
        - trid         : { str } - 任务记录编号。
        - name         : { str } - 用例记录名称。
        - type         : { str } - 用例记录类型。
        - created_date : { str } - 用例记录创建日期, 例如 2022-02-02。
        - state        : { str } - 用例记录状态。
        - start_time   : { str } - 用例记录开始时间。
        - end_time     : { str } - 用例记录结束时间。
        - page         : { str } - 当前页数。
        - number       : { str } - 单页数据量。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.CaseRecord)
        sql_handler.filter_equal_batch(paras)
        sql_handler.set_sort_desc(G_KEYWORD.DataBase.CaseRecordFieldKey.CRid)
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
        - crid          : { str } - 用例记录编号。
        - trid          : { str } - 任务记录编号。
        - name          : { str } - 用例记录名称。
        - type          : { str } - 用例记录类型。
        - created_date  : { str } - 用例记录创建日期, 例如 2022-02-02。
        - result        : { str } - 用例记录结果。
        - start_time    : { str } - 用例记录开始时间。
        - end_time      : { str } - 用例记录结束时间。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.CaseRecord)
        sql_handler.get(G_KEYWORD.DataBase.CaseRecordFieldKey.SpendTime, G_KEYWORD.Sqlite.SelectEvent.Sum)
        sql_handler.filter_equal_batch(paras)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def creation(
        trid: int,
        name: str,
        docs: str,
        type: str,
        created_date: str,
        start_time: str,
        state: str = G_CONST.State.Result.Null
    ) -> Any:
        """
        [ 创建用例记录 ]

        ---
        参数
        - trid         : { str } - 任务记录编号。
        - name         : { str } - 用例记录名称。
        - docs         : { str } - 用例记录说明。
        - type         : { str } - 用例记录类型。
        - created_date : { str } - 用例记录创建日期, 例如 2022-02-02。
        - start_time   : { str } - 用例记录开始时间。
        - state        : { str } - 用例记录状态。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.insert(G_KEYWORD.DataBase.TableName.CaseRecord)
        sql_handler.deduction([
            'NULL', trid, name, docs, type, created_date, state, start_time, 
            'NULL', 'NULL', 'NULL'
        ])
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def update(
        crid: int,
        state: str,
        end_time: str,
        spend_time: int,
        process: str
    ) -> Any:
        """
        [ 更新用例记录 ]

        ---
        参数
        - crid       : { int } - 用例记录编号。
        - state      : { str } - 用例记录状态。
        - end_time   : { str } - 用例记录结束时间。
        - spend_time : { int } - 用例记录消耗时间。
        - process    : { str } - 用例记录过程。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.update(G_KEYWORD.DataBase.TableName.CaseRecord)
        sql_handler.push(G_KEYWORD.DataBase.CaseRecordFieldKey.State, state)
        sql_handler.push(G_KEYWORD.DataBase.CaseRecordFieldKey.EndTime, end_time)
        sql_handler.push(G_KEYWORD.DataBase.CaseRecordFieldKey.SpendTime, spend_time)
        sql_handler.push(G_KEYWORD.DataBase.CaseRecordFieldKey.Process, process)
        sql_handler.filter_equal(G_KEYWORD.DataBase.CaseRecordFieldKey.CRid, crid)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def delete(paras: dict = {}) -> Any:
        """
        [ 删除用例记录 ]
        
        ---
        可选参数
        - trid         : { str } - 任务记录编号。
        - name         : { str } - 用例记录名称。
        - type         : { str } - 用例记录类型。
        - created_date : { str } - 用例记录创建日期, 例如 2022-02-02。
        - start_time   : { str } - 用例记录开始时间。
        - state        : { str } - 用例记录状态。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.delete(G_KEYWORD.DataBase.TableName.CaseRecord)
        sql_handler.filter_equal_batch(paras)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def delete_all() -> Any:
        """
        [ 删除全部项目 ]

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.delete(G_KEYWORD.DataBase.TableName.CaseRecord)
        return sql_handler
