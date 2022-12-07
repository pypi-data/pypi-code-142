# coding=utf-8

import pickle
import shutil
import logging
from collections import defaultdict
from importlib import import_module

from abc import abstractmethod, ABCMeta
from typing_extensions import Self
from exuse.extypings import SRecord
from typing import Any, Dict, Mapping, Sequence, List

from exuse.expath import create_dir, join, exists, isfile, abspath
from exuse import exio

from .env import EnvLoader
from .task import DepSet, Task
from .const import GRAPH_SAVING_TYPES
from .const import TASK_WAITING, TASK_RUNNING, TASK_SUCCESS, TASK_FAILED
from .const import TASK_GRAPH_WAITING, TASK_GRAPH_RUNNING, TASK_GRAPH_SUCCESS, TASK_GRAPH_FAILED


class BaseTaskGraph:
    """
    任务图模型：每个程序每执行一次为一个任务。
    一个程序在 n 个样本上执行 n 次生成 n 个任务。

    """
    __metaclass__ = ABCMeta
    GRAPH_WORKING_DIR = EnvLoader.GRAPH_WORKING_DIR

    def __init__(self, graph_name: str, output_dir: str, env: EnvLoader = None, kwargs=None):
        """
        Args:
            kwargs: 创建任务图时传入的其他参数，作为备份
        """
        self.graph_name = graph_name
        self.output_dir = create_dir(output_dir)
        self.env = env
        self.kwargs = kwargs

        self.tasks: Dict[str, Task] = {}
        self.START = Task('START')
        self.END = Task('END')

        # 模块单元的参数值，一般作为单元参数的默认值使用
        self.params: SRecord[dict] = {}
        self.templates: SRecord = {}

        self.sample_list_file = None

        self.meta_file = join(self.output_dir, 'meta.json')
        self.dumped_pkl_file = join(self.output_dir, f'taskgraph.pkl')
        self.commands_list_file = join(self.output_dir, 'commands.list')
        self.gv_file = join(self.output_dir, 'taskgraph.gv')
        self.gv_svg_file = join(self.output_dir, 'taskgraph.gv.svg')
        self.status_gv_file = join(self.output_dir, 'taskgraph.status.gv')
        self.status_gv_svg_file = join(self.output_dir, 'taskgraph.status.gv.svg')
        self.status_file = join(self.output_dir, 'status.json')

    # get_* 方法可以通过 grpc 方法批量访问
    #region

    def get_meta(self):
        return exio.load_json(self.meta_file)

    def get_commands(self):
        rows = exio.read_file(self.commands_list_file).strip().split('\n')
        return [r.split(' 🍍 ') for r in rows]

    def get_gv(self):
        return exio.read_file(self.gv_svg_file)

    def get_status_gv(self):
        return exio.read_file(self.status_gv_svg_file)

    def get_status(self):
        "任务状态"
        if exists(self.status_file):
            fst = exio.load_json(self.status_file)
        else:
            fst = {}
        data = {t: TASK_WAITING for t in self.tasks}
        for k in fst:
            data[k] = fst[k]
        return data

    def get_graph_status(self):
        "任务图状态"
        counts = defaultdict(int)
        for _, s in self.get_status().items():
            counts[s] += 1

        # 没有等待任务和运行中任务时，说明所有任务都处于成功或者失败状态
        # 此时任务图只可能是成功或者失败中的一种
        if counts['waiting'] + counts['running'] == 0:
            if counts['failed'] == 0:
                return TASK_GRAPH_SUCCESS
            else:
                return TASK_GRAPH_FAILED
        # 否则任务图只可能是等待或者运行中
        elif counts['running'] > 0:
            return TASK_GRAPH_RUNNING
        else:
            return TASK_GRAPH_WAITING

    #endregion

    @abstractmethod  # 子类型需要实现的抽象方法
    def define_graph(self, **kwargs):
        raise NotImplementedError('abstract metohd: define_graph')

    @property  # 按照依赖关系排好序的任务列表
    def ordered_tasks(self):
        tasks: List[Task] = []

        def _iterate(ts: List[Task]):
            if len(ts) == 0:
                return
            next_ts = []
            for t in ts:
                tasks.append(t)
                for c in t.children:
                    next_ts.append(c)
            _iterate(next_ts)

        _iterate([self.START])

        order = {}
        for i, t in enumerate(tasks):
            if t.task_name in ['START', 'END']:
                continue
            order[t.task_name] = i
        tasks = [tasks[i] for i in order.values()]

        if len(tasks) == 0:
            raise RuntimeError('no task appended in current graph')

        return tasks

    # 提供必要的参数，生成任务图
    def generate(self, **kwargs):

        # 子类需要实现的定义任务图方法 (self.tasks)
        self.define_graph(**kwargs)

        # 将没有依赖的任务挂载到 START 任务节点
        for task in self.tasks.values():
            if len(task.dependencies) != 0: continue
            for ik in task.unit.input_ports:
                task.set_dep(self.START, f'{task.task_name}#{ik}', ik)

        # 依次生成任务的执行命令
        for task in self.ordered_tasks:
            task.gen_command()

        ## SAVING ##

        # commands.list
        with open(self.commands_list_file, 'w') as wt:
            for task in self.ordered_tasks:
                print(f'{task.task_name} 🍍 {task.main_shell_cmd}', file=wt)

        # taskgraph.pkl
        with open(self.dumped_pkl_file, 'wb') as wb:
            pickle.dump(self, wb)

        # taskgraph.gv*
        self.draw()

        # meta.json
        meta = {'graph_name': self.graph_name}
        if self.kwargs: meta.update(self.kwargs)

        meta['tasks'] = {}
        for task in self.tasks.values():
            meta['tasks'][task.task_name] = {
                'task_name': task.task_name,
                'unit_name': task.unit_name,
                'outputs': task.computed_output_ports,
                'params': task.params,
            }
        exio.dump_json(meta, self.meta_file)

        return self

    # 绘制有向无环的任务图
    def draw(self, show_start=True, filename="taskgraph.gv", formats=None, node_styles=None):
        """
        Args:
            - `show_start` whether draw the START task node in the graph. Default `True`
            - `filename` output prefix. Default `'taskgraph.gv'` will generate four files
                - taskgraph.gv
                - taskgraph.gv.png
                - taskgraph.gv.svg
                - taskgraph.gv.pdf
            - `formats` types of file to generate. Default `['png', 'svg', 'pdf']`
            - `node_styles` task node styles, same as the options provided by graphviz
        """
        if formats is None: formats = GRAPH_SAVING_TYPES
        if node_styles is None: node_styles = {}

        # apt install graphviz
        from graphviz import Digraph
        dot = Digraph(
            directory=self.output_dir,
            filename=filename,
            comment=f'Task Graph ({self.graph_name})',
        )

        for task_name in self.tasks:
            dot.node(task_name, **node_styles.get(task_name, {}))

        if show_start:
            dot.node('START', style='filled', color='.7 .3 1')

        for task in self.tasks.values():
            # dependencies are drawed with solid lines
            for bd in task.dependencies:
                # don't show START node
                if bd.sender.is_start and not show_start: continue
                # optional input port has no value
                if bd.sender.params.get(bd.send) is None: continue
                dot.edge(bd.sender.task_name, bd.receiver.task_name)
            # waits are drawed with dotted lines
            for wt in task.waits:
                dot.edge(wt.task_name, task.task_name, style='dotted')

        for fmt in formats:
            dot.render(format=fmt, view=False)

    # 打印任务 shell 命令到控制台
    def print_commands(self):
        for task in self.ordered_tasks:
            print(f'\033[1;36m{task.task_name} 🍍\033[0m {task.main_shell_cmd}')

    # 挂载数据
    def set_input(self, t: str, k: str, v: Any) -> str:
        """
        将任务图的输入数据挂载到开始任务上，后续任务通过与开始任务的输出接口绑定来获得参数值
        """
        n = f'{t}#{k}'
        self.START.params[n] = v
        return n

    # 更新参数值
    def update_params(self, params: Mapping):
        for task in self.tasks.values():
            task.update_params(params.get(task.unit_name, {}), 'override')

    # 遍历任务图，取出可执行的任务
    def fetch_executable_tasks(self):
        _executable_tasks: List[Task] = []

        def traverse(tasks: Sequence[Task]):
            # 没有子任务的任务会调用空列表
            if len(tasks) == 0:
                return

            next_tasks = []

            for task in tasks:
                # 索引任务时忽略输出节点
                if task.task_name == 'END':
                    continue
                # 可执行任务
                is_ready = True
                # 所有父任务都是 SUCCESS
                for t in task.parents:
                    if t.status != TASK_SUCCESS:
                        is_ready = False
                        break
                # 所有需要等待的任务也必须成功
                for t in task.waits:
                    if t.status != TASK_SUCCESS:
                        is_ready = False
                        break
                # 自己是 WAITING
                if is_ready and task.status != TASK_WAITING:
                    is_ready = False

                # 任务可执行时执行任务
                if is_ready:
                    if task not in _executable_tasks:
                        _executable_tasks.append(task)
                # 任务成功时依次检测其子任务
                elif task.status == TASK_SUCCESS:
                    for t in task.children:
                        next_tasks.append(t)

            traverse(next_tasks)

        self.START.status = TASK_SUCCESS
        traverse(self.START.children)
        return _executable_tasks

    # 创建任务之前执行：检查任务名是否重复；合并参数
    def create_unit_task(
        self,
        task_name,
        unit_name=None,
        unit_config=None,
        dependencies=None,
        params=None,
        templates=None,
        waits=None,
    ):

        if task_name in self.tasks:
            raise Exception(f'{task_name} has been registered, maybe you should use other task name')

        ## 用创建任务提供的参数值覆盖从单元配置文件中加载的默认参数值
        task_params = {**self.params.get(task_name, self.params.get(unit_name, {}))}
        if params: task_params.update(params)

        task = Task(
            task_name=task_name,
            unit_name=unit_name,
            unit_config=unit_config,
            working_dir=self.output_dir,
            dependencies=dependencies,
            params=task_params,
            templates=templates,
            waits=waits,
            env=self.env,
        )
        self.tasks[task_name] = task
        return task

    @classmethod
    def load(cls: Self, pickle_path: str) -> Self:
        with open(pickle_path, 'rb') as rb:
            return pickle.load(rb)


