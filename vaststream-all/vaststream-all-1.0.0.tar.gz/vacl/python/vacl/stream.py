"""
Copyright (C) 2022-2023 VASTAI Technologies Co., Ltd. All Rights Reserved.
The information contained herein is confidential property of the company.
The user, copying, transfer or disclosure of such information is prohibited
except by express written agreement with VASTAI Technologies Co., Ltd.
"""
# coding: utf-8
__all__ = [
    "BALANCE_MODE", "CallBackStatus", "createOpGraph", "destroyOpGraph", "destroyOpStream", 
    "subscribeStreamReport", "createOpStream", "buildStream", "runStream", "runStreamAsync",
    "synchronizeStream", "synchronizeDevice", "getStreamCacheNumber", "requestOutputDataset",
    "createGraphInputOp", "connectOps", "createRunModelOp", "registerGetOutput", "registerGetOutputs",
    "VastaiStream", "VastaiGraph"
]

import inspect
from typing import Any, Union
from _vaststream_pybind11 import vacl as _vacl
from vaststream.vacm import Dataset
from vaststream.vace import Op, OpBase, destroyOp
from .utils import *
from .common import *
from .model import VastaiModel

class BALANCE_MODE():
    ONCE: int = _vacl.balance_mode.vaclBM_ONCE
    RUN: int = _vacl.balance_mode.vaclBM_RUN
    
class CallBackStatus(_vacl.callBackStatus):
    errorCode: int
    isStreamEnd: bool

# import abc
# class CallBack(metaclass=abc.ABCMeta):
#     @staticmethod
#     @abc.abstractmethod
#     def call(op: Op, inputDataset: Dataset, outputDataset: Dataset, status: CallBackStatus, userCtx: int):
#         """
#         The callback function of type vaclStreamReportCallback.\n
#         --------------\n
#         op: Pointer to a vace operator instance.\n
#         inputDataset: a vacm input dataset instance.\n
#         outputDataset: a vacm output dataset instance.\n
#         status: a vacl callback status.\n
#         userCtx: the user defined context.\n
#         """
#         pass

def createOpGraph() -> OpGraph:
    """
    create the vacl graph.\n
    """
    return OpGraph(_vacl.createOpGraph())

@err_check
def destroyOpGraph(graph: OpGraph) -> int:
    """
    destroy the vacl graph.\n
    --------------\n
    graph [in]: Pointer to a graph instance.\n
    """
    return _vacl.destroyOpGraph(graph.ptr)

@err_check
def destroyOpStream(stream: Stream) -> int:
    """
    destroy the vacl op stream.\n
    --------------\n
    stream [in]: Pointer to the address of vaclStream with the stream instance.\n
    """
    return _vacl.destroyOpStream(stream.ptr)

@err_check
def subscribeStreamReport(stream: Stream, callback: Any, userCtx: Any) -> int:
    """
    Subscribe a callback function to the stream to receive the result report when a specific stream operator execution is completed.\n
    --------------\n
    stream [in]: Pointer to a stream instance.\n
    callback(op, inputDataset, outputDataset, status, userCtx) [in]: The callback function of type vaclStreamReportCallback.\n
        op: Pointer to a vace operator instance.\n
        inputDataset: a vacm input dataset instance.\n
        outputDataset: a vacm output dataset instance.\n
        status: a vacl callback status.\n
        userCtx: the user defined context.\n
    userCtx [in]: The user defined context to be passed into the callback function.\n
    """
    # 校验回调函数参数
    sig = inspect.signature(callback)
    params = sig.parameters
    try:
        assert len(params) == 5
        for i, (_, v) in enumerate(params.items()):
            if i == 0: assert v.annotation == Op
            elif i == 1: assert v.annotation == Dataset
            elif i == 2: assert v.annotation == Dataset
            elif i == 3: assert v.annotation == CallBackStatus
    except:
        tips = """
        Please check your callback, it should be like this(add args's annotation):
        def callback(op: vace.Op, inputDataset: vacm.Dataset, outputDataset: vacm.Dataset, status: vacl.CallBackStatus, userCtx):
            pass
        """
        raise Exception(tips)

    def _callback(op: Any, inputDataset: Any, outputDataset: Any, status: CallBackStatus, userCtx: Any):
        input_ = Dataset(inputDataset)
        output_ = Dataset(outputDataset)
        op_ = Op(op)
        callback(op_, input_, output_, status, userCtx)

    return _vacl.subscribeStreamReport(stream.ptr, _callback, userCtx)

