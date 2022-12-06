"""
    发送器

    注意：这里使用了 struct 先发送消息头，才会去发送消息
"""
import os
import socket
import struct
from typing import Union
from gsocket import singal


class SocketSender:
    def __init__(self, client: socket.socket, size: int = None, encoding: str = None):
        """

        :param client: 连接
        :param size: 单次最大发送大小
        :param encoding: 编码格式
        """
        self.client = client
        self.size = size or 1024
        self.encoding = encoding or 'utf-8'

    def send(self, msg: Union[str, bytes]):
        """
        发送 TCP 消息
        并非是一次性发送完，所以要接收剩余长度

        :param msg:
        :return:
        """
        if isinstance(msg, str):
            msg = msg.encode(self.encoding)

        index = 0
        length = len(msg)

        while True:
            msg_send = msg[index:]
            self.send_msg_header(msg=msg_send)
            index = self.client.send(msg_send)  # 返回发送的长度

            if index < length:
                index += 1
            else:
                break

    def sendall(self, msg: Union[str, bytes]):
        """
        完整的发送 TCP 消息（推荐）

        :param msg:
        :return:
        """
        if isinstance(msg, str):
            msg = msg.encode(self.encoding)

        self.send_msg_header(msg=msg)
        self.client.sendall(msg)

    def sendfile(self, filepath: str):
        """
        发送文件

        :param filepath:
        :return:
        """
        self.send_file_header(filepath=filepath)

        with open(filepath, 'rb') as f:
            while True:
                data = f.read(self.size)
                if not data:
                    break

                self.sendall(msg=data)

    def send_msg_header(self, msg: bytes):
        """
        创建消息头

        :param msg:
        :return:
        """
        # 先发送标志
        header = struct.pack('i', len(msg))
        self.client.sendall(header)

    def send_file_header(self, filepath: str):
        """
        发送文件头

        :param filepath: 文件路径
        :return:
        """
        # 先告诉其将发送文件
        self.sendall(msg=singal.File)

        # 定义文件头信息（包含文件名和文件大小）
        file_header = struct.pack('128sl', os.path.basename(filepath).encode(self.encoding), os.stat(filepath).st_size)

        # 发送文件头
        self.client.sendall(file_header)
