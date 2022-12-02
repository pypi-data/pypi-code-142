# # -*- encoding: utf-8 -*-
# """
# @File     :   monogo_connection.py
# @Time     :   2021/5/20 10:33 上午
# @Author   :   Yutong Qian
# @Version  :   1.0
# @Contact  :   15868191756@163.com
# @Desc     :   阿里云数据库连接
#
# """
# from pymongo import MongoClient
# from global_var import *
# from util.json_util import *
# import json
# from bson import objectid
# import datetime
#
#
# class MongoDB(object):
#
#     def __init__(self):
#         self.mongo_host = MONGOIP
#         self.mongo_db = MONOGOBASE
#         self.mongo_port = MONGOPORT
#         self.username = MONGOUSER
#         self.password = MONGOPWD
#         self.mongo_url = 'mongodb://'+ MONGOIP + ':'+ str(MONGOPORT)
#         # self.mongo_host = '10.0.40.62'
#         # self.mongo_db = 'yk_base'
#         # self.mongo_port = 20000
#         # self.username = 'Hik706706'
#         # self.password = 'Alibaba&Cetiti'
#         try:
#             # client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
#             #单机连接
#             # self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port, username=self.username, password=self.password)
#             self.client = MongoClient(self.mongo_url,
#                                       port=self.mongo_port,
#                                       username=self.username,
#                                       password=self.password,
#                                       authSource='admin',
#                                       directConnection=True,
#                                       authMechanism='SCRAM-SHA-1'
#                                       )
#             # self.adb = self.client.get_database('admin')
#             self.db = self.client.get_database(self.mongo_db)
#             # self.db.authenticate('Hik706706', 'Alibaba&Cetiti')
#         except SystemError:
#             print("monogo Connection FAILED:(")
#
#     # def db_connect(self):
#     #     self.db = self.client[MONOGOBASE]
#     #     return self.db
#
#     def find_one_(self,mongo_collection, condition):
#         """数据读取"""
#         # db = get_conn()
#         self.collection = self.db.get_collection(mongo_collection)
#         self.data = self.collection.find_one(condition)
#         # print("数据库查询结果",self.data)
#         return self.data
#
#     def insert_one_(self,mongo_collection, result):
#         """单条数据插入"""
#         # db = get_conn()
#         # db = MC.db_connect()
#         # print('db',db)
#         try:
#             self.collection = self.db.get_collection(mongo_collection)
#             print('collection', self.collection)
#             self.collection.insert_one(result)
#             print('collection.insert_one(result)', self.collection.insert_one(result))
#         except Exception as e:
#             pass
#
#     def insert_many_(self,mongo_collection, result):
#         """批量数据插入"""
#         # db = get_conn()
#         self.collection = self.db.get_collection(mongo_collection)
#         self.collection.insert_many(result)
#
#     def delete_one_(self,mongo_collection, result):
#         """单条数据删除"""
#         # db = get_conn()
#         self.collection = self.db.get_collection(mongo_collection)
#         self.collection.delete_one(result)
#
#     def update_one_(self,mongo_collection, result):
#         """更新一条数据库"""
#         # db = get_conn()
#         self.collection = self.db.get_collection(mongo_collection)
#         self.collection.update_one(result)
#
#     def update_many_(self,mongo_collection, result):
#         """更新多条数据库"""
#         # db = get_conn()
#         self.collection = self.db.get_collection(mongo_collection)
#         self.collection.update_many(result)
#
#     def get_collection(self):
#         """获取所有数据库"""
#         return self.db.list_collection_names()
#
#     def close_connect(self):
#         try:
#             self.client.close()
#             logging.info("MongoDB连接已关闭")
#         except Exception as e:
#             logging.info("MongoDB连接已关闭失败")
#             return None
#
#
#
#
#
# MC = MongoDB()
# # def get_conn():
# #     """获取数据库连接"""
# #     return MC.db_connect()
#
# def tongyongSql(sqls):
#     for oneSql in str(sqls)[0:-1].split("&&"):
#         # print("原始sql语句：\n",oneSql)
#         print("**************************************************************")
#         #print("按照进行分割:\n"+ str(oneSql.split(".")))
#         tableName = str(oneSql.split(".")[1])
#         print("需要操作的表名字：   ", tableName)
#         # 获取数据库执行方式
#         way = str(oneSql.split(".")[2]).split("(")[0]
#         print("对数据库操作方法：   ", way)
#         # 获取json 构建dict
#         sql1 = "{" + oneSql.split("({")[1]
#         # print("sql1:", sql1)
#         sql2 = sql1.split(')')[0]
#         # sql =sql1
#         sql = json.loads(sql2)
#         print("sql:", sql)
#         print("sql", type(sql))
#         for key in  sql:
#             # print('key',key)
#             if key == '_id':
#                 a = sql[key]
#                 sql[key] = objectid.ObjectId(a)
#             t = ['createTimestamp','updateTimestamp','timeStamp','loginTime','validateDate','lastModifyPasswordTime','lastLoginTime']
#             for i in t:
#                 i = str(i)
#                 if i in key:
#                 # a = sql[key]
#                  sql[key] = datetime.datetime.now()-datetime.timedelta(days=1)
#             # if 'timeStamp' in key:
#             #     # a = sql[key]
#             #     sql[key] = datetime.datetime.now()
#                 # print('sql[key]',sql[key])
#         # sql = ast.literal_eval(sql1)
#         # jsonHandler = JsonHandler()
#         # sql = jsonHandler.json_to_dict(sql1)
#         print("sql:", sql)
#         print("数据库执行内容：   ", sql)
#         if way == "insertOne":
#             MC.insert_one_(tableName,sql)
#             print("执行 insertOne 操作")
#         if way == "insertMany":
#             MC.insert_many_(tableName,sql)
#             print("执行 insertMany 操作")
#         if way == "deleteOne":
#             MC.delete_one_(tableName,sql)
#             print("执行 deleteOne 操作")
#         if way == "find":
#             MC.find_one_(tableName,sql)
#             print("执行 find 操作")
#             return MC.find_one_(tableName,sql)
#         if way == "updateOne":
#             MC.update_one_(tableName,sql)
#             print("执行 updateOne 操作")
#         if way == "updateMany":
#             MC.update_one_(tableName,sql)
#             print("执行 updateOne 操作")
#
#
#
# if __name__ == "__main__":
#     MC = MongoDB()
#     print(MC.get_collection())
#     # sql = 'db.Company.find({"name":"testZyl"})'
#     # tongyongSql(sql)
#
#
#

