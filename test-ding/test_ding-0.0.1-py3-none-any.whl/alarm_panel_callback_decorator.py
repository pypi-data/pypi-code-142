
from functools import wraps
from drive_screen.alarm_api import user_list_api
from dash import no_update

import datetime
import flask
import os

def authenticate_admin(func):
    @wraps(func)
    def authenticate_and_call(*args, **kwargs):
        STATIC_PATH = os.path.join(os.getcwd(), 'drive_screen\static')

        print('STATIC_PATH',STATIC_PATH)
        return flask.send_from_directory(STATIC_PATH, 'style.css')

    return authenticate_and_call


def update_cycle_fun(func):
    @wraps(func)
    def update_cycle(*args, **kwargs):

        return  1000*int(args[1])
    return update_cycle


def card_output_deco(drive_alarm):
    def card_output_fun(func):
        @wraps(func)
        def card_output(*args):

            """
            更新card
            """
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            card, count,length = drive_alarm.card_output_fun()
            tip = "上次刷新时间：{}，共{}条显示{}条, 点击查询全部".format(current_time,count,length), 

            return card,tip
        return card_output
    return card_output_fun


def init_creator_list_deco(creator_list):
    def init_creator_list_fun(func):
        @wraps(func)
        def init_creator_list(*args, **kwargs):
            ans = []
            for x in creator_list:
                ans.append({
                    "label": x,
                    "value": x
                })
            return ans
        return init_creator_list
    return init_creator_list_fun
    

def init_service_list_deco(SERVER_HOST):
    def init_service_list_func(func):
        @wraps(func)
        def init_service_list(*args, **kwargs):

            """
            初始化服务列表
            """
            # print('*************')
            # global SERVER_HOST

            # print('creator check',creator)

            if args[0] is not None:
                res = user_list_api(SERVER_HOST,args[0])
                records = res['data']['records']

                ans, cache = [], {}
                for x in records:
                    ans.append({
                        "label": x["service_name"],
                        "value": x["service_name"]
                    })
                    cache[x["id"]] = x["service_name"]
                return ans, cache
            else:
                return no_update, no_update
        return init_service_list
    return init_service_list_func



def update_config_deco(drive_alarm):
    def update_config_fun(func):
        @wraps(func)
        def update_config(*args, **kwargs):
            if args[2]:
                drive_alarm.creator = args[2]
            if args[1]:
                drive_alarm.servicename = args[2]
            if args[3]:
                drive_alarm.time_delta = args[3]
            if args[4]:
                drive_alarm.time_cycle = args[4]
            if args[5]:
                drive_alarm.alarm_number = int(args[5])
            if args[6]:
                drive_alarm.panel_image_width = int(args[6])
            if args[7]:
                drive_alarm.panel_max_height = int(args[7])
        
        return no_update
    return update_config_fun


def toggle_modal_fun(func):
    @wraps(func)
    def toggle_modal(*args, **kwargs):

        if args[0] or args[1]:
            return not args[2]
        return args[2]        
    return toggle_modal



