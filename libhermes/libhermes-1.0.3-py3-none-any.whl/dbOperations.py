import logging
import os
import mysql.connector

class DbOperations():
    # agnostic class wrapping SQL database operations
    def __init__(self, host, database, user, password, logger=None):
        if logger:
            self.logger = logger
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s')
            self.logger = logging.getLogger(__name__)
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def SQL_upsert(self, SQL):
        self.logger.debug(f"[SQL_upsert] SQL: {SQL}")
        mysqlCnx = None
        if os.getenv("MODE_SKIP_MYSQL"):
            self.logger.warning("MODE_SKIP_MYSQL: Skip Database persistence")
            return
        try:
            mysqlCnx = mysql.connector.connect(host=self.host,
                                               database=self.database,
                                               user=self.user,
                                               password=self.password)
            if mysqlCnx.is_connected():
                mysqlCnx.cursor().execute(SQL)
                mysqlCnx.commit()
        except Exception as e:
            self.logger.exception(f"[SQL_upsert] MySql error: {e} \n{SQL}")
        finally:
            if mysqlCnx:
                mysqlCnx.disconnect()

    def SQL_select(self, SQL):
        self.logger.debug(f"[SQL_select] SQL: {SQL}")
        mysqlCnx = None
        res = None
        try:
            mysqlCnx = mysql.connector.connect(host=self.host,
                                               database=self.database,
                                               user=self.user,
                                               password=self.password)
            if mysqlCnx.is_connected():
                cursor = mysqlCnx.cursor()
                cursor.execute(SQL)
                res = cursor.fetchall()

        except Exception as e:
            self.logger.exception(f"[SQL_select] MySql error: {e} \n{SQL}")
        finally:
            if mysqlCnx:
                mysqlCnx.disconnect()
            return res
