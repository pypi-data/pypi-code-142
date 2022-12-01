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
[ 引擎代理 ]

"""
from .web.web_runner import WebRunner
from ..baseic.const import G_CONST
from ..baseic.structural.interpreter import AwakenTask
from ..core.interpreter.task_preprocessor import TaskPreprocessor


# --------------------------------------------------------------------------
class EngineAgency:
    """
    [ 引擎代理 ]

    """
    task_preprocessor: TaskPreprocessor
    """ 任务预处理程序 """


    # ----------------------------------------------------------------------
    def __init__(self) -> None:
        self.task_preprocessor = TaskPreprocessor()


    # ----------------------------------------------------------------------
    def start(self, task: AwakenTask):
        task = self.task_preprocessor.pretreatment(task)

        if task.translation.type == G_CONST.Type.Task.Web:
            runner = WebRunner(task)
            runner.start()
