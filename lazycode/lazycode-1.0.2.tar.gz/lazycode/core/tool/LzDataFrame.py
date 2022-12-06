from lazycode.core.BaseType import BaseType

import json
import pandas as pd
from enum import Enum
import copy


class LzDataFrameFun1(object):

    def convert_list(self, data_list: list): ...

    def convert_map(self, data_map: dict): ...

    def convert_text(self, data_text: str, column_sep: str = ',',
                     first_line_is_column_name: bool = False): ...

    def convert_json(self, data_json: str): ...

    def values_to_list(self) -> list: ...

    def to_map(self) -> dict: ...

    def to_text(self, have_header: bool = True, column_sep: str = ',') -> str: ...

    def to_json(self) -> str: ...

    def index_to_column(self, new_column_name: str): ...

    def column_to_index(self, column_name: str): ...

    def head(self, n: int): ...

    def tail(self, n: int): ...

    def iloc(self, i_index: list = None, i_column: list = None,
             i_index_start: int = None, i_index_end: int = None,
             i_column_start: int = None, i_column_end: int = None
             ): ...

    def loc(self, index_name_list: list = None, column_name_list: list = None): ...

    def rows_data_list(self) -> list: ...

    def columns_data_list(self) -> list: ...

    def get_column_value(self, column_name: str) -> dict: ...

    def get_index_value(self, index_name: str) -> dict: ...

    def rename_column(self, column_name_map: dict): ...

    def rename_index(self, index_name_map: dict): ...

    def drop_index_column(self): ...

    def drop_column(self, column_name_list: list): ...

    def drop_index_row(self, index_name_list: list): ...

    def apply_row(self, fun: callable, fun_data: object = None): ...

    def apply_column(self, fun: callable, fun_data: object = None): ...

    def merge_df_into_row(self, lzdataframe_list: list): ...

    def merge_df_into_column(self, lzdataframe_list: list, ignore_index: bool = True): ...

    def join(self, lzdataframe_list: list, on_columns: list, how="inner"): ...

    def group_by(self, by_columns: list) -> list: ...

    def filter_row(self, filter_map: dict): ...

    def filter_row_apply(self, fun: callable, fun_data: object = None): ...

    def update_row_data(self, filter_map: dict, update_data_map: dict = None): ...

    def column_astype(self, column: str, fun_astype: callable): ...

    def index_name_list(self) -> list: ...

    def column_name_list(self) -> list: ...

    def T(self): ...

    def row_number(self) -> int: ...

    def shape(self) -> list: ...

    def clear(self): ...


class LzDataFrame(BaseType, LzDataFrameFun1):
    pass


class FunctionEnum(Enum):
    APPLY_FUN_FUN: str = "APPLY_FUN_FUN"
    APPLY_FUN_DATA: str = "APPLY_FUN_DATA"

    FILTER_MAP: str = 'FILTER_MAP'
    UPDATE_DATA_MAP: str = 'UPDATE_DATA_MAP'


class DataFrameFunctions(object):
    __data_dict: dict = dict()

    def set(self, key: str, value: object):
        self.__data_dict[key] = value

    def get_data_dict(self):
        return self.__data_dict

    def apply_fun(self, series):
        fun = self.__data_dict[FunctionEnum.APPLY_FUN_FUN]
        apply_fun_data = self.__data_dict.get(FunctionEnum.APPLY_FUN_DATA, None)
        index = series.axe_type
        data_dict = series.to_dict()
        data_dict = fun(index, data_dict, apply_fun_data)
        r_series = pd.Series(data_dict)
        r_series.name = index
        return r_series

    def update_row_data_fun(self, series: pd.Series):
        index = series.name
        series_dict = series.to_dict()
        full_series_dict = {"__index__": index, **series_dict}
        FILTER_MAP = self.__data_dict.get(FunctionEnum.FILTER_MAP, None)
        UPDATE_DATA_MAP = self.__data_dict.get(FunctionEnum.UPDATE_DATA_MAP, None)
        print(FILTER_MAP)
        print(full_series_dict)
        need_update = False
        if FILTER_MAP:
            for fk, fv in FILTER_MAP.items():
                if isinstance(fv, list):
                    print(full_series_dict[fk], fv)
                    print(full_series_dict[fk] in fv)
                    if full_series_dict[fk] in fv:
                        need_update = True
                        break
                else:
                    if fv == full_series_dict[fk]:
                        need_update = True
                        break
        if need_update:
            keys = UPDATE_DATA_MAP.keys()
            for k in keys:
                if k not in series_dict.keys():
                    UPDATE_DATA_MAP.pop(k)
            series_dict = {**series_dict, **UPDATE_DATA_MAP}
            series = pd.Series(series_dict)
            series.name = index
        return series


