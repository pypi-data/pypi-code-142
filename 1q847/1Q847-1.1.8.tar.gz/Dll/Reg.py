import ctypes
import os,time
from subprocess import Popen, PIPE

from comtypes.client import CreateObject


class RegDm:

    @classmethod
    def reg(cls):
        path = os.path.dirname(__file__)
        reg_dm = ctypes.windll.LoadLibrary(path + r'\DmReg.dll')
        reg_dm.SetDllPathW(path + r'\dm.dll', 0)
        return CreateObject(r'dm.dmsoft')

    @classmethod
    def create_dm(cls):
        return CreateObject(r'dm.dmsoft')


class LDCmd:
    def __init__(self, path: str):
        os.putenv('Path', path)

    @staticmethod
    def read_message(cmd):
        res = Popen(cmd, stdout=PIPE, shell=True)
        res = res.stdout.read().decode(encoding='GBK')
        return res

    def lunch(self, order: str):
        self.read_message('ldconsole.exe launch --index ' + order)

    def quit(self, order: str):
        self.read_message(cmd='ldconsole.exe quit --index ' + order)

    def get_message(self):
        return self.read_message('ldconsole.exe  list2')
        # 索引，标题，顶层窗口句柄，绑定窗口句柄，是否进入android，进程PID，VBox进程PID

    def add(self, name: str):
        self.read_message('ldconsole.exe add --name ' + name)

    def remove(self, order: str):
        self.read_message('ldconsole.exe remove --index ' + order)

    def copy(self, name: str, order: str):
        self.read_message('ldconsole.exe copy --name ' + name + ' --from ' + order)

    def start_app(self, order: str, packagename: str):
        self.read_message('ldconsole.exe runapp --index ' + order + ' --packagename ' + packagename)

    def close_app(self, order: str, packagename: str):
        self.read_message('ldconsole.exe killapp --index ' + order + ' --packagename ' + packagename)

    def get_list_package(self, order: str):
        return self.read_message(cmd='ld.exe -s ' + order + '  pm list packages')

    def install_app(self, order: str, path: str):
        self.read_message('ldconsole.exe  installapp --index ' + order + ' --filename ' + path)

    def sort_wnd(self):
        self.read_message('ldconsole.exe sortWnd')

    def reboot(self, order: str):
        self.read_message('ldconsole.exe reboot --index ' + order)

    def get_appoint_message(self, order: str,index:int):
        my_list = self.get_message()
        items = my_list.splitlines()
        return items[int(order)].split(',')[index]


class Memory:
    def __init__(self, dx, hwd):
        self.__dx = dx
        self.hwd = hwd

    def get_call_address(self, s, model, off):
        # 返回16进制字符串地址
        module_size = self.__dx.GetModuleSize(self.hwd, model)
        base_address = self.__dx.GetModuleBaseAddr(self.hwd, model)
        end_address = module_size + base_address
        call_address = self.__dx.FindData(self.hwd, hex(base_address)[2:] + '-' + hex(end_address)[2:], s)
        return hex(int(call_address, 16) + int(off, 16))[2:]

    def x64_get_base_address(self, s, model, off):
        address = self.get_call_address(s, model, off)
        address_2 = self.__dx.readint(self.hwd, address, 4)
        return hex(int(address, 16) + address_2 + 4)[2:]

    def x32_get_base_address(self, s, model, off):
        address = self.get_call_address(s, model, off)
        address = self.__dx.readint(self.hwd, address, 4)
        return hex(address)[2:]

class Auto_Dm:
    def __init__(self,my_dx):

        self.dx=my_dx
        self.ret = None
        self.tup=None
    def reg(self,code,md)->int:
        return self.dx.reg(code,md)
    def BindWindowEx(self,hwnd,display,mouse,keypad,public,mode)->int:
        return self.dx.BindWindowEx(hwnd,display,mouse,keypad,public,mode)
    def EnumWindowByProcess(self,process_name,title,class_name,filter)->str:
        return self.dx.EnumWindowByProcess(process_name,title,class_name,filter)
    def set_path(self, s)->int:
        return self.dx.setpath(s)

    def FindPic(self,pic_name,t=100,x1=0, y1=0, x2=960, y2=540):
        t1 = time.time()
        while time.time() - t1 < t:
            self.ret = self.dx.FindPic(x1, y1, x2, y2, pic_name, '050505', 0.9, 0)
            if self.ret[2] != -1:
                print(f'find {pic_name}')
                return self
    def click_point(self,x,y,t=1):
        self.dx.MoveTo(x,y)
        for i in range(0, t):
            self.dx.LeftClick()
            time.sleep(0.1)
        return self

    def click(self,t=1):
        self.dx.MoveTo(self.ret[0],self.ret[1])
        for i in range(0, t):
            self.dx.LeftClick()
            time.sleep(0.1)
        return self
    def sleep(self, t):
        time.sleep(t)
        return self




if __name__ == '__main__':
    dm=RegDm.reg()
    auto_dm = Auto_Dm(dm)


