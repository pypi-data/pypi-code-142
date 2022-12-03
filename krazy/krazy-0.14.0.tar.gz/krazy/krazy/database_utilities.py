import sqlite3
import numpy as np
import pandas as pd
import pyodbc
import configparser
import sqlalchemy as sa
import urllib

def get_table_list(conn:sqlite3.connect)->list:
    '''
    get list of tables from sqlite3 db and returns a list with success boolean
    '''
    cur = conn.cursor()
    try:
        table_names = cur.execute("Select name from sqlite_master where type='table';")
        response_list = list(table_names.fetchall())
        table_list = []
        for table in response_list:
            table_list.append(table[0])
        return [True, table_list]

    except Exception as err:
        return (False, err)


def get_col_names(conn:sqlite3.connect, table:str)->list:
    '''
    get names of columns in a table along with success boolean from sqlite3 db
    '''
    cur = conn.cursor()
    try:
        cur.execute(f'Select * from {table};')
        names = np.array(cur.description)[:,0]
        return [True, names]

    except Exception as err:
        return [False, err]

def del_table(conn: sqlite3.connect, tables:list)->list:
    '''
    Delete a tables from sqlite3 db from list of tables and returns list of list:
    [deleted_tables, failed_tables]
    '''
    cur = conn.cursor()
    deleted_tables = []
    failed_tables = []

    for table in tables:
        try:
            cur.execute(f'Drop table {table};')
            conn.commit()
            deleted_tables.append(table)

        except Exception as err:
            return failed_tables.append([table, err])
    
    return [deleted_tables, failed_tables]

def del_table_all(conn: sqlite3.connect)->list:
    '''
    deletes all tables in sqlite3 db and returns list of tables deleted
    '''
    table_list = get_table_list(conn)
    response = del_table(conn, table_list)
    return response

def empty_tables(conn: sqlite3.connect)->list:
    '''
    Delete all records from all tables from sqlite3 db and returns success boolean as list
    '''
    tables_emptied = []
    cur = conn.cursor()
    table_list = get_table_list(conn)
    for table in table_list:
        cur.execute(f'Delete from {table};')
        tables_emptied.append(table)
    
    conn.commit()

    return [True, tables_emptied]

def database_repair(conn):
    '''
    compresses the sqlite3 db
    '''
    conn.execute('VACUUM')

def dtype_to_df(df: pd.DataFrame)->None:
    '''
    Accepts a dataframe and returns df containing column dtypes
    '''
    df_cols = pd.DataFrame(columns=['Type'], data=df.dtypes)
    df_cols.index.name = 'Col'
    df_cols.reset_index(inplace=True)
    return df_cols

# MS Sql erver related code below _____________________________

def connection_pyodbc(config_file_path)->pyodbc.connect:
    '''
    takes path to config file and connects to MS SQL server and returns pyodbc connection
    '''
    # read server config file
    config = configparser.ConfigParser()
    try:
        config.read(config_file_path)
        server = config['server_config']['server']
        database = config['server_config']['database']
        username = config['server_config']['username']
        password = config['server_config']['password']

        # connect to MS Sql Server

        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        conn = pyodbc.connect("Driver=SQL Server;Server="+server+";Database="+database+";uid="+username+";pwd="+password)

        return conn

    except Exception as err:
        print('Connection failure')
        print(err)
        return False

def connection_sqlalchemy(config_file_path)->sa.engine:
    '''
    takes path to config file and connects to MS SQL server and returns sqlalchemy connection
    '''
    # read server config file
    config = configparser.ConfigParser()
    try:
        config.read(config_file_path)
        server = config['server_config']['server']
        database = config['server_config']['database']
        username = config['server_config']['username']
        password = config['server_config']['password']
        
        # connect to MS Sql Server
        
        # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
        conn = "Driver=SQL Server;Server="+server+";Database="+database+";uid="+username+";pwd="+password
        conn = urllib.parse.quote_plus(conn)
        engine = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))
        
        return engine
    
    except Exception as err:
        print('Connection failure')
        print(err)
        return False
    
def get_table_names(conn, conn_type:str='sqlalchemy'):
    '''
    Get all tables names from MS SQL Server
    '''

    if conn_type == 'pyodbc':
        cursor = conn.cursor()
        table_list = []
        for row in cursor.tables():
            table_list.append(row.table_name)
        return table_list
    
    elif conn_type == 'sqlalchemy':
        table_list = sa.inspect(conn).get_table_names()
        return table_list
    
    else:
        return None

def table_search(table_name: str, conn, conn_type:str='sqlalchemy')->list:
    '''
    Searches for given table name in tables on MS SQL Server
    '''
    if conn_type=='pyodbc':
        table_names = get_table_names(conn, 'pyodbc')
    elif conn_type=='sqlalchemy':
        table_names=get_table_names(conn)
    else:
        table_names=False
    
    if table_name:
        srch_results = []
        for name in table_names:
            if table_name in name.lower():
                srch_results.append(name)
        return srch_results
    else:
        return None

def table_delete(table_name, conn:pyodbc.connect)->bool:
    '''
    Deletes given tabe on MS SQL Server
    '''
    table_list = table_search(table_name, conn, 'pyodbc')
    if table_name in table_list:
        cur = conn.cursor()
        cur.execute(f'Drop table {table_name};')
        conn.commit()
        return True
    else:
        return False