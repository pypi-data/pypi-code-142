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
[ 脚本执行器相关接口 ]

"""
import json

from flask import Response
from flask import Blueprint

from ..server_request_handler import URL_PREFIX
from ..server_request_handler import ServerRequestHandler
from ...db import DB
from ...db import SQL
from ....baseic.const import G_CONST
from ....baseic.keyword import G_KEYWORD
from ....baseic.common.configure import G_CONFIGURE
from ....baseic.structural.interpreter import AwakenTask
from ....baseic.decorator.web_api import deco_webapi_error_capture
from ....core.perform.pool_runtime import POOL_RUNTIME
from ....core.interpreter.grammar_parser import GRAMMAR_PARSER
from ....kit.engine_agency import EngineAgency


# 创建驱动代理
for _ in range(G_CONFIGURE.get(G_KEYWORD.Common.Config.EngineQueueMaxCount)):
    POOL_RUNTIME.engine_queue.put(EngineAgency())
    POOL_RUNTIME.sign_engine()


blueprint_runer = Blueprint('runer', __name__)
""" [ 脚本执行器接口蓝图实例 ] """


POST_RUNER_RUNNING_TASK    = '/runer/runing/task'
""" 接口URL - 运行任务 """
POST_RUNER_RUNNING_TASKS   = '/runer/runing/tasks'
""" 接口URL - 批量运行任务 """
POST_RUNER_RUNNING_PROJECT = '/runer/runing/project'
""" 接口URL - 运行项目 """


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_runer.route(''.join([URL_PREFIX, POST_RUNER_RUNNING_TASK]), methods=['POST'])
def post_running_task() -> Response:
    """
    [ POST - 运行任务 ]

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

    # 从数据库中获取数据
    db_data = DB.execute(SQL.Tasks.get_task_script(tid))
    task_info = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)[0]
    task_type = task_info.get(G_KEYWORD.DataBase.TasksFieldKey.Type)
    task_name = task_info.get(G_KEYWORD.DataBase.TasksFieldKey.Name)
    task_docs = task_info.get(G_KEYWORD.DataBase.TasksFieldKey.Docs)
    script_json = json.loads(task_info.get(G_KEYWORD.DataBase.TasksFieldKey.ScriptJson))

    # 解析成 Awaken 语法
    awaken_script_code = []
    awaken_script_code.append(f'TaskType = \'{task_type}\'')
    awaken_script_code.append(f'TaskName = \'{task_name}\'')
    awaken_script_code.append(f'TaskDocs = \'{task_docs}\'')

    if len(script_json['cases']) > 0:
        for case in script_json['cases']:
            # 声明用例
            case_statement = f'CASE :: {case["name"]}'
            if case['docs'] != '':
                case_statement += f' :: {case["docs"]}'
            awaken_script_code.append(case_statement)

            if len(case['logic']) > 0:
                for logic in case['logic']:
                    # TODO 暂未处理不同的逻辑块类型
                    driving_character = logic['list'][0]['drivingCharacter']
                    driving_parameter = []
                    for para_value in logic['list'][0]['drivingParameter']:
                        if para_value['value'] != '':
                            driving_parameter.append(para_value['value'])
                    
                    run_instructions = '    '
                    if logic['list'][0]['whetherThereReturn']:
                        if logic['list'][0]['namespaceKey'] != '':
                            if logic['list'][0]['namespaceScope'] == 'UNIVERSE':
                                run_instructions += '$'
                            run_instructions += f"{logic['list'][0]['namespaceKey']} = "
                        
                    run_instructions += f'{ driving_character }'
                    for para in driving_parameter:
                        run_instructions += f'  >>  {para}'

                    awaken_script_code.append(run_instructions)
            awaken_script_code.append('    ?? True')

    print(awaken_script_code)
    task_object = GRAMMAR_PARSER.parsing_json(awaken_script_code, task_type, tid)
    POOL_RUNTIME.task_queue.put(task_object)

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Message: '任务推送完毕 !',
    })
    return ServerRequestHandler.successful(result)


# @blueprint_runer.route(''.join([URL_PREFIX, TASK_URL_RUNNING_TASK_LIST]), methods=['POST'])
# def running_task_list():
#     """
#     [ 执行任务列表 ]

#     ---
#     必要参数:
#         tid { int } : 任务ID

#     """
#     try:
#         result = {}
#         # 解析请求参数
#         paras = ServerRequestHandler.analysis_request_parameter(
#             keys=['tid_list'],
#             must_keys=['tid_list']
#         )

#         for tid in paras['tid_list']:

#             # 从数据库中获取数据
#             task_script = DB.lock_read(SQL.Tasks.get_task_script(tid))[0][7]
#             script_json = json.loads(task_script)

#             # 解析成 Awaken 语法
#             awaken_script_code = []
#             awaken_script_code.append(f'TaskType = \'{script_json["type"]}\'')
#             awaken_script_code.append(f'TaskName = \'{script_json["name"]}\'')
#             awaken_script_code.append(f'TaskDocs = \'{script_json["docs"]}\'')

#             if len(script_json['cases']) > 0:
#                 for case in script_json['cases']:
#                     # 声明用例
#                     case_statement = f'CASE :: {case["name"]}'
#                     if case['docs'] != '':
#                         case_statement += f' :: {case["docs"]}'
#                     awaken_script_code.append(case_statement)

#                     if len(case['logic']) > 0:
#                         for logic in case['logic']:
#                             # TODO 暂未处理不同的逻辑块类型
#                             driving_character = logic['list'][0]['drivingCharacter']
#                             driving_parameter = []
#                             for para_value in logic['list'][0]['drivingParameter']:
#                                 if para_value['value'] != '':
#                                     driving_parameter.append(para_value['value'])
                            
#                             run_instructions = '    '
#                             if logic['list'][0]['whetherThereReturn']:
#                                 if logic['list'][0]['namespaceKey'] != '':
#                                     if logic['list'][0]['namespaceScope'] == 'UNIVERSE':
#                                         run_instructions += '$'
#                                     run_instructions += f"{logic['list'][0]['namespaceKey']} = "
                                
#                             run_instructions += f'{ driving_character }'
#                             for para in driving_parameter:
#                                 run_instructions += f'  >>  {para}'

#                             awaken_script_code.append(run_instructions)
#                     awaken_script_code.append('    ?? True')

#             task_object = GRAMMAR_PARSER.parsing_json(awaken_script_code, script_json['type'])
#             POOL_RUNTIME.task_queue.put(task_object)

#         # 返回值
#         result.update({'result': 'ok'})
#         return ServerRequestHandler.successful(result)

#     except BaseException as error:
#         return ServerRequestHandler.unsuccessful(str(error))
