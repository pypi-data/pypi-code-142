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
[ Awaken脚本语言解释器 ]

"""
from pathlib import Path

from .base_code_converter import BaseCodeConverter
from ...baseic.keyword import G_KEYWORD
from ...baseic.common.configure import G_CONFIGURE
from ...baseic.structural.interpreter import AwakenTask
from ...baseic.error.interpreter import AwakenInterpreterFileIsEmpty


class GrammarParser: ...


# --------------------------------------------------------------------------
class GrammarParser:
    """
    [ Awaken脚本语言解释器 ]

    """
    _base_code_converter: BaseCodeConverter
    """ 底层编码转换类 """

    
    # ----------------------------------------------------------------------
    def __init__(self) -> None:
        self._base_code_converter = BaseCodeConverter()


    # ----------------------------------------------------------------------
    def parsing_file(self, script_file_path: str | Path):
        """
        [ 解析自文件 ]

        ---
        描述
        - 解析本地的 Awaken 文件, 值得注意的是, 运行本地任务不会写入到数据库。

        ---
        参数
        - script_file_path : { str | Path } - 脚本文件路径。

        ---
        返回
        - AwakenTask : Awaken任务对象。

        """
        translation = self._base_code_converter.convert_file(script_file_path)

        if len(translation.codelines) == 0:
            raise AwakenInterpreterFileIsEmpty

        if G_CONFIGURE.get(G_KEYWORD.Common.Config.Debug):
            print('-------')
            for code in translation.codelines:
                print(code)
            print('-------')

        return AwakenTask(translation, False, 0)


    # ----------------------------------------------------------------------
    def parsing_json(self, script_codelines: list, task_type: str, database_task_id: int):
        """
        [ 解析自语句集 ]

        ---
        描述
        - 解析本地的 Awaken 文件, 值得注意的是, 运行本地任务不会写入到数据库。

        ---
        描述:
            NULL

        """
        translation = self._base_code_converter.convert_codelines(script_codelines, task_type)

        if len(translation.codelines) == 0:
            raise AwakenInterpreterFileIsEmpty

        if G_CONFIGURE.get(G_KEYWORD.Common.Config.Debug):
            print('-------')
            for code in translation.codelines:
                print(code)
            print('-------')

        return AwakenTask(translation, True, database_task_id)



# --------------------------------------------------------------------------
GRAMMAR_PARSER = GrammarParser()
""" Awaken脚本语言解释器实例 """
