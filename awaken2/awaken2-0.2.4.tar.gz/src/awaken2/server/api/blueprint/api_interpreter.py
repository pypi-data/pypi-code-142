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
[ 解释器相关接口 ]

"""
from flask import Response
from flask import Blueprint

from ..server_request_handler import URL_PREFIX
from ..server_request_handler import ServerRequestHandler
from ....baseic.decorator.web_api import deco_webapi_error_capture
from ....baseic.const import G_CONST
from ....baseic.keyword import G_KEYWORD
from ....kit.web.web_engine_method_map import WEB_INSTRUCTIONS


blueprint_interpreter = Blueprint('interpreter', __name__)
""" 解释器接口蓝图 """


POST_INTERPRETER_GET_INSTRUCTIONS = '/interpreter/instructions'
""" 接口URL - 获取指令集 """


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_interpreter.route(''.join([URL_PREFIX, POST_INTERPRETER_GET_INSTRUCTIONS]), methods=['POST'])
def post_instructions() -> Response:
    """
    [ POST - 获取指令集 ]

    ---
    必要参数:
    - task_type : { str } - 任务类型。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[G_KEYWORD.Api.InterpreterFieldKey.TaskType]
    )
    task_type = paras.get(G_KEYWORD.Api.InterpreterFieldKey.TaskType)

    # 获取任务类型的指令集
    instructions = []
    if task_type.upper() == G_CONST.Type.Task.Web:
        instructions = WEB_INSTRUCTIONS

    # 处理返回
    result.update({
        G_KEYWORD.Api.InterpreterFieldKey.Instructions: instructions
    })
    return ServerRequestHandler.successful(result)
