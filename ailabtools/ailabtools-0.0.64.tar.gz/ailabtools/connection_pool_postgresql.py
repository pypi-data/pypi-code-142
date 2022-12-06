from threading import Lock, Thread
import psycopg2
import time
import json
from ailabtools.zlogger import ZLogger
import sys


class ConnectionPoolPostgreSql():
    def __init__(self, min, max, host, port, user, password, database, n_try = 1, folder_log = "log", keep_connection = True, project_name="ConnectionPoolPostgreSql", print_log=False):
        self.min = min
        self.max = max
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.list_conn = []
        self.keep_connection = keep_connection
        self.print_log = print_log
        if(folder_log != "log"):
            self.folder_log = folder_log
        else:
            try:
                import const
                self.folder_log = const.LOG_FOLDER
            except:
                self.folder_log = folder_log
        self.local_logger = ZLogger(foler_log=self.folder_log, project_name=project_name)
        if(n_try > 0):
            self.n_try = n_try
        else:
            self.n_try = 1
        self.thread_lock = Lock()
        for i in range(min):
            #conn, time use or create, time check
            create_conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port,
                                    database=self.database)
            create_conn.set_session(autocommit=True)
            self.list_conn.append([create_conn, int(time.time()), int(time.time())])
        self.num_conn = min
        if(self.keep_connection):
            self.thread_auto_close_conn = Thread(target=self.__auto_close_conn, args=(10, 10,)).start()
    
    def close_cur_and_conn(self, cur, conn):
        try:
            cur.close()
        except:
            pass
        try:
            conn.rollback()
        except:
            pass
        
        try:
            conn.close()
        except:
            pass

    def error(self, param_log):
        if(self.print_log):
            print(json.dumps(param_log, ensure_ascii=False))
            sys.stdout.flush()
        else:
            self.local_logger.error(json.dumps(param_log, ensure_ascii=False))
    
    def info(self, param_log):
        if(self.print_log):
            print(json.dumps(param_log, ensure_ascii=False))
            sys.stdout.flush()
        else:
            self.local_logger.info(json.dumps(param_log, ensure_ascii=False))

    def __auto_close_conn(self, time_close, time_check):
        while(True):
            now = int(time.time())
            # for i in range(len(self.list_conn)):
            i = 0
            while(True):
                if(i >= len(self.list_conn)):
                    break
                try:
                    
                    self.thread_lock.acquire()
                    if(self.list_conn[i][2] < now):
                        if((now - self.list_conn[i][1] > time_close) and (self.num_conn > self.min)):
                            del self.list_conn[i]
                            self.num_conn -= 1
                        else:
                            self.list_conn[i][2] = now
                        i=0
                    else:
                        i = i + 1
                except:
                    import traceback
                    tb = traceback.format_exc()
                    self.error({"error": tb})
                finally:
                    self.thread_lock.release()

            time.sleep(time_check)
    def __get_conn(self, n_try = 5):
        item = None
        n_now = 0
        while(True):
            try:
                self.thread_lock.acquire()
                if(len(self.list_conn) > 0):
                    item = self.list_conn[0]
                    del self.list_conn[0]
                else:
                    if(self.num_conn < self.max):
                        create_conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port,
                                    database=self.database)
                        create_conn.set_session(autocommit=True)
                        item = [create_conn]
                        self.num_conn += 1
            except:
                import traceback
                tb = traceback.format_exc()
                self.error({"error": tb})
            finally:
                self.thread_lock.release()
            if(item is not None):
                break
            n_now += 1
            if(n_now >= n_try):
                return None
            time.sleep(0.01)
        return item[0]
    def __put_conn(self, conn):
        try:
            self.thread_lock.acquire()
            if(self.keep_connection):
                self.list_conn.append([conn, int(time.time()), int(time.time())])
            else:
                conn.close()
                self.num_conn -= 1
        except:
            import traceback
            tb = traceback.format_exc()
            self.error({"error": tb})
        finally:
            self.thread_lock.release()

    def execute(self, *args, **kwargs):
        conn = self.__get_conn()
        if(conn is None):
            self.error({"error": "Cannot create connection to db"})
            return None
        temp_n_try = 0
        do_again = False
        while(temp_n_try <= self.n_try):
            temp_n_try += 1
            result = None
            try:
                cur = conn.cursor()
                cur.execute(*args, **kwargs)
                result = cur.fetchall()
            except (psycopg2.InterfaceError, psycopg2.OperationalError) as e:
                #try
                result = None
                import traceback
                tb = traceback.format_exc()
                self.error({"error": tb})
                self.close_cur_and_conn(cur, conn)
                conn = psycopg2.connect(user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            port=self.port,
                                            database=self.database)
                conn.set_session(autocommit=True)
                cur = conn.cursor()
                do_again = True
            except psycopg2.ProgrammingError as e:
                result = None
                if "no results to fetch" in str(e):
                    pass
                else:
                    import traceback
                    tb = traceback.format_exc()
                    self.error({"error": tb})
                    self.close_cur_and_conn(cur, conn)
                    conn = psycopg2.connect(user=self.user,
                                                password=self.password,
                                                host=self.host,
                                                port=self.port,
                                                database=self.database)
                    conn.set_session(autocommit=True)
                    cur = conn.cursor()
            except Exception as e:
                result = None
                import traceback
                tb = traceback.format_exc()
                self.error({"error": tb})
                self.close_cur_and_conn(cur, conn)
                conn = psycopg2.connect(user=self.user,
                                            password=self.password,
                                            host=self.host,
                                            port=self.port,
                                            database=self.database)
                conn.set_session(autocommit=True)
                cur = conn.cursor()
            finally:
                cur.close()
            if(not do_again):
                break
        self.__put_conn(conn)
        return result

    def executeUpdate(self, *args, **kwargs):
        return self.execute(*args, **kwargs)
    
    