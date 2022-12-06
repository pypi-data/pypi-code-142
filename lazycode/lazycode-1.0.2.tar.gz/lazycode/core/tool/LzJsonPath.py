from enum import Enum
import re
from typing import List, Callable
from lazycode.core.LzNumber import LzNumberImp


class REGS(Enum):
    # 值为 list 的元素
    LIST_ELEMENT_REG = re.compile(r'^(.+?)\[(.+?)\]$')
    # [1:5:2], [1:5]
    LIST_REG1 = re.compile(r'^(.*?):(.*?)(:.+)?$')
    # [1] , [-1]
    LIST_REG2 = re.compile(r'^(-?\d+)$')
    # [1,2,3]
    LIST_REG3 = re.compile(r'^\d(,\d+)*$')

    # ?( fun.function_name ) ?( self.price > 12  )
    FILTER_LAMBDA_REG = re.compile(r'^\?\((.+?)\)$')
    FILTER_LAMBDA_REG1 = re.compile(r' *fun\.(.+?)(\(.*?\))? *$')
    FILTER_LAMBDA_REG2 = re.compile(r' *self\.(.+?) +(.+?) +(.+?) *$')


class LzJsonPath(object):
    pass


class LzJsonPathImp(LzJsonPath):
    __json_dict: dict = None
    __sep: str = None

    __deep_flag: str = None

    __burst_path_list: list = []
    __lambda_dict: dict = dict()
    __system_lambda_dict: dict = dict()

    def __init__(self, json_dict: dict, sep: str = '/') -> None:
        self.__json_dict = json_dict
        self.__sep = sep

        self.__deep_flag = f'{sep}{sep}'

    def register_function(self,
                          fun: Callable,
                          fun_name: str = None,
                          carry_data=None):
        '''

        :param fun: lambda LzJsonPathImpFun : ... -> List[Union[int, str]]
        :param fun_name: 注册的函数名称(默认和函数名相同)
        :param carry_data: 需要携带进函数的额外数据
        :return:
        '''
        if fun_name is None:
            fun_name = fun.__name__
        self.__lambda_dict[fun_name] = dict(
            function=fun,
            carry_data=carry_data
        )
        return self

    def __convert_string_args(self, str_args: str):
        str_args = str_args.strip()
        args = None
        if str_args != '':
            # todo 传入的文本参数解析
            args = str_args.split(',')
        return args

    def __get_value_path_list(self, pre_data, sub_path: str):
        list_reg = REGS.LIST_ELEMENT_REG.value.search(sub_path)

        if list_reg is not None:
            key_name = list_reg.group(1)
            list_txt = list_reg.group(2)
            list_value = pre_data[key_name]
            reg1 = REGS.LIST_REG1.value.search(list_txt)
            reg2 = REGS.LIST_REG2.value.search(list_txt)
            reg3 = REGS.LIST_REG3.value.search(list_txt)
            reg4 = REGS.FILTER_LAMBDA_REG.value.search(list_txt)
            if reg1 is not None:
                list_len = len(list_value)
                start = reg1.group(1)
                start = 0 if start is None else 0 if start == '' else int(start)
                end = reg1.group(2)
                end = list_len if end is None else list_len if end == '' else int(end)
                step = reg1.group(3)
                step = step.strip(':') if step is not None else step
                step = 1 if step is None else 1 if step == '' else int(step)
                return [f'{key_name}[{i}]' for i in range(start, end, step)]
            elif reg2 is not None:
                index = int(reg2.group(1))
                index = (len(list_value) + index) if index < 0 else index
                return [f'{key_name}[{index}]']
            elif reg3 is not None:
                index_list = list(map(int, reg3.group(0).split(',')))
                return [f'{key_name}[{index}]' for index in index_list]
            elif reg4 is not None:
                filter_lambda_text = reg4.group(1)
                filter_lambda_reg1 = REGS.FILTER_LAMBDA_REG1.value.search(filter_lambda_text)
                filter_lambda_reg2 = REGS.FILTER_LAMBDA_REG2.value.search(filter_lambda_text)
                # 用户自定义 fun.xxx
                if filter_lambda_reg1 is not None:
                    fun_name = filter_lambda_reg1.group(1)
                    fun_args = filter_lambda_reg1.group(2)[1:-1].strip()
                    fun = self.__lambda_dict[fun_name]['function']
                    carry_data = self.__lambda_dict[fun_name]['carry_data']
                    pre_element = pre_data
                    curr_element_key_name = key_name
                    curr_element_list = list_value
                    args = self.__convert_string_args(fun_args)

                    lz_arg = LzJsonPathImpFunArgs()
                    lz_arg.pre_element = pre_element
                    lz_arg.curr_element_key_name = curr_element_key_name
                    lz_arg.curr_element_value = curr_element_list
                    lz_arg.carry_data = carry_data
                    lz_arg.args = args

                    res_list = fun(lz_arg)
                    res_list = list(map(lambda i: f'{key_name}[{i}]', res_list))
                    return res_list
                elif filter_lambda_reg2 is not None:
                    ele_key_name = filter_lambda_reg2.group(1)
                    symbol = filter_lambda_reg2.group(2)
                    value = filter_lambda_reg2.group(3)
                    res_list = []
                    for i, ele in enumerate(list_value):
                        if ele_key_name in ele.keys():
                            ele_value = ele[ele_key_name]
                            if not LzNumberImp.is_number(str(ele_value)):
                                ele_value = f"'{ele_value}'"

                            is_save = eval(f'{ele_value} {symbol} {value}')
                            if is_save is True:
                                res_list.append(f'{key_name}[{i}]')
                    return res_list

            else:
                raise Exception(f'{list_txt} 无法解析')
        elif sub_path == '*':
            if isinstance(pre_data, dict):
                res = []
                for key, value in pre_data.items():
                    if isinstance(value, list):
                        res.extend([f'{key}[{i}]' for i in range(len(value))])
                    else:
                        res.append(key)
                return res
            else:
                raise Exception('* 只能表示字典中任意 key')
        else:
            return [sub_path]

    def __get_value_by_base_path(self, path: str):
        path_list = path.strip(self.__sep).split(self.__sep)
        data = self.__json_dict
        for sub_path in path_list:
            list_reg = REGS.LIST_ELEMENT_REG.value.search(sub_path)
            if list_reg is not None:
                key_name = list_reg.group(1)
                list_txt = list_reg.group(2)
                index = str(list_txt)
                data = data[key_name][int(list_txt)]
            else:
                data = data[sub_path]
        return data

    def get_path_burst(self, path: str) -> list:
        self.__burst_path_list.clear()
        self.__path_burst(self.__json_dict, '', path)
        return self.__burst_path_list

    # //k1/k2//k3
    def __path_burst(self, curr_data, pre_path: str, path: str) -> list:
        if path == '':
            self.__burst_path_list.append(pre_path)
            return self.__burst_path_list

        strip_path = path.strip(self.__sep)
        first_sep_index = strip_path.find(self.__sep)
        curr_ele_path = None
        tail_path = None
        if first_sep_index != -1:
            curr_ele_path = strip_path[:first_sep_index]
            tail_path = strip_path[first_sep_index:]
        else:
            curr_ele_path = strip_path
            tail_path = ''

        # //...
        if path.startswith(self.__deep_flag):
            if isinstance(curr_data, dict):
                keys = list(curr_data.keys())
                path_list = []
                for k in keys:
                    data = self.__get_value_by_base_path(f'{pre_path}{self.__sep}{k}')
                    if isinstance(data, list):
                        path_list.append((self.__get_value_path_list(curr_data, f'{k}[:]'), 'list'))
                    elif isinstance(data, dict):
                        path_list.append(([k], 'dict'))
                    else:
                        path_list.append(([k], 'ele'))

                sub_path_list = None
                try:
                    if curr_ele_path in curr_data.keys():
                        val = curr_data[curr_ele_path]
                        if isinstance(val, list):
                            curr_ele_path = f'{curr_ele_path}[:]'
                    sub_path_list = self.__get_value_path_list(curr_data, curr_ele_path)
                except Exception as e:
                    sub_path_list = [curr_ele_path]
                for pp_list, dtype in path_list:
                    if len(set(sub_path_list) - set(pp_list)) == 0:
                        for sub_path in sub_path_list:
                            curr_path = f'{pre_path}{self.__sep}{sub_path}'
                            self.__path_burst(self.__get_value_by_base_path(curr_path), curr_path, tail_path)
                    else:
                        if dtype in ['list', 'dict']:
                            for sub_path in pp_list:
                                curr_path = f'{pre_path}{self.__sep}{sub_path}'
                                self.__path_burst(self.__get_value_by_base_path(curr_path), curr_path, path)
                        else:
                            pass

            else:
                raise Exception(f"{self.__deep_flag} 后子元素只能为 字典类型")

        else:
            sub_path_list = self.__get_value_path_list(curr_data, curr_ele_path)
            for sub_path in sub_path_list:
                curr_path = f'{pre_path}{self.__sep}{sub_path}'
                self.__path_burst(self.__get_value_by_base_path(curr_path), curr_path, tail_path)

    def j_path(self, path: str):
        path_list = self.get_path_burst(path)
        return [self.__get_value_by_base_path(p) for p in path_list]


