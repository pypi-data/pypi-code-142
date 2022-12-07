# coding=utf-8

import os
import re
import shutil
import psutil
import logging
import subprocess
from inspect import isfunction
from collections import defaultdict
from typing import Callable, Dict, Generic, TypeVar, Union

from exuse.expath import join, exists, abspath, isabs, dirname, makedirs, create_dir
from exuse.extypings import Mapping, Sequence, Tuple, Self, List, SSRecord, SRecord
from exuse import exio

from .env import EnvLoader
from .unit import Unit, get_unit
from .const import SHELL_DIR, START_TASK, STDXXX_DIR, SUCCESS_DIR
from .const import TASK_WAITING, TASK_RUNNING, TASK_SUCCESS, TASK_FAILED

CURDIR = dirname(__file__)


def joinfv(f=None, v=None):
    """Join the param flag and value using whitespace"""
    return ''.join([
        '' if f is None else f'{f}',
        ' ' if f is not None and v is not None else '',
        '' if v is None else f'{v}',
    ])


T = TypeVar('T')


class Binding(Generic[T]):
    "任务间的依赖关系"

    def __init__(self, sender: T, send: str, receiver: T, receive: str, fmt=None):
        """
        Args:
        - `sender` 发送数据的任务实例
        - `send` 数据发送方要发送的端口（输出端口）
        - `receiver` 接受数据的任务实例
        - `receive` 数据接受方接受数据的端口（输入端口）
        - `fmt` 一个修正函数，参数是输出端口输出的值，返回输入端口接受的值
        """
        self.sender = sender
        self.send = send
        self.receiver = receiver
        self.receive = receive
        self.fmt = fmt

    def __str__(self) -> str:
        return f'Binding[{self.sender} {self.send} => {self.receiver} {self.receive}]'


# 依赖的声明方式
# [sender | (sender, send) | (sender, send, fmt)]
DepItem = Union[T, Tuple[T, str], Tuple[T, str, Callable[[str], str]] ]
DepSet = Union[DepItem[T], Sequence[DepItem[T]], Mapping[str, DepItem[T]], Mapping[str, Sequence[DepItem[T]]]]


