import json
import typing
from typing import Union

import grpc

from . import ZoneSenderData
from .ObjIo import *

from .Protos import TcpIpNode_pb2, TcpIpNode_pb2_grpc



class TcpIpNodeClient(object):
    def __init__(self) -> None:
        """
        TcpIpNode 的客户端
        """
        self._tcpipStub = TcpIpNode_pb2_grpc.TcpIpNodeStub(
            channel=grpc.insecure_channel(
                target='{0}:{1}'
                    .format(
                        ZoneSenderData.TCPIP_STACK_NODE_IP, 
                        ZoneSenderData.TCPIP_STACK_NODE_PORT),
                options = ZoneSenderData.GRPC_OPTIONS
            )
        )

    def Init(self,appBName:str = 'CANoe') -> 'int':
        try:
            res_ = self._tcpipStub.InitTcpIpStack(
                TcpIpNode_pb2.Common__pb2.generic_string(
                    text = appBName,
                )
            )
            print('Init result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000
    
    def GetVectorPortInfo(self) -> Union['int','list'] :
        try:
            res_ = self._tcpipStub.GetAllVectorPortInfo(
                TcpIpNode_pb2.Common__pb2.empty()
            )
            if res_.result.result == 0 :
                port_list = list()
                for item in res_.all_port :
                    item_dict = {'networkName':item.networkName,
                                 'switchName':item.switchName,
                                 'portName':item.portName,
                                 'portType':item.portType}
                    port_list.append(item_dict)
                return port_list
            else :
                raise Exception(f'{res_.result.reason}')
        except Exception as e_ :
            print(e_)
            return 1000
    
    def OpenVectorPort(self,networkName:str,switchName:str,portName:str,portType:str) :
        try:
            res_ = self._tcpipStub.OpenVectorPort(
                TcpIpNode_pb2.vector_port_info(
                    networkName = networkName,
                    switchName = switchName,
                    portName = portName,
                    portType = portType,
                )
            )
            return res_.result
        except Exception as e_ :
            print(e_)
    
    def Start(self) :
        try:
            res_ = self._tcpipStub.StartTcpIpStack(
                TcpIpNode_pb2.Common__pb2.empty()
            )
            return res_.result
        except Exception as e_ :
            print(e_)
    
    def Stop(self) :
        try:
            res_ = self._tcpipStub.StopTcpIpStack(
                TcpIpNode_pb2.Common__pb2.empty()
            )
            return res_.result
        except Exception as e_ :
            print(e_)