class LzJsonPathImpFunArgs(object):
    # 父级元素对象
    pre_element = None

    # 当前元素 key 名称
    curr_element_key_name = None

    # 当前元素 value
    curr_element_value = None

    # 元素下标需要保存的元素下标 list
    carry_data = None

    # 路径上传入的参数
    args = None


class LzJsonPathImpFun(object):

    @staticmethod
    def contain_field(lz_arg: LzJsonPathImpFunArgs) -> List[int]:
        """
            注册函数 模板. 获取包含指定字段的元素
        """
        # todo 使用解析完成的参数
        res_index = []
        for i, ele_dic in enumerate(lz_arg.curr_element_value):
            keys = list(ele_dic.keys())
            if len(set(keys) & set(lz_arg.args)) > 0:
                res_index.append(i)

        return res_index

# books = {
#     "store": {
#         "book": [
#             {"category": "reference",
#              "author": "Nigel Rees",
#              "title": "Sayings of the Century",
#              "price": 8.95
#              },
#             {"category": "fiction",
#              "author": "J. R. R. Tolkien",
#              "title": "The Lord of the Rings",
#              "isbn": "0-395-19395-8",
#              "price": 22.99
#              },
#             {"category": "fiction",
#              "author": "J. R. R. Tolkien",
#              "title": "The Lord of the Rings",
#              "isbn": "0-395-19395-8",
#              "price": 22.99
#              },
#             {"category": "reference",
#              "author": "Nigel Rees",
#              "title": "Sayings of the Century",
#              "price": 8.95
#              },
#         ],
#         "bicycle": {
#             "color": "red",
#             "price": 19.95,
#             "book": [
#                 {"category": "reference",
#                  "author": "Nigel Rees",
#                  "title": "Sayings of the Century",
#                  "price": 8.95
#                  },
#                 {"category": "fiction",
#                  "author": "J. R. R. Tolkien",
#                  "title": "The Lord of the Rings",
#                  "isbn": "0-395-19395-8",
#                  "price": 22.99
#                  }
#             ]
#         },
#         'kk': {
#             'kkk': {
#                 'kkkk': {
#                     'abc': 'value'
#                 },
#                 'kkkk2': {
#                     'abc': 'value2'
#                 }
#             }
#         }
#     }
# }
#
# lz = LzJsonPathImp(books)
#
# lz.j_path('/store/bicycle/color')
# lz.get_path_burst('/store//color')
# lz.get_path_burst('/store/book[1]')
# lz.get_path_burst('/store/book[:2]')
# lz.get_path_burst('/store/book[:]')
# lz.get_path_burst('/store/book[::2]')
# lz.get_path_burst('/store/book[-1]')
# lz.get_path_burst('//title')
# lz.get_path_burst('//book')
# lz.get_path_burst('/store/book[?(self.price > 10)]')
# lz.get_path_burst('/store/book[?(self.category in ["reference"])]')
#
# lz.register_function(LzJsonPathImpFun.contain_field)
# lz.get_path_burst('/store/book[?(fun.contain_field(isbn, price))]')
