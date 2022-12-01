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
[ 任务相关接口 ]

"""
import time
import json

from flask import Response
from flask import Blueprint

from ..server_request_handler import URL_PREFIX
from ..server_request_handler import ServerRequestHandler
from ...db import DB
from ...db import SQL
from ....baseic.const import G_CONST
from ....baseic.keyword import G_KEYWORD
from ....baseic.decorator.web_api import deco_webapi_error_capture


blueprint_tasks = Blueprint('tasks', __name__)
""" 任务接口蓝图 """


POST_TASKS_GET_TASKS_COUNT     = '/tasks/count'
""" 接口URL - 获取任务数量 """ 
POST_TASKS_GET_TASKS_LIST      = '/tasks/list'
""" 接口URL - 获取任务列表 """
POST_TASKS_GET_TASKS_CREATION  = '/tasks/creation'
""" 接口URL - 任务创建 """ 
POST_TASKS_GET_TASKS_MODIFY    = '/tasks/modify'
""" 接口URL - 任务编辑 """ 
POST_TASKS_GET_TASKS_DELETE    = '/tasks/delete'
""" 接口URL - 任务删除 """


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_tasks.route(''.join([URL_PREFIX, POST_TASKS_GET_TASKS_COUNT]), methods=['POST'])
def post_count() -> Response:
    """
    [ POST - 查询任务数量 ]

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
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        optional_keys=[
            G_KEYWORD.Api.TasksFieldKey.Tid,
            G_KEYWORD.Api.TasksFieldKey.Pid,
            G_KEYWORD.Api.TasksFieldKey.Type,
            G_KEYWORD.Api.TasksFieldKey.Name,
            G_KEYWORD.Api.TasksFieldKey.State,
            G_KEYWORD.Api.TasksFieldKey.CreatedDate,
            G_KEYWORD.Api.TasksFieldKey.RunNumber,
            G_KEYWORD.Api.TasksFieldKey.LastRunDate,
        ]
    )

    # 从数据库中获取数据
    db_data = DB.execute(SQL.Tasks.get_count(paras), return_data_type='LIST')
    count = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)[0][0]

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Count: count
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_tasks.route(''.join([URL_PREFIX, POST_TASKS_GET_TASKS_LIST]), methods=['POST'])
def post_list() -> Response:
    """
    [ POST - 查询任务列表 ]

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
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        optional_keys=[
            G_KEYWORD.Api.TasksFieldKey.Tid,
            G_KEYWORD.Api.TasksFieldKey.Pid,
            G_KEYWORD.Api.TasksFieldKey.Type,
            G_KEYWORD.Api.TasksFieldKey.Name,
            G_KEYWORD.Api.TasksFieldKey.State,
            G_KEYWORD.Api.TasksFieldKey.CreatedDate,
            G_KEYWORD.Api.TasksFieldKey.RunNumber,
            G_KEYWORD.Api.TasksFieldKey.LastRunDate,
            G_KEYWORD.Common.PagingDataFieldKey.Page,
            G_KEYWORD.Common.PagingDataFieldKey.Number,
        ]
    )

    # 从数据库中获取数据
    db_data = DB.execute(SQL.Tasks.get_list(paras))
    items = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)
    totai = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Totai)

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Items: items,
        G_KEYWORD.Api.TransactionFieldKey.Totai: totai,
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_tasks.route(''.join([URL_PREFIX, POST_TASKS_GET_TASKS_CREATION]), methods=['POST'])
def post_creation() -> Response:
    """
    [ POST - 任务创建 ]

    ---
    必要参数
    - pid  : { int } - 项目编号。
    - type : { int } - 任务类型。
    - name : { int } - 任务名称。

    ---
    可选参数:
    - docs : { str } - 任务说明。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[
            G_KEYWORD.Api.TasksFieldKey.Pid,
            G_KEYWORD.Api.TasksFieldKey.Type,
            G_KEYWORD.Api.TasksFieldKey.Name,
        ],
        optional_keys=[
            G_KEYWORD.Api.TasksFieldKey.Docs,
        ]
    )
    if not paras.get(G_KEYWORD.Api.TasksFieldKey.Docs):
        paras.update({G_KEYWORD.Api.TasksFieldKey.Docs : 'NULL'})

    # 从数据库中写入数据
    tid = DB.execute(SQL.Tasks.creation(
        pid =paras.get(G_KEYWORD.Api.TasksFieldKey.Pid),
        type=paras.get(G_KEYWORD.Api.TasksFieldKey.Type),
        name=paras.get(G_KEYWORD.Api.TasksFieldKey.Name),
        docs=paras.get(G_KEYWORD.Api.TasksFieldKey.Docs),
        created_date=time.strftime('%Y-%m-%d'),
        state=G_CONST.State.Project.Null,  # 状态, 暂时不实现
    ))
    DB.commit()

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Message: '任务创建成功 !',
        G_KEYWORD.Api.TasksFieldKey.Tid: tid
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_tasks.route(''.join([URL_PREFIX, POST_TASKS_GET_TASKS_MODIFY]), methods=['POST'])
def post_modify() -> Response:
    """
    [ POST - 任务编辑 ]

    ---
    必要参数
    - tid         : { int } - 任务编号。
    - name        : { int } - 任务名称。
    - docs        : { str } - 任务说明。
    - script_json : { Any } - 脚本JSON对象。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[
            G_KEYWORD.Api.TasksFieldKey.Tid,
            G_KEYWORD.Api.TasksFieldKey.Name,
            G_KEYWORD.Api.TasksFieldKey.Docs,
            G_KEYWORD.Api.TasksFieldKey.ScriptJson,
        ]
    )

    script_json = paras.get(G_KEYWORD.Api.TasksFieldKey.ScriptJson)
    script_json_string = json.dumps(script_json, ensure_ascii=False)

    DB.execute(SQL.Tasks.modify(
        tid =paras.get(G_KEYWORD.Api.TasksFieldKey.Tid), 
        name=paras.get(G_KEYWORD.Api.TasksFieldKey.Name), 
        docs=paras.get(G_KEYWORD.Api.TasksFieldKey.Docs), 
        script_json_string=script_json_string
    ))
    DB.commit()

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Message: '任务编辑成功 !'
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_tasks.route(''.join([URL_PREFIX, POST_TASKS_GET_TASKS_DELETE]), methods=['POST'])
def post_delete() -> Response:
    """
    [ POST - 任务删除 ]

    ---
    必要参数
    - tid : { int } - 任务编号。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[
            G_KEYWORD.Api.TasksFieldKey.Tid
        ]
    )
    tid = paras.get(G_KEYWORD.Api.TasksFieldKey.Tid)

    # 从数据库中写入数据
    DB.execute(SQL.Tasks.delete(tid=tid))
    DB.commit()

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Message: '任务删除成功 !'
    })
    return ServerRequestHandler.successful(result)
