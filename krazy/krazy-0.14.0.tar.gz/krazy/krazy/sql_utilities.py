import numpy as np
import pandas as pd
import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def get_table_list(conn:pyodbc.connect)->list:
    '''
    get list of tables and returns a list with success boolean
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
    get names of columns in a tablle along with success boolean
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
    Delete a tables from list of tables and returns list of list:
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
    deletes all tables in the database and returns list of tables deleted
    '''
    table_list = get_table_list(conn)
    response = del_table(conn, table_list)
    return response

def empty_tables(conn: sqlite3.connect)->list:
    '''
    Delete all records from all tables and returns success boolean as list
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
    compresses the database
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
