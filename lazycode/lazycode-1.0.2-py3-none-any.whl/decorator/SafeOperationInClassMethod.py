import copy
import logging
import time

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


class SafeInfo(object):
    __var_open_safe = True

    def open_safe(self):
        self.__var_open_safe = True

    def close_safe(self):
        self.__var_open_safe = False

    def get_safe(self) -> bool:
        return self.__var_open_safe


class SafeOperationInClassMethod(object):
    """
    使用位置: 添加在类方法上
    作用: 在类方法调用时, 会先创建一个新的实例对象再调用这个对象的类方法
    注意: 直接在类内部实例化的变量, 无法进行深度复制
    """

    def __call__(self, fun):  # 接受函数
        def wrapper(*args, **kwargs):
            # 获取类实例对象
            sf = args[0]

            if sf.get_safe() is True:
                # 复制一个新的实例对象
                # new_instance = getattr(args[0], self.__copy_fun_name)()
                new_instance = copy.deepcopy(sf)
                # 将新的实例对象作为参数传入
                args = (new_instance, *args[1:])

            # 执行函数, 返回执行结果
            return fun(*args, **kwargs)

        return wrapper  # 返回函数


class RunTimePrint(object):
    def __call__(self, fun):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = fun(*args, **kwargs)
            end = time.time()

            runtime = end - start
            logging.info(f'running time [ {runtime} s] detail function => {fun}')
            return res

        return wrapper


# class DemoTest(SafeInfo):
#     lis = None
#
#     def __init__(self, lis=None):
#         if lis:
#             self.lis = lis
#
#     @RunTimePrint()
#     def pop(self):
#         self.lis.pop()
#         time.sleep(3)
#         return self
#
#     def base_type(self):
#         return self.lis
#
#     def __str__(self) -> str:
#         return str(self.lis)
#
#
# lis = [1, 2, 3, 4, 5]
# dt = DemoTest(lis)
# print(dt)
# print(dt.pop())
# print(dt)
