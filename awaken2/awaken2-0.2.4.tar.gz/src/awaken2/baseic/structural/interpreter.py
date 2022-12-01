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
解释器结构体

"""
from ..const import G_CONST
from ..common.convert import try_converting_string_format
from ..error.interpreter import AwakenInterpreterParseException


class AwakenTranslation: ...
class AwakenTask: ...
class AwakenCase: ...
class AwakenCodeLine: ...


# --------------------------------------------------------------------------
class AwakenTranslation:
    """
    [ Awaken译文对象 ]

    ---
    描述
    - 该对象描述从 Awaken 语句集中解析翻译而来的底层译文与其他信息。

    """
    type: str
    codelines: list


    # ----------------------------------------------------------------------
    def __init__(self, type: str, codeline: list) -> ...:
        self.type = type
        self.codelines = codeline


# --------------------------------------------------------------------------
class AwakenTask:
    """ 
    [ Awaken任务对象 ]

    ---
    描述
    - 该对象描述自动化任务的完整信息。

    """
    translation: AwakenTranslation
    is_encapsulated: bool
    is_write_database: bool
    database_task_id: int
    namespace: dict
    cases: dict[str, AwakenCase]
    task_type: str


    # ----------------------------------------------------------------------
    def __init__(
        self, 
        translation: AwakenTranslation,
        is_write_database: bool, 
        database_task_id: int,
    ) -> ...:
        self.translation = translation
        self.is_write_database = is_write_database
        self.database_task_id = database_task_id
        self.task_type = translation.type


# --------------------------------------------------------------------------
class AwakenCase:
    """ 
    [ Awaken用例对象 ]

    ---
    描述
    - 该对象描述自动化任务用例的相关信息。

    """
    number: int
    name: str
    docs: str
    decorator: dict
    namespace: dict
    steps: list[AwakenCodeLine]

    def __init__(self, number, name, docs='', *_) -> ...:
        self.number = number
        self.name = name
        self.docs = docs
        self.decorator = {}
        self.namespace = {}
        self.steps = []


# --------------------------------------------------------------------------
class AwakenCodeLine:
    """ 
    [ Awaken代码行对象 ]

    ---
    描述
    - 该对象描述代码行的相关信息。

    """
    base_code: str
    number: int
    region: str
    type: str
    give_region: str
    give_name: str
    give_value: str
    funtion_region: str
    funtion_name: str
    funtion_value: str
    case_name: str
    case_docs: str
    decorator_key: str
    decorator_value: str
    assert_value: str


    # ----------------------------------------------------------------------
    def __init__(self, codeline: str) -> ...:
        self.base_code   = codeline
        codeline_splint = codeline.split(' ')
        self.number     = codeline_splint[0]
        self.region     = codeline_splint[1]
        self.type       = codeline_splint[2]

        if self.type == G_CONST.Interpreter.CodeLineType.Give:
            _give_splint     = codeline_splint[3].split(G_CONST.Interpreter.GrammarSymbol.ScopePrefix)
            self.give_region = _give_splint[0]
            self.give_name   = _give_splint[1]
            self.give_value  = try_converting_string_format(codeline_splint[4])

        elif self.type == G_CONST.Interpreter.CodeLineType.RGive:
            _give_splint        = codeline_splint[3].split(G_CONST.Interpreter.GrammarSymbol.ScopePrefix)
            _run_splint         = codeline_splint[4].split(G_CONST.Interpreter.GrammarSymbol.ScopePrefix)
            self.give_region    = _give_splint[0]
            self.give_name      = _give_splint[1]
            self.funtion_region = _run_splint[0]
            self.funtion_name   = _run_splint[1]
            self.funtion_value  = []
            if len(codeline_splint) >= 6:
                for value in codeline_splint[5:]:
                    self.funtion_value.append(try_converting_string_format(value))

        elif self.type == G_CONST.Interpreter.CodeLineType.Run:
            _run_splint         = codeline_splint[3].split(G_CONST.Interpreter.GrammarSymbol.ScopePrefix)
            self.funtion_region = _run_splint[0]
            self.funtion_name   = _run_splint[1]
            self.funtion_value  = []
            if len(codeline_splint) >= 5:
                for value in codeline_splint[4:]:
                    self.funtion_value.append(try_converting_string_format(value))

        elif self.type == G_CONST.Interpreter.CodeLineType.SCase:
            self.case_name = codeline_splint[3]
            self.case_docs = codeline_splint[4] if len(codeline_splint) == 5 else ''

        elif self.type == G_CONST.Interpreter.CodeLineType.SDecorator:
            self.decorator_key   = codeline_splint[2]
            self.decorator_value = codeline_splint[3]

        elif self.type == G_CONST.Interpreter.CodeLineType.Assert:
            self.assert_value = codeline_splint[3:]

        else:
            raise AwakenInterpreterParseException
