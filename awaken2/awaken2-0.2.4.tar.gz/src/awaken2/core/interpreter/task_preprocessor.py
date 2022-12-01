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
[ Awaken任务预处理程序 ]

"""
from ...baseic.const import G_CONST
from ...baseic.keyword import G_KEYWORD
from ...baseic.structural.interpreter import AwakenTask
from ...baseic.structural.interpreter import AwakenCase
from ...baseic.structural.interpreter import AwakenCodeLine
from ...baseic.error.engine import AwakenTaskPretreatmentError
from ...baseic.error.interpreter import AwakenInterpreterMethodWrongFul
from ...baseic.decorator.baseic import deco_singleton
from ...kit.common import ENGINE_TYPE_FUNCTION_MAP
from ...kit.global_method_map import GLOBAL_METHOD_FUNCTION_MAP
from ...kit.global_method_map import G_GLOBAL_METHOD


# --------------------------------------------------------------------------
@deco_singleton
class TaskPreprocessor:
    """
    [ Awaken任务预处理程序 ]

    """
    _task: AwakenTask
    """ 任务对象 """
    _temp_codeline: AwakenCodeLine
    """ 当前处理的代码行对象 """
    global_function_map: dict
    engine_function_map: dict


    # ----------------------------------------------------------------------
    def pretreatment(self, task: AwakenTask) -> AwakenTask:
        """
        [ 预处理 ]

        ---
        参数
        - task { AwakenTask } : 未处理的Awaken任务对象。

        ---
        返回
        - AwakenTask : 已处理的Awaken任务对象。

        """
        self._task = task
        try:
            self._init_namespace_by_task_type()
            self._running_preprocessing_instruction()
            self._task.is_encapsulated = True

        except Exception:
            raise AwakenTaskPretreatmentError

        return self._task


    # ----------------------------------------------------------------------
    def _init_namespace_by_task_type(self):
        """
        [ 初始化任务命名空间 ]

        """
        self._task.cases: dict = {}
        self._task.namespace: dict = {
            G_KEYWORD.Script.Namespace.TaskType: None,
            G_KEYWORD.Script.Namespace.TaskName: None,
            G_KEYWORD.Script.Namespace.TaskDocs: None
        }

        if self._task.translation.type == G_CONST.Type.Task.Web:
            self._task.namespace[G_KEYWORD.Script.Namespace.TaskType]    = G_CONST.Type.Task.Web
            self._task.namespace[G_KEYWORD.Script.Decorator.BrowserType] = G_CONST.Type.Browser.Chromium

        elif self._task.translation.type == G_CONST.Type.Task.Api:
            self._task.namespace[G_KEYWORD.Script.Namespace.TaskType]    = G_CONST.Type.Task.Api


    # ----------------------------------------------------------------------
    def _running_preprocessing_instruction(self):
        """
        [ 运行预处理指令 ]

        """
        # ------------------------------------------------------------------
        # 解析全局&&引擎方法映射字典
        # ------------------------------------------------------------------
        self.global_function_map = GLOBAL_METHOD_FUNCTION_MAP
        self.engine_function_map = ENGINE_TYPE_FUNCTION_MAP[self._task.translation.type]

        # ------------------------------------------------------------------
        # 循环全局域语句
        # 用例域语句将被存放至 cases 字典中等待引擎解析
        # ------------------------------------------------------------------
        for codeline in self._task.translation.codelines:
            self._temp_codeline = AwakenCodeLine(codeline)

            # 公域语句
            if self._temp_codeline.region == G_CONST.Interpreter.KEYWORD_IDENT_SCOPE_UNIVERSE:
                
                # 赋值逻辑
                if self._temp_codeline.type == G_CONST.Interpreter.CodeLineType.Give:
                    self._give_global_assignment(self._temp_codeline.give_name, self._temp_codeline.give_value)

                # 执行并赋值逻辑
                elif self._temp_codeline.type == G_CONST.Interpreter.CodeLineType.RGive:
                    result = self._running_common_function(self._temp_codeline.funtion_name, self._temp_codeline.funtion_value)
                    self._give_global_assignment(self._temp_codeline.give_name, result)

                # 执行逻辑
                elif self._temp_codeline.type == G_CONST.Interpreter.CodeLineType.Run:
                    self._running_common_function(self._temp_codeline.funtion_name, self._temp_codeline.funtion_value)

                # 声明逻辑
                elif self._temp_codeline.type == G_CONST.Interpreter.CodeLineType.SCase:
                    awaken_case = AwakenCase(
                        self._temp_codeline.number,
                        self._temp_codeline.case_name,
                        self._temp_codeline.case_docs,
                    )
                    self._task.cases[awaken_case.name] = awaken_case

            # 私域语句
            else:

                # 装饰器逻辑
                if self._temp_codeline.type == G_CONST.Interpreter.CodeLineType.SDecorator:
                    self._task.cases[self._temp_codeline.region].decorator.update({self._temp_codeline.decorator_key : self._temp_codeline.decorator_value})

                # 执行并赋值逻辑
                elif self._temp_codeline.type == G_CONST.Interpreter.CodeLineType.RGive:
                    self.verify_validity_method()

                # 执行逻辑
                elif self._temp_codeline.type == G_CONST.Interpreter.CodeLineType.Run:
                    self.verify_validity_method()

                # 其他语句
                else:
                    self._task.cases[self._temp_codeline.region].steps.append(self._temp_codeline)


    # ----------------------------------------------------------------------
    def _give_global_assignment(self, give_name: str, give_value: str):
        """
        [ 公域赋值封装 ]
        
        """
        give_path_node = give_name.split(G_CONST.Interpreter.GrammarSymbol.VariablePath)
        give_path_node_number = len(give_path_node)
        current_node = self._task.namespace

        if give_path_node_number > 1:
            i = 1
            for node in give_path_node:
                if i == give_path_node_number:
                    current_node.update({node: give_value})
                else:
                    if node not in current_node.keys():
                        current_node.update({node: {}})
                    current_node = current_node[node]
                    i += 1
        else:
            self._task.namespace.update({give_name : give_value})


    # ----------------------------------------------------------------------
    def _running_common_function(self, name: str, paras: list):
        """
        [ 公域运行方法封装 ]
        
        """
        try:
            if name not in self.global_function_map.keys():
                raise

            # --------------------------------------------------------------
            # 解析方法参数
            # --------------------------------------------------------------
            if len(paras) > 0:
                new_function_value = []

                for value in paras:
                    if isinstance(value, str):
                        value_quote_symbol_count = value[0:2].count(G_CONST.Interpreter.GrammarSymbol.Quote)
                        para = value[value_quote_symbol_count:]
                        para_statement_symbol_count = para.count(G_CONST.Interpreter.GrammarSymbol.VariablePath)

                        if para_statement_symbol_count != 0:
                            current_node = self._task.namespace
                            para_nodes = para.split(G_CONST.Interpreter.GrammarSymbol.VariablePath)

                            if len(para_nodes) > 1:
                                for node in para_nodes:
                                    try:
                                        current_node = current_node[node]
                                    except KeyError:
                                        error_message = G_CONST.Error.Interpreter.GrammarNamespaceNodeNotExist('#NODE#', node)
                                        AwakenTaskPretreatmentError(error_message)
                            else:
                                try:
                                    current_node = current_node[para_nodes[0]]
                                except:
                                    error_message = G_CONST.Error.Interpreter.GrammarNamespaceNodeNotExist('#NODE#', node)
                                    AwakenTaskPretreatmentError(error_message)

                            new_function_value.append(current_node)

                        else:
                            # 如果 para 存在于全局命名空间中则取出, 否则视为普通字符串
                            if para in self._task.namespace.keys():
                                new_function_value.append(self._task.namespace[para])
                                continue
                            else:
                                new_function_value.append(para)
                                continue

                    else:
                        new_function_value.append(value)

            result = self.global_function_map[name](G_GLOBAL_METHOD, *new_function_value)
            return result

        except KeyError:
            raise AwakenInterpreterMethodWrongFul(
                    self._temp_codeline.number,
                    self._temp_codeline.base_code,
                    name
                )


    # ----------------------------------------------------------------------
    def verify_validity_method(self):
        """
        [ 校验方法的有效性 ]

        """
        function_map = None
        if self._temp_codeline.funtion_region == G_CONST.Interpreter.CodeLineScopet.Global:
            function_map = self.global_function_map.keys()
        else:
            function_map = self.engine_function_map.keys()

        if self._temp_codeline.funtion_name in function_map:
            self._task.cases[self._temp_codeline.region].steps.append(self._temp_codeline)

        else:
            raise Exception