# -*- encoding: utf-8 -*-
"""
@File     :   monogo_connection.py
@Time     :   2021/5/20 10:33 上午
@Author   :   Yutong Qian
@Version  :   1.0
@Contact  :   15868191756@163.com
@Desc     :   阿里云数据库连接

"""
from pymongo import MongoClient
from global_var import *
from util.json_util import *
import json
from bson import objectid
import datetime


class MongoDB(object):

    def __init__(self):
        self.mongo_host = MONGOIP
        # self.mongo_db = MONOGOBASE
        self.mongo_port = MONGOPORT
        self.username = MONGOUSER
        self.password = MONGOPWD
        self.mongo_url = 'mongodb://'+ MONGOIP + ':'+ str(MONGOPORT)
        # self.mongo_host = '10.0.40.62'
        # self.mongo_db = 'yk_base'
        # self.mongo_port = 20000
        # self.username = 'Hik706706'
        # self.password = 'Alibaba&Cetiti'
        try:
            # client = pymongo.MongoClient(self.mongo_host, self.mongo_port)
            #单机连接
            # self.client = pymongo.MongoClient(self.mongo_host, self.mongo_port, username=self.username, password=self.password)
            self.client = MongoClient(self.mongo_url,
                                      port=self.mongo_port,
                                      username=self.username,
                                      password=self.password,
                                      authSource='admin',
                                      directConnection=True,
                                      authMechanism='SCRAM-SHA-1'
                                      )
            # self.adb = self.client.get_database('admin')
            # self.db = self.client.get_database(self.mongo_db)
            # self.db.authenticate('Hik706706', 'Alibaba&Cetiti')
        except SystemError:
            print("monogo Connection FAILED:(")

    def db_connect(self,mongo_db=MONOGOBASE):
        self.db = self.client.get_database(mongo_db)
        return self.db

    def find_one_(self,mongo_collection, condition,mongo_db=MONOGOBASE):
        """数据读取"""
        db = self.db_connect(mongo_db)
        self.collection = self.db.get_collection(mongo_collection)
        self.data = self.collection.find_one(condition)
        # print("数据库查询结果",self.data)
        return self.data

    def insert_one_(self,mongo_collection, result,mongo_db=MONOGOBASE):
        """单条数据插入"""
        db = self.db_connect(mongo_db)
        # db = MC.db_connect()
        # print('db',db)
        try:
            self.collection = self.db.get_collection(mongo_collection)
            print('collection', self.collection)
            self.collection.insert_one(result)
            print('collection.insert_one(result)', self.collection.insert_one(result))
        except Exception as e:
            pass

    def insert_many_(self,mongo_collection, result,mongo_db=MONOGOBASE):
        """批量数据插入"""
        db = self.db_connect(mongo_db)
        self.collection = self.db.get_collection(mongo_collection)
        self.collection.insert_many(result)

    def delete_one_(self,mongo_collection, result,mongo_db=MONOGOBASE):
        """单条数据删除"""
        db = self.db_connect(mongo_db)
        self.collection = self.db.get_collection(mongo_collection)
        self.collection.delete_one(result)

    def update_one_(self,mongo_collection, result,mongo_db=MONOGOBASE):
        """更新一条数据库"""
        db = self.db_connect(mongo_db)
        self.collection = self.db.get_collection(mongo_collection)
        self.collection.update_one(result)

    def update_many_(self,mongo_collection, result,mongo_db=MONOGOBASE):
        """更新多条数据库"""
        db = self.db_connect(mongo_db)
        self.collection = self.db.get_collection(mongo_collection)
        self.collection.update_many(result)

    def get_collection(self,mongo_db):
        """获取所有数据库"""
        b = self.db_connect(mongo_db)
        return self.db.list_collection_names()

    def close_connect(self):
        try:
            self.client.close()
            logging.info("MongoDB连接已关闭")
        except Exception as e:
            logging.info("MongoDB连接已关闭失败")
            return None


