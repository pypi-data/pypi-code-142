"""
    TCP 服务端

    菜鸟教程
    https://www.runoob.com/python/python-socket.html

    问题 1：粘包
        描述：即发送消息，接收方不知道单次发送大小，导致接收方一次接收到发送方的多次消息，导致粘包

        解决：使用 struct 模块，每次发送信息前，都发送一下当前数据的长度，再去接收
"""
import socket
import threading
import time
from pathlib import Path
from typing import List, Type
from loguru import logger
from gsocket.sender import SocketSender
from gsocket.receiver import SocketReceiver


class ServerHousekeeper(threading.Thread):
    def __init__(
            self,
            client: socket.socket,
            clients: List[socket.socket],
            size: int,
            timeout: int,
            receiver: SocketReceiver,
            encoding: str = None
    ):
        """
        服务于每个客户端连接的管家

        :param client: 当前连接客户端
        :param clients: 所有的客户端
        :param size: 接收的大小
        :param timeout: 超时时间
        :param receiver: 信息接收器
        :param encoding: 编码格式
        """
        super().__init__()
        self.client = client
        self.clients = clients
        self.size = size
        self.timeout = timeout
        self.receiver = receiver
        self.encoding = encoding or 'utf-8'

        self.address = self.client.getpeername()  # 客户端的 ip、port
        self.sender = self.receiver.sender

    def run(self) -> None:
        """
        客户端循环监听

        :return:
        """
        # 启动函数
        self.on_open()

        try:
            # 监听消息
            self.receiver.start()

            # 等待执行结束
            self.waiting_done()
        finally:
            # 关闭函数
            self.on_close()

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

    def waiting_done(self):
        """
        等待接收、发送线程执行完毕

        :return:
        """
        while True:
            if not self.receiver.is_alive():
                break

            time.sleep(0.1)

    def on_open(self):
        """
        客户端建立连接时

        :return:
        """
        self.clients.append(self.client)
        if self.client.gettimeout() is None:
            self.client.settimeout(self.timeout)
        logger.debug(f'建立新连接：{self.address}')

    def on_close(self):
        """
        客户端关闭时

        :return:
        """
        self.client.close()
        self.clients.remove(self.client)
        logger.debug(f"已断开连接：{self.address}")


class SocketServer:
    def __init__(
            self,
            host: str = None,
            port: int = None,
            listen: int = None,
            size: int = None,
            timeout: int = None,
            receiver: Type[SocketReceiver] = None,
            file_recv_path: str = None,
            encoding: str = None
    ):
        """

        :param host: host
        :param port: port
        :param listen: 一个服务同时处理几个
        :param size: 接受文件切片大小
        :param timeout: 超时时间
        :param receiver: 信息接收器
        :param file_recv_path: 文件接收路径
        :param encoding: 编码格式
        """
        self.host = host or '127.0.0.1'
        self.port = port or 8866
        self.listen = listen or 5
        self.size = size or 1024
        self.timeout = timeout or 30
        self.receiver = receiver or SocketReceiver
        self.file_recv_path = file_recv_path or Path(__file__).parent
        self.encoding = encoding or 'utf-8'

        self.server = None  # 服务端
        self.clients = []  # 存储所有连接的客户端

    def start_server(self):
        """
        开启 TCP 服务

        :return:
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(self.listen)

        logger.debug(f"服务端已启动，当前监听：{self.server.getsockname()}")

        while True:
            client, addr = self.server.accept()
            receiver = self.receiver(
                client=client,
                size=self.size,
                sender=SocketSender(client=client),
                file_recv_path=self.file_recv_path,
                encoding=self.encoding
            )
            ServerHousekeeper(
                client=client,
                clients=self.clients,
                size=self.size,
                timeout=self.timeout,
                receiver=receiver,
                encoding=self.encoding
            ).start()

    def __del__(self):
        self.server.close()


if __name__ == '__main__':
    SocketServer().start_server()
