
from bot_common.utils.db_utils import DbConfig, create_table_if_not_exists, db_connect, update_table, insert_into_table
from bot_common.utils.utils import catch_exception, get_time_now, clean_string, str_to_datetime
from bot_common.messages.message_model import MessageDbObj, NewMessageDbObj, DmMessageLightObj, message_headers as headers
from bot_common.messages.timeout_model import TimeoutObj
from bot_common.messages.timeout import NewTimeout

from datetime import timedelta
import itertools
from bot_common.utils.logging_conf import logger
from typing import List, Union
import json
from bot_common.lib_conf import void_message, messages_table_name


class NewMessages:
    def __init__(self, db_config: DbConfig):
        self.db, self.cursor = db_connect(db_config)
        self.tab_name = messages_table_name
        self.current_tmp = str_to_datetime(get_time_now())
        self.headers_keys = list(headers.keys())
        # +1 because we have the pk auto_increment element as first element
        self.company_idx = self.headers_keys.index('company_contact') + 1
        self.user_contact_idx = self.headers_keys.index('user_contact') + 1
        self.timestamp_idx = self.headers_keys.index('timestamp') + 1
        self.required_elapsed_seconds_default = 0
        self.single_user_parsed_messages = []
        self.single_user_messages = []
        self.single_message = []
        self.company_user_key = ()
        self.new_messages_dict = {}
        create_table_if_not_exists(self.db, self.cursor, self.tab_name, headers)

    @catch_exception
    def set_processed_and_parse(self):
        message_dict = dict(zip(self.headers_keys, self.single_message))
        message_dict['processed'] = 1
        message_obj = MessageDbObj.parse_obj(message_dict)
        self.single_user_parsed_messages.append(message_obj)
        # set processed=1 for the extracted messages
        update_table(self.db, self.cursor, message_dict, self.tab_name)

    @catch_exception
    def check_single_user_messages(self):
        user_last_received_tmp = str_to_datetime(self.single_user_messages[0][self.timestamp_idx])
        # time_elapsed_sec is the time elapsed from the given user's last message
        time_elapsed_sec = (self.current_tmp - user_last_received_tmp).total_seconds()
        # if it is passed a given amount of time since the user's last message,
        # we add the user messages between the processable ones, otherwise we wait for it
        timeout_obj = NewTimeout(self.db, self.cursor, TimeoutObj(company_contact=self.company_user_key[0], user_contact=self.company_user_key[1]))
        required_elapsed_seconds = timeout_obj.get(self.required_elapsed_seconds_default)

        logger.info(f'required_elapsed_seconds: {required_elapsed_seconds}')
        if time_elapsed_sec > required_elapsed_seconds:
            timeout_obj.delete()
            self.single_user_parsed_messages = []
            for message in self.single_user_messages:
                # mess[1:] because we need to remove the pk auto_increment element
                self.single_message = message[1:]
                self.set_processed_and_parse()
            self.new_messages_dict[self.company_user_key] = self.single_user_parsed_messages

    @catch_exception
    def get(self, required_elapsed_seconds_default: int):
        self.required_elapsed_seconds_default = required_elapsed_seconds_default
        # query for the unprocessed messages:
        # ORDER BY company, user_contact --> in order to allow the grouping by user_contact for different companies
        # ORDER BY timestamp DESC (per each user_contact) --> in order to have the last received message as first record
        get_new_messages_query = \
            f"SELECT * FROM {self.tab_name} WHERE processed = '0' ORDER BY company_contact, user_contact, timestamp DESC;"
        self.cursor.execute(get_new_messages_query)
        new_messages_ls = self.cursor.fetchall()
        # group by different user_contacts
        grouper = itertools.groupby(new_messages_ls, key=lambda x: (x[self.company_idx], x[self.user_contact_idx]))
        # cu_key = (company_contact, user_contact) tuple
        for cu_key, user_messages in grouper:
            logger.info(f'inside get_new_messages - (company_contact, user_contact): {cu_key}')
            self.company_user_key = cu_key
            self.single_user_messages = list(user_messages)
            self.check_single_user_messages()
        self.db.close()
        return self.new_messages_dict

    @catch_exception
    def set(self, new_message: NewMessageDbObj):
        new_message_dict = new_message.__dict__.copy()
        del new_message_dict['token']
        new_message_dict = dict((k, clean_string(v)) for k, v in new_message_dict.items())
        void_message_content = not bool(new_message_dict.get('user_message')) and not bool(new_message_dict.get('start_context'))
        new_message_dict['user_message'] = void_message if void_message_content else new_message_dict.get('user_message')
        new_message_dict['timestamp'] = get_time_now()
        new_message_dict['processed'] = 0
        insert_into_table(self.db, self.cursor, new_message_dict, self.tab_name)
        logger.info(f'>>> set_new_message {new_message_dict}')
        self.db.close()

# --------------- DELETE MESSAGES CLASS


class DeleteMessages:
    def __init__(self, db_config: DbConfig):
        self.db, self.cursor = db_connect(db_config)
        self.tab_name = messages_table_name
        self.company_contact = ''
        self.user_contact = ''
        self.current_tmp = str_to_datetime(get_time_now())
        create_table_if_not_exists(self.db, self.cursor, self.tab_name, headers)

    @catch_exception
    def expired(self, expired_ls: List[DmMessageLightObj]):
        for exp in expired_ls:
            self.company_contact = exp.company_contact
            self.user_contact = exp.session_id
            delete_expired_query = f"DELETE FROM {self.tab_name} WHERE company_contact = '{self.company_contact}' AND user_contact = '{self.user_contact}';"
            self.cursor.execute(delete_expired_query)
            NewTimeout(self.db, self.cursor, TimeoutObj(company_contact=self.company_contact, user_contact=self.user_contact)).delete()
            logger.info(f'>>> deleted ({self.company_contact}, {self.user_contact}) expired session')
        self.db.commit()
        self.db.close()

    @catch_exception
    def older_hours(self, delete_older_messages_hours):
        logger.info('INSIDE start_conn_delete_messages FUNCTION')
        timedelta_mins = timedelta(minutes=delete_older_messages_hours*60)
        delete_messages_before_tmp = self.current_tmp - timedelta_mins
        delete_expired_query = f"DELETE FROM {self.tab_name} WHERE timestamp < '{delete_messages_before_tmp}';"
        self.cursor.execute(delete_expired_query)
        NewTimeout(self.db, self.cursor).delete_older_hours(delete_older_messages_hours)
        self.db.commit()
        logger.info('>>> DELETED OLDER MESSAGES')
        self.db.close()