MC = MongoDB()
# def get_conn():
#     """获取数据库连接"""
#     return MC.db_connect()

def tongyongSql(sqls):
    for oneSql in str(sqls)[0:-1].split("&&"):
        print("原始sql语句：\n",oneSql)
        print("**************************************************************")
        #print("按照进行分割:\n"+ str(oneSql.split(".")))
        try:
            mongo_db = str(oneSql.split(".")[-1])
            if mongo_db in MONOGOBASES :
                mongo_db1 = mongo_db
            else:
                mongo_db1 = MONOGOBASE
        except:
            pass
        print("需要操作的数据库：", mongo_db1)
        tableName = str(oneSql.split(".")[1])
        print("需要操作的表名字：   ", tableName)
        # 获取数据库执行方式
        way = str(oneSql.split(".")[2]).split("(")[0]
        print("对数据库操作方法：   ", way)
        # 获取json 构建dict
        sql1 = "{" + oneSql.split("({")[1]
        # print("sql1:", sql1)
        sql2 = sql1.split(')')[0]
        # sql =sql1
        sql = json.loads(sql2)
        print("sql:", sql)
        print("sql", type(sql))
        for key in  sql:
            # print('key',key)
            if key == '_id':
                a = sql[key]
                sql[key] = objectid.ObjectId(a)
            t = ['createTimestamp','updateTimestamp','timeStamp','loginTime','validateDate','lastModifyPasswordTime','lastLoginTime','startTime','endTime']
            for i in t:
                i = str(i)
                if i in key:
                # a = sql[key]
                 sql[key] = datetime.datetime.now()
            # if 'timeStamp' in key:
            #     # a = sql[key]
            #     sql[key] = datetime.datetime.now()
                # print('sql[key]',sql[key])
        # sql = ast.literal_eval(sql1)
        # jsonHandler = JsonHandler()
        # sql = jsonHandler.json_to_dict(sql1)
        print("sql:", sql)
        print("数据库执行内容：   ", sql)
        if way == "insertOne":
            MC.insert_one_(tableName,sql,mongo_db1)
            print("执行 insertOne 操作")
        if way == "insertMany":
            MC.insert_many_(tableName,sql,mongo_db1)
            print("执行 insertMany 操作")
        if way == "deleteOne":
            MC.delete_one_(tableName,sql,mongo_db1)
            print("执行 deleteOne 操作")
        if way == "find":
            find_data = MC.find_one_(tableName,sql,mongo_db1)
            print("执行 find 操作")
            return find_data
        if way == "updateOne":
            MC.update_one_(tableName,sql,mongo_db1)
            print("执行 updateOne 操作")
        if way == "updateMany":
            MC.update_one_(tableName,sql,mongo_db1)
            print("执行 updateOne 操作")



if __name__ == "__main__":
    # MC = MongoDB()
    # print(MC.get_collection())
    # sql = 'db.Company.find({"name":"testZyl"})'
    # tongyongSql(sql)
    sql = 'db.User.find({"username":"testIrole001"})'
    sqldata = tongyongSql(sql)
    id = sqldata.get('_id')
    print(id)



