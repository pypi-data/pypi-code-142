"""
@Project:pymysql
@File:Model.py
@Author:函封封
@Date:9:23
"""

import pymysql

# mysql操作
class Model():
    def __init__(self,database=None,user=None,password=None,host="localhost",port=3306,charset="utf8"):
        if not all([database, user, password, host, port, charset]):
            try:
                from setting import DATABASES
            except Exception as err:
                raise ValueError(err)
            self.pymysql_con = pymysql.connect(**DATABASES)
        else:
            self.pymysql_con = pymysql.connect(database=database, user=user, password=str(password), host=host,port=port, charset=charset)
        self.mysql = self.pymysql_con.cursor() # 创建游标对象
        self.table_name = None  # 表名
        self.field = []  # 表字段

    def show_tables(self):
        """
        show_tables()方法：查询当前数据库中所有表
        :return: 返回一个列表
        """
        sql = f"""show tables;"""
        self.mysql.execute(sql)
        data = self.mysql.fetchall()
        table_list = []
        for i in data:   # 元组转换为列表
            table_list.append(i[0])
        return table_list # 返回当前数据库内所有的表

    def link_table(self, table_name=None, field=None):
        """
        link_table()方法：当前数据库中该表已存在直接返回，不存在则创建
        :param table_name: 表名
        :param field: 表字段
        :return: 连接成功：返回 True
        """
        self.table_name = table_name  # 将表名赋值给实例属性
        for i in field:
            field_name = i.split()[0]  # 获取所有的字段名，不含字段类型
            self.field.append(field_name)  # 获取该表的所有的字段名

        table_list = self.show_tables()  # 获取数据库里所有的表
        if self.table_name in table_list:  # 判断该表是否已存在
            print(f"——连接成功：{self.table_name}——")
            return True # 该表已存在！直接返回

        create_field = ",".join(field)  # 将所有的字段与字段类型以 “ , ” 拼接
        sql = f"""
             create table `{self.table_name}`(
                {create_field}
              );
         """
        self.mysql.execute(sql)
        print(f"——创建并连接成功：{self.table_name}——")
        return True

    def create(self,**kwargs):
        """
        create()方法：添加一行数据
        :param kwargs: 接收一个字典，key = value 字段 = 值
        :return: 添加成功：返回 True 添加失败：返回 Flase
        """
        try:
            value_list = []
            for i in self.field:
                value = kwargs.get(i)
                if value == None:
                    value = "NULL"
                else:
                    value = f"{value}" if isinstance(value, int) else f"'{value}'"
                value_list.append(value)
            field_sql = "`,`".join(self.field)
            create_sql = ",".join(value_list)

            # id 字段为null ，默认自增
            sql = f"""
                insert into `{self.table_name}`  (`{field_sql}`) values 
                ({create_sql});
            """
            self.mysql.execute(sql)
        except Exception as err:
            self.pymysql_con.rollback()
            print("错误信息：", err)
            return False
        else:
            self.pymysql_con.commit()
            return True

    def update(self, id, **kwargs):
        """
        update()方法：修改 id=? 数据
        :param id: 要修改行的 id
        :param kwargs: 接收一个字典，key == value 条件
        :return: 修改成功：返回 True 删除失败：返回 False
        """
        try:
            value_list = []
            for key, value in kwargs.items():
                if key in self.field:
                    if value == None:
                        value = f"{key}=NULL"
                    else:
                        value = f"{key}={value}" if isinstance(value, int) else f"{key}='{value}'"
                    value_list.append(value)
            update_sql = ",".join(value_list)

            sql = f"""
                    update `{self.table_name}` set {update_sql} where id = {id};
                """
            self.mysql.execute(sql)
        except Exception as err:
            self.pymysql_con.rollback()
            print("错误信息：", err)
            return False
        else:
            self.pymysql_con.commit()
            return True

    def delete(self, native_sql="",**kwargs):
        """
        delete()方法：删除条件满足的所有数据
        :param native_sql: 接收原生sql语句，用于复杂查询，如 order by,group by,子查询
        :param kwargs: 接收一个字典，key == value 条件
        :return: 删除成功：返回删除数据的条数 删除失败：返回 False
        """
        try:
            condition_sql = self.condition_sql(**kwargs)
            condition_sql = " ".join([condition_sql, native_sql])

            # 先查询满足条件的数据个数
            sql = f"""
                    select COUNT(id) from `{self.table_name}` where {condition_sql};
                """
            self.mysql.execute(sql)
            data = self.mysql.fetchall()
            delete_sum = data[0][0]

            # 删除数据
            sql = f"""
                    delete from `{self.table_name}` where {condition_sql};
                """
            self.mysql.execute(sql)
        except Exception as err:
            self.pymysql_con.rollback()
            print("错误信息：", err)
            return False
        else:
            self.pymysql_con.commit()
            return delete_sum

    def all(self,*args):
        """
        all()方法：查询所有数据
        :param args: 接收一个列表，查询结果表字段，可聚合查询
        :return: 返回查询到的所有行，为列表嵌套字典类型
        """
        result_field = args if len(args) != 0 else self.field
        select_field = "`,`".join(result_field)

        # 根据表名直接查询
        sql = f"""
            select `{select_field}` from `{self.table_name}`;
            """

        self.mysql.execute(sql)
        data = self.mysql.fetchall()

        result = self.result(result_field,data)
        return result # 最终返回查询集

    def filter(self, *args, native_sql="", **kwargs):
        """
        filter()方法：查询数据库
        :param native_sql: 接收原生sql语句，用于复杂查询，如 order by,group by,子查询
        :param args: 接收一个列表，查询结果表字段，可聚合查询
        :param kwargs: 接收一个字典，key == value 条件
        :return: 返回查询到的所有行，为列表嵌套字典类型
        """
        condition_sql = self.condition_sql(**kwargs)
        condition_sql = " ".join([condition_sql, native_sql])

        # 结果字段
        result_field = args if len(args) != 0 else self.field
        select_field = "`,`".join(result_field)

        sql = f"""
                select `{select_field}` from `{self.table_name}` where {condition_sql};
            """
        self.mysql.execute(sql)

        data = self.mysql.fetchall()
        result = self.result(result_field,data)
        return result


    def get(self, *args, native_sql="", **kwargs):
        """
        get()方法：查询数据库
        :param native_sql: 接收原生sql语句，用于复杂查询，如 order by,group by,子查询
        :param args: 接收一个列表，查询结果表字段，可聚合查询
        :param kwargs: 接收一个字典，key == value 条件
        :return: 返回查询到的第一行数据，为字典类型
        """
        condition_sql = self.condition_sql(**kwargs)
        condition_sql = " ".join([condition_sql, native_sql])

        # 结果字段
        result_field = args if len(args) != 0 else self.field
        select_field = "`,`".join(result_field)

        sql = f"""
            select `{select_field}` from `{self.table_name}` where {condition_sql};
        """
        self.mysql.execute(sql)
        data = self.mysql.fetchall()
        result = self.result(result_field, data)
        result = None if len(result) == 0 else result[0]
        return result
    def condition_sql(self, **kwargs):
        """
        condition_sql()组织条件语句
        :param kwargs: 接受一个字典，key == value 条件
        :return: sql条件语句
        """
        condition_list = []
        for key, value in kwargs.items():
            if key in self.field:
                sql = f"{key} is NULL" if value == None else f"{key}='{value}'"
                condition_list.append(sql)
        condition_sql = " and ".join(condition_list)
        return condition_sql

    def result(self, result_field, data):
        """
        result()组织数据
        :param result_field: 接受一个列表，数据为表字段，组织数据使用
        :param data: sql查询结果，为嵌套元组
        :return: 列表嵌套字典类型
        """
        result = []
        for i in data:
            temp = {}
            for k, j in enumerate(result_field):
                temp[j] = i[k]
            result.append(temp)
        # 返回查询集
        return result
