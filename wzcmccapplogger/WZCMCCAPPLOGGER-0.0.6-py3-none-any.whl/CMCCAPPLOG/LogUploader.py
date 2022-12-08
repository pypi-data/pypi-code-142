import redis
import pyodbc

class Obdcsql(object):

    def __init__(self, server, uid, pwd, database):

        # 数据库连接
        odbc = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (
            server, database, uid, pwd)
        self.db = pyodbc.connect(odbc)
        # 使用 cursor（）方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        # 使用 fetchone（）方法获取单条数据
    # 数据库插入
    def insert_record(self, sql):
        # SQL 插入语句
        try:
            # 执行 SQL 语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            # print('插入成功')
            return [True]
        # 捕获与数据库相关的错误
        except pyodbc.Error as err:
            # print(f'插入失败, CASE:{err}')
            # print(sql)
            # 如果发生错误就回滚
            self.db.rollback()
            print('插入失败' + str(err))
            raise err
            return [False]

    def update_record(self, sql, values):
        # SQL 插入语句
        try:
            # 执行 SQL 语句
            self.cursor.execute(sql, values)
            # 提交到数据库执行
            self.db.commit()
            # print('插入成功')
            return [True]
        # 捕获与数据库相关的错误
        except pyodbc.Error as err:

            # print(f'插入失败, CASE:{err}')
            # print(sql)
            # 如果发生错误就回滚
            self.db.rollback()
            print('更新失败' + str(err))
            raise err
            return [False]

    # 数据库删除
    def delete_record(self, sql):
        # SQL 删除语句
        try:
            # 执行 SQL 语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            # print('删除成功.')
            return [True]
        # 捕获与数据库相关的错误
        except pyodbc.Error as err:
            # print(f'删除失败, CASE:{err}')
            # 如果发生错误就回滚
            self.db.rollback()
            return [False]

    # 数据库查询
    def query_record(self, sql):
        # SQL 查询语句
        try:
            # 执行 SQL 语句
            self.cursor.execute(sql)
            '''
            fetchone()：该方法获取下一个查询结果集，结果集是一个对象。
            fetchall()：接收全部返回结果行。
            rowcount：返回执行 execute（）方法后影响的行数
            '''
            # 获取所有记录列表
            results = self.cursor.fetchall()
            # print('查询成功')
            return [True, results]
        # 捕获与数据库相关的错误
        except pyodbc.Error as err:
            print(f'查询失败, CASE:{err}')
            return [False]

    def quit(self):
        self.db.close()
