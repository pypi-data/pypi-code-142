"""
    Importing modules
"""
from typing import Literal
import pytz
from sqlalchemy import create_engine, Table, MetaData, Column, select, func, and_, column, or_
from sqlalchemy.dialects.postgresql import insert, array
from timescaleutils.constants.datatypes import DATATYPES
from timescaleutils.constants.app_conf import TIME_ZONE, TBL_NAME, connection
from timescaleutils.logger import logger as log
from docstr_md.python import PySoup, compile_md


class TimeScaleUtilsException:
    pass

class TimeScaleUtils:
    """
        A Utility Class for TimeScale DB.
    """

    def __init__(self):
        self.timezone = pytz.timezone(TIME_ZONE)

    def generate_md(self):
        """
        The generate_md function takes a BeautifulSoup object and returns a string of ReST formatted text.
        The function uses the sklearn compiler to convert the soup into ReST, and writes it to an output file.

        :param self: Reference the object itself
        :return: A string of the markdown file
        :doc-author: Trelent
        """
        soup = PySoup(path='C:/Users/kayef.ahamad/PycharmProjects/timeScaleUtils/timescaleutils/timescale.py',
                      parser='sklearn')

        try:
            print("aaa")
            compile_md(soup, compiler='sklearn',
                   outfile='C:/Users/kayef.ahamad/PycharmProjects/timeScaleUtils/READMEFILE.md')
        except Exception as e:
            print(str(e))

    # -------------------Enable Timescale Extension in Postgres------------------- #

    def enable_timescale(self) -> bool:
        """
        The enable_timescale function enables the Timescale Extension in Postgres.
        It returns True if successful, False otherwise.

        :param self: Access the class attributes
        :return: True if the timescale extension is enabled, false otherwise
        """

        try:
            dbengine = create_engine(connection)
            query = """CREATE EXTENSION IF NOT EXISTS timescaledb;"""
            with dbengine.connect() as conn:
                conn.execute(query)
                conn.close()
            return True
        except ConnectionError:
            return False

    # --------------Check Timescale Extension Enabled in Postgres----------------- #
    def check_timescale(self) -> bool:
        """
        The check_timescale function checks if the Timescale Extension is enabled or not.
        It returns True if it is enabled else False.

        :param self: Allow the method to reference attributes that are defined in the class
        :return: True if timescale extension is enabled else false
        :doc-author: Trelent
        """
        try:
            dbengine = create_engine(connection)
            query = """SELECT count(*) FROM pg_available_extensions WHERE name='timescaledb';"""
            with dbengine.connect() as conn:
                result = conn.execute(query).scalar()
                count = int(result)
                conn.close()
                return bool(count > 0)
        except Exception as exp:
            log.error(f'Check Timescale Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException
    # -----------------------------Creating Table--------------------------------- #
    def create_table(self, tbl_name, table_data) -> bool:
        """
        The create_table function creates a table in the database.
        It takes two arguments, tbl_name and table_data.
        tbl_name is the name of the table to be created and should be a string.
        table_data is data for each column in the new table as a list of lists with three elements per list:
        the column name, data type, and size (e.g., [['id', 'bigint', 0], ['names', 'varchar(200)']).

        :param tbl_name: string
        :param table_data: dict [{"column": 'id', "datatype": "bigint", "length": "0"},{"column": 'names',
        "datatype": "varchar", "length": "200"},{"column": 'date_time', "datatype": "timestamp", "length": "0"}]
        :param self: Access variables that belongs to the class :return: True if the table is created :doc-author:
        Trelent
        """
        tbl_data = []
        for n in table_data:
            tbl_list = [n["column"], n["datatype"], int(n["length"])]
            tbl_data.append(tbl_list)
        table_spec = [Column(n, DATATYPES[t](s) if s else DATATYPES[t]) for n, t, s in tbl_data]
        meta = MetaData()
        try:
            engine = create_engine(connection)
            if engine.dialect.has_table(engine.connect(), tbl_name):
                print("Table Already Exists!")
                return False

            Table(tbl_name, meta, *table_spec)
            meta.create_all(engine)
            print("Table Created !")
            return True
        except Exception as exp:
            log.error(f'Create Table Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    # -----------------------------Creating Index on Ps Table----------------------------------#
    def create_index(self, tbl_name, is_unique: Literal[True, False], columns) -> bool:
        """
        The create_index function creates an index on a table in the Postgres database.
        The function takes three arguments: tbl_name, is_unique, and columns. The tbl_name argument is a string that specifies the name of the table you want to create an index on (e.g., 'users'). The is_unique argument should be True if you want to create a unique index (e.g., UNIQUE INDEX). Finally, columns should be a list of strings where each element in the list represents one column that will be included in your index.

        :param tbl_name:
        :param columns:
        :param self: Access variables that belong to the class
        :param is_unique:Literal[True: Create unique index
        :return: True if the index is created else false
        :doc-author: Trelent
        """

        try:
            colstr = ','.join(columns)
            engine = create_engine(connection)
            query = """CREATE """
            if is_unique:
                query += """UNIQUE """
            query += """ INDEX ON """ + tbl_name + """ (""" + colstr + """ DESC);"""
            with engine.connect() as conn:
                conn.execute(query)
            return True
        except Exception as exp:
            log.error(f'Create Index Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException
        # -----------------------------Check Unique Index in Ps Table----------------------------------#

    def check_unique(self, tbl_name) -> bool:
        """
        The check_unique function checks if a unique index is available in the table.
        It takes two arguments, tbl_name which is the name of the table and returns True if
        the unique index exists else False.

        :param tbl_name:
        :param self: Access variables that belongs to the class
        :return: True if the unique index exists else false
        :doc-author: Trelent
        """
        try:
            engine = create_engine(connection)
            query = """ select  count(idx.relname)
                        from pg_index pgi
                            join pg_class idx on idx.oid = pgi.indexrelid
                            join pg_namespace insp on insp.oid = idx.relnamespace
                            join pg_class tbl on tbl.oid = pgi.indrelid
                            join pg_namespace tnsp on tnsp.oid = tbl.relnamespace
                        where pgi.indisunique 
                        and tnsp.nspname = 'public' 
                        and tbl.relname = '""" + tbl_name + """'"""
            with engine.connect() as conn:
                count = conn.execute(query).scalar()
                return bool(count > 0)
        except Exception as exp:
            log.error(f'Check Unique Index Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    # -----------------------------Creating Hypertable on Ps Table----------------------------------#
    def create_hypertable(self, tbl_name, column_name) -> bool:
        """
        The create_hypertable function creates a hypertable in Postgres.
        The function takes two arguments: tbl_name and column_name.
        tbl_name is the name of the table to be created as a hypertable, while column_name is the name of the time-based partitioning
        column for that table.

        :param self: Access variables that belong to the class
        :param tbl_name: Specify the table that you want to create a hypertable for
        :param column_name: Specify the name of the column that will be used to partition the table
        :return: True if the table is created else returns false
        :doc-author: Trelent
        """
        try:
            engine = create_engine(connection)
            source_metadata = MetaData(engine)
            tbl = Table(tbl_name, source_metadata, autoload=True)
            querycheckempty = select([func.count()]).select_from(tbl).scalar()
            if querycheckempty <= 0:
                query = """SELECT create_hypertable('""" + tbl_name + """','""" + column_name + """', if_not_exists 
                => TRUE); """
                with engine.connect() as conn:
                    conn.execute(query)
                return True
            print('Error : Hypertable can be created only on empty table')
            return False
        except Exception as exp:
            log.error(f'Create Hypertable Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    # -----------------------------Selecting data from Ps Table----------------------------------#
    def selectgroupdata(self, select_type: Literal["avg", "cols", "sum", "max", "min", "arr_agg", "all"],
                        timerange, condition, group_by, order_by, columns, limit) -> list:
        """
        The selectgroupdata function is used to select data from the table.
        It takes in a number of parameters, and returns a list of dictionaries.
        The first parameter is the type of data you want to select: avg, sum, min, max or all (all selects every column).
        The second parameter is optional - if not specified it will return all rows between start and end times (inclusive).
        If you do specify a range then only those rows within that time range will be returned. The third parameter allows you to filter by columns using where clauses.
        
        :param self: Access variables that belongs to the class
        :param select_type:Literal[&quot;avg&quot;: Select the average, sum, min, max values from the table
        :param &quot;cols&quot;: Select all columns from the table
        :param &quot;sum&quot;: Select the sum of a column
        :param &quot;max&quot;: Select the maximum value from a column
        :param &quot;min&quot;: Select the minimum value from a column
        :param &quot;arr_agg&quot;: Select the array_aggregate function from the database
        :param &quot;all&quot;]: Select all columns from the table
        :param group_by: Group the data by a column
        :param timerange: Specify the time range that you want to select 
        Format : {"start":"2022-11-01 12:00:00","end":"2022-11-02 12:00:00"}Specify the time range that you want to select
        :param condition: Filter the data
        Format : {"name": "orwhere/where", "condition": {"column2": "value2"}} Filter the data
        Format : {"name": "orwhere/where", "condition": {"column2": "value2"}}
        :param order_by: Order the data
        :param columns: Specify which columns you want to select
        :param limit: Limit the number of rows returned
        :return: The data that is selected from the table
        :doc-author: Trelent
        """

        try:
            typedict = {
                "avg": self.average,
                "sum": self.sum,
                "min": self.min,
                "max": self.max,
                "cols": self.columns,
                "array_agg": self.array_agg,
                'all': self.all
            }
            return typedict[select_type](timerange, condition, order_by, group_by, columns, limit)
        except Exception as exp:
            log.error(f'Select data Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    # ------------------------------  Insert data to PS table ------------------------------ #

    def insert(self, dataset) -> bool:
        """
        The insert function takes a dataset as an argument. The dataset is a list of dictionaries, where each dictionary
        is one row in the table. The insert function will iterate over the rows and insert them into the database.

        :param dataset:
        :param self: Reference the class instance
        :return: The number of rows inserted
        :doc-author: Trelent
        """
        try:
            db2 = create_engine(connection)
            source_metadata = MetaData(db2)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            insert_stmt = insert(tbl).values(dataset)
            # checking if any unique index is available in table
            if self.check_unique(TBL_NAME):
                # on conflict update data to new
                insert_stmt = insert_stmt.on_conflict_do_update(index_elements=[tbl.c.date_time, tbl.c.c3],
                                                                set_=insert_stmt.excluded)
            with db2.connect() as conn:
                conn.execute(insert_stmt)
            return True

        except Exception as exp:
            log.error(f'Insert Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    # ------------------------------  Delete data from PS table ------------------------------ #
    def delete(self, where) -> bool:
        """
        The delete function is used to delete data from the Postgres table.
        It takes in a dictionary as an argument, where the keys are column names and values are row values.
        If no condition is specified, it will delete all rows from the table.
        
        :param self: Access variables that belongs to the class
        :param where: Specify the condition of the data that needs to be deleted
        :return: True if the data is deleted else false
        :doc-author: Trelent
        """

        try:
            dbengine = create_engine(connection)
            source_metadata = MetaData(dbengine)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            query = tbl.delete()
            if where:
                for data in where:
                    query = query.where(and_(column(data) == where[data]))
                with dbengine.connect() as conn:
                    conn.execute(query)
                return True

            print("Condition is missing.")
            return False

        except Exception as exp:
            log.error(f'Delete Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    # --------------------------------Sub Functions[Avg | SUM | ALL | Cols]---------------------------------- #
    # average : Select Average of values
    # sum : Select sum of values
    # all : Select All Data
    # columns : Select Specific Columns
    # min : Select minimum value
    # max : Select maximum value
    # arr_agg : Select Array Aggregate of values
    def average(self, *args) -> list:
        """
        The average function is used to get the average of a column in the database.
        It takes in 4 parameters: timerange, where and orwhere.
        start and end are strings that represent dates in YYYY-MM-DD format.
        where is a dictionary containing columns as keys and values as values for those columns.
        orwhere is also a dictionary containing columns as keys and values for those columns.

        :param timerange: Specify the time range that you want to select 
        Format : {"start":"2022-11-01 12:00:00","end":"2022-11-02 12:00:00"}
        :param condition: Filter the data
        Format : {"name": "orwhere/where", "condition": {"column2": "value2"}}
        :param order_by:
        :param group_by:
        :param columns:
        :param limit:
        :param self: Access variables that belongs to the class
        :return: The average value of the values' column
        :doc-author: Trelent
        """
        timerange = args[0]
        condition = args[1]
        order_by = args[2]
        group_by = args[3]
        columns = args[4]
        limit = args[5]
        if condition:
            where = condition["condition"] if condition["name"] == "where" else {}
            orwhere = condition["condition"] if condition["name"] == "orwhere" else {}
        if timerange:
            start = timerange["start"]
            end = timerange["end"]
        try:
            engine = create_engine(connection)
            source_metadata = MetaData(engine)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            lists = [func.avg(tbl.c.value), column(group_by) if group_by else None]
            if columns:
                for col in columns:
                    lists.append(column(col))

            query = select(lists)
            if where:
                query = query.where(and_(column(data) == where[data] for data in where))
            if orwhere:
                query = query.where(or_(column(data) == orwhere[data] for data in orwhere))
            if start and end:
                query = query.where(and_(tbl.c.date_time.between(start, end)))
            if order_by:
                query = query.order_by(
                    column(order_by[0]).asc() if order_by[1] == "asc" else column(order_by[0]).desc())
            if group_by:
                query = query.group_by(column(group_by))
            if limit:
                query = query.limit(limit[0])
                try:
                    query = query.offset(limit[1])
                except IndexError:
                    return []
            with engine.connect() as conn:
                result = conn.execute(query).fetchall()
                list_of_results = [list(tup) for tup in result]
                return list_of_results
        except Exception as exp:
            log.error(f'Select data Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    def sum(self, *args) -> list:
        """
        The sum function takes a column name and returns the sum of all values in that column.
        The function can also take an optional start parameter, which will be used to filter the results by date_time greater than or equal to it.
        Similarly, end is another optional parameter that allows you to filter by date_time less than or equal to it.

        :param self: Access variables that belongs to the class
        :param timerange: Filter the data between a time range
                Format : {"start":"2022-11-01 12:00:00","end":"2022-11-02 12:00:00"}
        :param condition: Filter the data
                Format : {"name": "orwhere/where", "condition": {"column2": "value2"}}
        :param order_by: Order the results by a particular column
        :param group_by: Group the results by a column
        :param columns: Select the columns that you want to return
        :param limit: Limit the number of results returned
        :return: The sum of the values in a column
        :doc-author: Trelent
        """
        timerange = args[0]
        condition = args[1]
        order_by = args[2]
        group_by = args[3]
        columns = args[4]
        limit = args[5]

        if condition:
            where = condition["condition"] if condition["name"] == "where" else {}
            orwhere = condition["condition"] if condition["name"] == "orwhere" else {}
        if timerange:
            start = timerange["start"]
            end = timerange["end"]
        try:
            engine = create_engine(connection)
            source_metadata = MetaData(engine)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            lists = [func.sum(tbl.c.value), column(group_by) if group_by else None]
            if columns:
                for col in columns:
                    lists.append(column(col))

            query = select(lists)
            if where:
                query = query.where(and_(column(data) == where[data] for data in where))
            if orwhere:
                query = query.where(or_(column(data) == orwhere[data] for data in orwhere))
            if start and end:
                query = query.where(and_(tbl.c.date_time.between(start, end)))
            if order_by:
                query = query.order_by(
                    column(order_by[0]).asc() if order_by[1] == "asc" else column(order_by[0]).desc())
            if group_by:
                query = query.group_by(column(group_by))
            if limit:
                query = query.limit(limit[0])
                try:
                    query = query.offset(limit[1])
                except IndexError:
                    return []
            with engine.connect() as conn:
                result = conn.execute(query).fetchall()
                list_of_results = [list(tup) for tup in result]
                return list_of_results
        except Exception as exp:
            log.error(f'Select data Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    def all(self, *args) -> list:
        """
        The all function is used to get all the data from the database.


        :param timerange: Filter the data between a time range
                Format : {"start":"2022-11-01 12:00:00","end":"2022-11-02 12:00:00"}
        :param condition: Filter the data
                Format : {"name": "orwhere/where", "condition": {"column2": "value2"}}
        :param order_by: Order the data by a column
        :param group_by: Group the results by a column
        :param columns: Add extra column name to be fetched
        :param limit: Limit the number of rows returned
        :return: A list of average datas based on conditions
        :doc-author: Trelent
        """
        timerange = args[0]
        condition = args[1]
        order_by = args[2]
        group_by = args[3]
        columns = args[4]
        limit = args[5]

        if condition:
            where = condition["condition"] if condition["name"] == "where" else {}
            orwhere = condition["condition"] if condition["name"] == "orwhere" else {}
        if timerange:
            start = timerange["start"]
            end = timerange["end"]
        try:
            engine = create_engine(connection)
            source_metadata = MetaData(engine)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            lists = [tbl.c.value, column(group_by) if group_by else None]
            if columns:
                for col in columns:
                    lists.append(column(col))

            query = select(lists)
            if where:
                query = query.where(and_(column(data) == where[data] for data in where))
            if orwhere:
                query = query.where(or_(column(data) == orwhere[data] for data in orwhere))

            if start and end:
                query = query.where(and_(tbl.c.date_time.between(start, end)))
            if order_by:
                query = query.order_by(
                    column(order_by[0]).asc() if order_by[1] == "asc" else column(order_by[0]).desc())
            if group_by:
                query = query.group_by(column(group_by))
            if limit:
                query = query.limit(limit[0])
                try:
                    query = query.offset(limit[1])
                except IndexError:
                    return []
            with engine.connect() as conn:
                result = conn.execute(query).fetchall()
                list_of_results = [list(tup) for tup in result]
                return list_of_results
        except Exception as exp:
            log.error(f'Select data Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    def columns(self, *args) -> list:
        """
        The columns function takes in a list of column names and returns the data from those columns.
        The function also allows for filtering, sorting, grouping and limiting.


        :param self: Access variables that belongs to the class
        :param timerange: Select the data between a specific time range
            Format : {"start":"2022-11-01 12:00:00","end":"2022-11-02 12:00:00"}
        :param condition: Filter the data
            Format : {"name": "orwhere/where", "condition": {"column2": "value2"}}
        :param order_by: Sort the data
        :param group_by: Group the data by a column
        :param columns: Specify the columns that you want to fetch
        :param limit: Limit the number of rows returned
        :return: A list of columns
        :doc-author: Trelent
        """
        timerange = args[0]
        condition = args[1]
        order_by = args[2]
        group_by = args[3]
        columns = args[4]
        limit = args[5]

        if condition:
            where = condition["condition"] if condition["name"] == "where" else {}
            orwhere = condition["condition"] if condition["name"] == "orwhere" else {}
        if timerange:
            start = timerange["start"]
            end = timerange["end"]
        try:
            engine = create_engine(connection)
            source_metadata = MetaData(engine)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            lists = []
            for col in columns:
                lists.append(column(col))
            query = select(lists)
            if where:
                query = query.where(and_(column(data) == where[data] for data in where))
            if orwhere:
                query = query.where(or_(column(data) == orwhere[data] for data in orwhere))
            if start and end:
                query = query.where(and_(tbl.c.date_time.between(start, end)))
            if order_by:
                query = query.order_by(
                    column(order_by[0]).asc() if order_by[1] == "asc" else column(order_by[0]).desc())
            if group_by:
                query = query.group_by(column(group_by))
            if limit:
                query = query.limit(limit[0])
                try:
                    query = query.offset(limit[1])
                except IndexError:
                    return []
            with engine.connect() as conn:
                result = conn.execute(query).fetchall()
                list_of_results = [list(tup) for tup in result]
                return list_of_results
        except Exception as exp:
            log.error(f'Select data Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    def min(self, *args) -> list:
        """
        The min function returns the minimum value of a column in a table.
        The function takes up to three arguments:
            1) The name of the table to query.
            2) A filter condition that specifies which rows should be included in the result set.
               This argument is optional, and if omitted all rows will be included in the result set.

        :param self: Access variables that belongs to the class
        :param timerange: Specify the time range that you want to select
                Format : {"start":"2022-11-01 12:00:00","end":"2022-11-02 12:00:00"}
        :param condition: Filter the data
               Format : {"name": "orwhere/where", "condition": {"column2": "value2"}}
        :param order_by: Sort the data in ascending or descending order
        :param group_by: Group the data by a column
        :param columns: Fetch extra columns
        :param limit: Limit the number of rows returned
        :return: The minimum value of the column specified in the query
        :doc-author: Trelent
        """
        timerange = args[0]
        condition = args[1]
        order_by = args[2]
        group_by = args[3]
        columns = args[4]
        limit = args[5]

        if condition:
            where = condition["condition"] if condition["name"] == "where" else {}
            orwhere = condition["condition"] if condition["name"] == "orwhere" else {}
        if timerange:
            start = timerange["start"]
            end = timerange["end"]
        try:
            engine = create_engine(connection)
            source_metadata = MetaData(engine)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            lists = [func.min(tbl.c.value), column(group_by) if group_by else None]
            if columns:
                for col in columns:
                    lists.append(column(col))

            query = select(lists)
            if where:
                query = query.where(and_(column(data) == where[data] for data in where))
            if orwhere:
                query = query.where(or_(column(data) == orwhere[data] for data in orwhere))
            if start and end:
                query = query.where(and_(tbl.c.date_time.between(start, end)))
            if order_by:
                query = query.order_by(
                    column(order_by[0]).asc() if order_by[1] == "asc" else column(order_by[0]).desc())
            if group_by:
                query = query.group_by(column(group_by))
            if limit:
                query = query.limit(limit[0])
                try:
                    query = query.offset(limit[1])
                except IndexError:
                    return []
            with engine.connect() as conn:
                result = conn.execute(query).fetchall()
                list_of_results = [list(tup) for tup in result]
                return list_of_results
        except Exception as exp:
            log.error(f'Select data Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    def max(self, *args) -> list:
        """
        The max function is used to get the maximum value of a column based on conditions.
        The function takes in 6 parameters: timerange, condition, order_by and group_by.
        start and end are strings that represent the time period for which data should be fetched.
        where is a dictionary that contains columns as keys and values as values for those columns.
        orwhere is also a dictionary with same format as where, but it only accepts one key-value pair per column name unlike where which can accept multiple pairs under one column name (column names are unique).  The function returns all results from max

        :param timerange: Specify the time range that you want to select 
        Format : {"start":"2022-11-01 12:00:00","end":"2022-11-02 12:00:00"}
        :param condition: Filter the data
        Format : {"name": "orwhere/where", "condition": {"column2": "value2"}} 
        :param self: Access variables that belongs to the class
        :param order_by: Sort the result
        :param group_by: Group the data by a column
        :param columns: Fetch extra columns
        :param limit: Limit the number of rows returned
        :return: The maximum value of the specified column in a table
        :doc-author: Trelent
        """
        timerange = args[0]
        condition = args[1]
        order_by = args[2]
        group_by = args[3]
        columns = args[4]
        limit = args[5]

        if condition:
            where = condition["condition"] if condition["name"] == "where" else {}
            orwhere = condition["condition"] if condition["name"] == "orwhere" else {}
        if timerange:
            start = timerange["start"]
            end = timerange["end"]
        try:
            engine = create_engine(connection)
            source_metadata = MetaData(engine)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            lists = [func.max(tbl.c.value), column(group_by) if group_by else None]
            if columns:
                for col in columns:
                    lists.append(column(col))

            query = select(lists)
            if where:
                query = query.where(and_(column(data) == where[data] for data in where))
            if orwhere:
                query = query.where(or_(column(data) == orwhere[data] for data in orwhere))
            if start and end:
                query = query.where(and_(tbl.c.date_time.between(start, end)))
            if order_by:
                query = query.order_by(
                    column(order_by[0]).asc() if order_by[1] == "asc" else column(order_by[0]).desc())
            if group_by:
                query = query.group_by(column(group_by))
            if limit:
                query = query.limit(limit[0])
                try:
                    query = query.offset(limit[1])
                except IndexError:
                    return []
            with engine.connect() as conn:
                result = conn.execute(query).fetchall()
                list_of_results = [list(tup) for tup in result]
                return list_of_results
        except Exception as exp:
            log.error(f'Select data Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException

    def array_agg(self, *args) -> list:
        """
        Sub Function for getting group datas in List.

        :return:
        :param condition: Filter the data
        Format : {"name": "orwhere/where_and", "condition": {"column2": "value2"}}
        :param timerange: Specify the time range that you want to select 
        Format : {"start":"2022-11-01 12:00:00","end":"2022-11-02 12:00:00"}
        :param order_by: (List) Order By Column Name ASC/DESC.
            -- Format : ["column_name","desc"]
        :param group_by: (String) Group By Column Name
        :param columns: (List) Add extra Column Name to be fetched.
            -- Format : ["column_1","column_2","column_3"]
        :param limit: (List) For adding Limit.
            -- Format : [limit,offset]
        :return: List of group datas based on conditions.
        """
        timerange = args[0]
        condition = args[1]
        order_by = args[2]
        group_by = args[3]
        columns = args[4]
        limit = args[5]

        if condition:
            where_and = condition["condition"] if condition["name"] == "where" else {}
            where_or = condition["condition"] if condition["name"] == "orwhere" else {}
        if timerange:
            start = timerange["start"]
            end = timerange["end"]
        try:
            engine = create_engine(connection)
            source_metadata = MetaData(engine)
            tbl = Table(TBL_NAME, source_metadata, autoload=True)
            lists = [func.array_agg(array([tbl.c.value, tbl.c.time_stamp])),
                     column(group_by) if group_by else None]
            if columns:
                for col in columns:
                    lists.append(column(col))

            query = select(lists)
            if where_and:
                query = query.where(and_(column(data) == where_and[data] for data in where_and))
            if where_or:
                query = query.where(or_(column(data) == where_or[data] for data in where_or))
            if start and end:
                query = query.where(and_(tbl.c.date_time.between(start, end)))
            if order_by:
                query = query.order_by(
                    column(order_by[0]).asc() if order_by[1] == "asc" else column(order_by[0]).desc())
            if group_by:
                query = query.group_by(column(group_by))
            if limit:
                query = query.limit(limit[0])
                try:
                    query = query.offset(limit[1])
                except IndexError:
                    log.error(f'Select data Error : {str(IndexError)}', exc_info=True)
                    return []
            print(query)
            with engine.connect() as conn:
                result = conn.execute(query).fetchall()
                list_of_results = [list(tup) for tup in result]
                return list_of_results
        except Exception as exp:
            log.error(f'Select data Error : {str(exp)}', exc_info=True)
            raise TimeScaleUtilsException
