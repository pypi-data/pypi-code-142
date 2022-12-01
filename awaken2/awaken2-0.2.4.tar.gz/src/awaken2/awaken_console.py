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
[ Awaken 命令行工具 ]

---
描述
    - 该模块用于通过命令行的方式调用 Awaken。

"""
import sys

from .baseic.common.template_rendering import G_TEMPLATE_RENDERING


# --------------------------------------------------------------------------
# 命令行工具 Main 入口
# --------------------------------------------------------------------------
def main() -> ...:
    command    = 'order'  # 现持有命令
    parameters = []       # 现持有参数


    # ----------------------------------------------------------------------
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        argv    = sys.argv[2:]


    # ----------------------------------------------------------------------
    if command in ['order', '-order', '-o']:
        from .external.order import instruction_order
        instruction_order()


    # ----------------------------------------------------------------------
    elif command in ['init', '-init', '-i']:
        from .external.init_engineering import instruction_init_engineering
        instruction_init_engineering()


    # ----------------------------------------------------------------------
    elif command in ['make', '-make', '-m']:
        from .external.create_project import instruction_create_project
        instruction_create_project(argv)


    # ----------------------------------------------------------------------
    elif command in ['task', '-task', '-t']:
        from .external.create_task import instruction_create_task
        instruction_create_task(argv)


    # ----------------------------------------------------------------------
    elif command in ['run', '-run', '-r']:
        from .external.common import confirm_root_directory_runtime_project
        from .external.running_task import instruction_running_task
        confirm_root_directory_runtime_project()
        instruction_running_task(argv)


    # ----------------------------------------------------------------------
    elif command in ['server', '-server', '-s']:
        from .external.common import confirm_root_directory_runtime_project
        from .external.running_server import instruction_running_server
        confirm_root_directory_runtime_project()
        instruction_running_server(argv)


    # ----------------------------------------------------------------------
    elif command in ['help', '-help', '-h']:
        from .external.help import instruction_help
        instruction_help()


    # ----------------------------------------------------------------------
    elif command in ['version', '-version', '-v']:
        from .external.version import instruction_version
        instruction_version()


    # ----------------------------------------------------------------------
    elif command in ['update', '-update', '-u']:
        from .external.update import instruction_update
        instruction_update()


    # ----------------------------------------------------------------------
    else:
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken',
            is_show_number=False,
            source=[
                f'没有这样的指令:: [{ command }] !'
            ],
        )
        exit(0)
