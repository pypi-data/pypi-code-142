"""
    接收器

    注意：这里使用了 struct 先发送消息头，才会去发送消息，所以其它的程序发送的，没有头的话可能接收不到
"""
import socket
import struct
import threading
from pathlib import Path
from loguru import logger
from gsocket import singal
from typing import Generator
from gsocket.sender import SocketSender


class SocketReceiver(threading.Thread):
    def __init__(self, client: socket.socket, sender: SocketSender, size: int = None, file_recv_path: str = None,
                 encoding: str = None):
        """

        :param client: socket 连接
        :param size: 一次接收的最大大小
        :param sender: 发送器
        :param file_recv_path: 文件接收路径
        :param encoding: 编码格式
        """
        super().__init__(daemon=True)
        self.client = client
        self.size = size or 1024
        self.sender = sender
        self.file_recv_path = Path(file_recv_path)
        self.encoding = encoding or 'utf-8'

    def run(self) -> None:
        """
        监控数据接收

        :return:
        """
        try:
            while True:
                header = self.client.recv(4)  # 获取报头

                print(header)
                print(header.decode())
                if header == b'':
                    break

                msg_cache = self.recv_msg(header)

                # 判断是文件还是信息，分别发送到不同的接收函数
                if msg_cache == singal.File:
                    file_receiver = self.recv_file()
                    filename = next(file_receiver)
                    self.on_file(filename, file_receiver)
                elif msg_cache == singal.CLOSE:
                    break
                else:
                    self.on_message(msg_cache)
        except ConnectionError:
            logger.warning(f"远程主机断开：{self.client.getpeername()}")

    def recv_msg(self, header: bytes) -> bytes:
        """
        接收信息

        :param header: 消息头
        :return:
        """
        # 获取待接收数据长度
        length = struct.unpack('i', header)[0]

        # 计算每次接收的长度
        if length <= self.size:
            index = length
        else:
            index = self.size

        # 开始接收数据
        msg_cache = b''  # 已接收的数据
        received_length = 0  # 已接收长度
        while True:
            msg = self.client.recv(index)
            msg_cache += msg

            # 累加已接收长度
            received_length += len(msg)
            if received_length == length:
                break

            # 判断下次接收长度（针对这里 self.size 接收的比较小的情况）
            if length - received_length < self.size:
                index = length - received_length

        return msg_cache

    def recv_file(self):
        """
        接收信息，返回的是文件内容的迭代器

        :return:
        """
        file_header = struct.calcsize('128sl')
        file_buffer = self.client.recv(file_header)

        if file_buffer:
            filename, filesize = struct.unpack('128sl', file_buffer)
            filename = filename.strip(b'\x00').decode()

            yield filename

            filesize_count = 0
            while True:
                header = self.client.recv(4)
                data = self.recv_msg(header=header)
                filesize_count += len(data)

                if data:
                    yield data

                if filesize_count >= filesize:
                    break

    def send(self, msg: str):
        """
        发送消息

        :param msg:
        :return:
        """
        self.sender.send(msg=msg)

    def sendall(self, msg: str):
        """
        发送消息

        :param msg:
        :return:
        """
        self.sender.sendall(msg=msg)

    def sendfile(self, filepath: str):
        """
        发送文件

        :param filepath:
        :return:
        """
        self.sender.sendfile(filepath=filepath)

    def on_open(self):
        """
        客户端建立连接时

        :return:
        """
        pass

    def on_message(self, msg: bytes):
        """
        接收到消息时

        :param msg:
        :return:
        """
        logger.info(msg.decode(self.encoding))

    def on_file(self, filename: str, file_iterator: Generator):
        """
        接收到文件时

        :param filename: 文件名
        :param file_iterator: 文件内容生成器
        :return:
        """
        filepath = self.file_recv_path.joinpath(filename)
        with open(filepath, 'wb') as f:
            for file_buffer in file_iterator:
                f.write(file_buffer)

        logger.debug(f"文件已保存到本地：{filepath}")

    def on_close(self):
        """
        客户端关闭时

        :return:
        """
        pass
