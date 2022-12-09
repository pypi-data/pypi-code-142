# -*- coding: utf-8 -*-

import sqlite3
import os


class SqliteDb:
    """
    dbHandle = SqliteDb(db_file)
    dbHandle.exec(sql)
    dbHandle.fetchone()  or db_handel.fetchall()
    dbHandle.close()
    """
    debug = False

    def __init__(self, db_file=None):
        self.c = None
        self.conn = None
        self.db_file = None
        if db_file is not None:
            self.open(db_file)

    def open(self, db_file):
        if self.debug:
            print(f'db_file: {db_file}')

        if os.path.isfile(db_file):
            self.db_file = os.path.realpath(db_file)
            self.conn = sqlite3.connect(self.db_file)
            self.conn.text_factory = lambda x: str(x, 'utf-8', 'ignore')
            self.c = self.conn.cursor()
            return True
        else:
            return False

    def execute(self, sql):
        # 连接Sqlite执行Sql语言。
        if self.debug:
            print("""class SqliteDb self.DEBUG:\t execute: %s""" % str(sql))
        try:
            self.c.execute(sql)
            return True
        except Exception as e:
            if self.debug:
                print("""class SqliteDb self.DEBUG:\t ERROR: %s""" % str(e))
            return False

    def fetchall(self):

        result = self.c.fetchall()
        if self.debug:
            print(f"fetchall {result}")
        return result

    def fetchone(self):

        result = self.c.fetchone()
        if self.debug:
            print(f"fetchone {result}")
        return result

    def commit(self):
        if self.conn:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
