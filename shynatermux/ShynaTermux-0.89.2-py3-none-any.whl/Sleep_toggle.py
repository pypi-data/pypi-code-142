from ShynaDatabase import Shdatabase
from Shynatime import ShTime
import os
from ShynaTelegramBotNotification import BotNotify
import random


class SleepToggle:
    # Todo Add speech system
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    s_bot = BotNotify.BotShynaTelegram()

    def shyna_sleep(self):
        try:
            ran_good_night = ['Night night.',
                              'Sleep tonight.',
                              'Nighty Night',
                              'Sweet dreams!',
                              'Sleep well',
                              'Have a good sleep',
                              'Dream about me!',
                              'Go to bed, you sleepy head!',
                              'Sleep tight!',
                              'Time to ride the rainbow to dreamland!',
                              'Night Night.',
                              'Lights out!',
                              "See ya’ in the morning!",
                              "I’ll be right here in the morning.",
                              "Sleep snug as a bug in a rug!",
                              "Until tomorrow.",
                              "Always and forever!",
                              "If you need me, you know where to find me.",
                              'Can’t wait to wake you up tomorrow!']
            self.s_data.default_database = os.environ.get('alarm_db')
            self.s_data.query = "Insert into greeting (new_date, new_time,greet_string,from_device,of_device) VALUES('" \
                                + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','sleep','" \
                                + str(os.environ.get('device_id')) + "','" + str(os.environ.get('device_id')) + "')"
            self.s_data.create_insert_update_or_delete()
            self.s_bot.message = random.choice(ran_good_night)
            self.s_bot.bot_send_msg_to_master()
            cmd = "termux-tts-speak -s ALARM '"+str(self.s_bot.message)+"'"
            os.popen(cmd)
        except Exception as e:
            self.s_bot.message = "Exception at shyna_sleep" + str(e)
            self.s_bot.bot_send_msg_to_master()
            print(e)

    def shyna_wake(self):
        try:
            ran_good_morning = ["Rise and shine!",
                                "Top of the morning to you!",
                                "Good day to you.",
                                "Have a great day.",
                                "Hello there!",
                                "Wishing you the best for the day ahead.",
                                "How are you this fine morning?",
                                "Isn’t it a beautiful day today?",
                                "Wakey, wakey, eggs and bakey.",
                                "Look alive!",
                                "Good morning, sleepy head/wakey wakey, sleepy head",
                                "Look at what the cat dragged in!",
                                "What a pleasant morning we are having.",
                                "Morning!"]
            self.s_data.default_database = os.environ.get('alarm_db')
            self.s_data.query = "Insert into greeting (new_date, new_time,greet_string,from_device,of_device) VALUES('" \
                                + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','wake','" \
                                + str(os.environ.get('device_id')) + "','" + str(os.environ.get('device_id')) + "')"
            self.s_data.create_insert_update_or_delete()
            self.s_bot.message = random.choice(ran_good_morning)
            self.s_bot.bot_send_msg_to_master()
            cmd = "termux-tts-speak -s ALARM '" + str(self.s_bot.message) + "'"
            os.popen(cmd)
        except Exception as e:
            self.s_bot.message = "Exception at shyna_wake" + str(e)
            self.s_bot.bot_send_msg_to_master()
            print(e)

    def shyna_silent(self):
        try:
            ran_silent_msg = ["Bye",
                              "Goodbye",
                              "Bye-bye",
                              "Farewell",
                              "Cheerio",
                              "See you",
                              "I’m out",
                              "Take care",
                              "Take it easy",
                              "I’m off",
                              "Gotta go!",
                              "Bye for now",
                              "See you later",
                              "Keep in touch",
                              "See you soon",
                              "I gotta take off",
                              "See you next time",
                              "good day"]
            self.s_data.default_database = os.environ.get('alarm_db')
            self.s_data.query = "Insert into greeting (new_date, new_time,greet_string,from_device,of_device) VALUES('" \
                                + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','silent','" \
                                + str(os.environ.get('device_id')) + "','" + str(os.environ.get('device_id')) + "')"
            self.s_data.create_insert_update_or_delete()
            self.s_bot.message = random.choice(ran_silent_msg)
            self.s_bot.bot_send_msg_to_master()
        except Exception as e:
            self.s_bot.message = "Exception at shyna_silent" + str(e)
            self.s_bot.bot_send_msg_to_master()
            print(e)
        finally:
            pass

    def shyna_update_status(self, status_string):
        try:
            pass
        except Exception as e:
            self.s_bot.message = "Exception at shyna_update_status" + str(e)
            self.s_bot.bot_send_msg_to_master()
            print(e)
        finally:
            pass

    def start_from_here(self):
        try:
            cmd = os.popen("termux-dialog radio -t 'Choose Profile' -v 'Wake','Silent', 'Sleep'").read()
            new_dict = eval(cmd)
            if str(new_dict['text']) == "":
                pass
            else:
                if int(new_dict['index']) == 0:
                    self.shyna_wake()
                elif int(new_dict['index']) == 1:
                    self.shyna_silent()
                elif int(new_dict['index']) == 2:
                    self.shyna_sleep()
                else:
                    pass
        except Exception as e:
            self.s_bot.message = "Exception at start_from_here" + str(e)
            self.s_bot.bot_send_msg_to_master()
            print(e)


if __name__ == "__main__":
    SleepToggle().start_from_here()