def createOpStream(graph: OpGraph, mode: BALANCE_MODE = BALANCE_MODE.ONCE) -> Stream:
    """
    create the stream for running.\n
    --------------\n
    graph [in]: Pointer to a operator graph.\n
    mode [in]: Mode of stream to communicate with backend.\n
    """
    return Stream(_vacl.createOpStream(graph.ptr, mode))

def buildStream(stream: Stream) -> int:
    """
    Build the stream for running.\n
    --------------\n
     stream [in]: Pointer to a stream instance.\n
    """
    return _vacl.buildStream(stream.ptr)

def runStream(stream:Stream, datasetIn: Dataset, datasetOut: Dataset, timeout=100) -> int:
    """
    run the vacl stream.\n
    --------------\n
    stream [in]: Pointer to a stream instance. \n
    datasetIn [in]: Pointer to a vacmDataset with input.\n
    datasetOut [in]: Pointer to a vacmDataset with output instance. \n
    timeout [in]: Timeout value.\n
    """
    return _vacl.runStream(stream.ptr, datasetIn.ptr, datasetOut.ptr, timeout)

def runStreamAsync(stream:Stream, datasetIn: Dataset, datasetOut: Dataset) -> int:
    """
    run the vacl stream.\n
    --------------\n
    stream [in]: Pointer to a stream instance.\n
    input [in]: Pointer to a vacmDataset with input instance.\n
    output [in]: Pointer to a vacmDataset with output instance.\n
    """
    return _vacl.runStreamAsync(stream.ptr, datasetIn.ptr, datasetOut.ptr)

def synchronizeStream(stream:Stream, timeout: int=100) -> int:
    """
    Synchronize the running of a stream.\n
    --------------\n
    stream [in]: Pointer to a stream instance.\n
    timeout [in]: Timeout value (in millisecond). Value 0xFFFFFFFF (-1) means never timeout.\n
    """
    return _vacl.synchronizeStream(stream.ptr, timeout)

def synchronizeDevice(devId:int, timeout: int=100) -> int:
    """
    Synchronize the running of all stream of a device.\n
    --------------\n
    devId [in]: device index which maps to one die on a card. \n
    timeout [in]: Timeout value (in millisecond). Value 0xFFFFFFFF (-1) means never timeout.\n
    """
    return _vacl.synchronizeDevice(devId, timeout) 

def getStreamCacheNumber(stream:Stream) -> int:
    """
    Get the cache number of a stream.\n
    --------------\n
    stream [in]: Pointer to a stream instance.\n
    """
    return _vacl.getStreamCacheNumber(stream.ptr)

def requestOutputDataset(stream:Stream) -> Dataset:
    """
    request the output dataset.\n
    --------------\n
    stream [in]: Pointer to a stream instance.\n
    """
    return Dataset(_vacl.requestOutputDataset(stream.ptr))

def createGraphInputOp(graph: OpGraph, inputCnt: int) -> Op:
    """
    create the _vacl input op.\n
    --------------\n
    graph [in]: Pointer to a graph instance.\n
    inputCnt [in]: input number of a stream per batch .\n
    """
    return Op(_vacl.createGraphInputOp(graph.ptr, inputCnt))

@err_check
def connectOps(parent: Union[Op, OpBase], child: Union[Op, OpBase]) -> int:
    """
    connect the vacl op.\n
    --------------\n
    parent [in]: Pointer to the operator instance to be connected as parent node.\n
    child [in]: Pointer to the operator instance to be connected as child node.\n
    """
    if isinstance(parent, OpBase): parent = parent.op
    if isinstance(child, OpBase): child = child.op
    return _vacl.connectOps(parent.ptr, child.ptr)

