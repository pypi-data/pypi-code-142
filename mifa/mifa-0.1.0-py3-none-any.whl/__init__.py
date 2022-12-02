__author__ = """King Orz"""
__email__ = "kin9-0rz@outlook.com"
__version__ = "0.1.0"

import json
import os
import platform
import shutil
import subprocess
import time
from pathlib import Path

import psutil
import toml
from rich import print

__home__ = os.path.expanduser("~")

is_win = platform.system() == "Windows"

ANDROID_SDK_PATH = "ANDROID_SDK_PATH"
MITMPROXY_PATH = "MITMPROXY_PATH_PATH"
AVD_PACKAGE = "AVD_PACKAGE"
AVD_NAME = "AVD_NAME"
MITMPROXY_CACERT_NAME = "MITMPROXY_CACERT_NAME"

import configparser

configParser = configparser.ConfigParser()


class AVDConfig:
    def __init__(self, avd_name) -> None:
        self.avd_config_path = os.path.join(
            __home__, ".android", "avd", "{}.avd".format(avd_name)
        )
        self.config_path = os.path.join(self.avd_config_path, "config.ini")
        self.hardware_qemu_path = os.path.join(
            self.avd_config_path, "hardware-qemu.ini"
        )

    def update_config(self):
        with open(self.config_path, "r+", encoding="utf-8") as f:
            txt = f.read()
            txt = txt.replace("vm.heapSize=64M", "vm.heapSize=384")
            txt = txt.replace("hw.keyboard=no", "hw.keyboard=yes")
            txt = txt.replace("hw.gpu.enabled=no", "hw.gpu.enabled=yes")
            txt = txt.replace("hw.sdCard=yes", "hw.sdCard=no")
            txt = txt.replace("hw.ramSize=96M", "hw.ramSize=1536")
            txt += "skin.dynamic=yes\n"
            txt += "skin.name=1440x2880\n"
            txt += "skin.path=_no_skin\n"
            f.write(txt)
            # disk.dataPartition.path = <temp> disk.dataPartition.size=6G


class Configure:
    __cfg_path__ = os.path.join(__home__, ".mifa.toml")

    def __init__(self) -> None:
        self.cfg = {}
        self.__android_sdk_path = ""
        self.__mitmproxy_path = ""
        self.__avd_package = "system-images;android-28;google_apis;x86"
        self.__avd_name = "mavd9"
        self.__mitmproxy_cacert_name = ""

        self.load()

    @property
    def mitmproxy_cacert_name(self):
        return self.__mitmproxy_cacert_name

    @mitmproxy_cacert_name.setter
    def mitmproxy_cacert_name(self, name):
        self.__mitmproxy_cacert_name = name

    @property
    def android_sdk_path(self):
        return self.__android_sdk_path

    @android_sdk_path.setter
    def android_sdk_path(self, path):
        if not os.path.exists(path):
            print("{} 目录不存在".format(path))
            return
        self.__android_sdk_path = path

    @property
    def mitmproxy_path(self):
        return self.__mitmproxy_path

    @mitmproxy_path.setter
    def mitmproxy_path(self, path):
        if not os.path.exists(path):
            print("{} 目录不存在".format(path))
            return
        self.__mitmproxy_path = path

    @property
    def avd_package(self):
        return self.__avd_package

    @avd_package.setter
    def avd_package(self, package):
        self.__avd_package = package

    @property
    def avd_name(self):
        return self.__avd_name

    @avd_name.setter
    def avd_name(self, name):
        self.__avd_name = name

    def save(self):
        with open(self.__cfg_path__, "w") as f:
            toml.dump(
                {
                    ANDROID_SDK_PATH: self.android_sdk_path,
                    MITMPROXY_PATH: self.mitmproxy_path,
                    MITMPROXY_CACERT_NAME: self.mitmproxy_cacert_name,
                    AVD_PACKAGE: self.avd_package,
                    AVD_NAME: self.avd_name,
                },
                f,
            )
        self.load()

    def load(self):
        if not os.path.exists(self.__cfg_path__):
            self.save()
        self.cfg = toml.load(self.__cfg_path__)
        self.__android_sdk_path = self.cfg.get(ANDROID_SDK_PATH, "")
        self.__mitmproxy_path = self.cfg.get(MITMPROXY_PATH, "")
        self.__avd_package = self.cfg.get(
            AVD_PACKAGE, "system-images;android-28;google_apis;x86"
        )
        self.__avd_name = self.cfg.get(AVD_NAME, "mavd9")
        self.__mitmproxy_cacert_name = self.cfg.get(MITMPROXY_CACERT_NAME, "")

    def show(self):
        print(json.dumps(self.cfg, indent=2))


