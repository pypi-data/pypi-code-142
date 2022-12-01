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
数据库关键字
    
"""


# --------------------------------------------------------------------------
class TableName:
    """
    [ 表名关键字 ]

    """
    User = 'user'
    """ 用户表 """

    Role = 'role'
    """ 角色表 """
    
    Project = 'project'
    """ 项目表 """

    Tasks = 'tasks'
    """ 任务表 """

    TaskRecord = 'task_record'
    """ 任务记录表 """

    CaseRecord = 'case_record'
    """ 用例记录表 """


# --------------------------------------------------------------------------
class UserFieldKey:
    """
    [ 用户表字段名关键字 ]

    """
    UserId = 'user_id'
    """ 用户ID """

    UserNumber = 'user_number'
    """ 用户账号 """

    Password = 'password'
    """ 用户密码 """

    UserName = 'user_name'
    """ 用户名称 """

    Portrait = 'portrait'
    """ 用户头像 """

    RoleId = 'role_id'
    """ 用户角色ID """

    UserToken = 'user_token'
    """ 用户登录态 """


# --------------------------------------------------------------------------
class RoleFieldKey:
    """
    [ 角色表字段名关键字 ]

    """
    RoleId = 'role_id'
    """ 角色ID """

    RoleName = 'role_name'
    """ 角色名称 """

    RoleValue = 'role_value'
    """ 角色权限 """


# --------------------------------------------------------------------------
class ProjectFieldKey:
    """
    [ 项目表字段名关键字 ]

    """
    Pid = 'pid'
    """ 项目ID """

    Name = 'name'
    """ 项目名称 """

    Type = 'type'
    """ 项目类型 """

    Docs = 'docs'
    """ 项目说明 """

    State = 'state'
    """ 状态 """
    
    CreatedDate = 'created_date'
    """ 创建日期 """


# --------------------------------------------------------------------------
class TasksFieldKey:
    """
    [ 任务表字段名关键字 ]

    """
    Tid = 'tid'
    """ 任务ID """

    Pid = 'pid'
    """ 项目ID """

    Name = 'name'
    """ 名称 """

    Docs = 'docs'
    """ 说明 """

    Type = 'type'
    """ 类型 """

    CreatedDate = 'created_date'
    """ 创建日期 """

    State = 'state'
    """ 状态 """

    ScriptJson = 'script_json'
    """ 脚本Json """

    RunNumber = 'run_number'
    """ 运行次数 """

    LastRunDate = 'last_run_date'
    """ 最后运行日期 """

    LastRunTime = 'last_run_time'
    """ 最后运行时间 """

    SpendTime = 'spend_time'
    """ 消耗时间 """


# --------------------------------------------------------------------------
class TaskRecordFieldKey:
    """
    [ 任务记录字段名关键字 ]

    """
    TRid = 'trid'
    """ 编号 """

    Tid = 'tid'
    """ 所属任务ID """

    Name = 'name'
    """ 名称 """

    Docs = 'docs'
    """ 说明 """

    Type = 'type'
    """ 类型 """

    CreatedDate = 'created_date'
    """ 创建日期 """

    State = 'state'
    """ 状态 """

    StartTime = 'start_time'
    """ 开始时间 """

    EndTime = 'end_time'
    """ 结束时间 """

    SpendTime = 'spend_time'
    """ 消耗时间 """

    Process = 'process'
    """ 过程 """


# --------------------------------------------------------------------------
class CaseRecordFieldKey:
    """
    [ 用例记录字段名关键字 ]

    """
    CRid = 'crid'
    """ 编号 """

    TRid = 'trid'
    """ 所属任务记录ID """

    Name = 'name'
    """ 名称 """

    Docs = 'docs'
    """ 说明 """
    
    Type = 'type'
    """ 类型 """

    CreatedDate = 'created_date'
    """ 创建日期 """

    State = 'state'
    """ 状态 """

    StartTime = 'start_time'
    """ 开始时间 """

    EndTime = 'end_time'
    """ 结束时间 """

    SpendTime = 'spend_time'
    """ 消耗时间 """

    Process = 'process'
    """ 过程 """

