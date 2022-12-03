# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import datetime

import sqlalchemy
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError

from baitoolkit.common import type_util
from baitoolkit.common.context_manager import global_ctx
from baitoolkit.common.type_util import ValueObj
from baitoolkit.exception import assert_util, errors

"""
    Relationship database utilities
"""

__target_metadata = {}

PRIMARY_KEY = 'primary_key'


def metadata(bind_key):
    """
    create metadata instance for table declarative.
    :return:
    """
    if bind_key not in __target_metadata:
        __target_metadata[bind_key] = sqlalchemy.MetaData()
    return __target_metadata[bind_key]


def get_sql_engine(bind_key):
    """Return sql engine according to bind_key."""
    return global_ctx.db_client_manager.get_engine(bind_key)


def table(name, meta_data, *args, created_at=True, created_by=True, last_updated_at=True,
          last_updated_by=True, **kw):
    """
    Extend Table declarative features
    See https://docs.sqlalchemy.org/en/13/core/metadata.html
    """
    bind_key = kw['info']['bind_key']
    if name in __target_metadata[bind_key].tables:
        return __target_metadata[bind_key].tables[name]

    default_kws = type_util.ValueObj()
    default_args = []
    if created_at:
        primary_key = True if created_at == PRIMARY_KEY else False
        default_args.append(column('created_at', sqlalchemy.DateTime(), nullable=False, primary_key=primary_key,
                                   default=type_util.tz_utcnow(), comment="创建时间"))
    if created_by:
        primary_key = True if created_by == PRIMARY_KEY else False
        default_args.append(
            column('created_by', sqlalchemy.String(10), nullable=False, primary_key=primary_key, comment="创建人"))
    if last_updated_at:
        primary_key = True if last_updated_at == PRIMARY_KEY else False
        default_args.append(column('last_updated_at', sqlalchemy.DateTime(), nullable=False, primary_key=primary_key,
                                   default=type_util.tz_utcnow(), comment="最后修改时间"))
    if last_updated_by:
        primary_key = True if last_updated_by == PRIMARY_KEY else False
        default_args.append(column('last_updated_by', sqlalchemy.String(10), nullable=False, primary_key=primary_key,
                                   comment="最后修改人"))

    default_kws.mysql_engine = 'InnoDB'
    default_kws.mysql_charset = 'utf8mb4'
    ex_args = []
    ex_args.extend(default_args)
    ex_args.extend(args)
    ex_kws = {}
    ex_kws.update(default_kws)
    ex_kws.update(kw)
    table_instance = sqlalchemy.Table(name, meta_data, *ex_args, **ex_kws)
    return table_instance


def column(*args, **kw):
    """
    Extend Column declarative features
    See https://docs.sqlalchemy.org/en/13/core/metadata.html
    """
    field = sqlalchemy.Column(*args, **kw)
    return field


def index(name, *expressions, **kw):
    """
    Extend Index declarative features
    See https://docs.sqlalchemy.org/en/13/core/constraints.html
    """
    return sqlalchemy.Index(name, *expressions, **kw)


def bindparam(key, null=False, **kw):
    """
    Extend bindparam declarative features.
    See https://docs.sqlalchemy.org/en/13/core/sqlelement.html#sqlalchemy.sql.expression.bindparam
    :param key: See sqlalchemy.sql.elements.BindParameter
    :param null: Set callable_ arguments to avoid exception of 'Bind parameter 'process_remark' without a renderable value not allowed here.'
                if null is True
    :param kw: See sqlalchemy.sql.elements.BindParameter
    :return:
    """
    if null:
        def call():
            return None

        return sqlalchemy.bindparam(key, callable_=call, **kw)
    else:
        return sqlalchemy.bindparam(key, **kw)


def ddl(statement, on=None, context=None, bind=None):
    """Return Custom DDL phrases.
    Refer to https://docs.sqlalchemy.org/en/13/core/ddl.html?highlight=ddl#custom-ddl.
    """
    return sqlalchemy.DDL(statement, on=on, context=context, bind=bind)


def text(sql):
    """
    See https://docs.sqlalchemy.org/en/13/core/tutorial.html#using-textual-sql
    :param str sql: Raw sql
    :return: sqlalchemy.sql.text
    """
    return sqlalchemy.sql.text(sql)


