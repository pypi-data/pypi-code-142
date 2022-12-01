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
[ SQL蓝图 - 项目相关 ]

"""
from typing import Any

from ..sqlite_statement_handle import G_SQLITE_STATEMENT_HANDLE
from ....baseic.keyword import G_KEYWORD


# --------------------------------------------------------------------------
class SqlProject:
    """
    [ SQL蓝图 - 项目相关 ]

    """


    # ----------------------------------------------------------------------
    @staticmethod
    def get_count(paras: dict = {}) -> str:
        """
        [ 查询项目数量 ]

        ---
        可选参数:
        - pid          : { str } - 项目ID。
        - type         : { str } - 项目类型。
        - state        : { str } - 项目状态。
        - created_date : { str } - 项目创建日期, 例如 2022-02-02。

        """
        selecter = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.Project)
        selecter.get(G_KEYWORD.DataBase.ProjectFieldKey.Pid, G_KEYWORD.Sqlite.SelectEvent.Count)
        selecter.filter_equal_batch(paras)
        return selecter


    # ----------------------------------------------------------------------
    @staticmethod
    def get_list(paras: dict = {}) -> Any:
        """
        [ 查询项目列表 ]

        ---
        可选参数:
        - pid          : { str } - 项目ID。
        - type         : { str } - 项目类型。
        - state        : { str } - 项目状态。
        - created_date : { str } - 项目创建日期, 例如 2022-02-02。
        - page         : { str } - 当前页数。
        - number       : { str } - 单页数据量。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.Project)
        sql_handler.filter_equal_batch(paras)
        sql_handler.set_sort_desc(G_KEYWORD.DataBase.ProjectFieldKey.Pid)
        page   = paras.get(G_KEYWORD.Common.PagingDataFieldKey.Page)
        number = paras.get(G_KEYWORD.Common.PagingDataFieldKey.Number)
        sql_handler.set_data_limit(page, number)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def creation(
        type: str,
        name: str,
        docs: str,
        state: str,
        created_date: str,
    ) -> Any:
        """
        [ 项目创建 ]

        ---
        参数:
        - type         : { str } - 项目类型。
        - name         : { str } - 项目名称。
        - docs         : { str } - 项目说明。
        - state        : { str } - 项目状态。
        - created_date : { str } - 项目创建日期, 例如 2022-02-02。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.insert(G_KEYWORD.DataBase.TableName.Project)
        sql_handler.push(G_KEYWORD.DataBase.ProjectFieldKey.Pid, 'NULL')
        sql_handler.push(G_KEYWORD.DataBase.ProjectFieldKey.Type, type)
        sql_handler.push(G_KEYWORD.DataBase.ProjectFieldKey.Name, name)
        sql_handler.push(G_KEYWORD.DataBase.ProjectFieldKey.Docs, docs)
        sql_handler.push(G_KEYWORD.DataBase.ProjectFieldKey.State, state)
        sql_handler.push(G_KEYWORD.DataBase.ProjectFieldKey.CreatedDate, created_date)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def modify(
        pid: int,
        name: str,
        docs: str,
    ) -> Any:
        """
        [ 项目编辑 ]

        ---
        参数
        - pid  : { int } - 项目ID。
        - name : { str } - 项目名称。
        - docs : { str } - 项目说明。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.update(G_KEYWORD.DataBase.TableName.Project)
        sql_handler.push(G_KEYWORD.DataBase.ProjectFieldKey.Name, name)
        sql_handler.push(G_KEYWORD.DataBase.ProjectFieldKey.Docs, docs)
        sql_handler.filter_equal(G_KEYWORD.DataBase.ProjectFieldKey.Pid, pid)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def delete(pid: int) -> Any:
        """
        [ 项目删除 ]

        ---
        参数:
        - pid : { str } - 项目ID。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.delete(G_KEYWORD.DataBase.TableName.Project)
        sql_handler.filter_equal(G_KEYWORD.DataBase.ProjectFieldKey.Pid, pid)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def delete_all() -> Any:
        """
        [ 删除全部项目 ]

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.delete(G_KEYWORD.DataBase.TableName.Project)
        return sql_handler
