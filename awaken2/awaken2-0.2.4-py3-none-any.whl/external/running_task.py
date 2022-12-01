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
命令行指令 - 运行任务

"""
from pathlib import Path

from ..baseic.const import G_CONST
from ..baseic.common.template_rendering import G_TEMPLATE_RENDERING


# --------------------------------------------------------------------------
def instruction_running_task(argv: list):
    """
    [ 命令行指令 - 运行任务 ]
                                                                          
    ---
    参数:
    - argv : { list } - 参数列表。

    """
    if not G_CONST.Path.FilePath.EngineeringInit.exists():
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 运行任务',
            is_show_number=False,
            source=[
                '当前运行路径不是工程根目录;',
                '请在工程根目录执行该命令.'
            ],
        )
        exit(0)

    task_list = []
    def recursive_search_tasks(flist: list):
        for f in flist:
            if f.is_dir():
                nlist = list(f.glob('*'))
                recursive_search_tasks(nlist)
            else:
                if f.suffix[1:-4] == 'awaken':
                    task_list.append(f)

    if len(argv) >= 1:
        # 循环解析任务参数
        for task_arg in argv:
            if task_arg in ['.', '/', './', 'all', 'ALL']:
                task_arg_path = G_CONST.Path.CONSOLE_CWD
                task_projects = list(task_arg_path.glob('*'))
                recursive_search_tasks(task_projects)

            else:
                task_arg_path = Path(task_arg).resolve()
                # 如果参数路径指向目录
                if task_arg_path.is_dir():
                    task_projects = list(task_arg_path.glob('*'))
                    recursive_search_tasks(task_projects)

                # 如果参数路径指向文件
                else:
                    if task_arg_path.exists():
                        task_list.append(task_arg_path)


        if not G_CONST.Path.FilePath.EngineeringInit.exists():
            G_TEMPLATE_RENDERING.render_print(
                title='Awaken - 运行任务',
                is_show_number=False,
                source=[
                    '暂无任务可供执行 !',
                ],
            )
            exit(0)

        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 运行任务',
            is_show_number=False,
            source=[
                '多进程执行器正在消耗任务 ...',
                '等待执行的任务:',
                *[tn.name for tn in task_list]
            ],
        )

        from ..core.perform.perform_pool import PerFormPool
        from ..core.interpreter.grammar_parser import GrammarParser
        grammar_parser = GrammarParser()
        perform_pool = PerFormPool()
        for task in task_list:
            task = grammar_parser.parsing_file(task)
            perform_pool.put_task(task)
        perform_pool.running()
    
    else:
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 运行任务',
            is_show_number=False,
            source=[
                '运行任务指令参数异常 !',
                '示例:',
                '>> awaken -run task1',
                '>> awaken -run task1 task2',
                '>> awaken -run project1',
                '>> awaken -run .',
            ],
        )
        exit(0)
