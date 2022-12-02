import typing

class AutoSARData(object):
    def __init__(self) -> None:
        self.value = None        # 本对象的名字
        self.name = ''           # 本对象的名字
        pass

    def set(self, value:typing.Any):
        '''
        设置本类的值
        子类重写的时候，应该用 typing 或直接类型提示的方式明显的告诉用户入参的类型是什么
        如 int, str, float
        '''
        pass

    def get(self) -> typing.Any:
        '''
        返回本类的值
        子类重写的时候，应该用 typing 或直接类型提示的方式明显的告诉用户 get 的类型是什么
        如 int, str, float
        '''
        pass

    def pack(self) -> typing.Any:
        '''
        打包本对象
        子类继承的时候，应该用用 typing 或者直接类型提示的方式明显的告诉用户 pack 后的数据类型是什么
        子类重写该函数返回的类型根据子类的类型不同，可能是如下类型
        - ZoneSender.ObjIo.SomeipPackage
        - ZoneSender.ObjIo.LinSignal
        - ZoneSender.ObjIo.ZoneSenderObject 的各种子类
        '''

    def unpack(self, obj:typing.Any) -> None:
        '''
        将 ZoneSender.ObjIo 中的各种 obj 对象的值赋值给本对象
        :param obj: 子类继承的时候需要使用 typing 或直接类型提示的方式提示输入的类型
        调用该函数后，就可以在后面通过 . 的方式获取该对象成员变量的值
        如果解包失败，要 raise Error
        '''
        raise ValueError("未实现")