class TaskGraph(BaseTaskGraph):

    def add_fq(self, name: str, files: Sequence[str]):
        """Add fq files to the root task and return the root task"""
        if name in self.START.params:
            raise KeyError(f'{name} has been mounted!')
        self.START.params[name] = files
        return self.START

    def add_bwa(self, sname: str, fq1s: Sequence[str], fq2s: Sequence[str]):
        """run possible cat, run bwa and return the bwa task"""
        fq1_name = f'{sname}_fq1'
        fq2_name = f'{sname}_fq2'
        start = self.add_fq(fq1_name, fq1s)
        start = self.add_fq(fq2_name, fq2s)

        deps = {}

        if len(fq1s) == 1:
            deps['in1_fq'] = (start, fq1_name)
        else:
            _d = {'targets': (start, fq1_name)}
            cat = self.add_task(fq1_name, 'cat', _d, {'dest': f'{fq1_name}.fq.gz'})
            deps['in1_fq'] = (cat, 'dest')

        if len(fq2s) == 1:
            deps['in2_fq'] = (start, fq2_name)
        else:
            _d = {'targets': (start, fq2_name)}
            cat = self.add_task(fq2_name, 'cat', _d, {'dest': f'{fq2_name}.fq.gz'})
            deps['in2_fq'] = (cat, 'dest')

        return self.add_task(sname, 'bwamem2', deps)

    def add_task(
        self,
        sample_name: str,
        unit_name: str,
        dependencies: DepSet[Task] = None,
        templates: SRecord = None,
        params: SRecord = None,
        waits: Sequence[Task] = None,
    ):
        """为一个样本添加一个任务"""
        if params is None: params = {}
        if templates is None: templates = {}
        task_name = f'{unit_name}-{sample_name}'

        templates['SampleID'] = templates.get('SampleID', sample_name)
        templates['SampleName'] = templates.get('SampleName', sample_name)

        return self.create_unit_task(
            unit_name=unit_name,
            task_name=task_name,
            dependencies=dependencies,
            params=params,
            templates=templates,
            waits=waits,
        )

    def run(self, params_file, sample_list_file, **kwargs):
        # params_file = kwargs.get('params_file')
        # sample_list_file = kwargs.get('sample_list_file')

        if params_file and isfile(params_file):
            self.params_file = join(self.output_dir, 'params.json')
            self.params = exio.read_jsonlike_file(params_file)
            shutil.copy(params_file, self.params_file)

        if sample_list_file and isfile(sample_list_file):
            self.sample_list_file = join(self.output_dir, 'sample_list.tsv')
            shutil.copy(sample_list_file, self.sample_list_file)

        kwargs['sample_list_file'] = sample_list_file
        self.generate(**kwargs)

    @classmethod
    def create(
            cls: Self,
            name: str,  # graph name
            sample_list_file: str,
            working_dir: str = None,
            env_file: str = None,
            params_file: str = None,
            clean=False,  # whether remove graph dir if exists
            **kwargs,  # other args passed to __init__() and run()
    ) -> Self:
        if env_file is None:
            if exists('env.toml'):
                env_file = 'env.toml'
                logging.info(f'auto use env {abspath(env_file)}')
            else:
                logging.info(f'not use any env file!')
        env = EnvLoader(env_file, strict=True, checking_path=False)

        if working_dir is None:
            working_dir = create_dir(EnvLoader.GRAPH_WORKING_DIR)

        graph_dir = join(working_dir, name)
        if exists(graph_dir):
            if clean:
                shutil.rmtree(graph_dir)
            else:
                raise RuntimeError(f'{graph_dir} exists')
        logging.info(f'graph will work at {graph_dir}')

        graph: Self = cls(name, output_dir=graph_dir, env=env, kwargs=kwargs)
        graph.run(sample_list_file=sample_list_file, params_file=params_file, **kwargs)
        return graph


