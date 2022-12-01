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
[ 数据库 - 任务代理 ]

"""
import time

from .. import DB
from .. import SQL
from ....baseic.structural.interpreter import AwakenTask
from ....baseic.error.server import AwakenDatabaseAgentError


# --------------------------------------------------------------------------
class DbTaskRecordBroker:
    """
    [ 数据库 - 任务代理 ]

    ---
    描述
    - 该类将代理任务执行过程中的数据库写入事务。
    
    """
    _task: AwakenTask
    """ 任务对象 """
    _task_record_id: int
    """ 任务记录ID """
    _case_record_id: int
    """ 用例记录ID """
    _task_created_date: str
    """ 任务创建日期 """
    _task_start_time: str
    """ 任务开始时间 """
    _task_start_timestamp: int
    """ 任务开始时间戳 """
    _case_start_time: str
    """ 用例开始时间 """
    _case_start_timestamp: int
    """ 用例开始时间戳 """


    # ----------------------------------------------------------------------
    def __init__(self, task: AwakenTask):
        self._task = task


    # ----------------------------------------------------------------------
    def created_task(self, name: str, docs: str) -> int:
        """
        [ 创建任务记录 ]

        ---
        描述
        - 写入数据库任务记录。

        ---
        参数
        - name : { str } - 任务名称。
        - docs : { str } - 任务注释。

        ---
        返回
        - int : 写入的任务记录ID。

        """
        # 记录任务开始时间
        self._task_created_date    = time.strftime('%Y-%m-%d')
        self._task_start_time      = time.strftime('%H:%M:%S')
        self._task_start_timestamp = int(time.time())

        # 录入数据库任务记录
        try:
            self._task_record_id = DB.execute(SQL.TaskRecord.creation(
                self._task.database_task_id,
                name,
                docs,
                self._task.task_type,
                self._task_created_date,
                self._task_start_time,
            ))
            
        except BaseException:
            raise AwakenDatabaseAgentError

        return self._task_record_id


    # ----------------------------------------------------------------------
    def created_case(self, name: str, docs: str) -> int:
        """
        [ 创建用例记录 ]

        ---
        描述
        - 写入数据库用例记录。

        ---
        参数
        - name : { str } - 用例名称。
        - docs : { str } - 用例注释。

        ---
        返回
        - int : 写入的用例记录ID。

        """
        # 记录用例开始时间
        self._case_start_time = time.strftime('%H:%M:%S')
        self._case_start_timestamp = int(time.time())

        # 录入数据库用例记录
        self._case_record_id = DB.execute(SQL.CaseRecord.creation(
            self._task_record_id,
            name,
            docs,
            self._task.task_type,
            self._task_created_date,
            self._case_start_time,
        ))

        return self._case_record_id


    # ----------------------------------------------------------------------
    def update_case(
        self, 
        result: str, 
        process: str
    ):
        """
        [ 更新用例记录 ]

        ---
        参数
        - result : { str } - 结果。
        - process : { str } - 过程。

        """
        # 更新数据库用例记录
        DB.execute(SQL.CaseRecord.update(
            self._case_record_id,
            result,
            time.strftime('%H:%M:%S'),
            (int(time.time()) - self._case_start_timestamp),
            process
        ))


    # ----------------------------------------------------------------------
    def update_task(self, result: str, process: str):
        """
        [ 更新任务记录 ]

        ---
        参数
        - result : { str } - 结果。
        - process : { str } - 过程。

        """
        # 更新数据库任务记录
        DB.execute(SQL.TaskRecord.update(
            self._task_record_id,
            result,
            time.strftime('%H:%M:%S'),
            (int(time.time()) - self._task_start_timestamp),
            process,
        ))

        # 保存事务
        DB.commit()
