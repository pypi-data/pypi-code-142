#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   device_manage.py
@Time    :   2020/08/14 15:40:08
@Author  :   bianxinbing
@Version :   1.0
@Contact :   bianxinbing@baidu.com
@License :   Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
@Desc    :   None
"""
import os
import plistlib
import select
import shutil
import socket
import struct
import threading
import time
from typing import Dict

from logzero import logger


def analyse_usbmuxd_header(sock: socket.socket):
    """[summary]
    Args:
        sock (socket.socket): [description]
    Returns:
        [type]: [description]
    """
    big_end = False
    large_payload = False
    buffer_len = sock.recv(20)
    if len(buffer_len) != 20:
        if len(buffer_len) > 0:
            buffer_len1 = sock.recv(20 - len(buffer_len))
            buffer_len = buffer_len + buffer_len1
        else:
            logger.info("no data to recv")
            return 0, 0, 0, ''
    if buffer_len[4:8] == b"<?xm":
        dlen = struct.unpack(">I", buffer_len[:4])[0]
        big_end = True
        if dlen > 4096:
            large_payload = True
    elif buffer_len[16:] == b"<?xm":
        dlen = struct.unpack("I", buffer_len[:4])[0]
        if dlen > 4096:
            large_payload = True
    else:
        return -1, 0, 0, buffer_len
    return dlen, big_end, large_payload, buffer_len


def get_remain_package(dlen, sock):
    buffer = sock.recv(dlen - 20)
    while len(buffer) < dlen - 20:
        temp_buffer = sock.recv(dlen - 20 - len(buffer))
        buffer += temp_buffer
    return buffer


def analyse_packaget(buffer_len, buffer):
    plist = plistlib.loads(buffer_len[16:] + buffer)
    return plist


class SocketRelay():
    def __init__(self, local_sock: socket.socket, remote_sock: socket.socket):
        self.local_sock = local_sock
        self.remote_sock = remote_sock
        self.request_status = False
        self.response_status = False

    def request(self):
        while True:
            try:
                buffer = self.local_sock.recv(0x400)
                if len(buffer) == 0:
                    logger.debug("[-] No request data received! Breaking...")
                    self.response_status = False
                    # self.close_request()
                    self.close_sock()
                    break
                self.remote_sock.sendall(buffer)
            except Exception as e:
                logger.debug(e)
                break

    def response(self):
        while True:
            try:
                buffer = self.remote_sock.recv(0x400)
                if len(buffer) == 0:
                    logger.debug("[-] No response data received! Breaking...")
                    self.request_status = False
                    self.close_sock()
                    # self.close_response()
                    break
                self.local_sock.sendall(buffer)
            except Exception as e:
                logger.debug(e)
                break

    def close_sock(self):
        logger.debug(f"close {self.local_sock.fileno()}")
        logger.debug(f"close {self.remote_sock.fileno()}")
        self.local_sock.close()
        self.remote_sock.close()

    def close_request(self):
        while self.request_status:
            logger.debug('wait request_status')
            time.sleep(0.1)
        logger.debug("close request socket")
        self.local_sock.close()

    def close_response(self):
        while self.response_status:
            time.sleep(0.1)
        logger.debug("close response socket")
        self.remote_sock.close()


def transfer(src: socket.socket, dst):
    while True:
        buffer = src.recv(0x400)
        if len(buffer) == 0:
            logger.debug("[-] No data received! Breaking...")
            src.close()
            dst.close()
            return
        try:
            dst.sendall(buffer)
        except Exception as e:
            logger.debug(e)
            logger.debug("error")
            logger.debug(buffer)


def usbmuxd_proxy(local_sock, remote_devices):
    remote_socks = {}
    remote_sock_list = []
    for device in remote_devices.values():
        ip = device.ip
        port = device.port
        ip_port = "%s:%s" % (ip, port)
        if ip_port not in remote_socks.keys():
            logger.info((ip, port))
            if ip != "localhost":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port))
            else:
                sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                sock.connect(device.ios_usbmuxd_real)
            logger.debug(sock.fileno())
            remote_socks[ip_port] = sock
    while True:
        break_flag = True
        remote_sock_list = [sock for sock in remote_socks.values()]
        read_socks = [local_sock] + remote_sock_list
        rs, ws, xs = select.select(read_socks, [], read_socks)
        if local_sock in rs:
            dlen, big_end, large_payload, buffer_len = analyse_usbmuxd_header(
                local_sock)
            if len(buffer_len) == 0:
                logger.debug("no data")
                pass
            else:
                break_flag = False
                if dlen == -1:
                    buffer = local_sock.recv(8192)
                    logger.debug("unknow request:", (buffer_len + buffer))
                    for remote_sock in remote_sock_list:
                        remote_sock.sendall(buffer_len + buffer)
                elif large_payload:
                    buffer = local_sock.recv(8192)
                    for remote_sock in remote_sock_list:
                        remote_sock.sendall(buffer_len + buffer)
                elif not big_end:
                    dlen, version, resp, tag = struct.unpack(
                        "IIII", buffer_len[:16])
                    buffer = get_remain_package(dlen, local_sock)
                    plist = plistlib.loads(buffer_len[16:] + buffer)
                    logger.debug(
                        f"request {dlen}, {version}, {resp}, {tag}, {plist}")
                    if "MessageType" in plist and plist["MessageType"] == "ListDevices":
                        logger.debug("MessageType ListDevices")
                        device_list = {'DeviceList': []}
                        header = b""
                        for remote_sock in remote_sock_list:
                            remote_sock.sendall(buffer_len + buffer)
                            r_dlen, r_big_end, r_large_payload, r_buffer_len = analyse_usbmuxd_header(
                                remote_sock)
                            r_buffer = get_remain_package(r_dlen, remote_sock)
                            r_plist = plistlib.loads(
                                r_buffer_len[16:] + r_buffer)
                            logger.debug(f"return device {r_plist}")
                            for device_info in r_plist['DeviceList']:
                                for udid in remote_devices.keys():
                                    if udid == device_info['Properties']['SerialNumber']:
                                        device_info['DeviceID'] = remote_devices[udid].local_id
                                        device_info['Properties']['DeviceID'] = remote_devices[udid].local_id
                                        device_list['DeviceList'].append(
                                            device_info)
                            header = r_buffer_len[4:16]
                        logger.debug(f"finally return device {device_list}")
                        payload = plistlib.dumps(device_list)
                        dlen = len(payload) + 16
                        dlen = struct.pack("I", dlen)
                        buffer_len = dlen + buffer_len[4:]
                        buffer = payload[4:]
                        local_sock.sendall(buffer_len + buffer)
                    else:
                        if "MessageType" in plist and plist["MessageType"] == "Connect":
                            logger.debug("Connect")
                            dst_sock = None
                            for device in remote_devices.values():
                                if device.local_id == plist['DeviceID']:
                                    plist['DeviceID'] = device.remote_id
                                    dst_sock = remote_socks[device.ip +
                                                            ":" + str(device.port)]
                                    for other_remote_sock in remote_socks.values():
                                        if other_remote_sock != dst_sock:
                                            other_remote_sock.close()
                                    remote_socks.clear()
                                    remote_socks[device.ip + ":" +
                                                 str(device.port)] = dst_sock
                                    header = buffer_len[4:16]
                                    payload = plistlib.dumps(plist)
                                    dlen = struct.pack("I", (len(payload) + 16))
                                    dst_sock.sendall(dlen + header + payload)
                                    break
                            relay = SocketRelay(local_sock, dst_sock)
                            t1 = threading.Thread(target=relay.request)
                            t2 = threading.Thread(target=relay.response)
                            t1.start()
                            t2.start()
                            tl = []
                            tl.append(t1)
                            tl.append(t2)
                            logger.debug("wait connect thread")
                            for t in tl:
                                t.join()
                            logger.debug("connect thread finish")
                            break
                        elif "MessageType" in plist and plist["MessageType"] == "ReadPairRecord":
                            for device in remote_devices.values():
                                if device.udid == plist['PairRecordID']:
                                    dst_sock = remote_socks[device.ip +
                                                            ":" + str(device.port)]
                                    header = buffer_len[4:16]
                                    payload = plistlib.dumps(plist)
                                    dlen = struct.pack("I", (len(payload) + 16))
                                    dst_sock.sendall(dlen + header + payload)
                                    break
                        else:
                            for remote_sock in remote_sock_list:
                                remote_sock.sendall(buffer_len + buffer)
                else:
                    buffer = local_sock.recv(dlen - 16)
                    logger.info(buffer_len + buffer)
                    plist = plistlib.loads(buffer_len[4:] + buffer)
                    # if "Request" in plist and plist["Request"] == "StartSession":
                    #     try:
                    #         print("HostID",plist["HostID"],"SystemBUID",plist["SystemBUID"])
                    #     except Exception:
                    #         pass
                    for remote_sock in remote_sock_list:
                        remote_sock.sendall(buffer_len + buffer)
        remote_read_socks = [sock for sock in rs if sock != local_sock]
        logger.debug("len: %s", len(remote_read_socks))
        for remote_sock in remote_read_socks:
            dlen, big_end, large_payload, buffer_len = analyse_usbmuxd_header(
                remote_sock)
            if len(buffer_len) == 0:
                pass
            else:
                break_flag = False
                if dlen == -1:
                    buffer = remote_sock.recv(8192)
                    logger.info(f"unknow response:{buffer_len + buffer}")
                    try:
                        local_sock.sendall(buffer_len + buffer)
                    except Exception:
                        logger.error(dlen, big_end, large_payload,
                                     buffer_len + buffer)
                        logger.debug(local_sock)
                elif large_payload:
                    buffer = remote_sock.recv(8192)
                    local_sock.sendall(buffer_len + buffer)
                elif not big_end:
                    dlen, version, resp, tag = struct.unpack(
                        "IIII", buffer_len[:16])
                    buffer = get_remain_package(dlen, remote_sock)
                    plist = plistlib.loads(buffer_len[16:] + buffer)
                    logger.debug(
                        f"reponse {dlen}, {version}, {resp}, {tag}, {plist}")
                    if "DeviceID" in plist and 'Properties' in plist:
                        udid = plist["Properties"]["SerialNumber"]
                        if udid in remote_devices.keys():
                            local_id = remote_devices[udid].local_id
                            plist["DeviceID"] = local_id
                            plist["Properties"]["DeviceID"] = local_id
                            buffer = plistlib.dumps(plist)
                            dlen = len(buffer) + 16
                            dlen = struct.pack("I", dlen)
                            buffer = buffer[4:]
                            buffer_len = dlen + buffer_len[4:]
                        else:
                            continue
                    logger.info("response small end:")
                    logger.info(plist)
                    local_sock.sendall(buffer_len + buffer)
                else:
                    buffer = get_remain_package(dlen, remote_sock)
                    logger.info("response big end:", buffer)
                    local_sock.sendall(buffer_len + buffer)
        if break_flag:
            break
    logger.debug(f"close local {local_sock.fileno()}")
    local_sock.close()
    logger.debug(f"local_sock {local_sock.fileno()} closed")
    for sock in remote_socks.values():
        # sock.shutdown(socket.SHUT_RDWR)
        logger.debug(f"remote {sock.fileno()} closed")
        sock.close()
    logger.debug("finish")


class Device(object):
    def __init__(self, udid, ip, port):
        # self.platform = platform
        self.udid = udid
        self.ip = ip
        self.port = port
        if self.ip == "localhost":
            self.port = 8256
        self.local_id = -1
        self.remote_id = -1


DeviceDict = Dict[str, Device]


def get_local_devices():
    list_device_query = {'BundleID': 'org.libimobiledevice.usbmuxd', 'ClientVersionString': 'usbmuxd built for freedom',
                         'MessageType': 'ListDevices', 'ProgName': 'libusbmuxd', 'kLibUSBMuxVersion': 3}
    query_str = plistlib.dumps(list_device_query)
    dlen = len(query_str) + 16
    header = struct.pack("IIII", dlen, 1, 8, 0)
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    if os.path.exists("/var/run/usbmuxd_real"):
        sock.connect("/var/run/usbmuxd_real")
    else:
        sock.connect("/var/run/usbmuxd")
    sock.sendall(header + query_str)
    dlen, big_end, large_payload, buffer_len = analyse_usbmuxd_header(sock)
    buffer = get_remain_package(dlen, sock)
    plist = analyse_packaget(buffer_len, buffer)
    device_list = plist['DeviceList']
    device_udids = []
    for device_info in device_list:
        device_udids.append(device_info['Properties']['SerialNumber'])
    return device_udids


class IOSDevice(Device):
    def __init__(self, udid, ip, port) -> None:
        super(IOSDevice, self).__init__(udid, ip, port)
        self.ios_usbmuxd_real = "/var/run/usbmuxd_real"

    def set_local_id(self, local_id):
        self.local_id = local_id

    def set_remote_id(self, remote_id):
        self.remote_id = remote_id

    def connect(self):
        list_device_query = {'BundleID': 'org.libimobiledevice.usbmuxd',
                             'ClientVersionString': 'usbmuxd built for freedom',
                             'MessageType': 'ListDevices', 'ProgName': 'libusbmuxd', 'kLibUSBMuxVersion': 3}
        query_str = plistlib.dumps(list_device_query)
        dlen = len(query_str) + 16
        header = struct.pack("IIII", dlen, 1, 8, 0)
        ip = self.ip
        port = self.port
        if ip != "localhost":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
        else:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            if os.path.exists(self.ios_usbmuxd_real):
                sock.connect(self.ios_usbmuxd_real)
            else:
                sock.connect("/var/run/usbmuxd")
        sock.sendall(header + query_str)
        dlen, big_end, large_payload, buffer_len = analyse_usbmuxd_header(sock)
        buffer = get_remain_package(dlen, sock)
        plist = analyse_packaget(buffer_len, buffer)
        device_list = plist['DeviceList']
        find_device = False
        for device_info in device_list:
            if device_info['Properties']['SerialNumber'] == self.udid:
                self.remote_id = device_info["DeviceID"]
                find_device = True
                break
        if not find_device:
            logger.error(
                f"device connect failed on {self.ip}:{self.port} ! pls check device ip and port")
            return False
        logger.debug(
            f"device {self.udid} : (lcoal_id {self.local_id}) (remote_id {self.remote_id})")
        return True

    def disconnect(self):
        pass


class UsbmuxdRelay():
    def __init__(self, remote_devices):
        self.remote_devices: Dict = remote_devices
        self.usbmuxd = "/var/run/usbmuxd"
        self.usbmuxd_real = "/var/run/usbmuxd_real"
        self.__status = "init"

    def remove_device_by_udid(self, udid):
        self.remote_devices.pop(udid)

    def __replace_usbmuxd(self):
        if os.path.exists(self.usbmuxd):
            if not os.path.exists(self.usbmuxd_real):
                shutil.move(self.usbmuxd, self.usbmuxd_real)
            else:
                os.remove(self.usbmuxd)

    def __init_server(self):
        self.__replace_usbmuxd()
        self.usbmuxd_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.usbmuxd_sock.bind(self.usbmuxd)
        import stat
        os.chmod(self.usbmuxd, stat.S_IRWXO)
        self.usbmuxd_sock.listen(0x10)
        # self.__status = "init_server"

    def __relay(self):
        self.__init_server()
        while True and self.__status == "start":
            logger.debug("[+] ready accept...")
            local_sock, local_address = self.usbmuxd_sock.accept()
            logger.debug("[+] Tunnel connected! Transferring data...")
            s = threading.Thread(target=usbmuxd_proxy, args=(
                local_sock, self.remote_devices))
            s.start()

    def start(self):
        if self.__status != "start":
            self.__status = "start"
            self.relay_pid = threading.Thread(target=self.__relay, daemon=True)
            self.relay_pid.start()

    def join(self):
        self.relay_pid.join()

    def stop(self):
        self.__status = "stop"


class IOSDeviceManage(object):
    def __init__(self):
        self.remote_devices: DeviceDict = {}
        self.__device_index = 1
        self.local_devices = []

    def start(self):
        self.local_devices = get_local_devices()
        for udid in self.local_devices:
            self.add_device(IOSDevice(udid, "localhost", "8200"))
        check_thread = threading.Thread(target=self.check_local_device)
        check_thread.setDaemon(True)
        check_thread.start()

    def check_local_device(self):
        while True:
            new_device_list = get_local_devices()
            offline_devices = [d for d in self.local_devices if d not in new_device_list]
            new_devices = [d for d in new_device_list if d not in self.local_devices]
            for udid in offline_devices:
                self.remove_device_by_udid(udid)
                logger.error("local device [" + udid + "] offline")
                self.local_devices.remove(udid)
            for udid in new_devices:
                self.add_device(IOSDevice(udid, "localhost", "8200"))
                logger.error("new local device [%s] connect" % udid)
            self.local_devices = new_device_list
            time.sleep(10)

    def add_device(self, device: Device):
        if device.udid not in self.remote_devices.keys():
            device.local_id = self.__device_index
            self.__device_index += 1
            self.remote_devices[device.udid] = device
            device.connect()

    def remove_device_by_udid(self, udid):
        if udid not in self.remote_devices.keys():
            logger.error("device has not add into local devices list")
            return False
        else:
            self.remote_devices.pop(udid)
            return True

    def connect_devices(self):
        # for device in self.remote_devices.values():
        #     device.connect()
        self.usbmuxd_relay = UsbmuxdRelay(self.remote_devices)
        self.usbmuxd_relay.start()
        # time.sleep(2)
        # for device in self.remote_devices.values():
        #     device.connect()
        # TODO prepare iOS DeviceSupport

    def disconnect_devices(self):
        try:
            self.usbmuxd_relay.stop()
        except:
            pass
        if os.path.exists("/var/run/usbmuxd_real"):
            if os.path.exists("/var/run/usbmuxd"):
                os.remove("/var/run/usbmuxd")
                shutil.move("/var/run/usbmuxd_real", "/var/run/usbmuxd")
                logger.error("recovery usbmuxd")
            else:
                shutil.move("/var/run/usbmuxd_real", "/var/run/usbmuxd")
        self.remote_devices.clear()

    def disconnect_device_by_udid(self, udid):
        self.remove_device_by_udid(udid)
