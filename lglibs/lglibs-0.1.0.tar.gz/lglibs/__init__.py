import sys as _system
import inspect as _inspect
import time as _time
import os as _os
import base64 as _base64
import string as _string
from . import color as _color

if _os.name == "posix":
    import paramiko as _paramiko

def _merge_string_list(obj: list):
    new_string = ""
    for text in obj: new_string += text
    return new_string

class StringBytes:
    @staticmethod
    def encode(content: str, save: bool = False, save_path:str=None):
        if not save and save_path is not None:
            raise ValueError("save is off, but still have save path")
        elif save and save_path is None:
            raise ValueError("save is on, but save path is None")
        elif save and save_path is not None:
            file = open(save_path, "wb")
            file.write(_base64.b64encode(content.encode("ascii")))
            file.close()
        else:
            return _base64.b64encode(content.encode("ascii"))
    @staticmethod
    def decode(_bytes: bytes = None, read: bool = False, read_path: str = None):
        if _bytes is not None and read:
            raise ValueError("Bytes have been passed in but read mode is still on")
        elif not read and read_path is not None:
            raise ValueError("read is off, but still have read path")
        elif read and read_path is None:
            raise ValueError("read is on, but read path is None")
        elif read and read_path is not None:
            file = open(read_path, "rb")
            content = _base64.b64decode(file.read()).decode("utf-8")
            file.close()
            return content
        else:
            return _base64.b64decode(_bytes).decode("utf-8")

def decimal(obj: float):
    _obj = str(obj)
    returned = []
    for index in range(1, len(_obj)):
        if _obj[-index] == ".": break
        else: returned.append(_obj[-index])
    returned.reverse()
    rstring = ""
    for char in returned: rstring += char
    return rstring
def Round(obj: float, _to: int = 0):
    if not _to: return round(obj)
    if len(str(decimal(obj))) < _to:
        return round(obj, _to)
    decimals = list(str(decimal(obj)))
    count = 1
    AddOne = False
    if len(decimals) == 1: return obj
    try:
        if int(decimals[_to]) >= 5:
            decimals[_to - 1] = str(int(decimals[_to - 1]) + 1)
    except IndexError:
        count = 1
        while True:
            try:
                if int(decimals[_to - count]) >= 5:
                    decimals[_to - 1] = str(int(decimals[_to - 1]) + 1)
                break
            except IndexError: continue
    del decimals[_to: len(decimals)]
    while int(decimals[_to - count]) == 10:
        if _to - count <= 0: decimals[_to - count] = "0"; AddOne = True; break
        decimals[_to - count] = "0"
        decimals[_to - count - 1] = str(int(decimals[_to - count - 1]) + 1)
        count += 1
    decimals = _merge_string_list(decimals)
    Object = str(int(obj))
    res = Object + "." + decimals
    if AddOne: return float(res) + 1
    else: return float(res)
def Range(range_x: int or float, range_y: int or float = None, step: int or float = None):
    if range_y is None: range_y = range_x; range_x = 0
    if step is None: step = 1
    if range_x < range_y:
        while range_x < range_y:
            yield range_x
            range_x += step
    if range_x > range_y:
        while range_x >= range_y:
            yield range_x
            range_x -= step