def createRunModelOp(model: Union[Model, VastaiModel]) -> Op:
    """
    create the vacl run model op.\n
    --------------\n
    model [in]: Pointer to model instance.\n
    """
    if isinstance(model, VastaiModel):
        model = model.model
    return Op(_vacl.createRunModelOp(model.ptr))

@err_check
def registerGetOutput(stream: Stream, op: Union[Op, OpBase]) -> int:
    """
    Register a stream operator to the stream in order to get its output after model running.\n
    --------------\n
    stream [in]: Pointer to a stream instance.\n
    op [in]: Pointer to a vace operator instance whose outputs is that user want to get.\n
    """
    if isinstance(op, OpBase): op = op.op
    return _vacl.registerGetOutput(stream.ptr, op.ptr)

@err_check
def registerGetOutputs(stream: Stream, op: Union[Op, OpBase], opCount:int) -> int:
    """
    Register a stream operators to the stream in order to get its output after model running.\n
    --------------\n
    stream [in]: Pointer to a stream instance.\n
    ops [in]: Pointer to a vace operator array whose outputs is that user want to get.\n
    opCount [in]: the size of the vace operator array.\n
    """
    if isinstance(op, OpBase): op = op.op
    return _vacl.registerGetOutputs(stream.ptr, op.ptr, opCount)

class VastaiGraph():
    """
    Graph tool class.
    """
    def __init__(self, opGraph: OpGraph = None) -> None:
        """
        Graph tool class.\n
        --------------\n
        graph [in]: OpGraph have been created, if None create one.\n
        """
        if opGraph is None:
            self._graph = None
        else:
            self._graph = opGraph
        self.op_records = []
    
    def __enter__(self):
        self.create()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy()
    
    @property
    def graph(self) -> OpGraph:
        return self._graph
    
    def create(self) -> None:
        """
        create the vacl graph.
        """
        if self._graph is None:
            self._graph = createOpGraph()
    
    def createInputOp(self, inputCnt: int) -> Op:
        """
        create the _vacl input op.\n
        --------------\n
        inputCnt [in]: input number of a stream per batch .\n
        """
        assert self._graph is not None, "Please create graph."
        op = createGraphInputOp(self._graph, inputCnt)
        if op not in self.op_records: self.op_records.append(op)
        return op
    
    def connectOps(self, parent: Union[Op, OpBase], child: Union[Op, OpBase]) -> int:
        """
        connect the vacl op.\n
        --------------\n
        parent [in]: Pointer to the operator instance to be connected as parent node.\n
        child [in]: Pointer to the operator instance to be connected as child node.\n
        """
        if isinstance(parent, OpBase): parent = parent.op
        if isinstance(child, OpBase): child = child.op
        if parent not in self.op_records: self.op_records.append(parent)
        if child not in self.op_records: self.op_records.append(child)
        return connectOps(parent, child)
    
    def createRunModelOp(self, model: Union[Model, VastaiModel]) -> Op:
        """
        create the vacl run model op.\n
        --------------\n
        model [in]: Pointer to model instance.\n
        """
        return createRunModelOp(model)
    
    def destroy(self, includeOp: bool = False) -> None:
        """
        destroy the vacl graph.\n
        --------------\n
        includeOp [in]: Wether to destroy op in graph.\n
        """
        assert self._graph is not None, "Please create graph."
        destroyOpGraph(self._graph)
        # destory all op in op_records
        if includeOp:
            for op in self.op_records:
                destroyOp(op)
        self._graph = None
        self.op_records = []


