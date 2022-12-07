import os
import json
import shutil
import multiprocessing
from typing import Any, Mapping
from exuse import expath
from exuse.exlogging import init_logging
from concurrent.futures import ThreadPoolExecutor

from bioflowgraph import grpc, TaskPolling
from bioflowgraph.graphs import ApiTaskGraph

from bioflowgraph.const import TASK_GRAPH_WAITING, TASK_GRAPH_RUNNING, TASK_GRAPH_SUCCESS, TASK_GRAPH_FAILED
import logging

global_polling_processes = {}


def validateRequired(name, data, keys):
    for key in keys:
        if key not in data:
            return grpc.response(None, 1, f'no "{key}" provided in {name}')
    return None


class TaskGraphServicer(grpc.TaskGraphServicer):

    def RunTaskGraph(self, request, context):
        params = grpc.request(request)
        restore = params.get('restore', False)  # 恢复运行模式

        tg = None
        try:
            if restore:
                graph_name = params.get('graph_name')
                if graph_name is None:
                    raise Exception('The graph name must be provided when restore.')
                tg = ApiTaskGraph.restore(graph_name)
            else:
                # instantiate taskgtaph
                graph_name = params.get('graph_name')
                graph_config = params.get('graph_config')
                if graph_config is None:
                    raise Exception('The graph config must be provided.')
                tg = ApiTaskGraph.create({'graph_name': graph_name, **graph_config})
                # save data for inputs of taskgraph
                input_files = params.get('input_files')
                if isinstance(input_files, dict):
                    for task_name, files in input_files.items():
                        for output_key, content in files.items():
                            tg.save_input_file(task_name, output_key, content)

        except Exception as e:
            logging.error(e.args[0])
            return grpc.error_response(e.args[0])

        running_params = params.get('running_params', {})
        tp = TaskPolling(tg, **running_params)

        # TODO 加一个任务队列
        global global_polling_processes
        proc = multiprocessing.Process(target=tp.run)
        proc.start()
        global_polling_processes[tg.graph_name] = proc

        return grpc.response({
            'status': TASK_GRAPH_RUNNING,
            'graph_name': tg.graph_name,
        })
      

    def GetTaskGraphList(self, request, context):
        params = grpc.request(request)
        only_graphs = params.get('only', None)

        graphs = {}
        for graph_name in os.listdir(ApiTaskGraph.GRAPH_WORKING_DIR):
            if only_graphs is not None and graph_name not in only_graphs:
                continue
            graph_path = expath.join(ApiTaskGraph.GRAPH_WORKING_DIR, graph_name)
            try:
                graph = ApiTaskGraph.load(expath.join(graph_path, 'taskgraph.pkl'))
                graphs[graph_name] = {
                    'success': True,
                    'task_status': graph.get_status(),
                    'graph_status': graph.get_graph_status(),
                }
            except Exception as e:
                graphs[graph_name] = {
                    'success': False,
                    'message': e.args[0],
                }
        return grpc.response(graphs)

    def GetTaskGraph(self, request, context):
        params = grpc.request(request)
        graph_name: str = params['graph_name']
        graph = ApiTaskGraph.restore(graph_name)

        methods = {}
        for key in params['keys']:
            method = f'get_{key}'
            if hasattr(graph, method):
                methods[key] = method
            else:
                return grpc.error_response(f'graph ({graph_name}) has no method {method} for key {key}')

        returned = {}
        for key, method in methods.items():
            returned[key] = getattr(graph, method)()

        return grpc.response(returned)

    def GetTaskOutput(self, request, context):
        params = grpc.request(request)

        if 'graph_name' not in params:
            return grpc.error_response('graph_name must be provided')
        graph_name: str = params['graph_name']
        graph = ApiTaskGraph.restore(graph_name)
        meta = graph.get_meta()
        tasks: Mapping[str, Any] = meta['tasks']

        task_name = params.get('task_name')
        if task_name is None:
            # 未提供任务名时检测任务图是否只包含一个任务
            if len(tasks.keys()) == 1:
                task_name = tasks.keys()[0]
            else:
                return grpc.error_response('task_name must be provided')
        if task_name not in tasks:
            return grpc.error_response(f"task {task_name} not in the graph")
        task = tasks[task_name]
        outputs = task['outputs']

        output_key = params.get('output_key')
        if output_key is None:
            # 未提供输出名称时检测任务是否只有一个输出口
            ops = [k for k in outputs if k not in ('STDOUT', 'STDERR')]
            if len(ops) == 1:
                output_key = ops[0]
            else:
                return grpc.error_response('output_key must be provided')
        if output_key not in outputs:
            return grpc.error_response(f"task {task_name} don't have output {output_key}")
        target = outputs[output_key]

        with open(target) as rd:
            text = rd.read()
        return grpc.response({'type': 'tsv', 'data': text})

    def DeleteTaskGraph(self, request, context):
        params = grpc.request(request)
        try:
            graph_name: str = params['graph_name']
            graph = ApiTaskGraph.restore(graph_name)
            shutil.rmtree(graph.output_dir)
            logging.info(f'delete taskgraph: {graph.output_dir}')
            return grpc.response({'target': graph.output_dir})
        except ApiTaskGraph.TaskGraphNotExistsError as e:
            empty_dir = expath.dirname(e.args[0])
            if expath.exists(empty_dir):
                shutil.rmtree(empty_dir)
            return grpc.response({'target': empty_dir})
        # except Exception as e:
        #     return grpc.error_response(json.dumps(list(e.args)))


def start_server(address='[::]:60321'):
    server = grpc.GrpcServer(ThreadPoolExecutor(max_workers=10))
    grpc.add_TaskGraphServicer_to_server(TaskGraphServicer(), server)
    server.add_insecure_port(address)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    init_logging()
    start_server()