def literal(statement, engine):
    """
    Return the raw sql string of statement or Query.
    NOTE: This is entirely insecure. DO NOT execute the resulting strings.
    :param statement: sqlalchemy Insert, Update, Delete, Select or Query.
    :param engine: sqlalchemy engine instance
    :return str: Raw Sql
    """

    class StringLiteral(sqlalchemy.sql.sqltypes.String):
        """
        Teach SqlAlchemy how to literalize various things.
        """

        def literal_processor(self, dialect):
            super_processor = super(StringLiteral, self).literal_processor(dialect)

            def process(value):
                if value is None:
                    return 'NULL'
                if isinstance(value, int):
                    return str(value)
                if isinstance(value, datetime.datetime):
                    value = type_util.tz_datetime_to_str(value, fmt='%Y-%m-%d %H:%M:%S')
                if not isinstance(value, str):
                    value = str(value)
                result = super_processor(value)
                if isinstance(result, bytes):
                    result = result.decode(dialect.encoding)
                return result

            return process

    class LiteralDialect(engine.dialect.__class__):
        colspecs = {
            sqlalchemy.sql.sqltypes.String: StringLiteral,
            sqlalchemy.sql.sqltypes.Text: StringLiteral,
            sqlalchemy.sql.sqltypes.DateTime: StringLiteral,
            sqlalchemy.sql.sqltypes.NullType: StringLiteral,
        }

    if isinstance(statement, sqlalchemy.orm.Query):
        statement = statement.statement
    return statement.compile(
        dialect=LiteralDialect(),
        compile_kwargs={'literal_binds': True},
    ).string


def listen(target, identifier, fn, *args, **kw):
    """Register a listener function for the given target.
    Refer to https://docs.sqlalchemy.org/en/13/core/event.html#sqlalchemy.event.listen."""
    event.listen(target, identifier, fn, *args, **kw)


def listens_for(target, identifier, *args, **kw):
    """Decorate a function as a listener for the given target + identifier.
        Refer to https://docs.sqlalchemy.org/en/13/core/event.html#sqlalchemy.event.listens_for."""
    event.listens_for(target, identifier, *args, **kw)


def df_to_sa_types(df, length=255, precision=2):
    """
    Convert DataFrame types to SqlAlchemy types.
    :param df:DataFrame: DataFrame
    :param length:int: varchar length
    :param precision:int: the float precision
    :rtype: dict
    :return: the mapping of DataFrame types to SqlAlchemy types.
    """
    dic = {}
    for i, j in zip(df.columns, df.dtypes):
        if "object" in str(j):
            dic.update({i: sqlalchemy.types.NVARCHAR(length=length)})
        if "float" in str(j):
            dic.update({i: sqlalchemy.types.Float(precision=precision, asdecimal=True)})
        if "int" in str(j):
            dic.update({i: sqlalchemy.types.Integer()})
    return dic


def execute_stmt(connection, stmt, *multi_params, **params):
    """
    Execute statement
    :param connection: Sqlalchemy.engine.connect()
    :param stmt: sqlalchemy.insert update delete select text(raw sql)
    :return: sqlalchemy.result
    """
    try:
        result = connection.execute(stmt, *multi_params, **params)
    except IntegrityError as e:
        if e.orig.args[0] == 1062:
            raise errors.ExistingError(e.orig.args[1].replace('Duplicate ', ''))
        else:
            raise e
    return result


def execute_sql(connection, raw_sql, *multi_params, **params):
    """
    Execute statement
    :param connection: Sqlalchemy.engine.connect()
    :param str raw_sql:
    :return: sqlalchemy.result
    """
    stmt = text(raw_sql)
    return execute_stmt(connection, stmt, *multi_params, **params)


def execute_sql_in_tpl(connection, tpl_name: str, tpl_kwargs: dict, sql_params: tuple = None, return_df: bool = False):
    """
    Execute sql defined in jinja template.
    @param connection:
    @param tpl_name: template name.
    @param tpl_kwargs: arguments used in template.
    @param sql_params: (multi_params, params)
    @param return_df: if True, return pandas.DataFrame
    """
    # TODO..
    

def assert_unique(value_obj: ValueObj, label: str, unique_column_names: list = None, table_instance=None):
    """Check if unique in table_instance.
    :param ValueObj value_obj: the value to be verified.
    :param str label: the label to show in the error message.
    :param list unique_column_names: the unique column name list.
    :param TableBase table_instance: the table instance to check unique.
    """
    assert_util.assert_required(value_obj, "value_obj")
    assert_util.assert_required(unique_column_names, "unique_column_names")
    assert_util.assert_required(table_instance, "table_instance")
    wheres = list()
    error_data = dict()
    for name in unique_column_names:
        wheres.append(table_instance.column.get(name) == value_obj.get(name))
        error_data[name] = value_obj.get(name)
    if table_instance.primary_key in value_obj:
        wheres.append(table_instance.primary_key != value_obj.get(table_instance.primary_key))
    rows = table_instance.select_rows(wheres, limit=1)
    if len(rows) > 0:
        raise errors.ExistingError(label, type_util.obj_to_json(error_data))
    return True
