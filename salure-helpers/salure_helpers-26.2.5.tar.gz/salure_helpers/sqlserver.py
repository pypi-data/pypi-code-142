import ast
import json
import math
import time
from typing import Union

import pandas as pd
import pymysql
import warnings
from datetime import datetime


class SQLServer:

    def __init__(self, host, user, password, database, port=1433, debug=False):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.debug = debug

    def raw_query(self, query, insert=False):
        start = time.time()
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.execute(query)
        if insert:
            connection.commit()
            data = '{0} - Writing data took {1} seconds'.format(time.strftime('%H:%M:%S'), time.time() - start)
        else:
            data = cursor.fetchall()
        connection.close()
        return data

    def update(self, table: str, columns: list, values: list, filter=''):
        start = time.time()
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        update_values = ''

        def __map_strings(item):
            if isinstance(item, str):
                return '"' + str(item) + '"'
            elif isinstance(item, datetime):
                return '"' + item.strftime("%Y-%m-%d %H:%M:%S") + '"'
            else:
                return str(item)

        for index in range(len(columns)):
            if index != len(columns) - 1:
                update_values += "`{}` = {},".format(columns[index], __map_strings(values[index]))
            else:
                update_values += "`{}` = {}".format(columns[index], __map_strings(values[index]))
        update_values = update_values.replace('None', 'DEFAULT')
        query = "UPDATE `{}` SET {} {};".format(table, update_values, filter)
        if self.debug:
            print(query)
        cursor.execute(query)
        connection.commit()
        data = '{0} - Updating data took {1} seconds'.format(time.strftime('%H:%M:%S'), time.time() - start)
        connection.close()
        return data

    def select(self, table, selection, filter=''):
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
        cursor = connection.cursor()
        cursor.arraysize = 10000
        query = f"SELECT {selection} FROM {table} {filter}"
        if self.debug:
            print(query)
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return list(data)

    def insert(self, table: str, df: pd.DataFrame, columns: list = None, return_queries: bool = False) -> Union[list, str]:
        queries = []
        for i in range(math.ceil(len(df.index) / 1000)):
            # Split df in batches because you can insert maximum of 1000 rows in sql server at once
            df_batch = df[0 + i * 1000: 1000 + i * 1000]
            columns = columns if columns else ', '.join(str(column) for column in df_batch.columns)
            values = ', '.join(str(index[1:]) for index in df_batch.itertuples())
            values = values.replace('None', 'DEFAULT')
            values = values.replace('NaT', 'NULL')
            values = values.replace('nan', 'NULL')
            values = values.replace("'NULL'", "NULL")
            values = values.replace('"', "'")
            values = values.replace("\\\\'", "''")
            queries.append(f"""INSERT INTO {table} ({columns}) VALUES {values}""")

        if return_queries:
            return queries
        else:
            start = time.time()
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)
            cursor = connection.cursor()
            for query in queries:
                cursor.execute(query)
            connection.commit()
            connection.close()
            return '{0} - Writing data took {1} seconds'.format(time.strftime('%H:%M:%S'), time.time() - start)

