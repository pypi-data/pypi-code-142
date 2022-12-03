# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import time

import sqlalchemy

from baitoolkit.common import type_util
from baitoolkit.common.type_util import Singleton, ValueObj
from baitoolkit.database import rdb_alchemy
from baitoolkit.database.rdb_alchemy import get_sql_engine
from baitoolkit.exception import assert_util, errors
from baitoolkit.exception.errors import CreationError, UpdateError, DeleteError
from baitoolkit.param.param_validator import RequiredValidator, TypeValidator, LengthValidator


class TableBase(object, metaclass=Singleton):
    """
    Base class of Sql Table to add some basic properties and methods.
    """

    __table_name__ = None
    __table_dec__ = None
    __column_validators__ = None
    __row_validators__ = None
    __write_audit_log__ = True

    def __init__(self):
        """don't override this method otherwise below three properties will not be set due singleton."""
        self._table = self.__class__.__table_dec__
        self._column_validators = self.__class__.__column_validators__
        self._row_validators = self.__class__.__row_validators__

    @classmethod
    def get_instance(cls):
        """Return instance."""
        return cls()

    @property
    def engine(self):
        """Return engine of current table uses."""
        return get_sql_engine(self.__table_dec__.info['bind_key'])

    @property
    def name(self):
        """Return table name"""
        return self.__table_name__

    @property
    def connection(self):
        """Return a new connection."""
        return self.engine.connect()

    @property
    def table(self):
        """
        :return: SqlAlchemy.Table
        """
        if self._table is None or not isinstance(self._table, sqlalchemy.Table):
            raise NotImplementedError('self._table is not override in sub-class.')
        return self._table

    @property
    def column_validators(self) -> dict:
        return self._column_validators

    @property
    def row_validators(self) -> list:
        return self._row_validators

    @property
    def primary_key(self):
        """
        return primary key column of this table.
        :return:
        """
        columns = sqlalchemy.inspect(self.table).primary_key.columns
        if len(columns) == 0:
            return None
        return columns.values()[0]

    @property
    def column(self):
        """
        See https://docs.sqlalchemy.org/en/13/core/metadata.html
        :return: self.table.c
        """
        return self.table.c

    @staticmethod
    def sub_classes():
        """Return all sub-classes of TableBase"""
        scs = []
        for sc in TableBase.__subclasses__():
            scs.append(sc)
        return scs

    def create_table(self, connection):
        """
        Create table
        :param connection: Sqlalchemy.engine.connect()
        :return:
        """
        self.table.create(connection, checkfirst=True)

    def drop_table(self, connection):
        """
        drop one table
        :param connection: Sqlalchemy.engine.connect()
        :return: void
        """
        self.table.drop(connection)

    def insert(self, **kwargs):
        """
        See https://docs.sqlalchemy.org/en/13/core/dml.html
        :param dict kwargs: See sqlalchemy.sql.dml.Insert
        :return: sqlalchemy.sql.dml.Insert
        """
        return self.table.insert(kwargs)

    def update(self, **kwargs):
        """
        See https://docs.sqlalchemy.org/en/13/core/dml.html
        :param dict kwargs: See sqlalchemy.sql.dml.Update
        :return: sqlalchemy.sql.dml.Update
        """
        return self.table.update(**kwargs)

    def delete(self, **kwargs):
        """
        See https://docs.sqlalchemy.org/en/13/core/dml.html
        :param dict kwargs: See sqlalchemy.sql.dml.Delete
        :return: sqlalchemy.sql.dml.Delete
        """
        return self.table.delete(**kwargs)

    def select(self, columns=None, wheres=None, distinct=False, orders=None, **kwargs):
        """
        See https://docs.sqlalchemy.org/en/13/core/selectable.html#sqlalchemy.sql.expression.select
        :param list[Sqlalchemy.Column] columns:
        :param list[Sqlalchemy.whereclause] wheres:
        :param bool distinct:
        :param list[Sqlalchemy.Column] orders:
        :param dict kwargs: See sqlalchemy.sql.selectable.Select
        :return: sqlalchemy.sql.selectable.Select
        """
        stmt = self.table.select(distinct=distinct, **kwargs)
        if columns is not None and len(columns) > 0:
            stmt = stmt.with_only_columns(columns)
        wheres = [] if wheres is None else wheres
        orders = [] if orders is None else orders
        for where in wheres:
            stmt = stmt.where(where)
        for order in orders:
            stmt = stmt.order_by(order)
        return stmt

    def insert_row(self, value_obj, created_by, suffix=None, stmt=None, connection=None, **kwargs):
        """
        Insert one record to table.
        :param type_util.ValueObj value_obj:
        :param str suffix:
        :param str created_by:
        :param Sqlalchemy.sql.dml.Insert stmt:
        :param Sqlalchemy.engine.connect() connection:
        :param dict kwargs:
        :return:
        """
        assert_util.assert_required(value_obj, 'value_obj')
        assert_util.assert_required(created_by, 'created_by')
        value_obj.created_by = created_by
        value_obj.created_at = type_util.tz_utcnow()
        value_obj.last_updated_by = created_by
        value_obj.last_updated_at = type_util.tz_utcnow()
        self.assert_value_obj(value_obj)
        stmt = self._get_stmt(stmt, self.insert, suffix, **kwargs)
        stmt = stmt.values(**value_obj)
        connection = self.connection if connection is None else connection
        result = self.execute_statement(connection, stmt)
        if result.rowcount != 1:
            raise CreationError(self.name)
        return result.rowcount

    def update_row(self, row_id, value_obj, last_updated_by, suffix=None, stmt=None, connection=None, **kwargs):
        """
        Update one record of this table.
        :param str row_id: Primary key value
        :param type_util.ValueObj value_obj:
        :param str last_updated_by:
        :param str suffix:
        :param Sqlalchemy.sql.dml.Update stmt:
        :param Sqlalchemy.engine.connect() connection:
        :param dict kwargs:
        :return:
        """
        assert_util.assert_required(row_id, 'row_id')
        assert_util.assert_required(value_obj, 'value_obj')
        assert_util.assert_required(last_updated_by, 'last_updated_by')
        value_obj.last_updated_by = last_updated_by
        value_obj.last_updated_at = type_util.tz_utcnow()
        self.assert_value_obj(value_obj, strict=False)
        stmt = self._get_stmt(stmt, self.update, suffix, **kwargs)
        if self.primary_key.name in value_obj:
            del value_obj[self.primary_key.name]
        stmt = stmt.values(**value_obj)
        stmt = stmt.where(self.primary_key == row_id)
        connection = self.connection if connection is None else connection
        result = self.execute_statement(connection, stmt)
        if result.rowcount < 1:
            raise UpdateError(self.name)
        return result.rowcount

    def update_rows(self, table, wheres, value_obj, last_updated_by, suffix=None, stmt=None, connection=None, **kwargs):
        """
        Update multiple rows.
        :param rdb_table.TableBase table: table instance.
        :param wheres:
        :param value_obj:
        :param last_updated_by:
        :param str suffix:
        :param stmt:
        :param connection:
        :param kwargs:
        :return:
        """
        assert_util.assert_required(wheres, 'wheres')
        assert_util.assert_required(value_obj, 'value_obj')
        assert_util.assert_required(last_updated_by, 'last_updated_by')
        value_obj.last_updated_at = type_util.tz_utcnow()
        value_obj.last_updated_by = last_updated_by
        assert_util.assert_required(value_obj, 'value_obj')
        self.assert_value_obj(value_obj, strict=False)
        stmt = self._get_stmt(stmt, table.update, suffix, **kwargs)
        stmt = stmt.values(**value_obj)
        for where in wheres:
            stmt = stmt.where(where)
        connection = table.connection if connection is None else connection
        result = self.execute_statement(connection, stmt)
        return result.rowcount

    def delete_row(self, row_id, deleted_by, suffix=None, stmt=None, connection=None, **kwargs):
        """
        Delete one row of this table.
        :param str row_id:  Primary key
        :param str deleted_by:
        :param str suffix:
        :param Sqlalchemy.sql.dml.Delete stmt:
        :param Sqlalchemy.engine.connect() connection:
        :param dict kwargs:
        :return:
        """
        assert_util.assert_required(row_id, 'row_id')
        stmt = self._get_stmt(stmt, self.delete, suffix, **kwargs)
        stmt = stmt.where(self.primary_key == row_id)
        connection = self.connection if connection is None else connection
        result = self.execute_statement(connection, stmt)
        if result.rowcount < 1:
            raise DeleteError(self.name)
        return result.rowcount

    def delete_rows(self, wheres: list, deleted_by, suffix=None, stmt=None, connection=None, **kwargs):
        """
        Delete multiple rows by criteria.
        :param list wheres:
        :param str deleted_by:
        :param str suffix:
        :param Sqlalchemy.sql.dml.Select stmt:
        :param Sqlalchemy.engine.connect() connection:
        :param dict kwargs:
        :return:
        """
        assert_util.assert_required(wheres, 'wheres')
        assert_util.assert_required(deleted_by, 'deleted_by')
        wheres = [wheres] if not isinstance(wheres, list) else wheres
        stmt = self._get_stmt(stmt, self.delete, suffix, **kwargs)
        for where in wheres:
            stmt = stmt.where(where)
        connection = self.connection if connection is None else connection
        result = self.execute_statement(connection, stmt)
        return result.rowcount

    def select_row(self, row_id_or_wheres, suffix=None, stmt=None, connection=None, **kwargs):
        """
        Get one row by primary key.
        :param rdb_table.TableBase table: table instance.
        :param str|list row_id_or_wheres: Primary key or wheres
        :param str suffix:
        :param Sqlalchemy.sql.dml.Select stmt:
        :param Sqlalchemy.engine.connect() connection:
        :param dict kwargs:
        :return:
        """
        assert_util.assert_required(row_id_or_wheres, 'row_id_or_wheres')
        stmt = self._get_stmt(stmt, self.select, suffix, **kwargs)
        if isinstance(row_id_or_wheres, list):
            for where in row_id_or_wheres:
                stmt = stmt.where(where)
        else:
            stmt = stmt.where(self.primary_key == row_id_or_wheres)
        connection = self.connection if connection is None else connection
        result = self.execute_statement(connection, stmt).first()
        return result

    def select_rows(self, columns=None, wheres=None, distinct=False, orders=None, offset=0, limit=1000,
                    suffix=None, stmt=None, connection=None, **kwargs):
        """
        Select multiple rows
        :param list[Sqlalchemy.Column] columns:
        :param list[Sqlalchemy.whereclause] wheres:
        :param bool distinct:
        :param list[Sqlalchemy.Column] orders:
        :param offset:
        :param limit:
        :param str suffix:
        :param Sqlalchemy.sql.dml.Select stmt:
        :param Sqlalchemy.engine.connect() connection:
        :param dict kwargs:
        :return: One row object if limit == 1 else list[row object]
        """
        offset = 0 if offset is None else offset
        limit = 1000 if limit is None else limit
        wheres = list() if wheres is None else wheres
        stmt = self._get_stmt(stmt, self.select, suffix, columns=columns, wheres=wheres, distinct=distinct,
                              orders=orders, **kwargs)
        stmt = stmt.offset(offset)
        stmt = stmt.limit(limit)
        connection = self.connection if connection is None else connection
        result = self.execute_statement(connection, stmt)
        result = result.fetchall()
        return result

    def count(self, wheres=None, suffix=None, stmt=None, connection=None, **kwargs):
        """
        Return the record counts.
        :param list[Sqlalchemy.whereclause] wheres:
        :param str suffix:
        :param Sqlalchemy.sql.dml.Select stmt:
        :param Sqlalchemy.engine.connect() connection:
        :return:
        """
        stmt = self._get_stmt(stmt, self.select, suffix, wheres=wheres, **kwargs)
        stmt = stmt.with_only_columns([sqlalchemy.func.count(self.primary_key)])
        connection = self.connection if connection is None else connection
        result = self.execute_statement(connection, stmt)
        return result.fetchall()[0][0]

    def paginate_rows(self, columns=None, wheres=None, distinct=False, orders=None, page=1, per_page=20,
                      suffix=None, stmt=None,
                      stmt_count=None, connection=None, **kwargs):
        """
        :param list[Sqlalchemy.Column] columns:
        :param list[Sqlalchemy.whereclause] wheres:
        :param distinct:
        :param list[Sqlalchemy.Column] orders:
        :param int page:
        :param int per_page:
        :param str suffix:
        :param Sqlalchemy.sql.dml.Select stmt:
        :param Sqlalchemy.sql.dml.Select stmt_count:
        :param Sqlalchemy.engine.connect() connection:
        :return:
        """
        page = int(page)
        per_page = int(per_page)
        page = page if page is not None and page >= 1 else 1
        offset = (page - 1) * per_page
        rows = self.select_rows(self.table, columns=columns, wheres=wheres, distinct=distinct, orders=orders,
                                offset=offset, limit=per_page, suffix=suffix, stmt=stmt, connection=connection,
                                **kwargs)
        total = self.count(self.table, wheres=wheres, stmt=stmt_count, connection=connection)
        return type_util.Pagination(page, per_page, total, rows)

    def assert_value_obj(self, value_obj: ValueObj, strict=True):
        """Verify column values"""
        if self.column_validators is None or len(self.column_validators) < len(self.table.columns):
            raise errors.InternalError(message="Each column must define one Validator at least, "
                                                  "'validator.add_column_validators()' helps that.")
        for name, validators in self.column_validators.items():
            if not strict and name not in value_obj:
                continue
            for validator in validators:
                validator.validate(value_obj.get(name), name)

        if self.row_validators is not None:
            for validator in self.row_validators:
                validator.validate(value_obj, self.__class__.__name__, table_instance=self)

    @staticmethod
    def execute_statement(connection, stmt, *multiparams, **params):
        """Execute statement."""
        return rdb_alchemy.execute_stmt(connection, stmt, *multiparams, **params)

    @staticmethod
    def _get_stmt(stmt, stmt_func, suffix, **kwargs):
        if stmt is not None:
            return stmt
        stmt = stmt_func(suffix, **kwargs) if suffix is not None else stmt_func(**kwargs)
        return stmt


