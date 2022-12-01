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
[ 编辑器相关接口 ]

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


blueprint_editor = Blueprint('editor', __name__)
""" 编辑器接口蓝图 """


POST_EDITOR_TASKS_SCRIPT = '/editor/task_script'
""" 接口URL - 获取任务脚本 """
POST_EDITOR_SAVE_SCRIPT = '/editor/save_script'
""" 接口URL - 获取任务脚本 """ 


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_editor.route(''.join([URL_PREFIX, POST_EDITOR_TASKS_SCRIPT]), methods=['POST'])
def post_tasks_script() -> Response:
    """
    [ POST - 获取任务脚本 ]

    ---
    必要参数
    - tid : { str } - 任务编号。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[
            G_KEYWORD.Api.TasksFieldKey.Tid,
        ]
    )
    tid = paras.get(G_KEYWORD.Api.TasksFieldKey.Tid)

    # 从数据库中获取数据
    db_data = DB.execute(SQL.Tasks.get_task_script(tid=tid))
    item = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)[0]
    script_json = item.get(G_KEYWORD.DataBase.TasksFieldKey.ScriptJson).replace("'", '"')

    # 处理返回
    result.update({
        G_KEYWORD.Api.TasksFieldKey.Type: item.get(G_KEYWORD.DataBase.TasksFieldKey.Type),
        G_KEYWORD.Api.TasksFieldKey.Name: item.get(G_KEYWORD.DataBase.TasksFieldKey.Name),
        G_KEYWORD.Api.TasksFieldKey.Docs: item.get(G_KEYWORD.DataBase.TasksFieldKey.Docs),
        G_KEYWORD.Api.TasksFieldKey.ScriptJson: script_json
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_editor.route(''.join([URL_PREFIX, POST_EDITOR_SAVE_SCRIPT]), methods=['POST'])
def post_save_script() -> Response:
    """
    [ POST - 保存任务脚本 ]

    ---
    必要参数
    - tid : { str } - 任务编号。

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

    # 写入数据库
    DB.execute(SQL.Tasks.modify(
        tid=paras.get(G_KEYWORD.Api.TasksFieldKey.Tid),
        name=paras.get(G_KEYWORD.Api.TasksFieldKey.Name),
        docs=paras.get(G_KEYWORD.Api.TasksFieldKey.Docs),
        script_json_string=script_json
    ))
    DB.commit()

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Message: '任务保存成功 !'
    })
    return ServerRequestHandler.successful(result)
