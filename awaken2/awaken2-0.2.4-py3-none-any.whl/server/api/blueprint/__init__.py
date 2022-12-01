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
[ 接口模块蓝图 ]

"""
from .api_user import blueprint_user
from .api_interpreter import blueprint_interpreter
from .api_processing import blueprint_processing
from .api_project import blueprint_project
from .api_tasks import blueprint_tasks
from .api_editor import blueprint_editor
from .api_runer import blueprint_runer
from .api_record_task import blueprint_record_task
from .api_record_case import blueprint_record_case


__all__ = [
    blueprint_user,
    blueprint_interpreter,
    blueprint_processing,
    blueprint_project,
    blueprint_tasks,
    blueprint_editor,
    blueprint_runer,
    blueprint_record_task,
    blueprint_record_case,
]
