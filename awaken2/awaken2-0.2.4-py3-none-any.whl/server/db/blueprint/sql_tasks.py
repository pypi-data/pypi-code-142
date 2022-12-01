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
[ SQL蓝图 - 任务相关 ]

"""
import json
from typing import Any

from ..sqlite_statement_handle import G_SQLITE_STATEMENT_HANDLE
from ....baseic.const import G_CONST
from ....baseic.keyword import G_KEYWORD


# --------------------------------------------------------------------------
class SqlTasks:
    """
    [ SQL蓝图 - 任务相关 ]

    """


    # ----------------------------------------------------------------------
    @staticmethod
    def get_count(paras: dict = {}) -> Any:
        """
        [ 查询任务数量 ]

        ---
        可选参数
        - tid           : { str } - 任务编号。
        - pid           : { str } - 项目编号。
        - type          : { str } - 任务类型。
        - name          : { str } - 任务名称。
        - state         : { str } - 任务状态。
        - created_date  : { str } - 任务创建日期, 例如 2022-02-02。
        - run_number    : { str } - 运行次数。
        - last_run_date : { str } - 最后运行日期。

        """
        selecter = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.Tasks)
        selecter.get(G_KEYWORD.DataBase.TasksFieldKey.Tid, G_KEYWORD.Sqlite.SelectEvent.Count)
        selecter.filter_equal_batch(paras)
        return selecter


    # ----------------------------------------------------------------------
    @staticmethod
    def get_list(paras: dict = {}) -> Any:
        """
        [ 查询任务列表 ]

        ---
        可选参数
        - tid           : { str } - 任务编号。
        - pid           : { str } - 项目编号。
        - type          : { str } - 任务类型。
        - name          : { str } - 任务名称。
        - state         : { str } - 任务状态。
        - created_date  : { str } - 任务创建日期, 例如 2022-02-02。
        - run_number    : { str } - 运行次数。
        - last_run_date : { str } - 最后运行日期。
        - page          : { str } - 当前页数。
        - number        : { str } - 单页数据量。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.Tasks)
        sql_handler.filter_equal_batch(paras)
        sql_handler.set_sort_desc(G_KEYWORD.DataBase.TasksFieldKey.Tid)
        page   = paras.get(G_KEYWORD.Common.PagingDataFieldKey.Page)
        number = paras.get(G_KEYWORD.Common.PagingDataFieldKey.Number)
        sql_handler.set_data_limit(page, number)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def get_task_script(tid: int) -> Any:
        """
        [ 查询任务脚本 ]

        ---
        必要参数
        - tid : { str } - 任务编号。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.Tasks)
        sql_handler.get(G_KEYWORD.DataBase.TasksFieldKey.Type)
        sql_handler.get(G_KEYWORD.DataBase.TasksFieldKey.Name)
        sql_handler.get(G_KEYWORD.DataBase.TasksFieldKey.Docs)
        sql_handler.get(G_KEYWORD.DataBase.TasksFieldKey.ScriptJson)
        sql_handler.filter_equal(G_KEYWORD.DataBase.TasksFieldKey.Tid, tid)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def get_exist_task_dates(paras: dict = {}) -> Any:
        """
        [ 查询去重后的所有存在任务的日期列表 ]

        ---
        可选参数
        - tid           : { str } - 任务编号。
        - pid           : { str } - 项目编号。
        - name          : { str } - 任务名称。
        - type          : { str } - 任务类型。
        - created_date  : { str } - 任务创建日期, 例如 2022-02-02。
        - state         : { str } - 任务状态。
        - last_run_date : { str } - 最后运行日期。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.Tasks)
        sql_handler.filter_equal_batch(paras)
        sql_handler.get(G_KEYWORD.DataBase.TasksFieldKey.CreatedDate, G_KEYWORD.Sqlite.SelectEvent.Distinct)
        sql_handler.set_sort_desc(G_KEYWORD.DataBase.TasksFieldKey.Tid)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def creation(
        pid: int,
        type: str,
        name: str,
        docs: str,
        created_date: str,
        state: str = G_CONST.State.Result.Null
    ) -> Any:
        """
        [ 任务创建 ]

        ---
        参数:
        - pid          : { int } - 任务编号。
        - type         : { int } - 任务类型。
        - name         : { int } - 任务名称。
        - docs         : { str } - 任务说明。
        - created_date : { str } - 任务创建日期, 例如 2022-02-02。
        - state        : { str } - 任务状态。

        """
        # 初始脚本JSON
        script_json = {
            G_KEYWORD.Script.ScriptJson.Type     : type,
            G_KEYWORD.Script.ScriptJson.Name     : name,
            G_KEYWORD.Script.ScriptJson.Docs     : docs,
            G_KEYWORD.Script.ScriptJson.Namespace: [],
            G_KEYWORD.Script.ScriptJson.Cases    : [],
        }
        script_json_string = json.dumps(script_json, ensure_ascii=False)

        sql_handler = G_SQLITE_STATEMENT_HANDLE.insert(G_KEYWORD.DataBase.TableName.Tasks)
        sql_handler.deduction([
            'NULL', pid, type, name, docs, state, created_date, script_json_string, 0, 'NULL', 'NULL', 0
        ])
        return sql_handler


    # --------------------------------------------------------------------------
    @staticmethod
    def modify(
        tid: int,
        name: str,
        docs: str,
        script_json_string: str,
    ) -> Any:
        """
        [ 任务编辑 ]

        ---
        参数
        - tid                : { int } - 任务编号。
        - name               : { int } - 任务名称。
        - docs               : { str } - 任务说明。
        - script_json_string : { Any } - 脚本JSON字符串。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.update(G_KEYWORD.DataBase.TableName.Tasks)
        sql_handler.push(G_KEYWORD.DataBase.TasksFieldKey.Name, name)
        sql_handler.push(G_KEYWORD.DataBase.TasksFieldKey.Docs, docs)
        sql_handler.push(G_KEYWORD.DataBase.TasksFieldKey.ScriptJson, script_json_string)
        sql_handler.filter_equal(G_KEYWORD.DataBase.TasksFieldKey.Tid, tid)
        return sql_handler


    # --------------------------------------------------------------------------
    @staticmethod
    def set_state(
        tid: int,
        state: str,
    ) -> Any:
        """
        [ 设置状态 ]

        ---
        参数
        - tid   : { int } - 任务编号。
        - state : { str } - 任务状态。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.update(G_KEYWORD.DataBase.TableName.Tasks)
        sql_handler.push(G_KEYWORD.DataBase.TasksFieldKey.State, state)
        sql_handler.filter_equal(G_KEYWORD.DataBase.TasksFieldKey.Tid, tid)
        return sql_handler


    # --------------------------------------------------------------------------
    @staticmethod
    def delete(tid: int) -> Any:
        """
        [ 删除任务 ]

        ---
        参数
        - tid : { int } - 任务编号。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.delete(G_KEYWORD.DataBase.TableName.Tasks)
        sql_handler.filter_equal(G_KEYWORD.DataBase.TasksFieldKey.Tid, tid)
        return sql_handler


    # --------------------------------------------------------------------------
    @staticmethod
    def delete_form_project(pid: int) -> Any:
        """
        [ 删除指定项目的任务 ]

        ---
        参数
        - pid : { int } - 任务编号。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.delete(G_KEYWORD.DataBase.TableName.Tasks)
        sql_handler.filter_equal(G_KEYWORD.DataBase.TasksFieldKey.Pid, pid)
        return sql_handler
