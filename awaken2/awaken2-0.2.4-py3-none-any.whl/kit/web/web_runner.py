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
WEB执行器

"""
import time
import asyncio

from playwright.async_api import async_playwright

from .web_engine import WebEngine
from .web_engine_method_map import WEB_ENGINE_FUNCTION_MAP
from ...baseic.const import G_CONST
from ...baseic.keyword import G_KEYWORD
from ...baseic.common.configure import G_CONFIGURE
from ...baseic.error.baseic import G_ERROR_RECORDER
from ...baseic.structural.interpreter import AwakenTask
from ...baseic.structural.interpreter import AwakenCase
from ...baseic.structural.interpreter import AwakenCodeLine
from ...baseic.common.convert import try_converting_string_format
from ...baseic.error.engine import AwakenTaskPretreatmentError
from ...baseic.error.interpreter import AwakenInterpreterParseException
from ...baseic.error.interpreter import AwakenInterpreterStatementWrongFul
from ...baseic.error.interpreter import AwakenInterpreterStatementNoParameters
from ...baseic.error.interpreter import AwakenInterpreterCaseNotLogicAssert
from ...baseic.error.interpreter import AwakenInterpreterBaseCodeLineTypeError
from ...baseic.error.interpreter import AwakenInterpreterMethodWrongFul
from ...baseic.error.interpreter import AwakenInterpreterNamespaceNodeNotExist
from ...kit.global_method import G_GLOBAL_METHOD
from ...kit.global_method_map import GLOBAL_METHOD_FUNCTION_MAP
from ...server.db.broker.db_task_record_broker import DbTaskRecordBroker


# --------------------------------------------------------------------------
class WebRunner:
    """
    [ WEB执行器 ]

    """
    _task: AwakenTask
    _web_engine: WebEngine
    _use_case_in_execution: AwakenCase
    _task_db_broker: DbTaskRecordBroker


    # ----------------------------------------------------------------------
    def __init__(self, task: AwakenTask) -> None:
        self._task = task
        self._task_db_broker = DbTaskRecordBroker(task)


    # ----------------------------------------------------------------------
    def start(self):
        """
        [ 开始任务 ]

        """
        return asyncio.run(self._async_running_task())


    # ----------------------------------------------------------------------
    async def _async_running_task(self):
        """
        [ 协程执行任务 ]

        """
        task_state = G_CONST.State.Result.Null

        try:
            async with async_playwright() as playwright:
                # 创建并激活引擎
                self._web_engine = WebEngine()
                self._web_engine._init_playwright(playwright)

                # 数据库创建任务
                if self._task.is_write_database:
                    self._task_db_broker.created_task(
                        str(self._task.namespace[G_KEYWORD.Script.Namespace.TaskName]),
                        str(self._task.namespace[G_KEYWORD.Script.Namespace.TaskDocs]),
                    )

                # 启动浏览器
                await self._web_engine._browser_start(browser_type=self._task.namespace[G_KEYWORD.Script.Decorator.BrowserType])

                # 遍历任务的用例
                for awaken_case in self._task.cases.values():
                    self._use_case_in_execution = awaken_case

                    # 数据库创建用例
                    if self._task.is_write_database:
                        self._task_db_broker.created_case(
                            str(self._use_case_in_execution.name),
                            str(self._use_case_in_execution.docs)
                        )

                    try:
                        case_state = G_CONST.State.Result.Null
                        case_run_step = ''

                        # 启动页面
                        await self._web_engine._page_start()

                        # 遍历用例的步骤
                        for awaken_codeline in self._use_case_in_execution.steps:

                            # 赋值逻辑
                            if awaken_codeline.type == G_CONST.Interpreter.CodeLineType.Give:
                                self._give_cases_assignment(
                                    awaken_codeline.give_region,
                                    awaken_codeline.give_name,
                                    awaken_codeline.give_value,
                                )

                            # 执行并赋值逻辑
                            elif awaken_codeline.type == G_CONST.Interpreter.CodeLineType.RGive:
                                result = await self._running_function(awaken_codeline)
                                self._give_cases_assignment(
                                    awaken_codeline.give_region,
                                    awaken_codeline.give_name,
                                    result,
                                )
                                
                            # 执行逻辑
                            elif awaken_codeline.type == G_CONST.Interpreter.CodeLineType.Run:
                                await self._running_function(awaken_codeline)

                            # 断言逻辑
                            elif awaken_codeline.type == G_CONST.Interpreter.CodeLineType.Assert:
                                assert_result = self.assert_logic(awaken_codeline.assert_value)

                                if assert_result == True:
                                    case_state = G_CONST.State.Result.Success
                                else:
                                    case_state = G_CONST.State.Result.Unsuccess

                    except BaseException as error:
                        case_state = G_CONST.State.Result.Error
                        case_run_step = str(error)
                        G_ERROR_RECORDER.record(str(error))

                    finally:
                        if self._task.is_write_database:
                            self._task_db_broker.update_case(case_state, case_run_step)

                    # 等待一秒之后关闭浏览器
                    time.sleep(1)
                    await self._web_engine._page_close()

                task_state = G_CONST.State.Result.Success
                if self._task.is_write_database:
                    self._task_db_broker.update_task(task_state, '')
                    
                await self._web_engine._exit()

        except BaseException as error:
            task_state = G_CONST.State.Result.Unsuccess
            if self._task.is_write_database:
                self._task_db_broker.update_task(task_state, '')

            G_ERROR_RECORDER.template_out()


    # ----------------------------------------------------------------------
    async def _running_function(self, codeline: AwakenCodeLine):
        """
        [ 运行方法 ]

        """
        try:
            function_map = None
            function_engine = None
            
            if codeline.funtion_region == G_CONST.Interpreter.CodeLineScopet.Local:
                function_map = WEB_ENGINE_FUNCTION_MAP
                function_engine = self._web_engine
            else:
                function_map = GLOBAL_METHOD_FUNCTION_MAP
                function_engine = G_GLOBAL_METHOD
            
            if codeline.funtion_name not in function_map.keys():
                raise

            new_function_value = self.parsing_method_parameters(codeline.funtion_value)

            if codeline.funtion_region == G_CONST.Interpreter.CodeLineScopet.Global:
                result = function_map[codeline.funtion_name](function_engine, *new_function_value)
            else:
                result = await function_map[codeline.funtion_name](function_engine, *new_function_value)
            return result

        except KeyError:
            raise AwakenInterpreterMethodWrongFul(
                    codeline.number,
                    codeline.base_code,
                    codeline.funtion_name,
                )


    # ----------------------------------------------------------------------
    def _give_cases_assignment(self, give_region: str, give_name: str, give_value: str):
        """
        [ 私域赋值封装 ]

        """
        give_path_node = give_name.split(G_CONST.Interpreter.GrammarSymbol.Statement)
        give_path_node_number = len(give_path_node)
        current_node = None
        if give_region == G_CONST.Interpreter.CodeLineScopet.Local:
            current_node = self._use_case_in_execution.namespace
        else:
            current_node = self._task.namespace
        i = 1
        if give_path_node_number > 1:
            for node in give_path_node:
                if i == give_path_node_number:
                    current_node.update({node: give_value})
                else:
                    if node not in current_node.keys():
                        current_node.update({node: {}})
                    current_node = current_node[node]
                    i += 1
        else:
            current_node.update({give_name: give_value})


    # ----------------------------------------------------------------------
    def assert_logic(self, assert_value: list):
        condition_count = len(assert_value)
        assert_result = None

        if condition_count == 1:
            calculation_member = [assert_value[0]]
            assert_result = try_converting_string_format(self.parsing_method_parameters(calculation_member)[0])
            
        elif condition_count == 3:
            calculation_symbol = assert_value[1]
            calculation_lvalue = try_converting_string_format(self.parsing_method_parameters([assert_value[0]])[0])
            calculation_rvalue = try_converting_string_format(self.parsing_method_parameters([assert_value[2]])[0])

            try:
                if type(calculation_lvalue) != type(calculation_rvalue):
                    raise AwakenInterpreterParseException('断言异常 :: 参与断言的左值与右值类型不一致 !')
                if calculation_symbol == '==':
                    assert_result = calculation_lvalue == calculation_rvalue
                elif calculation_symbol == '>':
                    assert_result = calculation_lvalue > calculation_rvalue
                elif calculation_symbol == '>=':
                    assert_result = calculation_lvalue >= calculation_rvalue
                elif calculation_symbol == '<':
                    assert_result = calculation_lvalue < calculation_rvalue
                elif calculation_symbol == '<=':
                    assert_result = calculation_lvalue <= calculation_rvalue

            except Exception:
                return False

        return assert_result == True


    # ----------------------------------------------------------------------
    def parsing_method_parameters(self, source_data: list):
        """
        [ 解析方法参数 ]

        """
        filter_data = []
        if len(source_data) > 0:
            for value in source_data:
                if isinstance(value, str):
                    value_quote_symbol_count = value[0:2].count(G_CONST.Interpreter.GrammarSymbol.Quote)
                    para = value[value_quote_symbol_count:]

                    if value_quote_symbol_count != 0:
                        current_node = self._task.namespace
                    else:
                        current_node = self._use_case_in_execution.namespace

                    para_statement_symbol_count = para.count(G_CONST.Interpreter.GrammarSymbol.VariablePath)
                    if para_statement_symbol_count != 0:
                        para_nodes = para.split(G_CONST.Interpreter.GrammarSymbol.VariablePath)

                        if len(para_nodes) > 1:
                            for node in para_nodes:
                                try:
                                    current_node = current_node[node]
                                except KeyError:
                                    raise AwakenInterpreterNamespaceNodeNotExist(node)
                        else:
                            try:
                                current_node = current_node[para_nodes[0]]
                            except:
                                raise AwakenInterpreterNamespaceNodeNotExist(node)

                        filter_data.append(current_node)

                    else:
                        # 如果 para 存在于私域命名空间中则取出, 否则视为普通字符串
                        if para in current_node.keys():
                            filter_data.append(current_node[para])
                        else:
                            filter_data.append(para)
                else:
                    filter_data.append(value)

        return filter_data