class LzDataFrameImp(LzDataFrame):
    __dataframe: pd.DataFrame = None

    def __init__(self, base_type: pd.DataFrame):
        self.init(base_type)

    def __str__(self):
        return self.to_string()

    def init(self, base_type: pd.DataFrame):
        self.__dataframe = base_type

    def to_string(self) -> str:
        return str(self.__dataframe)

    def base_type(self):
        return self.__dataframe

    def copy(self):
        return LzDataFrameImp(copy.deepcopy(self.__dataframe))

    def convert_list(self, data_list: list):
        self.__dataframe = pd.DataFrame(data_list).T
        return self

    def convert_map(self, data_map: dict):
        self.__dataframe = pd.DataFrame(data_map).T
        return self

    def convert_text(self, data_text: str, column_sep: str = ',', first_line_is_column_name: bool = False):
        data_list = [line.split(column_sep) for line in data_text.split('\n')]
        columns = None
        if first_line_is_column_name:
            columns = data_list[0]
            data_list = data_list[1:]
        self.__dataframe = pd.DataFrame(data_list, columns=columns)
        return self

    def convert_json(self, data_json: str):
        self.__dataframe = pd.DataFrame(json.loads(data_json)).T
        return self

    def values_to_list(self) -> list:
        return self.__dataframe.values.tolist()

    def to_map(self) -> dict:
        return self.__dataframe.T.to_dict()

    def to_text(self, have_header: bool = True, column_sep: str = ',') -> str:
        data_list = self.__dataframe.values.tolist()
        if have_header:
            data_list = self.__dataframe.columns.tolist() + data_list
        data_list = [column_sep.join(line) for line in data_list]
        return '\n'.join(data_list)

    def to_json(self) -> str:
        return json.dumps(self.__dataframe.T.to_dict(), ensure_ascii=False)

    def index_to_column(self, new_column_name: str):
        self.__dataframe[new_column_name] = self.__dataframe.index
        return self

    def column_to_index(self, column_name: str):
        self.__dataframe.index = self.__dataframe[column_name]
        self.__dataframe = self.__dataframe.drop([column_name], axis=1)
        return self

    def head(self, n: int):
        return LzDataFrameImp(self.__dataframe.head(n))

    def tail(self, n: int):
        return LzDataFrameImp(self.__dataframe.tail(n))

    def iloc(self, i_index: list = None, i_column: list = None, i_index_start: int = None, i_index_end: int = None,
             i_column_start: int = None, i_column_end: int = None):
        if i_index:
            if i_column:
                return LzDataFrameImp(self.__dataframe.iloc[i_index, i_column])
            else:
                return LzDataFrameImp(self.__dataframe.iloc[i_index, i_column_start:i_column_end])
        else:
            if i_column:
                return LzDataFrameImp(self.__dataframe.iloc[i_index_start:i_index_end, i_column])
            else:
                return LzDataFrameImp(self.__dataframe.iloc[i_index_start:i_index_end, i_column_start:i_column_end])

    def loc(self, index_name_list: list = None, column_name_list: list = None):
        if index_name_list:
            if column_name_list:
                return LzDataFrameImp(self.__dataframe.loc[index_name_list, column_name_list])
            else:
                return LzDataFrameImp(self.__dataframe.loc[index_name_list, :])
        else:
            if column_name_list:
                return LzDataFrameImp(self.__dataframe.loc[:, column_name_list])
            else:
                return LzDataFrameImp(self.__dataframe.loc[:, :])

    def rows_data_list(self) -> list:
        return list(self.__dataframe.T.to_dict().items())

    def columns_data_list(self) -> list:
        return list(self.__dataframe.to_dict().items())

    def get_column_value(self, column_name: str) -> dict:
        return self.__dataframe.loc[:, column_name].to_dict()

    def get_index_value(self, index_name: str) -> dict:
        return self.__dataframe.loc[index_name, :].to_dict()

    def rename_column(self, column_name_map: dict):
        self.__dataframe = self.__dataframe.rename(columns=column_name_map)
        return self

    def rename_index(self, index_name_map: dict):
        self.__dataframe = self.__dataframe.rename(index=index_name_map)
        return self

    def drop_index_column(self):
        self.__dataframe = self.__dataframe.reset_index(drop=True)
        return self

    def drop_column(self, column_name_list: list):
        self.__dataframe = self.__dataframe.drop(labels=column_name_list, axis=1)
        return self

    def drop_index_row(self, index_name_list: list):
        self.__dataframe = self.__dataframe.drop(labels=index_name_list, axis=0)
        return self

    def apply_row(self, fun: callable, fun_data: object = None):
        '''
        fun(index, data_dict, apply_fun_data) ->  data_dict: ...
        '''
        df_fun = DataFrameFunctions()
        df_fun.set(FunctionEnum.APPLY_FUN_FUN, fun)
        df_fun.set(FunctionEnum.APPLY_FUN_DATA, fun_data)
        self.__dataframe = self.__dataframe.apply(df_fun.apply_fun, axis=1)
        return self

    def apply_column(self, fun: callable, fun_data: object = None):
        df_fun = DataFrameFunctions()
        df_fun.set(FunctionEnum.APPLY_FUN_FUN, fun)
        df_fun.set(FunctionEnum.APPLY_FUN_DATA, fun_data)
        self.__dataframe = self.__dataframe.apply(df_fun.apply_fun, axis=0)
        return self

    def merge_df_into_row(self, lzdataframe_list: list):
        self.__dataframe = pd.concat([self.__dataframe] + lzdataframe_list, axis=0)
        return self

    def merge_df_into_column(self, lzdataframe_list: list, ignore_index: bool = True):
        self.__dataframe = pd.concat([self.__dataframe] + lzdataframe_list, axis=1, ignore_index=ignore_index)
        return self

    def join(self, lzdataframe_list: list, on_columns: list, how="inner"):
        join_df_list = [self.__dataframe] + lzdataframe_list
        for df in join_df_list:
            self.__dataframe = pd.merge(self.__dataframe, df, on=on_columns, how=how)
        return self

    def group_by(self, by_columns: list) -> list:
        # [ ((v1,v2,...), pd.DataFrame), ((v1,v3,...), pd.DataFrame), ... ]
        gb_list = list(self.__dataframe.groupby(by=by_columns))
        return gb_list

    def filter_row(self, filter_map: dict):
        '''
        :param filter_map: 字典内元素为需要保留的元素
            {'column1' : ['v1','v2','v3',...], 'column2': 'v' }
        :return:
        '''
        for col, data in filter_map.items():
            if isinstance(data, list):
                self.__dataframe = self.__dataframe[self.__dataframe[col].isin(data)]
            else:
                self.__dataframe = self.__dataframe[self.__dataframe[col] == data]
        return self

    def filter_row_apply(self, fun: callable, fun_data: object = None):
        '''
        fun(index, data_dict, apply_fun_data) -> bool: ...
        '''
        df_fun = DataFrameFunctions()
        df_fun.set(FunctionEnum.APPLY_FUN_FUN, fun)
        df_fun.set(FunctionEnum.APPLY_FUN_DATA, fun_data)
        need_list = self.__dataframe.apply(df_fun.apply_fun, axis=1).values.tolist()
        need_list = [ele[0] for ele in need_list]
        self.__dataframe = self.__dataframe.loc[need_list, :]
        return self

    def update_row_data(self, filter_map: dict, update_data_map: dict = None):
        '''
        :param filter_map: 筛选出需要更新的数据行, __index__表示索引列 {'__index__': [0,1,2], 'column1': ['v1', 'v2'], 'column2': 'v3' }
        :param update_data_map:
        :return:
        '''
        df_fun = DataFrameFunctions()
        df_fun.set(FunctionEnum.FILTER_MAP, filter_map)
        df_fun.set(FunctionEnum.UPDATE_DATA_MAP, update_data_map)
        self.__dataframe = self.__dataframe.apply(df_fun.update_row_data_fun, axis=1)
        return self

    def column_astype(self, column: str, fun_astype: callable):
        self.__dataframe[column] = self.__dataframe[column].apply(func=fun_astype)
        return self

    def index_name_list(self) -> list:
        return self.__dataframe.index.tolist()

    def column_name_list(self) -> list:
        return self.__dataframe.columns.tolist()

    def T(self):
        self.__dataframe = self.__dataframe.T
        return self

    def row_number(self) -> int:
        return len(self.__dataframe.index.tolist())

    def shape(self) -> list:
        index_len = len(self.__dataframe.index.tolist())
        column_len = len(self.__dataframe.columns.tolist())
        return [index_len, column_len]

    def clear(self):
        self.__dataframe = pd.DataFrame(columns=self.__dataframe.columns.tolist())
        return self