def run_cmd(cmd_list: list, yes=None):
    try:
        proc = subprocess.Popen(
            cmd_list,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
        )

        if yes:
            proc.stdin.write(yes.encode())

        (output, error) = proc.communicate()
        output = output.decode("utf-8")
        error = error.decode("utf-8")

    except Exception as err:
        raise err

    return output, error


def run_cmd_async(cmd_list):
    """异步执行命令，运行某些阻塞命令的时候，直接退出。"""
    try:
        proc = subprocess.Popen(
            cmd_list,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
        )

        ret_code = None
        try:
            ret_code = proc.wait(3)
        except Exception as _:
            _

        if ret_code is not None and ret_code != 0:
            print("Error : {}".format(proc.stderr.readline().decode("utf-8")))

    except Exception as err:
        raise err


class SDKManager:
    def __init__(self) -> None:
        cfg = Configure()
        self.sdkmanager = os.path.join(
            cfg.android_sdk_path,
            "cmdline-tools",
            "latest",
            "bin",
            "sdkmanager.bat" if is_win else "sdkmanager",
        )

    def list_installed(self):
        r, _ = run_cmd([self.sdkmanager, "--list_installed"])
        arr = r.split("\n")
        flag = False

        packages = []
        for item in arr:
            if "-------" in item:
                flag = True
                continue
            if flag:
                if "|" not in item:
                    continue
                parts = item.split()
                packages.append(parts[0])
        return packages

    def list(self):
        return subprocess.Popen([self.sdkmanager, "--list"])

    def update(self):
        return subprocess.Popen([self.sdkmanager, "--update"])

    def install(self, name):
        proc = subprocess.Popen([self.sdkmanager, name])
        proc.wait()
        proc.kill()


class EmulatorManager:
    def __init__(self) -> None:
        cfg = Configure()
        self.avdmanager = os.path.join(
            cfg.android_sdk_path,
            "cmdline-tools",
            "latest",
            "bin",
            "avdmanager.bat" if is_win else "avdmanager",
        )
        self.sdkmanager = os.path.join(
            cfg.android_sdk_path,
            "cmdline-tools",
            "latest",
            "bin",
            "sdkmanager.bat" if is_win else "sdkmanager",
        )
        self.emulator = os.path.join(
            cfg.android_sdk_path,
            "emulator",
            "emulator.exe" if is_win else "emulator",
        )
        self.adb = os.path.join(
            cfg.android_sdk_path,
            "platform-tools",
            "adb.exe" if is_win else "adb",
        )
        self.cacerts_path = "/system/etc/security/cacerts"

    def _build_command(self, cmd):
        self._build_command_c(cmd, target=self._target)

    def delete_avd(self, name):
        cmds = [self.avdmanager, "delete", "avd", "-n", name]
        run_cmd(cmds)

    def create_avd(self, package: str, name: str, force=False):
        cmds = [
            self.avdmanager,
            "create",
            "avd",
            "-k",
            "system-images;android-28;google_apis;x86",
            "-n",
            "mavd9",
            "-f",
            "--device",
            "pixel_2_xl",
        ]
        # id: 18 or "pixel_2_xl"
        # Name: Pixel 2 XL
        # OEM : Google

        run_cmd(cmds, "no")
        # hw.keyboard=no

    def list_avds(self):
        cmds = [self.emulator, "-list-avds"]
        r, _ = run_cmd(cmds)
        return r.split()

    def has_avd(self, name):
        return name in self.list_avds()

    def start_avd(self, name, proxy=None):
        cmds = [
            self.emulator,
            "-avd",
            name,
            "-writable-system",
            "-tcpdump",
            "net.pcap",
        ]

        if proxy:
            cmds.append("-http-proxy")
            cmds.append(proxy)

        if self.__avd_is_ready():
            return

        run_cmd_async(cmds)
        time.sleep(3)

        # NOTE SDK异常的情况，adb找不到模拟器
        if self.adb_devices() is None:
            raise Exception("adb could not found any devices.")

        while True:
            if self.__avd_is_ready():
                time.sleep(1)
                break

    def adb_devices(self):
        r, _ = run_cmd([self.adb, "devices"])
        if "\r\n" in r.strip():
            arr = r.strip().split("\r\n")
        else:
            arr = r.strip().split("\n")
        if len(arr) == 1:
            return

        devices = []
        for item in arr[1:]:
            devices.append(item.split()[0])
        return devices

    def __avd_is_ready(self):
        r, _ = run_cmd([self.adb, "shell", "getprop", "sys.boot_completed"])
        if len(r.split()) == 0:
            return False
        return r.split()[0] == "1"

    def remount(self):
        run_cmd([self.adb, "root"])
        run_cmd([self.adb, "remount"])

    def install_cert(self, cert_path):
        self.remount()
        run_cmd([self.adb, "push", cert_path, self.cacerts_path])
        # NOTE 不是必要操作
        # https://kpj.github.io/misc/InterceptingHTTPTraffic.html
        # target_path = Path(os.path.join(self.cacerts_path)).as_posix()
        # run_cmd(
        #     [
        #         self.adb,
        #         "chmod",
        #         "664",
        #         target_path,
        #     ]
        # )
        run_cmd([self.adb, "unroot"])
        self.reboot()

    def push(self, local_path, remove_path):
        run_cmd([self.adb, "push", local_path, remove_path])

    def check_cert(self, cert_name):
        target_path = Path(os.path.join(self.cacerts_path)).as_posix()
        r, _ = run_cmd([self.adb, "shell", "ls", target_path])
        return cert_name in r.split()

    def root(self):
        run_cmd([self.adb, "root"])

    def reboot(self):
        run_cmd([self.adb, "reboot"])
        while True:
            if self.__avd_is_ready():
                time.sleep(3)
                break

    def close(self):
        run_cmd([self.adb, "emu", "kill"])


