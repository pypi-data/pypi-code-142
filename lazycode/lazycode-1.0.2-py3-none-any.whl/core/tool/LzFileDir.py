import os
import shutil
import datetime
import inspect

from lazycode.core.BaseType import BaseType


class LzFileDir(BaseType):
    __path: str = None

    def make_file(self, encoding='utf-8') -> bool: ...

    def read_content(self, mode='r', encoding='utf-8') -> object: ...

    def write_content(self, content, mode='w', encoding='utf-8') -> bool: ...

    def make_dirs(self) -> bool: ...

    def check_file_or_dir_exists(self) -> bool: ...

    def is_file(self) -> bool: ...

    def is_dir(self) -> bool: ...

    def rename_file_or_dir(self, new_name: str) -> bool: ...

    def remove_file_dir(self) -> bool: ...

    def abspath(self): ...

    def join(self, path: str): ...

    def split_dir_file(self) -> list: ...

    def base_dir(self): ...

    def get_filename(self): ...

    def get_drive(self) -> str: ...

    def get_suffix(self) -> str: ...

    # 获取文件, 大小(字节)
    def file_info_filesize(self) -> int: ...

    # 文件最后访问 时间
    def file_info_lvtime(self) -> str: ...

    # 文件最后修改 时间
    def file_info_lmtime(self) -> str: ...

    # 文件创建 时间
    def file_info_lctime(self) -> str: ...

    def deep_copy_file(self, to_path: str) -> bool: ...

    def list_dir_files(self) -> list: ...

    # 递归获取目录下的文件和目录, 包含三个参数 (当前目录路径, 当前目录下的所有目录, 当前目录下的所有文件)
    def walk(self) -> list: ...

    def deep_walk_all_file(self) -> list: ...

    # 获取对象的文件路径 inspect.getfile(LzFileDir().__class__)
    def get_class_file_path(self, obj: object): ...


class LzFileDirImp(LzFileDir):
    __path: str = None

    def __init__(self, path: str = None):
        self.init(path)

    def __str__(self) -> str:
        return self.to_string()

    def init(self, path: str):
        self.__path = path

    def to_string(self) -> str:
        return self.__path

    def base_type(self):
        return self.__path

    def copy(self):
        return LzFileDirImp(self.__path)

    def make_file(self, encoding='utf-8') -> bool:
        os.mknod(self.__path)
        return True

    def read_content(self, mode='r', encoding='utf-8') -> object:
        content = None
        with open(file=self.__path, mode=mode, encoding=encoding) as f:
            content = f.read()
        return content

    def write_content(self, content, mode='w', encoding='utf-8') -> bool:
        with open(file=self.__path, mode=mode, encoding=encoding) as f:
            f.write(content)
        return True

    def make_dirs(self) -> bool:
        os.makedirs(self.__path)
        return True

    def check_file_or_dir_exists(self) -> bool:
        return os.path.exists(self.__path)

    def is_file(self) -> bool:
        return os.path.isfile(self.__path)

    def is_dir(self) -> bool:
        print(self.__path)
        return os.path.isdir(self.__path)

    def rename_file_or_dir(self, new_name: str) -> bool:
        new_name = os.path.join(os.path.dirname(self.__path), new_name)
        os.rename(self.__path, new_name)
        return True

    def remove_file_dir(self) -> bool:
        if os.path.isfile(self.__path):
            os.remove(self.__path)
        else:
            shutil.rmtree(self.__path)

        return True

    def abspath(self):
        self.__path = os.path.abspath(self.__path)
        return self

    def join(self, path: str):
        self.__path = os.path.join(self.__path, path)
        return self

    def split_dir_file(self) -> list:
        return list(os.path.split(self.__path))

    def base_dir(self):
        self.__path = os.path.dirname(self.__path)
        return self

    def get_filename(self):
        return os.path.split(self.__path)[1]

    def get_filename_not_suffix(self):
        return os.path.splitext(os.path.split(self.__path)[1])[0]

    def get_drive(self) -> str:
        return os.path.splitdrive(self.__path)[0]

    def get_suffix(self) -> str:
        return os.path.splitext(self.__path)[1]

    # 获取文件, 大小(字节)
    def file_info_filesize(self) -> int:
        return os.stat(self.__path).st_size

    # 文件最后访问 时间
    def file_info_lvtime(self) -> str:
        timestamp = os.stat(self.__path).st_atime
        return datetime.datetime.fromtimestamp(timestamp).strftime(fmt='%Y-%m-%d %H:%M:%S.%f')

    # 文件最后修改 时间
    def file_info_lmtime(self) -> str:
        timestamp = os.stat(self.__path).st_mtime
        return datetime.datetime.fromtimestamp(timestamp).strftime(fmt='%Y-%m-%d %H:%M:%S.%f')

    def file_info_lctime(self) -> str:
        timestamp = os.stat(self.__path).st_ctime
        return datetime.datetime.fromtimestamp(timestamp).strftime(fmt='%Y-%m-%d %H:%M:%S.%f')

    def deep_copy_file(self, to_path: str) -> bool:
        shutil.copy2(self.__path, to_path)
        return True

    def list_dir_files(self) -> list:
        return os.listdir(self.__path)

    def walk(self) -> list:
        return list(os.walk(self.__path))

    def deep_walk_all_file(self) -> list:
        all_file = []
        for path, dirs, files in os.walk(self.__path):
            all_file.append(path)
            all_file.extend([os.path.join(path, f) for f in files])
        return all_file

    def get_class_file_path(self, obj: object):
        self.__path = inspect.getfile(obj.__class__)
        return self


# lz = LzFileDirImp()
#
# print(lz.get_class_file_path(BaseType()).base_dir().deep_walk_all_file())
#
# print(lz)