class VastaiStream():
    """
    Stream tool class.
    """
    def __init__(self, opGraph: Union[OpGraph, VastaiGraph], mode: BALANCE_MODE = BALANCE_MODE.ONCE):
        """
        Stream tool class.\n
        --------------\n
        graph [in]: graph have been created.\n
        """
        if isinstance(opGraph, OpGraph):
            self.opGraph = opGraph
        else:
            self.opGraph = opGraph.graph
        self.mode = mode
        self._stream = None

    def __enter__(self):
        self.create()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy()
    
    @property
    def stream(self) -> Stream:
        return self._stream
    
    @property
    def cacheNum(self) -> int:
        return self.getStreamCacheNumber()

    def create(self) -> None:
        """
        create the stream for running.
        """
        if self._stream is None:
            self._stream = createOpStream(self.opGraph, self.mode)
    
    def destroy(self) -> None:
        """
        destroy the vacl op stream.
        """
        assert self._stream is not None, "Please create stream."
        destroyOpStream(self._stream)
        self._stream = None

    def build(self) -> int:
        """
        build the stream.
        """
        assert self._stream is not None, "Please create stream."
        return buildStream(self._stream)
    
    def run(self, datasetIn: Dataset, datasetOut: Dataset, timeout:int = 100) -> int:
        """
        run the stream.\n
        --------------\n
        datasetIn [in]: Pointer to a vacmDataset with input.\n
        datasetOut [in]: Pointer to a vacmDataset with output instance. \n
        timeout [in]: Timeout value.\n
        """
        assert self._stream is not None, "Please create stream."
        return runStream(self._stream, datasetIn, datasetOut, timeout)
    
    def registerGetOutput(self, runmodelOp:Op) -> int:
        """
        Register a stream operator to the stream in order to get its output after model running.\n
        --------------\n
        op [in]: Pointer to a vace operator instance whose outputs is that user want to get.\n
        """
        assert self._stream is not None, "Please create stream."
        return registerGetOutput(self._stream, runmodelOp)
    
    def registerGetOutputs(self, runmodelOp:Op, opCount:int) -> int:
        """
        Register a stream operators to the stream in order to get its output after model running.\n
        --------------\n
        ops [in]: Pointer to a vace operator array whose outputs is that user want to get.\n
        opCount [in]: the size of the vace operator array.\n
        """
        assert self._stream is not None, "Please create stream."
        return registerGetOutputs(self._stream, runmodelOp, opCount)
    
    def requestOutputDataset(self) -> Dataset:
        """
        request the output dataset.\n
        """
        assert self._stream is not None, "Please create stream."
        return requestOutputDataset(self._stream)
    
    def subscribeStreamReport(self, callback:Any, userCtx: Any) -> int:
        """
        Subscribe a callback function to the stream to receive the result report when a specific stream operator execution is completed.\n
        --------------\n
        callback(op, inputDataset, outputDataset, status, userCtx) [in]: The callback function of type vaclStreamReportCallback.\n
            op: Pointer to a vace operator instance.\n
            inputDataset: a vacm input dataset instance.\n
            outputDataset: a vacm output dataset instance.\n
            status: a vacl callback status.\n
            userCtx: the user defined context.\n
        userCtx [in]: The user defined context to be passed into the callback function.\n
        """
        assert self._stream is not None, "Please create stream."
        return subscribeStreamReport(self._stream, callback, userCtx)

    def runStreamAsync(self, datasetIn:Dataset, datasetOut:Dataset) -> int:
        """
        run the vacl stream.\n
        --------------\n
        input [in]: Pointer to a vacmDataset with input instance.\n
        output [in]: Pointer to a vacmDataset with output instance.\n
        """
        assert self._stream is not None, "Please create stream."
        return runStreamAsync(self._stream, datasetIn, datasetOut)
    
    def getStreamCacheNumber(self) -> int:
        """
        Get the cache number of a stream.\n
        """
        assert self._stream is not None, "Please create stream."
        return getStreamCacheNumber(self._stream)
    
    def synchronize(self, timeout: int = 100) -> int:
        """
        Synchronize the running of a stream.\n
        --------------\n
        timeout [in]: Timeout value (in millisecond). Value 0xFFFFFFFF (-1) means never timeout.\n
        """
        assert self._stream is not None, "Please create stream."
        return synchronizeStream(self._stream, timeout)
    
    