# 为 MS 平台设计的任务图类
class MsTaskGraph(BaseTaskGraph):
    # 将一组文件路径作为输入挂载到 start 任务上
    def set_input_files(self, key: str, filepaths: Sequence[str]):
        if key in self.START.params:
            raise KeyError(f'{key} has been used')
        self.START.params[key] = filepaths
        return self.START

    # 将一个文件列表挂载到开始节点上，按照实际需求可以选择将多个文件连接成单个文件，返回依赖数据
    def cat_input_files(self, key: str, filepaths: Sequence[str], concatenate=False):
        # 首先挂载输入文件列表
        start = self.set_input_files(key, filepaths)
        if not concatenate or len(filepaths) == 1: return (start, key)
        # 添加一个 cat 任务，将该任务作为后续任务的依赖
        cat = self.create_unit_task(
            unit_name='cat',
            task_name=f'cat-{key}',
            dependencies={'targets': (start, key)},
            templates={'dest': f'{key}.fq.gz'},
        )
        return (cat, 'dest')


# multi-sample pipelines extends this class.
class MultiSampleTaskGraph(TaskGraph):
    pass


def import_graph_module(gm_path: str) -> TaskGraph:
    """
    导入任务图模块: 每个任务图定义在一个模块中，并通过 ExportedGraph 导出
    """
    try:
        return import_module(gm_path).ExportedGraph
    except ModuleNotFoundError:
        gm_path = f'bioflowgraph.graphs.{gm_path}'
        return import_module(gm_path).ExportedGraph
