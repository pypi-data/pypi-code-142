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
解释器模块相关异常

"""
from .baseic import AwakenBaseError


# --------------------------------------------------------------------------
class AwakenInterpreterParseException(AwakenBaseError):
    """ [ 解释器异常::解析出现异常 ] """


# --------------------------------------------------------------------------
class AwakenInterpreterFileIsEmpty(AwakenBaseError):
    """ [ 解释器异常::脚本文件为空 ] """


# --------------------------------------------------------------------------
class AwakenInterpreterSymbolWrongFul(AwakenBaseError):
    """ [ 解释器异常::语法符不合法 ] """

    def __init__(
        self, 
        codeline_number: int, 
        codeline_content: str,
        error_symbol: str,
    ):
        self.codeline_number = codeline_number
        self.codeline_content = codeline_content
        self.error_symbol = error_symbol
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'编码行数: {self.codeline_number}',
            f'编码语句: {self.codeline_content}',
            f'上述语句中的语法符 "{ self.error_symbol }" 不合法 .',
            '通过 awaken -help 或相关的文档寻求帮助 .'
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenInterpreterStatementWrongFul(AwakenBaseError):
    """ [ 解释器异常::关键字不合法 ] """

    def __init__(
        self, 
        codeline_number: int, 
        codeline_content: str,
        error_keyword: str,
    ):
        self.codeline_number = codeline_number
        self.codeline_content = codeline_content
        self.error_keyword = error_keyword
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'编码行数: {self.codeline_number}',
            f'编码语句: {self.codeline_content}',
            f'上述语句中的关键字 "{ self.error_keyword }" 不合法 .',
            '通过 awaken -help 或相关的文档寻求帮助 .'
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenInterpreterStatementNoParameters(AwakenBaseError):
    """ [ 解释器异常::语法声明关键字无参数 ] """

    def __init__(
        self, 
        codeline_number: int, 
        codeline_content: str,
        error_keyword: str,
    ):
        self.codeline_number = codeline_number
        self.codeline_content = codeline_content
        self.error_keyword = error_keyword
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'编码行数: {self.codeline_number}',
            f'编码语句: {self.codeline_content}',
            f'上述语句中的关键字 "{ self.error_keyword }" 没有携带参数 .',
            '通过 awaken -help 或相关的文档寻求帮助 .'
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenInterpreterCaseNotLogicAssert(AwakenBaseError):
    """ [ 解释器异常::用例未断言 ] """

    def __init__(self, case_name: str):
        self.case_name = case_name
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'用例 "{ self.case_name }" 未完成断言 .',
            '通过 awaken -help 或相关的文档寻求帮助 .'
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenInterpreterBaseCodeLineTypeError(AwakenBaseError):
    """ [ 解释器异常::语法底层编码行类型异常 ] """

    def __init__(self, base_code_line_type: str):
        self.base_code_line_type = base_code_line_type
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'无法识别的编码行类型 "{ self.base_code_line_type }" .',
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenInterpreterMethodWrongFul(AwakenBaseError):
    """ [ 解释器异常::方法不合法 ] """

    def __init__(
        self, 
        codeline_number: int, 
        codeline_content: str,
        error_method_name: str,
    ):
        self.codeline_number = codeline_number
        self.codeline_content = codeline_content
        self.error_method_name = error_method_name
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'编码行数: {self.codeline_number}',
            f'编码语句: {self.codeline_content}',
            f'上述语句中的方法关键字 "{ self.error_method_name }" 不是合法的方法 .',
            '通过 awaken -help 或相关的文档寻求帮助 .'
        ]
        return super().__str__()


# --------------------------------------------------------------------------
class AwakenInterpreterNamespaceNodeNotExist(AwakenBaseError):
    """ [ 解释器异常::语法命名空间不存在节点 ] """

    def __init__(self, node_name: str):
        self.node_name = node_name
        super().__init__()

    def __str__(self) -> str:
        self.bas_message = [
            f'命名空间不存在节点 "{ self.node_name }" .',
        ]
        return super().__str__()
