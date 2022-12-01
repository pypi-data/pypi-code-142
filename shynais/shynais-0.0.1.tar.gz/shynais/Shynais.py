from ShynaDatabase import Shdatabase
from Shynatime import ShTime
import os
from ShynaTelegramBotNotification import BotNotify


class ShynaIs:
    """
    This is for tracking and checking activities. It will store the data in table
    and Notification package should take care of sending notification in case there is something unexpected
    1) is_location_service_on?
    """

    result = []
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    s_telegram_bot = BotNotify.BotShynaTelegram()
    is_this = False
    additional_note = False
    last_run_status = False

    def update_table(self, question_is, status):
        """Instead of re-writing the code for insert table, this function will insert the status for particular
        process by itself. """
        try:
            self.s_data.default_database = os.environ.get('twelve_db')
            if self.additional_note is False:
                self.s_data.query = "Insert into shyna_is (question_is,task_date,task_time,new_status," \
                                    "additional_note) VALUES('" + str(question_is) + "','" + str(self.s_time.now_date) + \
                                    "','" + str(self.s_time.now_time) + "','" + str(status) + "','" \
                                    + str(self.additional_note) + \
                                    "') ON DUPLICATE KEY UPDATE task_date='" + str(self.s_time.now_date) + \
                                    "', task_time='" + str(self.s_time.now_time) + "' , new_status='" \
                                    + str(status) + "', question_is='" + str(question_is) + "'"
                # print(self.s_data.query)
            else:
                self.s_data.query = "Insert into shyna_is (question_is,task_date,task_time,new_status," \
                                    "additional_note) VALUES('" + str(question_is) + "','" + str(self.s_time.now_date) + \
                                    "','" + str(self.s_time.now_time) + "','" + str(status) + "','" \
                                    + str(self.additional_note) + \
                                    "') ON DUPLICATE KEY UPDATE task_date='" + str(self.s_time.now_date) + \
                                    "', task_time='" + str(self.s_time.now_time) + "', new_status='" + str(status) + \
                                    "', additional_note= '" + str(self.additional_note) + \
                                    "', question_is='" + str(question_is) + "'"
                # print(self.s_data.query)
            self.s_data.create_insert_update_or_delete()
        except Exception as e:
            print(e)
            self.s_telegram_bot.message = "There issue at Shyna_Is with update table for " + question_is + str(e)
            self.s_telegram_bot.bot_send_msg_to_master()
            self.insert_ttm_sent(s_sentence=str(self.s_telegram_bot.message))

    def insert_ttm_sent(self, s_sentence):
        try:
            self.s_data.default_database = os.environ.get("taskmanager_db")
            self.s_data.query = "Insert into TTM_sent (task_date,task_time,sent,from_device_id) VALUES('" \
                                + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','" \
                                + str(s_sentence) + "','" + str(os.environ.get("device_id")) + "')"
            self.s_data.create_insert_update_or_delete()
        except Exception as e:
            self.s_telegram_bot.message = "There issue at Shyna_Is with TTM_sent for " + str(s_sentence) + str(e)
            self.s_telegram_bot.bot_send_msg_to_master()
            print(e)

    def is_location_received_from_primary_mobile(self):
        self.is_this = False
        task_time_sequence = []
        try:
            self.s_data.default_database = os.environ.get('status_db')
            self.s_data.query = "SELECT task_time FROM last_run_check where task_date='" + \
                                str(self.s_time.now_date) + "' AND process_name='location_check' "
            self.result = self.s_data.select_from_table()
            for result in self.result:
                for item in result:
                    task_time_sequence.append(item)
            time_diff = (self.s_time.string_to_time_with_date(
                time_string=str(self.s_time.now_time)) - self.s_time.string_to_time_with_date(
                time_string=str(task_time_sequence[0]))).total_seconds()
            # print(time_diff)
            if int(time_diff) <= 70:
                self.is_this = True
            else:
                self.is_this = False
        except Exception as e:
            self.is_this = False
            print(e)
            self.s_telegram_bot.message = "Exception at is_location_received_from_primary_mobile " + str(e)
            self.s_telegram_bot.bot_send_msg_to_master()
        finally:
            try:
                self.s_data.default_database = os.environ.get("twelve_db")
                self.s_data.query = "Select last_run_status from shyna_is where question_is='termux_online' " \
                                    "or question_is='primary_location'"
                self.result = self.s_data.select_from_table()
                # print(self.result[0][0], self.result[1][0])
                if str(self.is_this).lower() == str(self.result[0][0]).lower() or str(self.is_this).lower() == str(
                        self.result[1][0]).lower():
                    pass
                else:
                    self.s_data.default_database = os.environ.get('twelve_db')
                    self.s_data.query = "Update shyna_is set last_run_status='" + str(self.is_this) + \
                                        "' where question_is='primary_location'"
                    self.s_data.create_insert_update_or_delete()
                    self.s_data.default_database = os.environ.get('twelve_db')
                    self.s_data.query = "Update shyna_is set last_run_status='" + str(self.is_this) + \
                                        "' where question_is='termux_online'"
                    self.s_data.create_insert_update_or_delete()
                    if str(self.is_this).lower() == 'true':
                        self.s_telegram_bot.message = "Termux back online"
                        self.s_telegram_bot.bot_send_msg_to_master()
                        self.insert_ttm_sent(s_sentence=str(self.s_telegram_bot.message))
                    else:
                        self.s_telegram_bot.message = "Termux Offline"
                        self.s_telegram_bot.bot_send_msg_to_master()
                        self.insert_ttm_sent(s_sentence=str(self.s_telegram_bot.message))
            except Exception as e:
                print(e)
            finally:
                self.update_table(question_is="primary_location", status=self.is_this)
                self.update_table(question_is="termux_online", status=self.is_this)
                return self.is_this


if __name__ == '__main__':
    ShynaIs().is_location_received_from_primary_mobile()
