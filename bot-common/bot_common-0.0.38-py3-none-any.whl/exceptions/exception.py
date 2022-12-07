from bot_common.utils.utils import catch_exception, get_time_now, clean_string, validate_time
from bot_common.utils.db_utils import DbConfig, create_table_if_not_exists, db_connect, insert_into_table
from bot_common.exceptions.exception_model import ExceptionObj, exception_headers as headers
from bot_common.utils.logging_conf import logger
from typing import List
from bot_common.lib_conf import exceptions_table_name
import json
import time

int_fields = []
dump_fields = []
str_special_char_fields = []
clean_str_fields = ['error_message']
float_fields = []


class ExceptionSession(ExceptionObj):
    def extract_data(self):
        data = self.__dict__.copy()
        data['timestamp'] = self.timestamp if validate_time(self.timestamp) else get_time_now()
        for field in dump_fields:
            data[field] = clean_string(json.dumps(data[field])).replace('\\', '\\\\')
        for field in str_special_char_fields:
            data[field] = data[field].replace("\\", "\\\\").replace("'", "\\'")
        for field in int_fields:
            data[field] = int(data[field])
        for field in clean_str_fields:
            data[field] = clean_string(data[field])
        for field in float_fields:
            data[field] = round(float(data[field]), 2)
        return data

    @catch_exception
    def write(self, db_config: DbConfig):
        tab_name = exceptions_table_name
        session_db, session_cursor = db_connect(db_config)
        create_table_if_not_exists(session_db, session_cursor, tab_name, headers)
        data_dict = self.extract_data()
        insert_into_table(session_db, session_cursor, data_dict, tab_name)
        logger.info(f'Writing sessions success')
        session_db.close()


class ExceptionManager:
    @catch_exception
    def __init__(self, tmp: str, db_config: DbConfig):
        self.tmp = tmp
        self.tab_name = exceptions_table_name
        self.session_db, self.session_cursor = db_connect(db_config)
        create_table_if_not_exists(self.session_db, self.session_cursor, self.tab_name, headers)

    @catch_exception
    def delete(self):
        delete_session_query = f"DELETE FROM {self.tab_name} WHERE timestamp <= '{self.tmp}';"
        self.session_cursor.execute(delete_session_query)
        self.session_db.commit()
        self.session_db.close()

    @catch_exception
    def get(self) -> List[ExceptionObj]:
        get_session_query = f"SELECT * FROM {self.tab_name} WHERE timestamp <= '{self.tmp}' ORDER BY timestamp DESC;"
        self.session_cursor.execute(get_session_query)
        myresult = self.session_cursor.fetchall()
        self.session_db.close()
        out_ls = []
        for res in myresult:
            # res[1:] because we need to remove the pk auto_increment element
            out_dict = dict(zip(headers, res[1:]))
            out_dict['timestamp'] = str(out_dict['timestamp'])
            out_ls.append(ExceptionObj.parse_obj(out_dict))
        return out_ls
