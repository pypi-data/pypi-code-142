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
接口关键字
    
"""


# --------------------------------------------------------------------------
class UserFieldKey:
    """
    [ 用户字段名关键字 ]

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

    Token = 'token'
    """ 用户Token """

    Role = 'role'
    """ 用户角色 """


# --------------------------------------------------------------------------
class ProjectFieldKey:
    """ 
    [ 项目字段名关键字 ]

    """
    Count = 'count'
    """ 项目数量 """

    List = 'list'
    """ 项目列表 """

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
    [ 任务字段名关键字 ]

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


# --------------------------------------------------------------------------
class InterpreterFieldKey:
    """
    [ 解释器字段名关键字 ]

    """
    TaskType = 'task_type'
    """ 任务类型 """
    
    Instructions = 'instructions'
    """ 指令集 """


# --------------------------------------------------------------------------
class ProcessingFieldKey:
    """
    [ 数据处理字段名关键字 ]

    """
    Url = 'url'
    """ URL """

    Document = 'document'
    """ DOM文档 """


# --------------------------------------------------------------------------
class TransactionFieldKey:
    """
    [ 事务处理字段名关键字 ]

    """
    Result = 'result'
    """ 结果 """

    Code = 'code'
    """ 状态编码 """

    Items = 'items'
    """ 项目 """

    Totai = 'total'
    """ 合计 """

    Data = 'data'
    """ 数据 """

    Count = 'count'
    """ 数量 """

    Message = 'message'
    """ 消息 """

    Time = 'time'
    """ 时间 """
