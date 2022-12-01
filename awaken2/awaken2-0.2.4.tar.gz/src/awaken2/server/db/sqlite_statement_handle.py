# Copyright 2022 quinn.7@foxmail.com All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
[ SQLite语句处理器 ]

"""
from ...baseic.keyword import G_KEYWORD
from ...baseic.decorator.baseic import deco_singleton
from ...baseic.error.database import AwakenDatabaseTableNotFoundError
from ...baseic.error.database import AwakenDatabaseTableNotFoundFieldError
from ...baseic.error.database import AwakenDatabaseTableDeductionInserteError


class SqliteSelecter: ...
class SqliteInserter: ...
class SqliteUpdater : ...
class SqliteDeleter : ...


# --------------------------------------------------------------------------
@deco_singleton
class SqliteStatementHandle:
    """
    [ SQLite语句处理器 ]
    
    """
    _table_structure = {}
    """ 表结构映射 """


    # ----------------------------------------------------------------------
    def create_table(self, table_name: str, table_field: dict, if_not_exists: bool = True) -> str:
        """
        [ 建表 ]

        ---
        参数
        - table_name    : { str }  - 表名。
        - table_field   : { dict } - 表字段。
        - if_not_exists : { bool } - 建表时如果不存在则创建。

        ---
        返回
        - { str } : 建表语句。

        """
        # 表结构字典将保留一份表结构数据作为某些方法的数据格式处理依赖
        self._table_structure.update({table_name : {}})

        # 处理表字段语句
        table_field_sentence = ''
        for tfmn, tfmv in table_field.items():
            if len(table_field_sentence) > 0:
                table_field_sentence += ', \n'
            table_field_sentence += f'\t{tfmn} {tfmv}'
            self._table_structure[table_name].update({tfmn : tfmv}) # 更新表结构字典

        # 拼接返回
        not_exists_keyword = G_KEYWORD.Sqlite.CreateTable.IfNotExists if if_not_exists else ''
        return f'CREATE TABLE {not_exists_keyword} {table_name} \n(\n {table_field_sentence} \n);'


    # ----------------------------------------------------------------------
    def select(self, table_name: str) -> SqliteSelecter:
        """
        [ 表查询 ]

        ---
        参数
        - table_name : { str } - 表名。

        ---
        返回
        - { SqliteSelecter } : 指向表的SQLite选择器对象。

        """
        # 如果表不存在表结构中则抛出异常
        if table_name not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundError(table_name)

        return SqliteSelecter(table_name, self._table_structure[table_name])


    # ----------------------------------------------------------------------
    def insert(self, table_name: str) -> SqliteInserter:
        """
        [ 表插入 ]

        ---
        参数
        - table_name : { str } - 表名。

        ---
        返回
        - { SqliteInserter } : 指向表的SQLite插入操作器对象。

        """
        # 如果表不存在表结构中则抛出异常
        if table_name not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundError(table_name)

        return SqliteInserter(table_name, self._table_structure[table_name])


    # ----------------------------------------------------------------------
    def update(self, table_name: str) -> SqliteInserter:
        """
        [ 表更新 ]

        ---
        参数
        - table_name : { str } - 表名。

        ---
        返回
        - { SqliteUpdater } : 指向表的SQLite更新操作器对象。

        """
        # 如果表不存在表结构中则抛出异常
        if table_name not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundError(table_name)

        return SqliteUpdater(table_name, self._table_structure[table_name])


    # ----------------------------------------------------------------------
    def delete(self, table_name: str) -> SqliteDeleter:
        """
        [ 表删除 ]

        ---
        参数
        - table_name : { str } - 表名。

        ---
        返回
        - { SqliteDeleter } : 指向表的SQLite删除操作器对象。

        """
        # 如果表不存在表结构中则抛出异常
        if table_name not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundError(table_name)

        return SqliteDeleter(table_name, self._table_structure[table_name])


# --------------------------------------------------------------------------
class SqliteSelecter:
    """
    [ SQLite查询处理器 ]

    """
    _table_name: str
    """ 表名 """
    _table_structure: dict
    """ 表结构 """
    _query_items: dict
    """ 查询项 """
    _filter_items: dict
    """ 过滤项 """
    _sort_items: dict
    """ 排序项 """
    _page: int
    """ 页码 """
    _number: int
    """ 数据量 """
    _data_alias: list
    """ 数据别名 """


    # ----------------------------------------------------------------------
    def __init__(self, table_name: str, table_structure: dict) -> ...:
        """
        [ SQLite查询处理器 ]

        ---
        参数
        - table_name      : { str }  - 表名。
        - table_structure : { dict } - 表结构。

        """
        self._table_name = table_name
        self._table_structure = table_structure
        self._query_items = {}
        self._filter_items = {}
        self._sort_items = {}
        self._page   = None
        self._number = None
        self._data_alias = []


    # ----------------------------------------------------------------------
    def __str__(self) -> str:
        statement_select = self._processing_query_statement()
        statement_filter = self._processing_filter_statement()
        statement_sort   = self._processing_sort_statement()
        statement_limit  = self._processing_data_limit_statement()
        return f'{statement_select} \nFROM \n\t{self._table_name} \n{statement_filter} \n{statement_sort} \n{statement_limit}'


    # ----------------------------------------------------------------------
    def get(self, field: str, event: str = None) -> ...:
        """
        [ 查询项 ]

        ---
        描述
        - 新增一个查询项, 执行语句后返回查询项数据。

        ---
        参数
        - field : { str } - 字段。
        - event : { str } - 查询事件, None表示不使用事件。
        
        """
        if field not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundFieldError(table_name=self._table_name, field_name=field)
        else:
            self._query_items.update({field : event})

    
    # ----------------------------------------------------------------------
    def filter_equal(self, field: str, value: str) -> ...:
        """
        [ 过滤相等 ]

        ---
        描述
        - 新增一个过滤项, 过滤掉字段与值相等的数据。

        ---
        参数
        - field : { str } - 字段。
        - value : { str } - 字段的值。

        """
        if field not in self._table_structure.keys():
            ...
        else:
            self._filter_items.update({field : value})


    # ----------------------------------------------------------------------
    def filter_equal_batch(self, field_dict: dict):
        for k, v in field_dict.items():
            self.filter_equal(k, v)


    # ----------------------------------------------------------------------
    def set_sort_asc(self, field: str):
        """
        [ 设置正序排序 ]

        """
        if field not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundFieldError(table_name=self._table_name, field_name=field)
        else:
            self._sort_items.update({field : G_KEYWORD.Sqlite.SortType.Asc})


    # ----------------------------------------------------------------------
    def set_sort_desc(self, field: str):
        """
        [ 设置逆序排序 ]

        """
        if field not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundFieldError(table_name=self._table_name, field_name=field)
        else:
            self._sort_items.update({field : G_KEYWORD.Sqlite.SortType.Desc})


    # ----------------------------------------------------------------------
    def set_data_limit(self, page, number):
        """
        [ 设置数据限制 ]

        """
        if page and number:
            self._page   = int(page)
            self._number = int(number)


    # ----------------------------------------------------------------------
    def _processing_query_statement(self):
        """
        [ 处理查询语句 ]

        """
        # 查询项为空则返回 SELECT *
        if len(self._query_items) == 0:
            for key in self._table_structure.keys():
                self._query_items.update({key: None})

        field_statement = ''
        for tfmn, tfmv in self._query_items.items():
            if len(field_statement) > 0:
                field_statement += ', '
            if tfmv == None:
                field_statement += tfmn
                self._data_alias.append(tfmn)
            else:
                field_statement += f'{tfmv}({tfmn})'
                self._data_alias.append(f'{tfmv.lower()}')

        return f'SELECT \n\t{field_statement}'


    # ----------------------------------------------------------------------
    def _processing_filter_statement(self):
        """
        [ 处理过滤语句 ]

        """
        # 过滤项为空则返回空字符串
        if len(self._filter_items) == 0:
            return ''

        field_statement = ''
        for wherek, wherev in self._filter_items.items():
            if len(field_statement) > 0:
                field_statement += '\nAND\n\t'

            # 如果过滤项是数据库数值类型则不加引号
            if self._table_structure.get(wherek) in [
                G_KEYWORD.Sqlite.DataType.IdKey,
                G_KEYWORD.Sqlite.DataType.Int,
                G_KEYWORD.Sqlite.DataType.IntNotNull
            ]:
                field_statement += f'{wherek} = {wherev}'
            else:
                field_statement += f"{wherek} = '{wherev}'"

        return f'WHERE \n\t{field_statement}'


    # ----------------------------------------------------------------------
    def _processing_sort_statement(self):
        """
        [ 处理排序语句 ]

        """
        if len(self._sort_items) == 0:
            return ''
        field_statement = ''
        for tfmn, tfmv in self._sort_items.items():
            if len(field_statement) > 0:
                field_statement += ', '
            field_statement += f'{tfmn} {tfmv}'
        return f'ORDER BY \n\t{field_statement}'


    # ----------------------------------------------------------------------
    def _processing_data_limit_statement(self):
        """
        [ 处理数据限制语句 ]

        """
        if self._page and self._number:
            # 计算偏移量
            limit_begin = 0
            if self._page > 1:
                limit_begin = (self._page - 1) * self._number
            return f'LIMIT \n\t{ limit_begin }, { self._number }'
        else:
            return ''


# --------------------------------------------------------------------------
class SqliteInserter:
    """
    [ SQLite插入处理器 ]

    """
    _with_lock: bool
    """ 是否带锁 """
    _table_name: str
    """ 表名 """
    _table_structure: dict
    """ 表结构 """
    _insert_items: dict
    """ 插入项 """


    # ----------------------------------------------------------------------
    def __init__(self, table_name: str, table_structure: dict) -> ...:
        """
        [ SQLite插入处理器 ]

        ---
        参数
        - table_name      : { str }  - 表名。
        - table_structure : { dict } - 表结构。

        """
        self._with_lock = False
        self._table_name = table_name
        self._table_structure = table_structure
        self._insert_items = {}


    # ----------------------------------------------------------------------
    def __str__(self) -> str:
        statement_items  = self._processing_items_statement()
        statement_values = self._processing_values_statement()
        return f'INSERT INTO {self._table_name} \n(\n{statement_items}\n)\nVALUES \n(\n{statement_values}\n)'


    # ----------------------------------------------------------------------
    def lock(self) -> ...:
        """
        [ 带锁 ]

        """
        self._with_lock = True


    # ----------------------------------------------------------------------
    def deduction(self, values: list) -> ...:
        """
        [ 推导入表 ]

        ---
        描述
        - 自动根据表结构

        ---
        参数
        - values : { str } - 字段值列表。
        
        """
        table_structure_keys = self._table_structure.keys()
        if len(values) < len(table_structure_keys):
            raise AwakenDatabaseTableDeductionInserteError(
                self._table_name, len(table_structure_keys), len(values)
            )
        else:
            push_dict = dict(zip(table_structure_keys, values))
            for key, value in push_dict.items():
                self.push(key, value)


    # ----------------------------------------------------------------------
    def push(self, field: str, value: str = 'NULL') -> ...:
        """
        [ 插入项 ]

        ---
        描述
        - 新增一个插入项。

        ---
        参数
        - field : { str } - 字段。
        - value : { str } - 字段值。
        
        """
        if field not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundFieldError(table_name=self._table_name, field_name=field)
        else:
            self._insert_items.update({field : value})


    # ----------------------------------------------------------------------
    def _processing_items_statement(self):
        """
        [ 处理项语句 ]

        """
        # 过滤项为空则返回空字符串
        if len(self._insert_items) == 0:
            return ''

        statement = ''
        for itemn, _ in self._insert_items.items():
            if len(statement) > 0:
                statement += ', \n'
            statement += f'\t{itemn}'

        return statement


    # ----------------------------------------------------------------------
    def _processing_values_statement(self):
        """
        [ 处理值语句 ]

        """
        # 过滤项为空则返回空字符串
        if len(self._insert_items) == 0:
            return ''

        statement = ''
        for itemn, itemv in self._insert_items.items():
            if len(statement) > 0:
                statement += ', \n'

            # 如果过滤项是数据库数值类型则不加引号
            if self._table_structure.get(itemn) in [
                G_KEYWORD.Sqlite.DataType.IdKey,
                G_KEYWORD.Sqlite.DataType.Int,
                G_KEYWORD.Sqlite.DataType.IntNotNull,
            ]:
                statement += f'\t{itemv}'
            else:
                statement += f"\t'{itemv}'"

        return statement


# --------------------------------------------------------------------------
class SqliteUpdater:
    """
    [ SQLite更新处理器 ]

    """
    _with_lock: bool
    """ 是否带锁 """
    _table_name: str
    """ 表名 """
    _table_structure: dict
    """ 表结构 """
    _updata_items: dict
    """ 更新项 """
    _filter_items: dict
    """ 过滤项 """


    # ----------------------------------------------------------------------
    def __init__(self, table_name: str, table_structure: dict) -> ...:
        """
        [ SQLite更新处理器 ]

        ---
        参数
        - table_name      : { str }  - 表名。
        - table_structure : { dict } - 表结构。

        """
        self._with_lock = False
        self._table_name = table_name
        self._table_structure = table_structure
        self._updata_items = {}
        self._filter_items = {}


    # ----------------------------------------------------------------------
    def lock(self) -> ...:
        """
        [ 带锁 ]

        """
        self._with_lock = True


    # ----------------------------------------------------------------------
    def __str__(self) -> str:
        statement_updatas = self._processing_updatas_statement()
        statement_filter  = self._processing_filter_statement()
        return f'UPDATE \n\t{self._table_name} \nSET\n{statement_updatas}\n{statement_filter}'


    # ----------------------------------------------------------------------
    def push(self, field: str, value: str = None) -> ...:
        """
        [ 更新项 ]

        ---
        描述
        - 新增一个更新项。

        ---
        参数
        - field : { str } - 字段。
        - value : { str } - 字段值。
        
        """
        if field not in self._table_structure.keys():
            raise AwakenDatabaseTableNotFoundFieldError(table_name=self._table_name, field_name=field)
        else:
            self._updata_items.update({field : value})


    # ----------------------------------------------------------------------
    def filter_equal(self, field: str, value: str) -> ...:
        """
        [ 过滤相等 ]

        ---
        描述
        - 新增一个过滤项, 过滤掉字段与值相等的数据。

        ---
        参数
        - field : { str } - 字段。
        - value : { str } - 字段的值。

        """
        if field not in self._table_structure.keys():
            ...
        else:
            self._filter_items.update({field : value})


    # ----------------------------------------------------------------------
    def filter_equal_batch(self, field_dict: dict):
        for k, v in field_dict.items():
            self.filter_equal(k, v)


    # ----------------------------------------------------------------------
    def _processing_updatas_statement(self):
        """
        [ 处理更新语句 ]

        """
        # 查询项为空则返回 SELECT *
        if len(self._updata_items) == 0:
            return ''

        field_statement = ''
        for tfmn, tfmv in self._updata_items.items():
            if len(field_statement) > 0:
                field_statement += ', \n'

            # 如果过滤项是数据库数值类型则不加引号
            if self._table_structure.get(tfmn) in [
                G_KEYWORD.Sqlite.DataType.IdKey,
                G_KEYWORD.Sqlite.DataType.Int,
                G_KEYWORD.Sqlite.DataType.IntNotNull
            ]:
                field_statement += f'\t{tfmn} = {tfmv}'
            else:
                field_statement += f"\t{tfmn} = '{tfmv}'"
                # tfmv = str(tfmv)
                # if tfmv[0] == '"' and tfmv[-1] == '"' or tfmv[0] == "'" and tfmv[-1] == "'":
                #     tfmv = ''.join(["'", tfmv[1: -1] ,"'"])
                #     field_statement += f'\t{tfmn} = {tfmv}'
                # else:
                #     field_statement += f"\t{tfmn} = '{tfmv}'"

        return f'{field_statement}'


    # ----------------------------------------------------------------------
    def _processing_filter_statement(self):
        """
        [ 处理过滤语句 ]

        """
        # 过滤项为空则返回空字符串
        if len(self._filter_items) == 0:
            return ''

        field_statement = ''
        for wherek, wherev in self._filter_items.items():
            if len(field_statement) > 0:
                field_statement += '\nAND\n\t'

            # 如果过滤项是数据库数值类型则不加引号
            if self._table_structure.get(wherek) in [
                G_KEYWORD.Sqlite.DataType.IdKey,
                G_KEYWORD.Sqlite.DataType.Int,
                G_KEYWORD.Sqlite.DataType.IntNotNull
            ]:
                field_statement += f'{wherek} = {wherev}'
            else:
                field_statement += f'{wherek} = "{wherev}"'

        return f'WHERE \n\t{field_statement}'


# --------------------------------------------------------------------------
class SqliteDeleter:
    """
    [ SQLite删除处理器 ]

    """
    _with_lock: bool
    """ 是否带锁 """
    _table_name: str
    """ 表名 """
    _table_structure: dict
    """ 表结构 """
    _filter_items: dict
    """ 过滤项 """


    # ----------------------------------------------------------------------
    def __init__(self, table_name: str, table_structure: dict) -> ...:
        """
        [ SQLite删除处理器 ]

        ---
        参数
        - table_name      : { str }  - 表名。
        - table_structure : { dict } - 表结构。

        """
        self._with_lock = False
        self._table_name = table_name
        self._table_structure = table_structure
        self._filter_items = {}


    # ----------------------------------------------------------------------
    def lock(self) -> ...:
        """
        [ 带锁 ]

        """
        self._with_lock = True


    # ----------------------------------------------------------------------
    def __str__(self) -> str:
        statement_filter  = self._processing_filter_statement()
        return f'DELETE FROM \n\t{self._table_name} \n{statement_filter}'


    # ----------------------------------------------------------------------
    def filter_equal(self, field: str, value: str) -> ...:
        """
        [ 过滤相等 ]

        ---
        描述
        - 新增一个过滤项, 过滤掉字段与值相等的数据。

        ---
        参数
        - field : { str } - 字段。
        - value : { str } - 字段的值。

        """
        if field not in self._table_structure.keys():
            ...
        else:
            self._filter_items.update({field : value})


    # ----------------------------------------------------------------------
    def filter_equal_batch(self, field_dict: dict):
        for k, v in field_dict.items():
            self.filter_equal(k, v)


    # ----------------------------------------------------------------------
    def _processing_updatas_statement(self):
        """
        [ 处理更新语句 ]

        """
        # 查询项为空则返回 SELECT *
        if len(self._updata_items) == 0:
            return ''

        field_statement = ''
        for tfmn, tfmv in self._updata_items.items():
            if len(field_statement) > 0:
                field_statement += ', \n'

            # 如果过滤项是数据库数值类型则不加引号
            if self._table_structure.get(tfmn) in [
                G_KEYWORD.Sqlite.DataType.IdKey,
                G_KEYWORD.Sqlite.DataType.Int,
                G_KEYWORD.Sqlite.DataType.IntNotNull
            ]:
                field_statement += f'\t{tfmn} = {tfmv}'
            else:
                field_statement += f'\t{tfmn} = "{tfmv}"'

        return f'{field_statement}'


    # ----------------------------------------------------------------------
    def _processing_filter_statement(self):
        """
        [ 处理过滤语句 ]

        """
        # 过滤项为空则返回空字符串
        if len(self._filter_items) == 0:
            return ''

        field_statement = ''
        for wherek, wherev in self._filter_items.items():
            if len(field_statement) > 0:
                field_statement += '\nAND\n\t'

            # 如果过滤项是数据库数值类型则不加引号
            if self._table_structure.get(wherek) in [
                G_KEYWORD.Sqlite.DataType.IdKey,
                G_KEYWORD.Sqlite.DataType.Int,
                G_KEYWORD.Sqlite.DataType.IntNotNull
            ]:
                field_statement += f'{wherek} = {wherev}'
            else:
                field_statement += f'{wherek} = "{wherev}"'

        return f'WHERE \n\t{field_statement}'


_: ...

# --------------------------------------------------------------------------
G_SQLITE_STATEMENT_HANDLE = SqliteStatementHandle()
""" SQLite语句处理器全局实例 """
