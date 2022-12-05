from bot_common.utils.utils import catch_exception, get_time_now, clean_string
from bot_common.utils.db_utils import DbConfig, create_table_if_not_exists, db_connect, update_table, insert_into_table
from bot_common.logs.log_model import LogObject, log_headers as headers
from bot_common.utils.logging_conf import logger
import json
import time
from bot_common.lib_conf import logs_table_prefix

# In "other_logs" we store some specific information to describe how we reached
# the current flow step and the main features extracted along the path,
# these are non-generic_logs (call_reason and other specific features).

int_fields = ['conv_duration_sec', 'fallback', 'handover', 'handover_incomprehension', 'conv_step_num',
              'closed', 'expired', 'redirect', 'closed_formality', 'hangup', 'unclosed_success', 'solicit']
dump_fields = ['other_logs']
str_special_char_fields = []
clean_str_fields = ['bot_message', 'current_user_utterance', 'log_transcript']
float_fields = ['intent_confidence']


class Log(LogObject):
    @catch_exception
    def extract_data(self):
        data = self.__dict__.copy()
        data['timestamp'] = get_time_now()
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
        tab_name = logs_table_prefix + self.company
        logs_db, logs_cursor = db_connect(db_config)
        create_table_if_not_exists(logs_db, logs_cursor, tab_name, headers)
        data_dict = self.extract_data()
        logger.info('-- WRITING LOGS --')
        try:
            insert_into_table(logs_db, logs_cursor, data_dict, tab_name)
            logger.info(f'Writing logs success')
        except Exception as err:
            time.sleep(1)
            try:
                data_dict['timestamp'] = get_time_now()
                insert_into_table(logs_db, logs_cursor, data_dict, tab_name)
                logger.info(f'Writing logs success (at second try) - {err}')
            except Exception as e:
                raise Exception(f'Exception in writing logs: {e}')
        finally:
            logs_db.close()
