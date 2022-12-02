import pymysql
from timeit import default_timer
from global_var import *



# def get_connection():
#      conn = pymysql.connect(host=host,port=port,user=user,password=paword,database=db)
#      return conn

    # ---- 使用 with 的方式来优化代码
class MysqlManager(object):

    def __init__(self, charset='utf8'):
        self.__db = MYSQLBASE
        self.__user = MYSQLUSER
        self.__passwd = MYSQLPWD
        self.__host = MYSQLIP
        self.__port = MYSQLPORT
        self.__charset = charset
        self.__connect = None
        self.__cursor = None

    def connect_db(self):
        """
        dbManager._connect_db()
        连接数据库
        :return:
        """
        params = {
            "db": self.__db,
            "user": self.__user,
            "passwd": self.__passwd,
            "host": self.__host,
            "port": self.__port,
            "charset": self.__charset
        }
        self.__connect = pymysql.connect(**params)
        self.__cursor = self.__connect.cursor()

    def Close_DB(self):
        """
        dbManager._close_db()
        :return:
        """
        self.__cursor.close()
        self.__connect.close()


    def insert_one(self,sql):
        self.connect_db()
        self.__cursor.execute(sql)
        # print(self.__cursor.execute(sql))
        self.__connect.commit()
        last_id = self.__connect.insert_id()
        return last_id
        self.Close_DB()

    def delect_one(self,sql):
        self.connect_db()
        self.__cursor.execute(sql)
        self.__connect.commit()
        data = self.__cursor.fetchall()
        # print('data',data)
        return data
        self.Close_DB()


    def update_one(self,sql):
        self.connect_db()
        count = self.__cursor.execute(sql)
        return count
        self.Close_DB()

    def find_one(self,sql):
        self.connect_db()
        self.__cursor.execute(sql)
        self.__connect.commit()
        data = self.__cursor.fetchone()
        print(data)
        return data
        self.Close_DB()

mq = MysqlManager()
# select * from tablename where id =1
# insert into tablename(字段名,字段名...) values(值,值...)
# delect from tablename where id = 1
# update tablename set name = 'xx' where id =1
def tongyongMYSql(sqls):
    for oneSql in str(sqls)[0:-1].split("&&"):
        print("**************************************************************")
        way = str(oneSql.split(" ")[0])
        print("对数据库操作方法：   ", way)
        if way == "INSERT":
            mq.insert_one(oneSql)
            print("执行 insert_one 操作")
        if way == "DELETE":
            mq.delect_one(oneSql)
            print("执行 delect_one 操作")
        if way == "SELECT":
            result = mq.find_one(oneSql)
            return result
            print("执行 find_one 操作")
        if way == "UPDATE":
            mq.update_one(oneSql)
            print("执行 update_one 操作")




if __name__ == '__main__':

    # db = MysqlManager()
    # db.find_one(sql="select * from supplier")
    # sqls = "SELECT * FROM burying_points WHERE event_id = 'X001001'&&SELECT * FROM data_server "
    # sqls = "INSERT INTO burying_points (id, event_id, event_type, para1, para2, para3, para4, para5, create_by, create_time, update_by, update_time) VALUES ('5102', 'testX001001', 'click', '03', NULL, NULL, NULL, NULL, NULL, '2021-06-02 10:59:00', NULL, NULL);"
    sqls = f"SELECT * FROM sys_group WHERE group_name = 'autoGroup';"
    a = tongyongMYSql(sqls)
    print(a)









