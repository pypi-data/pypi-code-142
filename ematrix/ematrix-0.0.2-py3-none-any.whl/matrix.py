# -*- coding:utf-8 -*-
# Auther: Zed
"""
It's beautiful right? ^_^

dm = Matrix()
print('data_matrix:', dm)
res = dm[dm['code'] == '000001']
print('data_matrix_slice:\n', res)
------------------------------
data_matrix:
             ['close', 'high', 'low', 'open', 'ret']
100
000001  [0.80676805 0.30489957...0.83385824 0.56749199]
000002  [0.0158474  0.65408549...0.14293321 0.76696439]
                  ......

200
000001  [0.62020139 0.96969446...0.76984185 0.14326731]
000002  [0.82182821 0.10924971...0.9967727  0.51963606]
                  ......
                  ......
400
...
000003  [0.15914842 0.99641071...0.15914842 0.99641071]
Dimension: ['timestamp', 'code', 'features'], Shape: (4, 3, 5), dtype: matrix

data_matrix_slice:
         close      high       low      open       ret
100  0.806768  0.304900  0.210918  0.833858  0.567492
200  0.620201  0.969694  0.754948  0.769842  0.143267
300  0.008385  0.087556  0.994873  0.706558  0.752703
400  0.388965  0.946414  0.967339  0.567995  0.071485

update:
    2022-12-02 23:52  :
        Increased function matrix.T(axis_one,axis_two), then you can transform two axis,just like pd.DataFrame().T
        dm.T(0, 2)
        print('-' * 30)
        print('transform!')
        print(dm)

        dm.T('code', 'timestamp')
        print('-' * 30)
        print('transform!')
        print(dm)
    2022-12-03 0:31  :
        Increased params type in function matrix.T, then you can use 'list' as params
        dm.T(['code','timestamp','features'])
        print('-' * 30)
        print('transform!')
        print(dm)
    2022-12-04 22:49  :
        Increased handle df_dict to np.ndarray and axis_name, then user can import df list easily to matrix
        e.g:
            data_list = os.listdir()
            data_list = [data.split('.')[0] for data in data_list if data.endswith('.csv')]

            df_dict = {}
            for data in data_list:
                df = pd.read_csv(data + '.csv')
                df.index = df["trade_date"]  # 请确保dataframe.index是数据的时间,或者是有意义且不重复的值
                df_dict[data] = df
            dm = Matrix(df_dict, axis_name=['code', 'datetime', 'features'])
    next plan:
            1. Update dm element: dm.append(matrix0/DataFrame) or matrix2=em.concat([matrix0,matrix1])
            2. IO stream: dm.read/to pandas_df,pkl,csv
            3. Increase logic operation such as '>= <= > < !=/~ and & or / in' : dm[20220105<=datetime and code in ['000001','000002']]
            4. Increase more __magic_function__ such as __del__: del dm["feature=='close'"] / dm.delete('datetime<=20220105')
            5. Query function: dm.query("20220105<=datetime<=20220506 and code in ['000001','000002'] and feature.capital>float(1e9)")
            6. Increase function fill_na: dm.fill_na('forward_value/backward_value/zero_value/avg_value')
            7. Del dm[dm[::3]:ClassMatrix]
            -1. More simular pd.DataFrame operation function in Matrix
"""

import numpy as np
from typing import Union, NewType
from copy import deepcopy
import pandas as pd

set_print_limit = False  # 显示有限的输出设置
_SeriesType = Union[dict, tuple, list]

_SeriesTypeBase = [tuple, list]


def row_fill_na(data: pd.DataFrame, fill_list) -> pd.DataFrame:
    _na_data = np.full([len(fill_list), data.shape[1]], np.nan)

    new_data = np.vstack((data, _na_data))

    _index = list(data.index)
    _index.extend(fill_list)
    new_df = pd.DataFrame(new_data, index=_index, columns=data.columns)
    new_df.sort_index(inplace=True)
    # new_df = pd.concat([data, new_df])
    return new_df