def frange(a: list, start=0, end=0): return range(start, len(a) + end)
def calculator(algorithm: str) -> int or float:
    class cache(): 
        def __init__(self, value: object) -> None: self.value = value
        def clear(self) -> None: self.value = ""; self = None
    def Indexs(mainlist:list, listarg: list) -> list:
        p = [].copy()
        for index in range(len(mainlist)):
            if mainlist[index] == listarg:
                p.append(index)
        return p
    algm: list = list(algorithm)
    Sposes: list = None
    Dposes: list = None
    Qposes: list = None
    if "*" in algm: Sposes: list = Indexs(algm, "*")
    if "/" in algm: Dposes: list = Indexs(algm, "/")
    if "^" in algm: Qposes: list = Indexs(algm, "^")
    caches: cache = cache(str())
    for index in range(len(algm)):
        if algm[index] != " ": caches.value += algm[index]
    # 这里去处空格
    algm = list(caches.value); caches.clear()
    count: int = int()
    # 数字合并
    while True:
        try:
            if algm[count] == ".":
                p = str()
                for x in algm[count - 1: count + 2]: p += str(x)
                del algm[count - 1: count + 2]
                algm.insert(count - 1, p)
            if algm[count] == "-":
                X = algm[count] + algm[count + 1]
                del algm[count: count + 2]
                algm.insert(count, X)
            x: str = str(int(algm[count]))
            y: str = str(int(algm[count + 1]))
            del algm[count: count + 2]
            algm.insert(count, x + y)
            count = 0
        except ValueError: count += 1; continue
        except IndexError: break
    # 转化数字
    for index in range(len(algm)):
        try: algm[index] = float(algm[index])
        except ValueError: continue
    # 加减运算
    if not Sposes and not Dposes and not Qposes:
        while True or True or True or True:
            try:
                p = algm[0] + algm[2]
                del algm[:3]
                algm.insert(0, p)
            except IndexError: break
            
        return algm[0]
    else:
        caches: cache = cache(int())
        counts: cache = cache(list())
        #while "(" in algm:
            
        if "*" in algm: Sposes: list = Indexs(algm, "*")
        if "/" in algm: Dposes: list = Indexs(algm, "/")
        if "^" in algm: Qposes: list = Indexs(algm, "^")
        sort = dict().copy()
        for positions in Sposes: sort[positions] = "Sposes"
        for positions in Dposes: sort[positions] = "Dposes"
        for positions in Qposes: sort[positions] = "Qposes"
        # insert SDQ to sort dict
        position = dict()
        poslist = sorted(sort.keys())
        for pos in poslist: position[pos] = sort[pos]
        count = 0
        for index, types in position.items():
            index -= count
            if types == "Sposes": X = algm[index - 1] * algm[index + 1]
            if types == "Dposes": X = algm[index - 1] / algm[index + 1]
            if types == "Qposes": X = algm[index - 1] ** algm[index + 1]
            del algm[index - 1: index + 2]
            count += 2
            algm.insert(index - 1, X)
        new_algorithm = str()
        for algms in algm: new_algorithm += str(algms)
        return calculator(new_algorithm)


def get_ttyinfo():
    fd = _system.stdin.fileno()
    old_ttyinfo = _termios.tcgetattr(fd)
    new_ttyinfo = old_ttyinfo[:]
    new_ttyinfo[3] &= ~_termios.ICANON
    new_ttyinfo[3] &= ~_termios.ECHO
    return fd, old_ttyinfo, new_ttyinfo


# Convert variable name to string
def nameof(var):
    callers_local_vars = _inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var][0]

def breakdown(obj):
    return_list = [].copy()
    for index in range(len(obj)):
        try:
            for _index in range(len(obj[index])):
                return_list.append(obj[index][_index])
        except TypeError:
            continue
    return return_list
                
def var(value):
    try:
        int(value)
        if "." in value:
            return float(value)
        else: return int(value)
    except ValueError:
        if value.lower() in ("none", "null"):
            return None
        if value.lower() == "true":
            return True
        if value.lower() == "false":
            return False
        import ast
        return ast.literal_eval(value)

class cursor:
    def __init__(self):
        self._ci = None
        if _os.name == "nt":
            self._msvcrt = __import__("msvcrt")
            self._ctypes = __import__("ctypes")
            class _CursorInfo(self._ctypes.Structure):
                _fields_ = [("size", self._ctypes.c_int), ("visible", self._ctypes.c_byte)]
            self._ci = _CursorInfo()
    def hide(self):
        if _os.name == "nt":
            handle = self._ctypes.windll.kernel32.GetStdHandle(-11)
            self._ctypes.windll.kernel32.GetConsoleCursorInfo(handle, self._ctypes.byref(self.ci))
            self._ci.visible = False
            self._ctypes.windll.kernel32.SetConsoleCursorInfo(handle, self._ctypes.byref(self.ci))
        elif _os.name == "posix":
            _system.stdout.write("\033[?25l")
            _system.stdout.flush()
    def show(self):
        if _os.name == "nt":
            handle = self._ctypes.windll.kernel32.GetStdHandle(-11)
            self._ctypes.windll.kernel32.GetConsoleCursorInfo(handle, self._ctypes.byref(self.ci))
            self._ci.visible = True
            self._ctypes.windll.kernel32.SetConsoleCursorInfo(handle, self._ctypes.byref(self.ci))
        elif _os.name == "posix":
            _system.stdout.write("\033[?25h")
            _system.stdout.flush()
    if _os.name == "posix":
        import re as _re
        import tty as _tty
        import termios as _termios
        def position(self):
            _buffer = ""
            stdin = _system.stdin.fileno()
            termios_attrs = _termios.tcgetattr(stdin)
            try:
                _tty.setcbreak(stdin, _termios.TCSANOW)
                _system.stdout.write("\x1b[6n")
                _system.stdout.flush()
                while True:
                    _buffer += _system.stdin.read(1)
                    if _buffer[-1] == "R": break
            finally:
                _termios.tcsetattr(stdin, _termios.TCSANOW, termios_attrs)
            try:
                matches = _re.match(r"^\x1b\[(\d*);(\d*)R", _buffer)
                groups = matches.groups()
            except AttributeError:
                return None
            class pos: x = int(groups[1]); y = int(groups[0])
            return pos