class Task:
    """Task is the running process of Unit"""

    def __init__(
        self: Self,
        # 每个任务在其所在的任务图中具有唯一的任务名称
        # 在多样本任务图中，任务名称一般由执行单元名称加样本名称构成
        # 在单样本任务图中，任务名称一般由执行单元名称加时间戳构成
        task_name: str,
        # 直接使用bfg时需要指定一个执行单元名称
        # bfg直接从自带的或者环境文件注册的位置读取对应执行单元的配置
        unit_name: str = None,
        # 与平台对接时后端直接从数据库中取出执行单元的配置对象传递给bfg服务
        # 提供 unit_config 时忽略 unit_name
        unit_config: Dict = None,
        # 任务的工作目录，一般指的是任务图的输出目录
        # 每个任务会在任务图的输出目录下先以自己执行单元的名称建立一个子目录
        # 然后在该子目录下再以任务名称建立一个子目录存放任务的所有结果
        # 所以任务的输出目录是：任务图工作目录/任务图名称/执行单元名称/任务名称
        working_dir: str = None,
        # 该任务依赖的所有任务，依赖的完整声明形式是：
        # {当前任务的某个输入口: 依赖的任务及其输出口 }
        # 几个例子：
        # - ={'b1': A} B任务的b1输入依赖于A任务的唯一输出
        # 当b1是唯一输出时可以简写为 =A
        # - ={'b1': (A, 'a1')} B任务的b1输入依赖于A任务的a1输出
        # 当b1是唯一输出时可以简写为 =(A, 'a1')
        # - ={'b2': [C, (D, 'd2')] } B任务的b2输入依赖于C任务的唯一输出和D任务的d2输出
        # 当b2是唯一输出时可以简写为 =[C, (D, 'd2')]
        dependencies: DepSet[Self] = None,
        # 该任务与已经存在的某些任务没有数据流动关系（非依赖），只是简单的需要等待某些任务执行完成
        waits: Sequence[Self] = None,
        # 执行任务需要的具体参数值
        params: SRecord = None,
        # 执行任务需要的模板变量的值
        templates: SRecord = None,
        # 执行任务需要的环境变量对象
        env: EnvLoader = None,
    ):
        self.task_name: str = task_name  # 任务图中的任务名称是唯一的
        self.status: int = TASK_WAITING  # 任务的实时运行状态，默认为等待运行
        self.vis_status: int = TASK_WAITING  # 重载任务时的状态，用于绘图; 因为重载时失败的任务会被修改为等待，才能置入队列开始运行, 所以需要一个单独的变量记录
        self.pid = None  # 任务正在使用的或者使用过的进行号
        self.working_dir: str = working_dir  # 任务子目录的保存位置，在任务图中运行时该路径指向任务图的输出目录
        self.params: SRecord = {} if params is None else params  # 任务的运行时参数，键是参数名称，值是参数值
        self.env: EnvLoader = env  # 任务运行的生信环境

        self.children: List[Self] = []  # 直接依赖本任务的子任务列表
        self.parents: List[Self] = []  # 本任务直接依赖的任务列表
        # 当前节点与其父节点和子节点的连接关系
        self.inputs: SSRecord = {}  # { parent_unit.some_output => this_unit.some_input }
        self.outputs: SSRecord = {}  # { this_unit.some_output => child_unit.some_input }
        # 任务的依赖任务，格式为 {self_input_key: (DepTask, dep_output_key, tpl)}
        # tpl 是一个字符串，可以对 DepTask.dep_output_key 的路径进行校正
        # 可以用 {} 表示依赖任务输出路径的 basename
        # 适用于依赖任务的 output_key 是一个目录，而下游任务只依赖于目录下的一个文件的情况
        self.dependencies: List[Binding[Self]] = []
        self.waits = [] if waits is None else waits  # 与依赖类似，等待也是一种依赖关系，但是它与父任务间没有 IO 交换

        # 拼接命令时对参数值中的模板变量进行替换，模板变量用 ${} 表示
        tpls = {} if templates is None else templates
        tpls['TaskName'] = self.task_name
        tpls['WorkingDir'] = self.working_dir
        self.templates = tpls

        self.output_dir: str = None  # 任务输出目录
        self.shell_dir: str = None  # 保存命令
        self.stdxxx_dir: str = None  # 保存输出和错误

        self.shell_cmd: str = None  # 任务完整的命令
        self.shell_cmd_main: str = None  # 任务命令的主干部分
        self.shell_file: str = None  # 保存完整命令的文件
        self.success_flag_file: str = None  # 任务成功时需要创建的标志文件

        self.stdout_file: str = None
        self.stderr_file: str = None

        # 实际渲染的参数值
        self.computed_params: SRecord = {}
        self.computed_output_ports: SSRecord = None

        self.unit: Unit = None
        self.unit_name: str = None
        self.__registered_deps = []
        if unit_config is None:
            if unit_name is not None:
                registered_units = self.env.registered_module_units
                if unit_name not in registered_units:
                    raise Exception(f'unit {unit_name} not registered in env')
                fp = registered_units[unit_name]
                config = exio.read_jsonlike_file(fp)
                config['unit'] = config['unit_name'] = unit_name
                self.setup_unit(config)
                self.setup_deps(dependencies)
        else:
            unit_name = unit_config.get('unit', unit_config.get('unit_name'))
            config = {**unit_config, 'unit': unit_name, 'unit_name': unit_name}
            self.setup_unit(config)
            self.setup_deps(dependencies)

    #region __
    # 如果提供了执行单元，执行执行单元的初始化设置
    def setup_unit(self, config):
        self.unit_name = config['unit_name']
        self.output_dir = create_dir(self.working_dir, self.unit_name, self.task_name)
        self.shell_dir = create_dir(self.output_dir, SHELL_DIR)
        self.stdxxx_dir = create_dir(self.output_dir, STDXXX_DIR)
        self.shell_file = join(self.shell_dir, f'{self.task_name}.sh')
        self.success_flag_file = join(create_dir(self.output_dir, SUCCESS_DIR), self.task_name)
        self.templates['UnitName'] = self.unit_name
        self.templates['OutputDir'] = self.output_dir
        self.templates['ShellDir'] = self.shell_dir
        self.templates['StdxxxDir'] = self.stdxxx_dir

        unit = self.unit = get_unit(config)
        for k, d in unit.params.items():
            if unit.is_output_port(k):
                self.params[k] = self.params.get(k, unit.get_output_default(k))
            elif unit.is_input_port(k):
                self.params[k] = self.params.get(k, unit.get_input_default(k))
            elif 'default' in d:
                self.params[k] = self.params.get(k, d['default'])
        return unit

    # 如果执行单元已经初始化了，处理依赖
    def setup_deps(self, deps):
        if deps is None: return

        ## 处理依赖的各种形式 returns {sender, send, fmt}
        def parse_dep(item):
            # dependencies = Task
            # 当前任务的唯一输入端依赖于指定任务的唯一输出端
            if isinstance(item, Task):
                sender: Task = item
                send = sender.unit.unique_output_port
                return {'sender': sender, 'send': send, 'fmt': None}
            # dependencies = (sender, send, fmt?)
            # 当前任务的唯一输入端依赖于指定任务的某个输出端
            elif isinstance(item, tuple):
                assert len(item) >= 2, 'at least provide sender and send'
                assert isinstance(item[0], Task), f'sender is not a Task: {item[0]}'
                sender: Task = item[0]
                send = item[1]
                if sender.task_name != START_TASK:
                    assert item[1] in sender.unit.output_ports, f'{send} is not output port of {sender}'
                fmt = None if len(item) == 2 else item[2]
                return {'sender': sender, 'send': send, 'fmt': fmt}
            else:
                raise TypeError(f'unknown dep item type: {type(item)}')

        dependencies = None
        if not isinstance(deps, dict):
            dependencies = {self.unit.unique_input_port: deps}
        else:
            dependencies = deps

        for receive, _dep in dependencies.items():
            dep_list = _dep
            if not isinstance(_dep, list):
                dep_list = [dep_list]

            for _dep in dep_list:
                dep = parse_dep(_dep)
                self.set_dep(dep['sender'], dep['send'], receive, dep['fmt'])

    def set_dep(self, sender: Self, send: str = None, receive: str = None, fmt: str = None):
        """创建新的依赖
        
        Args:
            dep_task: 依赖的任务
            sender: 依赖任务的输出端
            receiver: 本任务的输入端
            replacer: 用输出替换输入时进行一定的处理
        """

        k = f'{sender}.{send}=>{self}.{receive}'
        if k in self.__registered_deps:
            raise Exception(f'{sender}.{sender} has already append to the dependencies of {self}.{receive}')

        # 和依赖任务间不存在文件交换
        if send is None or receive is None:
            self.dependencies.append(Binding(sender, None, self, None))
        else:
            self.dependencies.append(Binding(sender, send, self, receive, fmt))

        if sender not in self.parents:
            self.parents.append(sender)

        if self not in sender.children:
            sender.children.append(self)

    def __eq__(self, other: Self) -> bool:
        return self.task_name == other.task_name

    def __str__(self) -> str:
        # return f'task \033[1;31m{self.task_name}\033[0m'
        return f'\033[1;31m{self.task_name}\033[0m'

    @property
    def desc(self):
        name = self.task_name
        d_a = [d[0].task_name for d in self.dependencies.values()]
        d_s = '' if len(d_a) == 0 else ', deps=[' + ', '.join(d_a) + ']'
        ws = [t.task_name for t in self.waits]
        w_s = '' if len(self.waits) == 0 else ', waits=[' + ', '.join(ws) + ']'
        p_a = [o.task_name for o in self.parents if o.task_name != 'START']
        p_s = '' if len(p_a) == 0 else ', parents=[' + ', '.join(p_a) + ']'
        c_a = [o.task_name for o in self.children if o.task_name != 'END']
        c_s = '' if len(c_a) == 0 else ', children=[' + ', '.join(c_a) + ']'
        return f'Task<{name}{p_s}{w_s}{c_s}{d_s}>'

    @property
    def is_start(self):
        return self.task_name == START_TASK

    # 移除模板变量和环境变量
    def r(self, s):
        s = str(s)
        if '${' in s:
            # 从环境文件中读取值替换模板变量
            if '${env:' in s:
                for x in re.findall(r'\$\{env:(\S+?)\}', s):
                    s = s.replace("${env:%s}" % x, self.env.get_raw(x))
            # 从参数字典中读取参数值替换模板变量
            elif '${params:' in s:
                for x in re.findall(r'\$\{params:(\S+?)\}', s):
                    if self.params.get(x) is None:
                        raise RuntimeError(f'Failed to read template "{x}" from parameters')
                    s = s.replace("${params:%s}" % x, self.params[x])

            # 普通模板变量需要在创建任务时单独指定，找不到时会报错
            else:
                for tpl in re.findall(r'\$\{.*?\}', s):
                    tpl_var = tpl[2:-1]
                    if tpl_var not in self.templates:
                        raise Exception(f'No template value provided for "{tpl_var}" for {self}')
                    s_or_f = self.templates[tpl_var]
                    if isfunction(s_or_f):
                        s = s_or_f(s)
                    else:
                        s = s.replace(tpl, s_or_f)
        return s

    #endregion

    def gen_command(self, save=True):
        """可以提供参数值覆盖初始化时提供的默认参数"""
        unit = self.unit
        computed_params = {}  # 计算之后的参数

        ## 1. 计算输入参数的真实参数值（self.params）
        # 考虑到输入参数可能是列表类型，所以参数值统一处理成 list 类型
        receive_mappings = defaultdict(list)
        for bd in self.dependencies:
            values = bd.sender.params.get(bd.send)
            if values is None: continue
            if isinstance(values, str):
                values = [values]

            for v in values:
                if bd.fmt is not None:
                    v = bd.fmt(v)
                receive_mappings[bd.receive].append(v)
        for receive, arr in receive_mappings.items():
            self.params[receive] = arr

        ## 2. 参数检查
        for k, d in self.unit.params.items():
            # 检查必须参数是否都获得了参数值
            is_required = d.get('required', False)
            if is_required and self.params.get(k) is None:
                raise Exception(f'{self}: parameter "{k}" is required!')
            # 检查枚举参数的值是否合法
            if d.get('type') == 'choices' and self.params.get(k) not in d['choices']:
                raise ValueError(f'{self}: choices parameter "{k}" is invalid!')

        ## 3. 校正输出参数的路径值
        for k in self.unit.output_ports:
            # 执行单元的输出口不在参数字典中时，自动忽略该输出口
            if k not in self.unit.params: continue
            # 在参数字典中的输出口必须提供有效的路径值
            assert self.params[k], f'{self}: value for output parameter "{k}" is not provided!'

            # 输出参数值一定是一个字符串
            v = self.params[k]
            assert isinstance(v, str)
            if v.startswith('#') or v.startswith('/') or isabs(v):
                pass
            elif v in ('&1', 'stderr', 'STDERR'):
                pass
            else:
                self.params[k] = abspath(join(self.output_dir, v))

        # executor & subexecutor
        exe = self.env.get_path(unit.executor)
        sub_exe = unit.sub_executor
        full_exe = f'{exe} {sub_exe}' if sub_exe else exe
        cmds = [self.r(full_exe)]
        stdout_cmd = None
        stderr_cmd = None

        for pn, pd in unit.params.items():
            pv = self.params.get(pn)
            # 没有参数值的参数就跳过了
            if pv is None: continue

            cmd = None

            pt, pf = pd['type'], pd['flag']

            if pt == 'bool':
                computed_params[pn] = pv
                if pv is True:
                    cmd = joinfv(pf, None)

            elif pt in ('int', 'float'):
                cmd = joinfv(pf, pv)
                computed_params[pn] = pv

            else:
                if pf == '>':
                    rpv = self.r(pv)
                    stdout_cmd = '>' + rpv
                    self.stdout_file = rpv
                    computed_params[pn] = rpv

                elif pf == '2>':
                    rpv = self.r(pv)
                    stderr_cmd = '2>' + rpv
                    self.stderr_file = rpv
                    computed_params[pn] = rpv

                elif pt == 'list' or pt == 'mvlist':
                    v = self.r(' '.join(pv))
                    cmd = joinfv(pf, v)
                    computed_params[pn] = v

                elif pt == 'mflist':
                    if isinstance(pv, str):
                        pv = [pv]
                    arr = [self.r(i) for i in pv]
                    cmd = self.r(' '.join([f'{pf} {i}' for i in arr]))
                    computed_params[pn] = arr

                else:
                    if isinstance(pv, list):
                        assert len(pv) == 1
                        v = self.r(pv[0])
                    else:
                        v = self.r(pv)
                    cmd = joinfv(pf, v)
                    computed_params[pn] = v
                    self.params[pn] = v

            if cmd: cmds.append(cmd)

        if stdout_cmd: cmds.append(stdout_cmd)
        if stderr_cmd: cmds.append(stderr_cmd)
        cmd = ' '.join(cmds)

        # 命令执行完成之后创建一个 .TASK_DONE 文件表示任务成功
        self.main_shell_cmd = cmd
        cmd = f"({cmd}) && (touch {self.success_flag_file})"
        self.shell_cmd = cmd

        if save:
            if exists(self.shell_file):
                raw_shell = exio.read_file(self.shell_file)
                if cmd != raw_shell:
                    logging.warning(f'override {self} shell: {self.shell_file}')
                    # logging.info(self.main_shell_cmd)
                    exio.write(cmd, self.shell_file)
            else:
                exio.write(cmd, self.shell_file)

        self.computed_params = computed_params

        ## 计算输出端口的真实值 ##
        self.computed_output_ports = {}
        for opk, opv in self.unit.output_defs.items():
            # 输入端口是一个输出参数
            if opk in self.params:
                self.computed_output_ports[opk] = self.computed_params[opk]
            # 输出由程序自己产生，而不是通过输出参数指定
            else:
                self.computed_output_ports[opk] = join(self.output_dir, self.r(opv))

        return cmd

    # def reset_status(self):
    #     """重置任务状态为 TASK_SUCCESS 或者 TASK_WAITING"""
    #     if exists(self.success_flag_file):
    #         self.status = TASK_SUCCESS
    #     else:
    #         self.status = TASK_WAITING
    def clean_output_dir(self):
        if not exists(self.output_dir): return
        for k in os.listdir(self.output_dir):
            if k in ('_shell'): continue
            v = join(self.output_dir, k)
            shutil.rmtree(v)

    def refresh_status(self):
        """
        刷新任务状态。
        成功和失败的任务不再刷新。
        生成 success 文件将任务置为成功。

        """
        if self.status in (TASK_SUCCESS, TASK_FAILED):
            return

        # 生成 success 文件表示任务成功
        if exists(self.success_flag_file):
            self.status = TASK_SUCCESS

        # 没有分配进程号表示等待中
        elif self.pid is None:
            self.status = TASK_WAITING

        else:
            try:
                proc = psutil.Process(self.pid)
                self.status = TASK_RUNNING
                if proc.status() == 'zombie':
                    proc.wait()
            # 任务拥有进程号，但是该进程没有在运行，同时也没有生成 success 文件，判定为失败
            except psutil.NoSuchProcess:
                self.status = TASK_FAILED

        self.vis_status = self.status

    def start(self):
        if self.shell_cmd is not None:
            flag_dir = dirname(self.success_flag_file)
            if not exists(flag_dir):
                makedirs(flag_dir)
            proc = subprocess.Popen(self.shell_cmd, shell=True, cwd=self.output_dir, stdout=subprocess.PIPE)
            self.pid = proc.pid
            self.status = TASK_RUNNING
        else:
            raise Exception(f'No command generated for {self.task_name}')

    def update_params(self, params: SRecord, solve_conflict="ignore"):
        """更新任务参数值"""
        assert solve_conflict in ['ignore', 'override']
        for k, v in params.items():
            if k in self.params:
                if solve_conflict == 'override':
                    self.params[k] = v
            else:
                self.params[k] = v