def columns_fill_na(data: pd.DataFrame, fill_list) -> pd.DataFrame:
    _na_data = np.full([data.shape[0], len(fill_list)], np.nan)
    new_data = np.hstack((data, _na_data))
    _columns = list(data.columns)
    _columns.extend(fill_list)
    new_df = pd.DataFrame(new_data, index=data.index, columns=_columns)

    return new_df


def diff_calcu(total_list, _array_list):
    _diff_list = list(set(total_list) - set(_array_list))
    return sorted(_diff_list)


def df_dict2matrix(df_dict, axis_name=None):
    if axis_name is None:
        axis_name = ['code', 'datetime', 'features']
    index = []
    row = []
    columns = []

    df_info_dict = {}
    for key, value in df_dict.items():
        index.append(key)

        row.extend(list(value.index.values))
        columns.extend(list(value.columns.values))
        df_info_dict[key] = {
            'row': list(value.index.values),
            'columns': list(value.columns.values),
        }
    # def value_fill_na_check():
    values_dict = {}
    for key, value in deepcopy(df_info_dict).items():
        diff_row = diff_calcu(row, value['row'])
        diff_columns = diff_calcu(columns, value['columns'])

        if diff_row:

            new_df = row_fill_na(df_dict[key], diff_row)

            if diff_columns:
                new_df = columns_fill_na(new_df, diff_columns)
            new_df.sort_index(inplace=True)
            values_dict[key] = new_df
            continue
        if diff_columns:
            new_df = columns_fill_na(df_dict[key], diff_columns)
            new_df.sort_index(inplace=True)
            values_dict[key] = new_df
        else:
            df_dict[key].sort_index(inplace=True)
            values_dict[key] = df_dict[key]

    first_data_key = list(values_dict.keys())[0]
    first_data = values_dict[first_data_key]

    index = list(values_dict.keys())
    row = list(first_data.index)  # 时间记得排序
    columns = list(first_data.columns)

    axis_name = {axis_name[0]: index, axis_name[1]: row, axis_name[2]: columns}
    _array = np.empty([1, len(row), len(columns)])
    # print(_array)

    for key, value in values_dict.items():
        # print(value)
        _array = np.vstack((_array, [value.values]))
    _array = _array[1:]
    return _array, axis_name


def check_Series_unit(series):
    _len = 0
    _type = None
    _type0 = None
    _type1 = None
    if type(series) == list:
        for i, value in enumerate(series):

            if (type(value) == tuple or type(value) == list) and len(value) == 2:
                if not _len:
                    _len = len(value)
                elif _len != len(value):
                    raise ValueError(f'error length {series}')
                if not _type0:
                    # index类型
                    _type0 = type(value[0])
                    # value类型
                    _type1 = type(value[1])

                else:
                    if _type0 != type(value[0]) or _type1 != type(value[1]):
                        raise ValueError(f'error type {series} of {value}')
            else:
                if not _type:
                    _type = type(value)
                else:
                    if _type != type(value):
                        raise ValueError(f'error type {series}')

    if _type0:
        return 2, _type1
    else:
        return 1, _type


def check_Series_dtype(dtype):
    if dtype == str:
        dtype = 'str'
    elif dtype == float:
        dtype = 'float'
    elif dtype == int:
        dtype = 'int'
    elif dtype == bool:
        dtype = 'bool'
    elif dtype == dict:
        dtype = 'dict'
    return dtype