class MitmproxyManager:
    def __init__(self):
        cfg = Configure()
        self.mitmweb = os.path.join(
            cfg.mitmproxy_path,
            "mitmweb.exe" if is_win else "mitmweb",
        )
        self.mitmdump = os.path.join(
            cfg.mitmproxy_path,
            "mitmdump.exe" if is_win else "mitmdump",
        )
        self.mitmproxy_cert_dir = os.path.join(__home__, ".mitmproxy")
        self.cer_path = os.path.join(__home__, ".mitmproxy", "mitmproxy-ca-cert.cer")
        self.__check_certs()
        self.mitmweb_process = None

    def check_openssl(self):
        paths = (
            os.environ["PATH"].split(";") if is_win else os.environ["PATH"].split(":")
        )
        openssl_name = "openssl.exe" if is_win else "openssl"
        for cmdpath in paths:
            if os.path.isdir(cmdpath) and openssl_name in os.listdir(cmdpath):
                print(":white_check_mark: openssl is ok.")
                return True
        print(":x: please install openssl.")
        return False

    def gen_android_cert(self):
        """Generate cert file for Android

        CA Certificates in Android are stored by the name of their hash,
        with a ‘0’ as extension (Example: c8450d0d.0). It is necessary to
        figure out the hash of your CA certificate
        and copy it to a file with this hash as filename.
        Otherwise Android will ignore the certificate.

        Returns:
            _type_: _description_
        """
        if not self.check_openssl():
            print("openssl does not exist.")
            return
        r = subprocess.check_output(
            [
                "openssl",
                "x509",
                "-inform",
                "PEM",
                "-subject_hash_old",
                "-in",
                self.cer_path,
            ]
        )
        name = r.decode().split()[0] + ".0"
        path = os.path.join(self.mitmproxy_cert_dir, name)
        shutil.copy(self.cer_path, path)
        return path

    def run_mitmweb(self):
        self.mitmweb_process = subprocess.Popen(
            [self.mitmweb],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )

    def kill_mitmweb(self):
        pobj = psutil.Process(self.mitmweb_process.pid)
        for c in pobj.children(recursive=True):
            c.kill()
        self.mitmweb_process.kill()

    def __check_certs(self):
        if os.path.exists(self.cer_path):
            return
        self.__generate_certs()

    def __generate_certs(self):

        proc = subprocess.Popen([self.mitmdump], stdout=subprocess.PIPE)
        time.sleep(3)
        # NOTE Windows需要杀死它的子进程。
        pobj = psutil.Process(proc.pid)
        for c in pobj.children(recursive=True):
            c.kill()
        pobj.kill()