class console:
    @staticmethod
    def write(*content, timer: int = 0.02, skip=breakdown(_color.__color__),sep=" " ,end="\n", wait=((",", 0.5), (".", 0.5), ("!", 0.5), ("?", 0.5)), replace=None):
        for text in content:
            text = str(text)
            for index in range(len(text)):
                wd = text[index]
                if replace:
                    for re in replace:
                        if wd == re[0]: wd = re[1]
                _system.stdout.write(wd)
                _system.stdout.flush()
                if type(skip) is str and wd != skip: _time.sleep(timer)
                elif type(skip) is list and wd not in skip: _time.sleep(timer)
                for w in wait:
                    if wd == w[0]: _time.sleep(w[1])
            _system.stdout.flush()
        print(end=end, flush=True)
    @staticmethod
    def read(putout: str = "", rtype=str, **args):
        console.write(putout, end="", **args)
        return rtype(input(""))
    @staticmethod
    def clearline(): _system.stdout.write("\r" + " " * _os.get_terminal_size().columns + "\r"); _system.stdout.flush()
    @staticmethod
    def reline(): print(end="\033[F", flush=True)
    if _os.name == "posix":
        import termios as _termios
        @staticmethod
        def simulation(desc="command: ", key_event=lambda **kwargs: tuple(kwargs.values())):
            import subprocess
            subprocess.run("", shell=True)
            cs = cursor()
            def writef(content):
                _system.stdout.write(content)
                _system.stdout.flush()
            command = ""
            ttyinfo = get_ttyinfo()
            key = ""
            writef(desc)
            while 1:
                _termios.tcsetattr(ttyinfo[0], _termios.TCSANOW, ttyinfo[2])
                key = _os.read(ttyinfo[0], 7).decode("utf-8")
                _termios.tcsetattr(ttyinfo[0], _termios.TCSANOW, ttyinfo[1])
                if key == "\n": break
                elif key == "\x7f":
                    try:
                        ocmd = list(command)
                        del ocmd[cs.position().x - 2]
                        command = _merge_string_list(ocmd)
                        writef("\r" + " " * (len(command) + len(desc) + 1) + "\r")
                        writef(desc + command)
                        continue
                    except IndexError:
                        command = ""
                        writef("\r" + " " * (len(command) + len(desc) + 1) + "\r")
                        writef(desc + command)
                        continue
                elif key == "\x1b[A" or key == "\x1b[B": key = ""
                
                command, key, ttyinfo = key_event(command = command, key = key, ttyinfo = ttyinfo)
                #print(cs.position().x)
                if len(command) >= cs.position().x:
                    lcmd = list(command)
                    lcmd.insert(cs.position().x - 1, key)
                    command = _merge_string_list(lcmd)
                else: command += key
                writef("\r" + desc + command)
            print(flush = True)
            command = command.split(" ")
            return command

class Bytes:
    def __init__(self, obj, tag="b"):
        if type(obj) is list: self.object = obj
        else: self.object = [obj]
        self.length = len(obj)
        self.tag = tag.upper()
        self.tags = ["BIT", "B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB", "BB", "NB", "DB",
                    "bit", "b", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "BiB", "NiB", "DiB"]
        self.__check__(tag)
        
    def __check__(self, obj):
        if obj in self.tags: pass
        elif obj.upper() in self.tags: pass
        else: raise TypeError(f"unknown byte type \"{obj}\"")
    
    def convert(self, ByteType: str):
        self.__check__(ByteType)
        if self.tag.lower() == "bit" or ByteType.lower() == "bit":
            pass
        else:
            index = self.tags.index(self.tag)
            convertindex = self.tags.index(ByteType)
            out = self.tags[index: convertindex]
            for _ in frange(out):
                if index > convertindex: self.length = self.length * 1024
                else: self.length = self.length / 1024
            self.tag = ByteType
            
            newObj = list()
            
            