# axis_name = ['timestamp', 'code', 'features']
def _print(data: _SeriesType, head=0, tail=0):
    _print_len = 10
    if not head:
        __head = 5
    else:
        __head = head
    if not tail:
        __tail = 5
    else:
        __tail = tail
    _print_data = ''
    if type(data) == dict:
        _length = len(data.keys())
        if set_print_limit and _length > _print_len:
            keys = list(data.keys())
            up5 = keys[:__head]
            down5 = keys[-__tail:]
            for i, value in enumerate(up5):
                _print_data += f'{value} {data[value]}\n'
            if head:
                return _print_data
            _print_data += '...\n'
            _print_data_tail = ''
            for i, value in enumerate(down5):
                _print_data_tail += f'{value} {data[value]}\n'
            if tail:
                return _print_data_tail
            else:
                _print_data += _print_data_tail

        else:
            for key, value in data.items():
                _print_data += f'{key} {value}\n'

    elif type(data) == tuple or type(data) == list:
        _length = len(data)
        if set_print_limit and _length > _print_len:
            for i in range(__head):
                _print_data += f'{data[i][0]} {data[i][1]}\n'
            _print_data += '...\n'
            _print_data_tail = ''
            for i in range(__tail - 1, -1, -1):
                _print_data_tail += f'{data[i][0]} {data[i][1]}\n'
            if tail:
                return _print_data_tail
            else:
                _print_data += _print_data_tail
        else:

            for i in range(len(data)):
                _print_data += f'{data[i][0]} {data[i][1]}\n'

    else:
        raise ValueError(f'error type {data}')

    return _print_data


_loc = NewType('_loc', dict)
_SeriesDtype = Union[dict, tuple, str, int, float, list, _loc]


class Series:
    def __init__(self, series: list, name: str = 'Undefined', unique=False, astype: str = None):

        self.dtype = object
        self.astype = astype

        self.name = name
        self._series = series
        self._series_value = []
        self.length = len(self._series)
        self.index = list(range(self.length))
        self.unique = unique
        self._set_series()

    def _set_series(self):
        _res, _type = check_Series_unit(self._series)
        if _res == 1:
            self._series_value = np.array(self._series)
            self._series = list(zip(self.index, self._series_value))

        else:
            _series_values = []
            _series_values_index = []
            for i, value in enumerate(self._series):
                _series_values_index.append(value[0])
                _series_values.append(value[1])
            self.index = _series_values_index
            _series_values = np.array(_series_values)
            self._series = list(zip(self.index, _series_values))
            self._series_value = _series_values

        if self.astype:
            self.dtype = self.astype
        else:
            self.dtype = check_Series_dtype(_type)

    @property
    def values(self):
        return self._series_value

    def __eq__(self, other):

        _res = []
        if self.unique:
            for i, value in enumerate(self._series):

                if value[1] == other:
                    _res = [(self.name, i)]
                    return Series(_res, 'loc.unique', True, 'loc')
            if not _res:
                _res = [(self.name, None)]
                return Series(_res, 'loc.unique', True, 'loc')
        else:

            for value in self._series:
                if value[1] == other:
                    _res.append(True)
                else:
                    _res.append(False)

            return Series(_res, self.name)

    def __str__(self):
        _data = _print(self._series)
        info = f'Name: {self.name}, Length:{self.length}, dtype:{self.dtype}'
        return _data + info

    def __repr__(self):
        return str(self)




_MatrixGetSingleItemType = Union[str, int, Series]
_MatrixGetMultiItemType = Union[str, int, Series]
_MatrixAxisNameType = Union[dict, list]
MatrixGetDataType = Union[np.ndarray, list, tuple, dict, None]


class DataFrame:
    def __init__(self, matrix_np: np.ndarray = None, axis_name: dict = None):
        # matrix_np:二维np矩阵， axis_name：行列名

        if not axis_name or matrix_np is None:
            # test data:
            axis_name = {'index': ['000001', '000002', '000003'],
                         'columns': ['close', 'high', 'low', 'open', 'ret']}
            matrix_np = np.random.random([3, 5])
        self.data = matrix_np
        self.axis_name = axis_name
        self.index = self.axis_name['index']
        self.columns = self.axis_name['columns']

    def to_pandas_df(self) -> pd.DataFrame:
        _df = pd.DataFrame(self.data)
        _df.index = self.index
        _df.columns = self.columns
        return _df

    def _print(self):
        pass

    def __str__(self):
        _df = self.to_pandas_df()
        return str(_df)

    def __repr__(self):
        _df = self.to_pandas_df()
        return _df


