
from bot_common.utils.db_utils import DbConfig, create_table_if_not_exists, db_connect, update_table
from bot_common.utils.utils import catch_exception, get_time_now, clean_string, str_to_datetime
from bot_common.messages.timeout_model import TimeoutObj, timeout_headers as headers
from bot_common.utils.logging_conf import logger
from datetime import timedelta
from bot_common.lib_conf import timeout_table_name


class NewTimeout:
    def __init__(self, db, cursor, new_timeout: TimeoutObj = None):
        self.db, self.cursor = db, cursor
        self.tab_name = timeout_table_name
        self.new_timeout = new_timeout
        self.current_tmp = str_to_datetime(get_time_now())
        self.timeout_sec_idx = list(headers.keys()).index('timeout_sec') + 1
        create_table_if_not_exists(self.db, self.cursor, self.tab_name, headers)

    @catch_exception
    def get(self, required_elapsed_seconds_default):
        get_timeout_query = \
            f"SELECT * FROM {self.tab_name} WHERE company_contact = '{self.new_timeout.company_contact}' AND user_contact = '{self.new_timeout.user_contact}';"
        self.cursor.execute(get_timeout_query)
        new_timeout_ls = self.cursor.fetchall()
        if new_timeout_ls:
            return new_timeout_ls[0][self.timeout_sec_idx]
        else:
            return required_elapsed_seconds_default

    @catch_exception
    def delete(self):
        delete_timeout_query = f"DELETE FROM {self.tab_name} WHERE company_contact = '{self.new_timeout.company_contact}' AND user_contact = '{self.new_timeout.user_contact}';"
        self.cursor.execute(delete_timeout_query)

    @catch_exception
    def delete_older_hours(self, delete_older_timeout_hours):
        logger.info('INSIDE start_conn_delete_timeout FUNCTION')
        timedelta_mins = timedelta(minutes=delete_older_timeout_hours * 60)
        delete_timeout_before_tmp = self.current_tmp - timedelta_mins
        delete_expired_query = f"DELETE FROM {self.tab_name} WHERE timestamp < '{delete_timeout_before_tmp}';"
        self.cursor.execute(delete_expired_query)
        logger.info('>>> DELETED OLDER TIMEOUT')


@catch_exception
def set_timeout(new_timeout: TimeoutObj, db_config: DbConfig):
    db, cursor = db_connect(db_config)
    create_table_if_not_exists(db, cursor, timeout_table_name, headers)
    new_timeout_dict = new_timeout.__dict__
    new_timeout_dict = dict((k, clean_string(str(v))) for k, v in new_timeout_dict.items())
    new_timeout_dict['timestamp'] = get_time_now()
    new_timeout_dict['timeout_sec'] = int(new_timeout_dict['timeout_sec'])
    update_table(db, cursor, new_timeout_dict, timeout_table_name)
    logger.info(f'>>> set_new_timeout {new_timeout_dict}')
    db.close()
