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
命令行指令 - 创建任务

"""
from ..baseic.common.template_rendering import G_TEMPLATE_RENDERING
from ..baseic.environment.project_file_handle import G_PROJECT_FILE_HANDLE


# --------------------------------------------------------------------------
def instruction_create_task(argv: list):
    """
    [ 命令行指令 - 创建任务 ]

    ---
    参数
    - argv : { list } - 参数列表。

    """
    if len(argv) >= 3:
        project_name = argv[0]
        task_type    = argv[1]
        task_list    = argv[2:]

        G_PROJECT_FILE_HANDLE.task_create(project_name, task_type, task_list)
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 创建任务',
            is_show_number=False,
            source=[
                '任务创建成功:',
                *task_list
            ],
        )

    else:
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 创建任务',
            is_show_number=False,
            source=[
                '创建任务指令参数异常 !',
                '示例:',
                '>> awaken -task project web task',
                '>> awaken -task project web task1 task2',
            ],
        )

    exit(0)
