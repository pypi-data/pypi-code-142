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
[ SQL语句映射 ]

"""
from .blueprint.sql_user import SqlUser
from .blueprint.sql_project import SqlProject
from .blueprint.sql_tasks import SqlTasks
from .blueprint.sql_record_task import SqlTaskRecord
from .blueprint.sql_record_case import SqlCaseRecord


# --------------------------------------------------------------------------
class AwakenSql(object):
    """
    [ SQL语句映射类 ]

    """


    # ----------------------------------------------------------------------
    @property
    def User(self) -> SqlUser:
        """
        [ 用户相关 ]

        """
        return SqlUser


    # ----------------------------------------------------------------------
    @property
    def Project(self) -> SqlProject:
        """
        [ 项目相关 ]

        """
        return SqlProject


    # ----------------------------------------------------------------------
    @property
    def Tasks(self) -> SqlTasks:
        """
        [ 任务相关 ]

        """
        return SqlTasks


    # ----------------------------------------------------------------------
    @property
    def TaskRecord(self) -> SqlTaskRecord:
        """
        [ 任务记录相关 ]

        """
        return SqlTaskRecord


    # ----------------------------------------------------------------------
    @property
    def CaseRecord(self) -> SqlCaseRecord:
        """
        [ 用例记录相关 ]

        """
        return SqlCaseRecord
