import pandas as pd 
import sqlite3


def read(path):
    con=sqlite3.connect(path)
    return con

def list_tables(con):
    cur=con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cur.fetchall()

def display_table(table,con):
    cursor=con.cursor()
    cursor.execute('SELECT * FROM {}'.format(table))
    index= [i[0] for i in cursor.description]
    dataframe=pd.DataFrame(cursor.fetchall(),columns=index)
    return dataframe.set_index(dataframe.columns[0])


def ExecuteScriptsFromFile(filepath, connessione):
    fd = open(filepath, 'r')
    sql = fd.read()
    fd.close()
    one=''.join(sql.split('\n'))
    reso=[x +';' for x in one.split(';')]
    reso.pop(-1)
    for i,x in enumerate(reso):
        try:
            cursor=connessione.cursor()
            cursor.execute(x)
            cursor.close()
        except:
            print(f'Error at Line {i}')