if _os.name == "posix":
    import re as _re
    import tty as _tty
    import termios as _termios
    
    
    class Server:
        class __SFTP:
            def __init__(self, ssh: _paramiko.SSHClient = None):
                if ssh is not None:
                    self.scp = ssh.open_sftp()
            def update(self, *args, **kwargs):
                self.scp.get(*args, **kwargs)
            def upload(self, *args, **kwargs):
                self.scp.put(*args, **kwargs)
            def close(self):
                self.scp.close()
        def __init__(self, host: str, user: str, password: str, keypath: str, port: int = 22, **kwargs):
            self.ssh = _paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(_paramiko.AutoAddPolicy())
            self.host = host
            self.user = user
            self.password = password
            self.keypath = keypath
            self.port = port
            self.kwargs = kwargs
            self.sftp = self.__SFTP(None)
    
        def connect(self, timeout: int = 3, wait_time: float = 5.5):
            while True:
                try:
                    self.ssh.connect(self.host, self.port, self.user, self.password, key_filename=self.keypath, **self.kwargs)
                    break
                except Exception as error:
                    _time.sleep(wait_time)
                    timeout -= 1
                    if timeout <= 0:
                        return error
            self.sftp = self.__SFTP(self.ssh)
    
        def get_connect_count(self):
            return int(self.send("netstat -na | grep ESTABLISHED | wc -l").get("stdout"))
        
        def send(self, command):
            class Standard:
                def __init__(self, stdin: _paramiko.channel.ChannelStdinFile, stdout: _paramiko.channel.ChannelFile, stderr: _paramiko.channel.ChannelStderrFile):
                    self.input = stdin
                    self.output = stdout
                    self.error = stderr
                    self.stdin = stdin
                    self.stdout = stdout
                    self.stderr = stderr
                    self.value = (stdin, stdout, stderr)
                def __getitem__(self, key):
                    if key is int: return self.value[key]
                    if key is str: return self.__dict__[key]
                def get(self, standard):
                    if type(standard) is str:
                        return self.__dict__[standard].read().decode("utf-8")
                    else: return standard.read().decode("utf-8")
    
            return Standard(*tuple(self.ssh.exec_command(command)))
    
        def get(self, server_file, local_file=None, mode="r"):
            if local_file is None: local_file = server_file
            self.sftp.update(server_file, local_file)
            file = open(local_file, mode)
            content = file.read()
            file.close()
            _os.remove(local_file)
            return content
    
        def disconnect(self):
            self.ssh.close()
            self.sftp.close()
        

    def KeyDownContinue(event=lambda fd: _os.read(fd, 7).decode("utf-8")):
        fd = _system.stdin.fileno()
        old_ttyinfo = _termios.tcgetattr(fd)
        new_ttyinfo = old_ttyinfo[:]
        new_ttyinfo[3] &= ~_termios.ICANON
        new_ttyinfo[3] &= ~_termios.ECHO
        _termios.tcsetattr(fd, _termios.TCSANOW, new_ttyinfo)
        key = event(fd)
        _termios.tcsetattr(fd, _termios.TCSANOW, old_ttyinfo)
        return key

    def getpass(echo="*"):
        fd = _system.stdin.fileno()
        old_ttyinfo = _termios.tcgetattr(fd)
        new_ttyinfo = old_ttyinfo[:]
        new_ttyinfo[3] &= ~_termios.ICANON
        new_ttyinfo[3] &= ~_termios.ECHO
        password = ""
        key = ""
        while key != "\n":
            _termios.tcsetattr(fd, _termios.TCSANOW, new_ttyinfo)
            key = _os.read(fd, 7).decode("utf-8")
            _termios.tcsetattr(fd, _termios.TCSANOW, old_ttyinfo)
            if key == "\x7f":
                password = password[:-1]
                _system.stdout.write("\r" + " " * (len(password) + len(echo)) + "\r")
                _system.stdout.flush()
                _system.stdout.write(echo * len(password))
                _system.stdout.flush()
                continue
            password += key
            _system.stdout.write("\r")
            _system.stdout.flush()
            _system.stdout.write(echo * len(password))
            _system.stdout.flush()
        print(flush=True)
        return password


