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
[ Awaken 数据库 ]

"""
import sqlite3
from typing import Any
from threading import Lock

from .sqlite_statement_handle import SqliteUpdater
from .sqlite_statement_handle import SqliteDeleter
from .sqlite_statement_handle import SqliteSelecter
from .sqlite_statement_handle import SqliteInserter
from .sqlite_statement_handle import G_SQLITE_STATEMENT_HANDLE
from ...baseic.const import G_CONST
from ...baseic.keyword import G_KEYWORD
from ...baseic.error.server import AwakenDataBaseError
from ...baseic.decorator.baseic import deco_singleton


# --------------------------------------------------------------------------
@deco_singleton
class AwakenDb(object):
    """
    [ Awaken 数据库 ]

    ---
    描述
    - 基于 SQLite 数据库封装了一些常用功能。

    """
    _conn: sqlite3.Connection = None
    """ 数据库连接对象 """
    _lock: Lock = Lock()
    """ 数据库互斥锁 """


    # ----------------------------------------------------------------------
    def __init__(self):
        try:
            # 创建/连接数据库
            if not self._conn:
                self.connect()
                self.commit()
 
        except Exception as error:
            raise AwakenDataBaseError(str(error))


    # ----------------------------------------------------------------------
    def execute(self, sql_handle: Any, with_lock: bool = False, return_data_type: str = 'DICT'):
        """
        [ 执行SQLitem句柄 ]

        """
        # print(str(sql_handle))

        if isinstance(sql_handle, SqliteSelecter):
            return self._execute_sqlite_handle_query(sql_handle, with_lock, return_data_type)
        
        elif isinstance(sql_handle, SqliteInserter):
            return self._execute_sqlite_handle_write(sql_handle, with_lock)

        elif isinstance(sql_handle, SqliteUpdater):
            return self._execute_sqlite_handle_write(sql_handle, with_lock)

        elif isinstance(sql_handle, SqliteDeleter):
            return self._execute_sqlite_handle_write(sql_handle, with_lock)
            
        else:
            raise AwakenDataBaseError('无效的SQLitem句柄对象 !')


    # ----------------------------------------------------------------------
    def _execute_sqlite_handle_query(self, sql_handle: Any, with_lock: bool = False, return_data_type: str = 'DICT') -> list:
        """
        [ 执行SQLite查询句柄 ]

        """
        result = {
            G_KEYWORD.Common.TransactionFieldKey.Totai: 0,
            G_KEYWORD.Common.TransactionFieldKey.Items: [],
        }
        sql_sentence = str(sql_handle)
        return_field = sql_handle._data_alias

        # 数据库查询
        db_result: list
        if with_lock:
            with self._lock:
                db_result = self._query(sql_sentence)
        else:
            db_result = self._query(sql_sentence)

        # 处理返回数据
        if return_data_type == 'DICT':
            for item in db_result:
                item = dict(zip(return_field, item))
                result[G_KEYWORD.Common.TransactionFieldKey.Totai] += 1
                result[G_KEYWORD.Common.TransactionFieldKey.Items].append(item)
        else:
            for item in db_result:
                result[G_KEYWORD.Common.TransactionFieldKey.Totai] += 1
                result[G_KEYWORD.Common.TransactionFieldKey.Items].append(item)
    
        return result


    # ----------------------------------------------------------------------
    def _execute_sqlite_handle_write(self, sql_handle: Any, with_lock: bool = False) -> int:
        """
        [ 执行SQLite写入句柄 ]

        """
        result: int
        sql_sentence = str(sql_handle)

        # 数据库写入
        if with_lock:
            with self._lock:
                result = self._write(sql_sentence)
        else:
            result = self._write(sql_sentence)

        return result


    # ----------------------------------------------------------------------
    def _query(self, sql_sentence: str) -> list:
        """
        [ 无锁读取 ]

        ---
        描述
        - 执行查询语句, 该函数不会持有数据库锁。

        ---
        参数
        - sql_sentence : { str } - SQLite 查询语句。

        ---
        返回
        - list : 查询结果列表。

        """
        try:
            cur = self._conn.cursor()  # 创建游标
            cur.execute(sql_sentence)  # 执行语句
            result = cur.fetchall()    # 获取结果
            cur.close()                # 注销游标
            return result              # 返回数据

        except Exception as error:
            raise AwakenDataBaseError(str(error))


    # ----------------------------------------------------------------------
    def _write(self, sql: str) -> int:
        """
        [ 无锁写入 ]

        ---
        描述
        - 执行写入语句, 该函数不会持有数据库锁。

        ---
        参数
        - sql : { str } - SQLite 查询语句。

        ---
        返回
        - int : 写入数据后返回该条数据的自增ID。

        """
        try:
            cur = self._conn.cursor()  # 创建数据库游标
            cur.execute(sql)           # 执行查询语句
            add_id = cur.lastrowid     # 获取数据自增ID
            cur.close()                # 注销数据库游标
            return add_id              # 返回数据自增ID

        except Exception as error:
            raise AwakenDataBaseError(str(error))


    # ----------------------------------------------------------------------
    def connect(self):
        """
        [ 数据库连接 ]

        """
        # 创建数据库连接对象
        self._conn = sqlite3.connect(G_CONST.Path.FilePath.EngineeringDatabase, check_same_thread=False)
        # 创建数据库游标
        Cur = self._conn.cursor()
        
        # 构建数据库表
        for key, value in CreateTableSql.__dict__.items():
            if '__' in key:
                continue
            Cur.execute(value)

        # 注销数据库游标
        Cur.close()


    # ----------------------------------------------------------------------
    def commit(self):
        """
        [ 事务保存 ]

        """
        self._conn.commit()


    # ----------------------------------------------------------------------
    def rollback(self):
        """
        [ 事务回滚 ]

        """
        self._conn.rollback()


    # ----------------------------------------------------------------------
    def quit(self):
        """
        [ 关闭数据库连接 ]

        """
        self._conn.close()


# --------------------------------------------------------------------------
class CreateTableSql(object):
    """
    [ 建表语句 ]

    """


    # ----------------------------------------------------------------------
    User = G_SQLITE_STATEMENT_HANDLE.create_table(
        table_name=G_KEYWORD.DataBase.TableName.User,
        table_field={
            G_KEYWORD.DataBase.UserFieldKey.UserId     : G_KEYWORD.Sqlite.DataType.IdKey,
            G_KEYWORD.DataBase.UserFieldKey.UserNumber : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.UserFieldKey.Password   : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.UserFieldKey.UserName   : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.UserFieldKey.Portrait   : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.UserFieldKey.RoleId     : G_KEYWORD.Sqlite.DataType.Int,
            G_KEYWORD.DataBase.UserFieldKey.UserToken  : G_KEYWORD.Sqlite.DataType.Text,
        }
    )
    """
    [ 建表语句 - 用户表 ]

    """


    # ----------------------------------------------------------------------
    Project = G_SQLITE_STATEMENT_HANDLE.create_table(
        table_name=G_KEYWORD.DataBase.TableName.Project,
        table_field={
            G_KEYWORD.DataBase.ProjectFieldKey.Pid         : G_KEYWORD.Sqlite.DataType.IdKey,
            G_KEYWORD.DataBase.ProjectFieldKey.Type        : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.ProjectFieldKey.Name        : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.ProjectFieldKey.Docs        : G_KEYWORD.Sqlite.DataType.Text,
            G_KEYWORD.DataBase.ProjectFieldKey.State       : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.ProjectFieldKey.CreatedDate : G_KEYWORD.Sqlite.DataType.DateNotNull,
        }
    )
    """
    [ 建表语句 - 项目表 ]

    """


    # ----------------------------------------------------------------------
    Tasks = G_SQLITE_STATEMENT_HANDLE.create_table(
        table_name=G_KEYWORD.DataBase.TableName.Tasks,
        table_field={
            G_KEYWORD.DataBase.TasksFieldKey.Tid         : G_KEYWORD.Sqlite.DataType.IdKey,
            G_KEYWORD.DataBase.TasksFieldKey.Pid         : G_KEYWORD.Sqlite.DataType.IntNotNull,
            G_KEYWORD.DataBase.TasksFieldKey.Type        : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.TasksFieldKey.Name        : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.TasksFieldKey.Docs        : G_KEYWORD.Sqlite.DataType.Text,
            G_KEYWORD.DataBase.TasksFieldKey.State       : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.TasksFieldKey.CreatedDate : G_KEYWORD.Sqlite.DataType.DateNotNull,
            G_KEYWORD.DataBase.TasksFieldKey.ScriptJson  : G_KEYWORD.Sqlite.DataType.Text,
            G_KEYWORD.DataBase.TasksFieldKey.RunNumber   : G_KEYWORD.Sqlite.DataType.IntNotNull,
            G_KEYWORD.DataBase.TasksFieldKey.LastRunDate : G_KEYWORD.Sqlite.DataType.Date,
            G_KEYWORD.DataBase.TasksFieldKey.LastRunTime : G_KEYWORD.Sqlite.DataType.Date,
            G_KEYWORD.DataBase.TasksFieldKey.SpendTime   : G_KEYWORD.Sqlite.DataType.Int,
        }
    )
    """
    [ 建表语句 - 任务表 ]

    """


    # ----------------------------------------------------------------------
    TaskRecord = G_SQLITE_STATEMENT_HANDLE.create_table(
        table_name=G_KEYWORD.DataBase.TableName.TaskRecord,
        table_field={
            G_KEYWORD.DataBase.TaskRecordFieldKey.TRid        : G_KEYWORD.Sqlite.DataType.IdKey,
            G_KEYWORD.DataBase.TaskRecordFieldKey.Tid         : G_KEYWORD.Sqlite.DataType.IntNotNull,
            G_KEYWORD.DataBase.TaskRecordFieldKey.Name        : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.TaskRecordFieldKey.Docs        : G_KEYWORD.Sqlite.DataType.Text,
            G_KEYWORD.DataBase.TaskRecordFieldKey.Type        : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.TaskRecordFieldKey.CreatedDate : G_KEYWORD.Sqlite.DataType.DateNotNull,
            G_KEYWORD.DataBase.TaskRecordFieldKey.State       : G_KEYWORD.Sqlite.DataType.Text,
            G_KEYWORD.DataBase.TaskRecordFieldKey.StartTime   : G_KEYWORD.Sqlite.DataType.DateNotNull,
            G_KEYWORD.DataBase.TaskRecordFieldKey.EndTime     : G_KEYWORD.Sqlite.DataType.DateNotNull,
            G_KEYWORD.DataBase.TaskRecordFieldKey.SpendTime   : G_KEYWORD.Sqlite.DataType.Int,
            G_KEYWORD.DataBase.TaskRecordFieldKey.Process     : G_KEYWORD.Sqlite.DataType.Text,
        }
    )
    """
    [ 建表语句 - 任务记录表 ]

    """


    # ----------------------------------------------------------------------
    CaseRecord = G_SQLITE_STATEMENT_HANDLE.create_table(
        table_name=G_KEYWORD.DataBase.TableName.CaseRecord,
        table_field={
            G_KEYWORD.DataBase.CaseRecordFieldKey.CRid        : G_KEYWORD.Sqlite.DataType.IdKey,
            G_KEYWORD.DataBase.CaseRecordFieldKey.TRid        : G_KEYWORD.Sqlite.DataType.IntNotNull,
            G_KEYWORD.DataBase.CaseRecordFieldKey.Name        : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.CaseRecordFieldKey.Docs        : G_KEYWORD.Sqlite.DataType.Text,
            G_KEYWORD.DataBase.CaseRecordFieldKey.Type        : G_KEYWORD.Sqlite.DataType.TextNotNull,
            G_KEYWORD.DataBase.CaseRecordFieldKey.CreatedDate : G_KEYWORD.Sqlite.DataType.DateNotNull,
            G_KEYWORD.DataBase.CaseRecordFieldKey.State       : G_KEYWORD.Sqlite.DataType.Text,
            G_KEYWORD.DataBase.CaseRecordFieldKey.StartTime   : G_KEYWORD.Sqlite.DataType.DateNotNull,
            G_KEYWORD.DataBase.CaseRecordFieldKey.EndTime     : G_KEYWORD.Sqlite.DataType.Date,
            G_KEYWORD.DataBase.CaseRecordFieldKey.SpendTime   : G_KEYWORD.Sqlite.DataType.Int,
            G_KEYWORD.DataBase.CaseRecordFieldKey.Process     : G_KEYWORD.Sqlite.DataType.Text,
        }
    )
    """
    [ 建表语句 - 用例记录表 ]

    """
