"""
    TCP 客户端

    示例1：
        tcp = SocketClient()
        tcp.send(msg="你好啊，今天是10.05号")
        tcp.sendall(msg="你好啊，今天是10.05号")
        tcp.close()

    示例2：
        with SocketClient() as tcp:
            tcp.send(msg="你好啊，今天是10.05号")
            tcp.sendall(msg="你好啊，今天是10.05号")
            tcp.sendfile(r'D:\Download\wallpaper\wallhaven-3lo8q3_1920x1080.png')
"""
import socket
from typing import Type
from pathlib import Path
from gsocket import singal
from gsocket.sender import SocketSender
from gsocket.receiver import SocketReceiver


class SocketClient:
    def __init__(
            self,
            host: str = None,
            port: int = None,
            size: int = None,
            timeout: int = None,
            receiver: Type[SocketReceiver] = None,
            file_recv_path: str = None,
            encoding: str = None,
    ):
        """

        :param host: host
        :param port: port
        :param size: 单次接收大小
        :param timeout: 超时时间
        :param receiver: 信息接收器
        :param file_recv_path: 文件接收路径
        :param encoding: 编码格式
        """
        self.host = host or '127.0.0.1'
        self.port = port or 8866
        self.size = size or 1024
        self.timeout = timeout or 30
        receiver = receiver or SocketReceiver
        self.file_recv_path = file_recv_path or Path(__file__).parent
        self.encoding = encoding

        # 创建连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.client.settimeout(self.timeout)
        self.closed = False
        self.sender = SocketSender(client=self.client)
        self.receiver = receiver(
            client=self.client,
            size=self.size,
            sender=self.sender,
            file_recv_path=self.file_recv_path,
            encoding=self.encoding
        )
        self.receiver.start()

    def connect(self):
        """
        创建连接

        :return:
        """

        return self

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

    def _send_close_signal(self):
        """
        发送结束信号，让服务器释放连接

        :return:
        """
        self.send(singal.CLOSE)

        while True:
            if not self.receiver.is_alive():
                break

    def close(self):
        if not self.closed:
            self._send_close_signal()
            self.client.close()
            self.closed = True

    def __enter__(self):
        self.connect()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
