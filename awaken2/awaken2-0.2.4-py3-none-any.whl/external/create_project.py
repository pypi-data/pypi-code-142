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
命令行指令 - 创建项目

"""
from ..baseic.common.template_rendering import G_TEMPLATE_RENDERING
from ..baseic.environment.project_file_handle import G_PROJECT_FILE_HANDLE


# --------------------------------------------------------------------------
def instruction_create_project(argv: list):
    """
    [ 命令行指令 - 创建项目 ]

    ---
    参数
    - argv : { list } - 参数列表。

    """
    if len(argv) >= 1:
        projects = argv[0:]
        
        G_PROJECT_FILE_HANDLE.project_create(projects)
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 创建项目',
            is_show_number=False,
            source=[
                '项目创建成功:',
                *projects
            ],
        )

    else:
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 创建项目',
            is_show_number=False,
            source=[
                '创建项目指令参数异常 !',
                '示例:',
                '>> awaken -make project',
                '>> awaken -make project1 project2',
            ],
        )
    exit(0)
