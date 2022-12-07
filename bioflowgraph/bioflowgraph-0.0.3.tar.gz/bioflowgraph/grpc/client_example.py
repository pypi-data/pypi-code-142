import json
from exuse.exlogging import init_logging
from exuse import exio

from bioflowgraph import grpc


def RunTaskGraph():
    with grpc.GrpcInsecureChannel('localhost:60321') as channel:
        stub = grpc.TaskGraphStub(channel)

        config = exio.load_json('gutmeta_pipeline.json')
        response = stub.RunTaskGraph(
            grpc.request({
                'graph_config': config,
                'running_params': {
                    'maxsize': 1,
                    'interval': 10,
                },
            }))
        print(grpc.response(response))


def GetTaskGraphList():
    with grpc.GrpcInsecureChannel('localhost:60321') as channel:
        stub = grpc.TaskGraphStub(channel)

        response = stub.GetTaskGraphList(grpc.request())
        print(grpc.response(response))


if __name__ == '__main__':
    init_logging()
    RunTaskGraph()
    # GetTaskGraphList()