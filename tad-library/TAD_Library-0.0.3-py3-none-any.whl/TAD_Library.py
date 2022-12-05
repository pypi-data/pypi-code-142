import logging
import socket

global client_socket
logger = logging.getLogger(__name__)

def TAD_Connect(ip, port):
    """
    TAD-B 연결 함수 입니다.

        :param ip(string) : IP address (ex. "123.456.789.111")

        :param port(int) : port number (ex. 1234)

        :returns : None
    """
    global client_socket

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))



def TAD_Disconnect():
    global client_socket
    try:
        client_socket.close()
        return 1
    except:
        return 0


def TAD_IsConnect() -> bool:
    global client_socket
    try:
        client_socket.send("CHECK")
        return True
    except Exception as e:
        logger.exception("unexpected exception when checking if a socket is closed")
        return False


def TAD_SendCmd(cmd):
    """
    TAD 장비 명령어 전달 함수 입니다.

        :param cmd(bytearray) : Byte Array (ex. [0x01, 0x01, 0x01])

        :returns : None
    """
    global client_socket
    try:
        client_socket.send(cmd)
        return 1
    except:
        return 0

def TAD_SetSwitch(btnNum, state):
    """
    TAD-B 버튼 제어 함수 입니다.

        :param btnNum(int) : Button Index(0~11)

        :param state(int) : On(0x01) / Off(0x00)

        :returns : None
    """
    global client_socket
    data = bytearray([btnNum,state])

    TAD_SendCmd(data)

def TAD_SetVoltage(voltage):
   """
   TAD-B 전압 제어 함수 입니다.

       :param btnNum(int) : Voltage Value (0~30)

       :returns : None
   """
   global client_socket
   data = bytearray([0x12, voltage])

   TAD_SendCmd(data)