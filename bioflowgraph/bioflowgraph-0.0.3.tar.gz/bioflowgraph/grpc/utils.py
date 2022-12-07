# coding=utf-8
import json
import re
import logging
import subprocess
from typing import Mapping

from exuse import exio
from exuse.expath import dirname, basename, filename, join

from .flowgraph_pb2 import GenericGrpcResponse, GenericGrpcRequest

# bioflowgraph.grpc will export these members of grpc
# all members exported from grpc start with "Grpc"
FIRST_EXPORTS = [
    'from grpc import secure_channel as GrpcSecureChannel',
    'from grpc import insecure_channel as GrpcInsecureChannel',
    'from grpc import server as GrpcServer',
    'from grpc import RpcContext as GrpcContext',
]

LAST_EXPORTS = [
    'from .utils import request',
    'from .utils import response',
    'from .utils import error_response',
    'from .utils import call',
]


def run_better_protoc(proto_path, output_dir):
    proto_file = basename(proto_path)
    proto_key = filename(proto_file)
    proto_dir = dirname(proto_path)
    cmd_list = [
        'python',
        '-m',
        'grpc_tools.protoc',
        '-I',
        proto_dir,
        '--python_out',
        output_dir,
        '--grpc_python_out',
        output_dir,
        proto_file,
    ]
    logging.info(f"will execute:\n{' '.join(cmd_list)}")
    subprocess.run(cmd_list)

    ## 替换默认的导入方式
    grpc_file = join(output_dir, f'{proto_key}_pb2_grpc.py')
    text = exio.read_file(grpc_file).replace(
        f"import {proto_key}_pb2 as {proto_key}__pb2",
        f"from . import {proto_key}_pb2 as {proto_key}__pb2",
    )
    exio.write(text, grpc_file)

    ## 在 __init__.py 中集中导出
    items = FIRST_EXPORTS

    _ = join(output_dir, f'{proto_key}_pb2_grpc.py')
    for k in re.findall(r'class (\w+)\(', exio.read_file(_)):
        items.append(f"from .{proto_key}_pb2_grpc import {k}")
    for k in re.findall(r'def (\w+)\(servicer', exio.read_file(_)):
        items.append(f"from .{proto_key}_pb2_grpc import {k}")
    _ = join(output_dir, f'{proto_key}_pb2.py')
    for k in re.findall(r'(\w+) = _reflection\.', exio.read_file(_)):
        items.append(f"from .{proto_key}_pb2 import {k}")

    for item in LAST_EXPORTS:
        items.append(item)

    init_path = join(output_dir, '__init__.py')
    exio.write('\n'.join(items), init_path)


# 目标对象只要是给定类型中的一个，返回真
def isinstance_some(obj, types):
    "obj 是否是 types 中的某一种类型"
    for t in types:
        if isinstance(obj, t):
            return True
    return False


# 将数据打包成请求，或者从请求中解析出数据
def request(obj=None):
    """
    If `data` is `None`, unpack `data` from request to built-in dict or list object.
    If `data` is not `None`, pack `data` to request.
    """
    # unpack: request.data must be a stringified `dict` instance
    if isinstance(obj, GenericGrpcRequest):
        if obj.data == '':
            return {}
        if obj.data.startswith('{'):
            return json.loads(obj.data)
        else:
            raise TypeError('request.data must be a stringified `dict` instance')

    # pack: data must be `None` or a `dict` instance
    else:
        if obj is None:
            return GenericGrpcRequest()
        if isinstance(obj, dict):
            return GenericGrpcRequest(data=json.dumps(obj))
        else:
            raise TypeError('data must be `None` or a `dict` instance')


# 将数据打包成响应，或者从响应中解析出数据
def response(obj=None, errcode=0, message='ok'):
    """
    将数据封装成 Response 对象，或者从 Response 对象中拆解出数据。
    如果 obj 本身是 Response 对象，则此方法从 Response 对象中拆解数据。
    否则此方法会将 obj 数据打包成 Response 对象，此时可以同时指定其 errcode 和 message 参数。
    打包数据时, errcode 默认为 0, 表示方法调用正常; message 默认为 'ok'
    """
    # unpack: response.data must be '' or a stringified `dict` or `list` instance
    # when response.data is '', it means the server did not send any data
    if isinstance(obj, GenericGrpcResponse):
        if obj.data.startswith('{') or obj.data.startswith('['):
            return {'errcode': obj.errcode, 'message': obj.message, 'data': json.loads(obj.data)}
        elif obj.data == '':
            return {'errcode': obj.errcode, 'message': obj.message}
        else:
            raise TypeError('response.data must be '
                            ' or a stringified `dict` or `list` instance')

    # pack: data must be `None` or a `list` or `dict` instance
    else:
        wrapped = None
        if obj is None:
            wrapped = None
        elif isinstance_some(obj, [list, dict]):
            wrapped = json.dumps(obj)
        else:
            raise TypeError('data must be `None` or a `list` or `dict` instance')
        return GenericGrpcResponse(errcode=errcode, message=message, data=wrapped)


# 一个简单的错误响应
def error_response(message, errcode=1):
    return response(None, errcode=errcode, message=message)

# 调用 stub 对象的某个方法，自动完成请求打包和响应解包的过程
def call(stub_method, request_data):
    req = request(request_data)
    res = stub_method(req)
    return response(res)