class Matrix:
    # 可接收多个pd.DataFrame聚合为Matrix数据类型
    # 标准样例：第一维度为时间，第二维度为合约标的代码，第三维度为特征因子features
    # 均需要外部提供，标准协议为：
    # axis_name={'timestamp':[xx,xx,xx],
    #            'code':[xx,xx,xx],
    #            'features':[xx,xx,xx],
    #           }
    # 需要解决一个问题：如果两个dataframe的长度不一致时如何解决
    def __init__(self, data: MatrixGetDataType = None, axis_name: _MatrixAxisNameType = None, unique=True):
        # unique如果能确保值是唯一的，那么可提高性能

        self._dimension_dict = {}  # 轴名为key，维度为value
        self._dimension_num_dict = {}  # 维度为key，轴名为value
        self.unique = unique

        if type(data) == np.ndarray:
            data: np.ndarray
            if len(data.shape) < 3:
                raise ValueError(f'error data dimension:{len(data.shape)}')
        elif type(data) == dict:
            data, axis_name = df_dict2matrix(data, axis_name=axis_name)

        # list, tuple, dict 内部装着pd.dataframe

        elif type(data) != np.ndarray or not axis_name:
            # test data:
            axis_name = {'timestamp': [100, 200, 300, 400], 'code': ['000001', '000002', '000003'],
                         'features': ['close', 'high', 'low', 'open', 'ret']}
            data = np.random.random([4, 3, 5])
            # big data
            # axis_name = {'timestamp': list(range(1000)), 'code': list(range(5000)),
            #              'features': list(range(100))}
            # data = np.random.random([1000, 5000, 100])

        self.data = data
        self.axis_name = axis_name

        self.index = None
        self.index_name = None
        self.row = None
        self.row_name = None
        self.columns = None
        self.columns_name = None

        self._axis_name_dict = {}
        self._axis_name_key = []
        self.init()

    # 转置的概念：要借助numpy进行0，1，2轴任意转置
    def pandas_df_to_matrix(self, df_dict: dict):
        # 把多个pandas.dataframe数据放入df_dict中，然后循环处理为numpy.ndarray矩阵，最终变为matrix类

        pass

    def T(self, axis_one, axis_two=None):
        if type(axis_one) == int and type(axis_two) == int:
            axis_one_num, axis_two_num = axis_one, axis_two

        elif type(axis_one) == str and type(axis_two) == str:
            axis_one_num, axis_two_num = self._dimension_dict[axis_one], self._dimension_dict[axis_two]

        elif type(axis_one) == list and not axis_two:
            if len(axis_one) == 3:
                if axis_one[0] == axis_one[1] or axis_one[1] == axis_one[2] or axis_one[0] == axis_one[2]:
                    raise ValueError(f'Error value, element should not be same value {axis_one}')
                if type(axis_one[0]) == str and type(axis_one[1]) == str and type(axis_one[2]) == str:
                    _one, _two, _three = self._dimension_dict[axis_one[0]], self._dimension_dict[axis_one[1]], \
                                         self._dimension_dict[axis_one[2]]
                    axis_one = [_one, _two, _three]
                elif type(axis_one[0]) == int and type(axis_one[1]) == int and type(axis_one[2]) == int:
                    _d = [0, 1, 2]
                    if axis_one[0] not in _d or axis_one[1] not in _d or axis_one[2] not in _d:
                        raise ValueError(f'Error value element in {axis_one}, it should be between in 0-2')

                else:
                    raise ValueError(f'Error type element in {axis_one}, it should be str or in')
                new_queue = axis_one
                self.data = self.data.transpose(new_queue)
                self._T(new_queue)
                return self
            else:
                raise ValueError(f"Error param length: {axis_one}, it's length should be 3")
        else:
            raise ValueError(
                f'Error type param: {axis_one, axis_two}, it should double int or str or axis_one is list and axis_two is None ')

        self.data = self.data.swapaxes(axis_one_num, axis_two_num)

        if axis_one_num == 0 and axis_two_num == 1 or axis_one_num == 1 and axis_two_num == 0:
            new_queue = [1, 0, 2]

        elif axis_one_num == 0 and axis_two_num == 2 or axis_one_num == 2 and axis_two_num == 0:
            new_queue = [2, 1, 0]
        elif axis_one_num == 1 and axis_two_num == 2 or axis_one_num == 2 and axis_two_num == 1:
            new_queue = [0, 2, 1]
        else:
            raise ValueError(f'error axis_num or axis_name: {axis_one, axis_two}')
        self._T(new_queue)
        return self

    def _T(self, new_queue):
        _dimension_dict = {}
        _axis_name_dict = {}
        for num in new_queue:
            _axis_name = self._dimension_num_dict[num]
            _axis_name_dict[_axis_name] = self.axis_name[_axis_name]
        self.axis_name = _axis_name_dict
        self.init()


    def append(self,auto_fix=False):
        # auto_fix=True:如果用户能确保加入的维度和Matrix.value维度一样，那么就不需要作维度相等判断，因此性能会更高
        pass

    def concat(self):
        # 拼接两个matrix数据
        pass

    def init(self):

        if len(self.data.shape) != 3:
            raise ValueError(f'error data shape {self.data}')
        if len(self.axis_name.keys()) != 3:
            raise ValueError(f'error axis_name len {self.data}')
        i = 0
        for key, value in self.axis_name.items():
            self._dimension_dict[key] = i
            self._dimension_num_dict[i] = key
            if i == 0:
                self.index = value
                self.index_name = key
            elif i == 1:
                self.row = value
                self.row_name = key
            else:
                self.columns = value
                self.columns_name = key
            i += 1
        self._axis_name_to_range()

    def _axis_name_to_range(self):
        _data_dict = {}
        for key, value in self.axis_name.items():
            # 用于实现类似loc精确定位矩阵元素
            _data_dict[key] = dict(zip(value, list(range(len(value)))))

        self._axis_name_dict = _data_dict
        self._axis_name_key = list(self._axis_name_dict.keys())

    # ToDo 像df.loc一样定位数据
    @property
    def loc(self):
        return

    # ToDo 像df.query一样条件查询数据
    def query(self):
        # res=matrix.query('100<=timestamp<=200 and close>21.5 or high>=100 and code=="000001.SZ"')
        #
        pass

    def __getitem__(self, *item):

        if len(item) == 1:
            item = item[0]

            item: _MatrixGetSingleItemType
            if type(item) == str:
                # dm['data_xx']:返回某维度所有index
                if item not in self._axis_name_key:
                    raise ValueError(f'{item} not exist in Matrix')

                return Series(list(self._axis_name_dict[item].keys()), item, self.unique)
            elif type(item) == Series:

                # Series类用于提供定位信息，根据dtype又分为bool和loc
                if item.dtype == 'bool':

                    if item.name not in self._dimension_dict:
                        raise ValueError(f'error {item.name} not in {self._dimension_dict}')
                    _dimension = self._dimension_dict[item.name]

                    if _dimension == 0:
                        _res = []

                        for i in range(len(item.values)):
                            if item.values[i]:
                                _res.append(self.data[i, :, :])
                        _res = np.array(_res)
                        _row_name = self._axis_name_key[1]
                        _columns_name = self._axis_name_key[2]
                        df_axis_name = dict(
                            index=self.axis_name[_row_name],
                            columns=self.axis_name[_columns_name]
                        )

                        return DataFrame(_res[0], df_axis_name)

                    elif _dimension == 1:
                        _res = []

                        for i in range(len(item.values)):
                            if item.values[i]:
                                _res.append(self.data[:, i, :])
                        _res = np.array(_res)
                        _row_name = self._axis_name_key[0]
                        _columns_name = self._axis_name_key[2]
                        df_axis_name = dict(
                            index=self.axis_name[_row_name],
                            columns=self.axis_name[_columns_name]
                        )

                        return DataFrame(_res[0], df_axis_name)
                    else:
                        _res = []

                        for i in range(len(item.values)):
                            if item.values[i]:
                                _res.append(self.data[:, :, i])
                        _res = np.array(_res)

                        _row_name = self._axis_name_key[0]
                        _columns_name = self._axis_name_key[1]
                        df_axis_name = dict(
                            index=self.axis_name[_row_name],
                            columns=self.axis_name[_columns_name]
                        )

                        return DataFrame(_res[0], df_axis_name)
                elif item.dtype == 'loc':

                    if not len(item.values):
                        return
                    if len(item.values) == 1:

                        _dimension = self._dimension_dict[item.index[0]]
                        if _dimension == 0:
                            _res = [self.data[item.values[0], :, :]]

                            _res = np.array(_res)
                            _row_name = self._axis_name_key[1]
                            _columns_name = self._axis_name_key[2]
                            df_axis_name = dict(
                                index=self.axis_name[_row_name],
                                columns=self.axis_name[_columns_name]
                            )

                            return DataFrame(_res[0], df_axis_name)

                        elif _dimension == 1:
                            _res = [self.data[:, item.values[0], :]]

                            _res = np.array(_res)
                            _row_name = self._axis_name_key[0]
                            _columns_name = self._axis_name_key[2]
                            df_axis_name = dict(
                                index=self.axis_name[_row_name],
                                columns=self.axis_name[_columns_name]
                            )

                            return DataFrame(_res[0], df_axis_name)

                        else:

                            _res = [self.data[:, :, item.values[0]]]

                            _res = np.array(_res)
                            _row_name = self._axis_name_key[0]
                            _columns_name = self._axis_name_key[1]
                            df_axis_name = dict(
                                index=self.axis_name[_row_name],
                                columns=self.axis_name[_columns_name]
                            )

                            return DataFrame(_res[0], df_axis_name)

            elif type(item) == list:

                if self.unique:
                    return

        else:

            print('_MatrixGetMultiItemType')
            pass

    @property
    def values(self):
        return self.data

    def _print(self):

        _axis_name_list = []
        _reverse_dimension = {v: k for k, v in self._dimension_dict.items()}
        columns_str = list(self._axis_name_dict[_reverse_dimension[2]].keys())
        if len(columns_str) > 10:
            columns_str = str(columns_str[:2])[:-1] + '...' + str(columns_str[:2])[1:]
        _print_data = "\n             " + str(columns_str)

        for i, value in enumerate(self.data):
            if i >= 2:
                last_count = list(self._axis_name_dict[_reverse_dimension[0]].keys())[-1]
                last_row = list(self._axis_name_dict[_reverse_dimension[1]].keys())[-1]
                last_data = self.data[-1][-1]
                if len(last_data) >= 5:
                    last_data = str(last_data[:2])[:-1] + '...' + str(last_data[:2])[1:]

                _print_data += '                  ......\n' + str(last_count) + '\n' + '...\n' + str(
                    last_row) + '  ' + str(last_data)
                break

            _p = list(self._axis_name_dict[_reverse_dimension[0]].keys())[i]
            _print_data += '\n' + str(_p) + '\n'
            for j in range(len(value)):
                if j >= 2:
                    _print_data += '                  ......\n'
                    break

                _print_data += str(list(self._axis_name_dict[_reverse_dimension[1]].keys())[j])
                _value = value[j]
                # 控制列
                if len(_value) >= 5:
                    _value = str(_value[:2])[:-1] + '...' + str(_value[-2:])[1:]
                _print_data += '  ' + str(_value) + '\n'

        _matrix_info = f'\nIndex: {self._axis_name_key[0]}, Row: {self._axis_name_key[1]}, Columns: {self._axis_name_key[2]}, Shape: {self.data.shape}, dtype: matrix'
        _print_data += _matrix_info + '\n'
        return _print_data

    def __str__(self):
        return self._print()



