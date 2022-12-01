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
[ 项目管理器 ]

"""
import shutil
from pathlib import Path

from ..const import G_CONST
from ..broadcast.awaken_log import G_LOG
from ..error.project import AwakenProjectInitNotExistsError
from ..error.project import AwakenEngineeringInitNotExistsError
from ...kit.common import TASK_TEMPLATE_MAP
from ...baseic.decorator.baseic import deco_singleton


SCRIPT_FILE_LOCAT_RULES = '*.awaken-*'
""" 脚本文件定位正则规则 """


# --------------------------------------------------------------------------
@deco_singleton
class ProjectFileHandle:
    """
    [ 项目管理器 ]

    ---
    描述
    - 用以管理本地的项目文件。
    
    """


    # ----------------------------------------------------------------------
    def get_projects(self) -> list[str]:
        """
        [ 获取本地项目列表 ]

        ---
        描述
        - 在本地工程目录中获取项目列表。

        ---
        返回
        - list[str] : 本地项目列表。

        """
        self._check_engineering_catalog()
        project_list = []
        for path in list(G_CONST.Path.ACTUALLY_CWD.glob('*')):
            try:
                if self._check_project_catalog(path):
                    project_list.append(path.stem)
            except AwakenProjectInitNotExistsError:
                ...
        return project_list


    # ----------------------------------------------------------------------
    def get_tasks(self, project_name: str) -> list[str]:
        """
        [ 获取本地项目的任务列表 ]

        ---
        描述
        - 在本地工程的项目目录中获取任务列表。

        ---
        返回
        - list[str] : 本地任务路径对象列表。

        """
        project_path = self._name_converted_to_path_object(project_name)
        self._check_project_catalog(project_path)
        return [name.stem for name in list(project_path.glob(SCRIPT_FILE_LOCAT_RULES))]


    # ----------------------------------------------------------------------
    def project_create(self, name: str | list) -> dict[str:bool]:
        """
        [ 项目创建 ]

        ---
        描述
        - 在本地工程目录中创建项目。

        ---
        参数
        - name : { str | list} - 项目名称, 传递列表则批量创建。

        ---
        返回
        - dict[str: bool] : 项目创建结果字典。
        
        """
        self._check_engineering_catalog()
        name = self._name_format_processing(name)
        create_results = {}
        for pn in name:
            try:
                pp = G_CONST.Path.ACTUALLY_CWD.joinpath(pn)
                if not pp.exists():
                    pp.mkdir(parents=True, exist_ok=True)
                    pp.joinpath(G_CONST.Name.FileName.ProjectInit).touch(mode=0o777, exist_ok=True)
                create_results.update({pn : True})

            except BaseException as error:
                G_LOG.error(f'创建项目异常 :: {error}')
                create_results.update({pn : False})

        return create_results


    # ----------------------------------------------------------------------
    def project_delete(self, name: str | list) -> dict[str:bool]:
        """
        [ 项目删除 ]

        ---
        描述
        - 在本地工程目录中创建项目。

        ---
        参数
        - name : { str | list} - 项目名称, 传递列表则批量删除。

        ---
        返回
        - dict[str: bool] : 项目删除结果字典。
        
        """
        self._check_engineering_catalog()
        name = self._name_format_processing(name)
        delete_results = {}
        for pn in name:
            try:
                pp = G_CONST.Path.ACTUALLY_CWD.joinpath(pn)
                if pp.exists():
                    shutil.rmtree(pp)
                    delete_results.update({pn : True})
                else:
                    raise

            except BaseException as error:
                G_LOG.error(f'删除项目异常 :: {error}')
                delete_results.update({pn : False})

        return delete_results


    # ----------------------------------------------------------------------
    def project_rename(self, old_name: str | list, new_name: str | list) -> dict[str:str]:
        """
        [ 项目重命名 ]

        ---
        描述
        - 在本地工程目录中更新项目的名称。

        ---
        参数
        - old_name : { str | list} - 旧项目名称, 传递列表则批量重命名, 如果传递列表时需与 new_name 的值一一对应。
        - new_name : { str | list} - 新项目名称, 传递列表则批量重命名, 如果传递列表时需与 old_name 的值一一对应。

        ---
        返回
        - dict[str: bool] : 项目重命名结果字典。
        
        """
        self._check_engineering_catalog()
        old_name = self._name_format_processing(old_name)
        new_name = self._name_format_processing(new_name)
        rename_results = {}
        for oldn, newn in dict(zip(old_name, new_name)).items():
            try:
                oldp = G_CONST.Path.ACTUALLY_CWD.joinpath(oldn)
                newp = G_CONST.Path.ACTUALLY_CWD.joinpath(newn)
                if oldp.exists() \
                and self._check_project_catalog(oldp) \
                and not newp.exists():
                    oldp.rename(newp)
                    rename_results.update({oldn : True})
                else:
                    raise

            except BaseException as error:
                G_LOG.error(f'项目重命名异常 :: {error}')
                rename_results.update({oldn : False})
        
        return rename_results


    # ----------------------------------------------------------------------
    def task_create(self, project_name: str, task_type: str, task_name: str | list) -> dict[str:str]:
        """
        [ 任务创建 ]

        ---
        描述
        - 在本地项目目录中创建任务文件。

        ---
        参数
        - project_name : { str } - 项目目录名称。
        - task_type : { str } - 任务类型。
        - task_name : { str | list} - 任务名称, 传递列表则批量创建。

        ---
        返回
        - dict[str: bool] : 任务创建结果字典。
        
        """
        task_name = self._name_format_processing(task_name)
        project_path = self._name_converted_to_path_object(project_name)
        self._check_project_catalog(project_path)

        if task_type.upper() not in TASK_TEMPLATE_MAP:
            raise

        create_results = {}
        for btn in task_name:
            try:
                task_name = f'{btn}.awaken-{task_type.lower()}'
                task_path = project_path.joinpath(task_name)
                if not task_path.exists():
                    task_template = TASK_TEMPLATE_MAP[task_type.upper()]
                    task_template = task_template.replace('#TASK_NAME#', btn)
                    task_template = task_template.replace('#TASK_TYPE#', task_type.upper())
                    task_path.touch(mode=0o777)
                    task_path.write_bytes(bytes(task_template, encoding='UTF8'))
                create_results.update({btn : True})

            except BaseException as error:
                G_LOG.error(f'创建任务异常 :: {error}')
                create_results.update({btn : False})

        return create_results


    # ----------------------------------------------------------------------
    def task_delete(self, project_name: str, task_name: str | list) -> dict[str:str]:
        """
        [ 任务删除 ]

        ---
        描述
        - 在本地项目目录中删除任务文件。

        ---
        参数
        - project_name : { str } - 项目目录名称。
        - task_name : { str | list} - 任务名称, 传递列表则批量删除。

        ---
        返回
        - dict[str: bool] : 任务删除结果字典。
        
        """
        task_name = self._name_format_processing(task_name)
        project_path = self._name_converted_to_path_object(project_name)
        self._check_project_catalog(project_path)

        delete_results = {}
        task_glob = list(project_path.glob(SCRIPT_FILE_LOCAT_RULES))
        project_tasks = dict(zip([n.stem for n in task_glob], task_glob))

        for task_name in task_name:
            try:
                if task_name in project_tasks.keys():
                    project_tasks[task_name].unlink()
                    delete_results.update({task_name : True})
                else:
                    raise

            except BaseException as error:
                G_LOG.error(f'删除任务异常 :: {error}')
                delete_results.update({task_name : False})

        return delete_results


    # ----------------------------------------------------------------------
    def task_rename(self, project_name: str, old_task_name: str | list, new_task_name: str | list) -> dict[str:str]:
        """
        [ 任务重命名 ]

        ---
        描述
        - 在本地工程的项目目录中更新任务的名称。

        ---
        参数
        - project_name : { str } - 项目目录名称。
        - old_task_name : { str | list} - 旧任务名称, 传递列表则批量重命名, 如果传递列表时需与 new_name 的值一一对应。
        - new_task_name : { str | list} - 新任务名称, 传递列表则批量重命名, 如果传递列表时需与 old_name 的值一一对应。

        ---
        返回
        - dict[str: bool] : 项目重命名结果字典。
        
        """
        old_task_name = self._name_format_processing(old_task_name)
        new_task_name = self._name_format_processing(new_task_name)
        project_path = self._name_converted_to_path_object(project_name)
        self._check_project_catalog(project_path)

        rename_results = {}
        for oldn, newn in dict(zip(old_task_name, new_task_name)).items():
            try:
                project_file_glob = list(project_path.glob(SCRIPT_FILE_LOCAT_RULES))
                project_task_list = dict(zip([n.stem for n in project_file_glob], project_file_glob))
                if oldn in project_task_list.keys():
                    oldp = project_task_list[oldn]
                    newp = oldp.with_stem(newn)
                    oldp.rename(newp)
                    rename_results.update({oldn : True})
                else:
                    raise

            except BaseException as error:
                G_LOG.error(f'任务重命名异常 :: {error}')
                rename_results.update({oldn : False})
        
        return rename_results

    
    # ----------------------------------------------------------------------
    def _check_engineering_catalog(self, path: Path = None) -> bool:
        """ 
        [ 检查工程目录 ]

        ---
        描述
        - 检查当前运行域是否是工程根目录。

        ---
        参数
        - path : { Path } - 工程目录路径对象, 为空则表示当前运行域。

        """
        engineering_path = path if path else G_CONST.Path.ACTUALLY_CWD
        if not engineering_path.joinpath(G_CONST.Name.FileName.EngineeringInit).exists():
            raise AwakenEngineeringInitNotExistsError([
                '当前目录非工程目录 !',
                '通过 "awaken -init" 命令初始化工程 .'
            ])
        return True


    # ----------------------------------------------------------------------
    def _check_project_catalog(self, path: Path = None) -> bool:
        """ 
        [ 检查项目目录 ]

        ---
        描述
        - 检查当前运行域是否是项目根目录。

        ---
        参数
        - path : { Path } - 项目目录路径对象, 为空则表示当前运行域。

        """
        project_path: Path
        if path:
            if not path.exists():
                raise AwakenProjectInitNotExistsError([
                f'项目路径"{path}"不存在 !',
                '请于工程根目录中创建项目目录, 再创建任务 .'
            ])
            project_path = path
        else:
            project_path = G_CONST.Path.ACTUALLY_CWD

        if not project_path.joinpath(G_CONST.Name.FileName.ProjectInit).exists():
            raise AwakenProjectInitNotExistsError([
                '当前目录非工程的项目目录(缺少项目ini) !',
                '请于工程根目录中创建项目目录, 再进入项目目录中创建任务 .'
            ])
        return True
    

    # ----------------------------------------------------------------------
    def _name_converted_to_path_object(self, name: str = None):
        if not name:
            return G_CONST.Path.ACTUALLY_CWD
        else:
            return G_CONST.Path.ACTUALLY_CWD.joinpath(name)


    # ----------------------------------------------------------------------
    def _name_format_processing(self, name: str | list) -> list:
        if isinstance(name, str):
            name = [name]
        return name


# --------------------------------------------------------------------------
G_PROJECT_FILE_HANDLE = ProjectFileHandle()
""" 项目管理器全局实例 """