class TableSplitMixin(object):
    """
        The mixin base class of table object to be split. The table object must
        has SqlAlchemy.Table property with the name of 'table' , 'connection' property
        that is created by SqlAlchemy.create_connection and '__table_name__' property
    """

    SUFFIXES_UPDATE_TIMESPAN = 10 * 60

    def __init__(self):
        self._suffixes = set()  # all the suffixes of the same model
        self._suffixes_last_update_time = 0

    def table_name(self, suffix):
        """
        Get table name by attaching suffix
        :param str suffix: the suffix of table name which is to be divided.
        :return:
        """
        assert_util.assert_required(suffix, 'suffix')
        assert_util.assert_required(self.__table_name__, 'self.__table_name__')
        return '%s_%s' % (self.__table_name__, suffix)

    @property
    def suffixes(self):
        """
        Get the all the table suffixes of the same model
        :return: set of suffix
        """
        if time.time() - getattr(self, '_last_suffixes_update_time', 0) > self.SUFFIXES_UPDATE_TIMESPAN:
            self._update_suffixes(self.connection)
        return self._suffixes

    def _update_suffixes(self, connection):
        """
        update all suffixes of one table
        :param connection: Sqlalchemy.engine.connect()
        :return:
        """
        self._suffixes_last_update_time = time.time()
        self._suffixes = set()
        if self.__table_name__:
            prefix = '%s_' % self.__table_name__
        else:
            raise errors.RequiredError('self.__table_name__')

        for table_name in connection.engine.table_names():
            if table_name.startswith(prefix):
                suffix = table_name[len(prefix):]
                self._suffixes.add(suffix)

    def create_table(self, connection, suffix):
        assert_util.assert_required(suffix, 'suffix')
        self.table.name = self.table_name(suffix)
        super().create_table(connection)
        self._update_suffixes(connection)

    def drop_table(self, connection, suffix):
        assert_util.assert_required(suffix, 'suffix')
        if suffix not in self._suffixes:
            self._update_suffixes(connection)
        if suffix not in self.projects:
            return
        self.table.name = self._table_names(suffix)
        super().drop_table(connection)
        self._update_suffixes(connection)

    def insert(self, suffix, **kwargs):
        self.assert_suffix(self.connection, suffix, create_table=True)
        self.table.name = self.table_name(suffix)
        return super().insert(**kwargs)

    def update(self, suffix, **kwargs):
        self.assert_suffix(suffix)
        self.table.name = self.table_name(suffix)
        return super().update(**kwargs)

    def delete(self, suffix, **kwargs):
        self.assert_suffix(suffix)
        self.table.name = self.table_name(suffix)
        return super().delete(**kwargs)

    def select(self, suffix, columns=None, wheres=None, distinct=False, orders=None, **kwargs):
        self.assert_suffix(suffix)
        self.table.name = self.table_name(suffix)
        return super().select(columns=columns, wheres=wheres, distinct=distinct, orders=orders, **kwargs)

    def assert_suffix(self, connection, suffix, create_table=False):
        assert_util.assert_required(suffix, 'suffix')
        if suffix not in self.suffixes:
            self._update_suffixes(connection)
        if suffix not in self.suffixes:
            if not create_table:
                raise errors.NoFoundError('table', self.table_name(suffix))
            else:
                self.create_table(connection, suffix)
                self._update_suffixes(connection)


def add_column_validators(table_dec, column_validators: dict):
    """Generate required, type and length validators."""

    def add_column_validator(col, validators):
        if col.primary_key and col.autoincrement:
            return
        if not col.nullable:
            validators.append(RequiredValidator())
        validators.append(TypeValidator(col.type.python_type))
        if col.type.python_type == str:
            validators.append(LengthValidator(max_length=col.type.length))

    for column in table_dec.columns:
        if column_validators.get(column.name) is None:
            column_validators[column.name] = list()
        add_column_validator(column, column_validators.get(column.name))

    return True
