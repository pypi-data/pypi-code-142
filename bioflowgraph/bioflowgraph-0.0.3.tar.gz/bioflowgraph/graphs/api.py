from typing import Mapping
from typing_extensions import Self
from bioflowgraph import BaseTaskGraph
from bioflowgraph.env import Env
from bioflowgraph import exceptions

from exuse import expath
from exuse.extime import timestamp


# 解析流程配置文件中的依赖关系
def parse_cfg_deps(graph, deps):
    _deps = {}
    for receive, dep in deps.items():
        arr = dep
        if isinstance(dep, str):
            arr = [arr]
        for i, x in enumerate(arr):
            if '.' in x:
                t = x.split('.')[0]
                s = x.split('.')[1]
                arr[i] = (graph.tasks[t], s)
            else:
                arr[i] = graph.tasks[t]
        _deps[receive] = arr
    return _deps


class ApiTaskGraph(BaseTaskGraph):

    TaskGraphNotExistsError = exceptions.TaskGraphNotExistsError

    @property
    def START_OUTPUT_DIR(self):
        "用来存储 START 任务相关的数据，例如输入文件"
        return expath.create_dir(expath.join(self.output_dir, 'START'))

    def save_input_file(self, task_name: str, key: str, file: str):
        "将平台发过来的文件字符串保存到任务图下的对应位置"
        task_dir = expath.create_dir(self.START_OUTPUT_DIR, task_name)
        output_file = expath.join(task_dir, key)
        with open(output_file, 'w') as wt:
            wt.write(file)

    def define_graph(self, tasks, units):
        for task_name, task_config in tasks.items():
            unit_name = task_config['unit']
            params = task_config.get('params', {})
            dependencies = task_config.get('dependencies', {})
            waits = task_config.get('waits', [])
            self.create_unit_task(
                task_name=task_name,
                # unit_name=unit_name,
                unit_config=units[unit_name],
                dependencies=parse_cfg_deps(self, dependencies),
                waits=[self.tasks[k] for k in waits],
                templates=task_config.get('templates', {}),
                params=params,
            )

    # @deprecate
    # 通过设置环境变量 BFG_ENV_FILE 来设置默认的环境文件路径
    @classmethod  # 运行单个任务
    def create_for_task(cls, cfg: Mapping) -> Self:
        unit_name = cfg['unit']
        task_name = unit_name
        # graph_name = f"STG-{unit_name}-{timestamp()}"
        graph_name = f"STG_{timestamp()}"
        working_dir = expath.create_dir(cfg.get('working_dir', Env.GRAPH_WORKING_DIR))
        output_dir = expath.join(working_dir, graph_name)
        if expath.exists(output_dir):
            raise Exception(f'{output_dir} exists')
        graph = cls(task_name, output_dir, Env())

        for k, v in cfg['params'].items():
            graph.set_input(task_name, k, v)

        td = {'unit': cfg['unit'], 'params': cfg['params']}
        # generate 接收的关键字参数会全部传递给 define_graph
        return graph.generate(tasks={task_name: td})

    @classmethod
    def create(cls, cfg: Mapping, restore=False) -> Self:
        """
        ```
        cfg: { 
            inputs: {
                [task_ame: string]: {
                    [input_key: string]: string
                }
            }
            tasks: {
                [task_name]: {
                    unit: string
                    params: any[]
                    dependencies: any
                    templates: any
                    waits: string[]
                    module: string
                }
            }
            units: {
                [unit_name: string]: UnitRecord
            }
        }
        ```
        """

        graph_name = cfg.get('graph_name', f'ATG_{timestamp()}')
        working_dir = cfg.get('working_dir', Env.GRAPH_WORKING_DIR)

        working_dir = expath.create_dir(working_dir)
        output_dir = expath.join(working_dir, graph_name)

        if restore is False and expath.exists(output_dir):
            raise exceptions.TaskGraphExistsError(f'{output_dir} exists')

        graph = cls(graph_name, output_dir, Env())

        for t, d in cfg['inputs'].items():
            for k, v in d.items():
                fp: str = v
                # 约定：平台端传过来的文件的路径会以 START 开头，需要改成绝对路径
                if isinstance(fp, str):
                    if fp.startswith('START/'):
                        fp = expath.join(graph.output_dir, v)
                elif isinstance(fp, list):
                    ys = []
                    for x in fp:
                        y = x
                        if x.startswith('START/'):
                            y = expath.join(graph.output_dir, x)
                        ys.append(y)
                    fp = ys
                    
                # 所有不存在的文件路径都尝试去任务图输出目录下查找
                elif not expath.exists(fp):
                    fp = expath.join(graph.output_dir, v)
                    if not expath.exists(fp):
                        raise FileNotFoundError(fp)
                graph.set_input(t, k, fp)

        graph.generate(tasks=cfg['tasks'], units=cfg['units'])
        return graph

    @staticmethod
    def restore(graph_name: str):
        if expath.exists(graph_name):
            pkl_path = graph_name
        else:
            pkl_path = expath.join(ApiTaskGraph.GRAPH_WORKING_DIR, graph_name, 'taskgraph.pkl')
            if not expath.exists(pkl_path):
                raise exceptions.TaskGraphNotExistsError(pkl_path)
        return ApiTaskGraph.load(pkl_path)


ExportedGraph = ApiTaskGraph
