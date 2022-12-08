from asyncore import ExitNow
from types import WrapperDescriptorType
from dash import Input, Output,State, callback,no_update,clientside_callback,ClientsideFunction

import datetime
import flask
import os
import dash_bootstrap_components as dbc
from functools import wraps
from drive_screen.alarm_panel import *
from drive_screen.style import *
from drive_screen.alarm_api import user_list_api
from drive_screen.alarm_panel_callback_decorator import *

# import inspect
# import functools
# import dynamic_function_loader
# from copy import copy
# from retry import retry


    


def panel_callback(app,drive_alarm,creator_list,SERVER_HOST):
    try:
        app.config.external_stylesheets.append('/static/style.css')
        @app.server.route('/static/<resource>')
        def serve_static(resource):
            # print('resource',resource)
            STATIC_PATH = os.path.join(os.getcwd(), 'drive_screen\static')

            # print('STATIC_PATH',STATIC_PATH)
            return flask.send_from_directory(STATIC_PATH, resource)
    except:
        pass

    try:

   
        # app.config.external_stylesheets.append('/static/style.css')
        # @authenticate_admin
       

        @app.callback(
            Output('card_output', 'children'),
            Output("tips_button", "children"),
            Input('apply', 'n_clicks'),
            Input('interval_1m', 'n_intervals')
            # prevent_initial_call=True
        )
        def card_output_fun(n1,intervals):
            """
            更新card
            """
            # print('更新card')
            # global drive_alarm
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            card, count,len = drive_alarm.card_output_fun()
            tip = "上次刷新时间：{}，共{}条显示{}条, 点击查询全部".format(current_time,count,len), 

            return card,tip


        ### 初始化报警创建者
        @app.callback(
                Output("alert_creator", "options"),
                Input('alert_creator', 'id')
            )
        def init_creator_list(id):
            # global creator

            # print('creator',creator)

            ans = []
            for x in creator_list:
                ans.append({
                    "label": x,
                    "value": x
                })
            return ans



        ### 更新报警服务的下拉框
        @app.callback(
                [Output("alert_tbl_ServiceName", "options"), Output("memory_service_info", "data")],
                Input('alert_creator', 'value'),
                
            )
        def init_service_list(creator):
            """
            初始化服务列表
            """
            # print('*************')
            # global SERVER_HOST

            # print('creator check',creator)

            if creator is not None:

                res = user_list_api(SERVER_HOST,creator)
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

        ##### 根据报警配置的信息更新drive_alarm的初始化参数
        @app.callback(
            Output('confirm', 'n_clicks'), 
            Input('confirm', 'n_clicks'),
            State('alert_tbl_ServiceName', 'value'),
            State('alert_creator', 'value'),
            State('filter_hours', 'value'),
            State('update_cycle', 'value'),
            State('panel_show_number', 'value'),
            State('panel_image_width', 'value'),
            State('panel_max_height'  , 'value'),
            prevent_initial_call=True
        )
        def update_config(n1,servicename,creator,time_delta,cycle,panel_number,panel_image_width,panel_max_height):
            # print('servicename',servicename)
            # print('time_delta',time_delta)
            # print('cycle',cycle)
            # global drive_alarm

            # print('creator new',creator)
            # print('service_name old',drive_alarm.servicename)

            if creator:
                drive_alarm.creator = creator
            if servicename:
                drive_alarm.servicename = servicename
            if time_delta:
                drive_alarm.time_delta = time_delta
            if cycle:
                drive_alarm.time_cycle = cycle
            if panel_number:
                drive_alarm.alarm_number = int(panel_number)
            if panel_image_width:
                drive_alarm.panel_image_width = int(panel_image_width)
            if panel_max_height:
                drive_alarm.panel_max_height = int(panel_max_height)
            
            return no_update


        ###报警配置框的确认按钮关闭功能定义
        @app.callback(
            Output("modal_config", "is_open"),
            [Input("alarm_config", "n_clicks"), Input('confirm', 'n_clicks'),],
            [State("modal_config", "is_open")],
        )
        def toggle_modal(n1,n2,is_open):
            if n1 or n2:
                return not is_open
            return is_open
    except:
        try:
            # app.config.external_stylesheets.append('/static/style.css')

            # @app.server.route('/static/<resource>')
            # def serve_static_2(resource):
            #     print('resource',resource)
            #     STATIC_PATH = os.path.join(os.getcwd(), 'demo_project\static')

            #     print('STATIC_PATH',STATIC_PATH)
            #     return flask.send_from_directory(STATIC_PATH, resource)

            @app.callback(
                Output('card_output', 'children'),
                Output("tips_button", "children"),
                Input('apply', 'n_clicks'),
                Input('interval_1m', 'n_intervals')
                # prevent_initial_call=True
            )
            def card_output_fun_2(n1,intervals):
                """
                更新card
                """
                # print('更新card')
                # global drive_alarm
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                card, count,len = drive_alarm.card_output_fun()
                tip = "上次刷新时间：{}，共{}条显示{}条, 点击查询全部".format(current_time,count,len), 

                return card,tip


            ### 初始化报警创建者
            @app.callback(
                    Output("alert_creator", "options"),
                    Input('alert_creator', 'id')
                )
            def init_creator_list_2(id):
                # global creator

                # print('creator',creator)

                ans = []
                for x in creator_list:
                    ans.append({
                        "label": x,
                        "value": x
                    })
                return ans



            ### 更新报警服务的下拉框
            @app.callback(
                    [Output("alert_tbl_ServiceName", "options"), Output("memory_service_info", "data")],
                    Input('alert_creator', 'value'),
                    
                )
            def init_service_list_2(creator):
                """
                初始化服务列表
                """
                # print('*************')
                # global SERVER_HOST

                print('creator check',creator)

                if creator is not None:

                    res = user_list_api(SERVER_HOST,creator)
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

            ##### 根据报警配置的信息更新drive_alarm的初始化参数
            @app.callback(
                Output('confirm', 'n_clicks'), 
                Input('confirm', 'n_clicks'),
                State('alert_tbl_ServiceName', 'value'),
                State('alert_creator', 'value'),
                State('filter_hours', 'value'),
                State('update_cycle', 'value'),
                State('panel_show_number', 'value'),
                State('panel_image_width', 'value'),
                State('panel_max_height'  , 'value'),
                prevent_initial_call=True
            )
            def update_config_2(n1,servicename,creator,time_delta,cycle,panel_number,panel_image_width,panel_max_height):
                print('servicename',servicename)
                # print('time_delta',time_delta)
                # print('cycle',cycle)
                # global drive_alarm

                # print('creator new',creator)
                print('service_name old',drive_alarm.servicename)

                if creator:
                    drive_alarm.creator = creator
                if servicename:
                    drive_alarm.servicename = servicename
                if time_delta:
                    drive_alarm.time_delta = time_delta
                if cycle:
                    drive_alarm.time_cycle = cycle
                if panel_number:
                    drive_alarm.alarm_number = int(panel_number)
                if panel_image_width:
                    drive_alarm.panel_image_width = int(panel_image_width)
                if panel_max_height:
                    drive_alarm.panel_max_height = int(panel_max_height)
                
                return no_update


            ###报警配置框的确认按钮关闭功能定义
            @app.callback(
                Output("modal_config", "is_open"),
                [Input("alarm_config", "n_clicks"), Input('confirm', 'n_clicks'),],
                [State("modal_config", "is_open")],
            )
            def toggle_modal_2(n1,n2,is_open):
                if n1 or n2:
                    return not is_open
                return is_open
        except:
            app.config.external_stylesheets.append('/static/style.css')

            @app.server.route('/static/<resource>')
            def serve_static_3(resource):
                print('resource',resource)
                STATIC_PATH = os.path.join(os.getcwd(), 'demo_project\static')

                print('STATIC_PATH',STATIC_PATH)
                return flask.send_from_directory(STATIC_PATH, resource)

            @app.callback(
                Output('card_output', 'children'),
                Output("tips_button", "children"),
                Input('apply', 'n_clicks'),
                Input('interval_1m', 'n_intervals')
                # prevent_initial_call=True
            )
            def card_output_fun_3(n1,intervals):
                """
                更新card
                """
                # print('更新card')
                # global drive_alarm
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                card, count,len = drive_alarm.card_output_fun()
                tip = "上次刷新时间：{}，共{}条显示{}条, 点击查询全部".format(current_time,count,len), 

                return card,tip


            ### 初始化报警创建者
            @app.callback(
                    Output("alert_creator", "options"),
                    Input('alert_creator', 'id')
                )
            def init_creator_list_3(id):
                # global creator

                # print('creator',creator)

                ans = []
                for x in creator_list:
                    ans.append({
                        "label": x,
                        "value": x
                    })
                return ans



            ### 更新报警服务的下拉框
            @app.callback(
                    [Output("alert_tbl_ServiceName", "options"), Output("memory_service_info", "data")],
                    Input('alert_creator', 'value'),
                    
                )
            def init_service_list_3(creator):
                """
                初始化服务列表
                """
                # print('*************')
                # global SERVER_HOST

                print('creator check',creator)

                if creator is not None:

                    res = user_list_api(SERVER_HOST,creator)
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

            ##### 根据报警配置的信息更新drive_alarm的初始化参数
            @app.callback(
                Output('confirm', 'n_clicks'), 
                Input('confirm', 'n_clicks'),
                State('alert_tbl_ServiceName', 'value'),
                State('alert_creator', 'value'),
                State('filter_hours', 'value'),
                State('update_cycle', 'value'),
                State('panel_show_number', 'value'),
                State('panel_image_width', 'value'),
                State('panel_max_height'  , 'value'),
                prevent_initial_call=True
            )
            def update_config_3(n1,servicename,creator,time_delta,cycle,panel_number,panel_image_width,panel_max_height):
                print('servicename',servicename)
                # print('time_delta',time_delta)
                # print('cycle',cycle)
                # global drive_alarm

                # print('creator new',creator)
                print('service_name old',drive_alarm.servicename)

                if creator:
                    drive_alarm.creator = creator
                if servicename:
                    drive_alarm.servicename = servicename
                if time_delta:
                    drive_alarm.time_delta = time_delta
                if cycle:
                    drive_alarm.time_cycle = cycle
                if panel_number:
                    drive_alarm.alarm_number = int(panel_number)
                if panel_image_width:
                    drive_alarm.panel_image_width = int(panel_image_width)
                if panel_max_height:
                    drive_alarm.panel_max_height = int(panel_max_height)
                
                return no_update


            ###报警配置框的确认按钮关闭功能定义
            @app.callback(
                Output("modal_config", "is_open"),
                [Input("alarm_config", "n_clicks"), Input('confirm', 'n_clicks'),],
                [State("modal_config", "is_open")],
            )
            def toggle_modal_3(n1,n2,is_open):
                if n1 or n2:
                    return not is_open
                return is_open
    #### card 报警列表框
    # print('panel_callback start')
    # app.config.external_stylesheets.append([dbc.themes.BOOTSTRAP,'/static/style.css'])
    # app.config.external_stylesheets.append(['/static/style.css'])
    # app.config.external_stylesheets=['/static/style.css',dbc.themes.BOOTSTRAP]
    # try:
    #     app.config.external_stylesheets.append('/static/style.css')
        
    #     @app.server.route('/static/<resource>')
    #     @authenticate_admin
    #     # def serve_static(resource):
    #     #     return None
    #     # def serve_static(resource):
    #     #     # print('resource',resource)
    #     #     STATIC_PATH = os.path.join(os.getcwd(), 'drive_screen\static')

    #     #     print('STATIC_PATH',STATIC_PATH)
    #     #     return flask.send_from_directory(STATIC_PATH, resource)

    #     ### 更新周期变更
    #     @app.callback(
    #         Output('interval_1m', 'interval'),
    #         Input('confirm', 'n_clicks'),
    #         State('update_cycle', 'value'),
    #     )
    #     @update_cycle_fun
    #     # def update_cycle_fun(n1,n):
    #     #     # print('interval_new',1000*int(n))
    #     #     return 1000*int(n)

    #     @app.callback(
    #         Output('card_output', 'children'),
    #         Output("tips_button", "children"),
    #         Input('apply', 'n_clicks'),
    #         Input('interval_1m', 'n_intervals'),
            
    #         # prevent_initial_call=True
    #     )
    #     @card_output_deco(drive_alarm)
    #     # def card_output_fun(n1,intervals,drive_alarm):
    #     #     """
    #     #     更新card
    #     #     """
    #     #     # print('更新card')
    #     #     # global drive_alarm
    #     #     current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #     #     card, count,len = drive_alarm.card_output_fun()
    #     #     tip = "上次刷新时间：{}，共{}条显示{}条, 点击查询全部".format(current_time,count,len), 

    #     #     return card,tip


    #     ### 初始化报警创建者
    #     @app.callback(
    #             Output("alert_creator", "options"),
    #             Input('alert_creator', 'id')
    #         )
    #     @init_creator_list_deco(creator_list)
    #     # def init_creator_list(id):
    #     #     # global creator

    #     #     # print('creator',creator)

    #     #     ans = []
    #     #     for x in creator_list:
    #     #         ans.append({
    #     #             "label": x,
    #     #             "value": x
    #     #         })
    #     #     return ans



    #     ### 更新报警服务的下拉框
    #     @app.callback(
    #             [Output("alert_tbl_ServiceName", "options"), Output("memory_service_info", "data")],
    #             Input('alert_creator', 'value'),
                
    #         )
    #     @init_service_list_deco(SERVER_HOST)
    #     # def init_service_list(creator):
    #     #     """
    #     #     初始化服务列表
    #     #     """
    #     #     # print('*************')
    #     #     # global SERVER_HOST

    #     #     # print('creator check',creator)

    #     #     if creator is not None:

    #     #         res = user_list_api(SERVER_HOST,creator)
    #     #         records = res['data']['records']

    #     #         ans, cache = [], {}
    #     #         for x in records:
    #     #             ans.append({
    #     #                 "label": x["service_name"],
    #     #                 "value": x["service_name"]
    #     #             })
    #     #             cache[x["id"]] = x["service_name"]
    #     #         return ans, cache
    #     #     else:
    #     #         return no_update, no_update


    #     ###报警配置框的确认按钮关闭功能定义
    #     @app.callback(
    #         Output("modal_config", "is_open"),
    #         [Input("alarm_config", "n_clicks"), Input('confirm', 'n_clicks'),],
    #         [State("modal_config", "is_open")],
    #     )
    #     @toggle_modal_fun
    #     def compile_1():
    #         pass    
    # except:
    #     app.config.external_stylesheets.append('/static/style.css')
        
    #     @app.server.route('/static/<resource>')
    #     @authenticate_admin
    #     # def serve_static(resource):
    #     #     return None
    #     # def serve_static(resource):
    #     #     # print('resource',resource)
    #     #     STATIC_PATH = os.path.join(os.getcwd(), 'drive_screen\static')

    #     #     print('STATIC_PATH',STATIC_PATH)
    #     #     return flask.send_from_directory(STATIC_PATH, resource)

    #     ### 更新周期变更
    #     @app.callback(
    #         Output('interval_1m', 'interval'),
    #         Input('confirm', 'n_clicks'),
    #         State('update_cycle', 'value'),
    #     )
    #     @update_cycle_fun
    #     # def update_cycle_fun(n1,n):
    #     #     # print('interval_new',1000*int(n))
    #     #     return 1000*int(n)

    #     @app.callback(
    #         Output('card_output', 'children'),
    #         Output("tips_button", "children"),
    #         Input('apply', 'n_clicks'),
    #         Input('interval_1m', 'n_intervals'),
            
    #         # prevent_initial_call=True
    #     )
    #     @card_output_deco(drive_alarm)
    #     # def card_output_fun(n1,intervals,drive_alarm):
    #     #     """
    #     #     更新card
    #     #     """
    #     #     # print('更新card')
    #     #     # global drive_alarm
    #     #     current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #     #     card, count,len = drive_alarm.card_output_fun()
    #     #     tip = "上次刷新时间：{}，共{}条显示{}条, 点击查询全部".format(current_time,count,len), 

    #     #     return card,tip


    #     ### 初始化报警创建者
    #     @app.callback(
    #             Output("alert_creator", "options"),
    #             Input('alert_creator', 'id')
    #         )
    #     @init_creator_list_deco(creator_list)
    #     # def init_creator_list(id):
    #     #     # global creator

    #     #     # print('creator',creator)

    #     #     ans = []
    #     #     for x in creator_list:
    #     #         ans.append({
    #     #             "label": x,
    #     #             "value": x
    #     #         })
    #     #     return ans



    #     ### 更新报警服务的下拉框
    #     @app.callback(
    #             [Output("alert_tbl_ServiceName", "options"), Output("memory_service_info", "data")],
    #             Input('alert_creator', 'value'),
                
    #         )
    #     @init_service_list_deco(SERVER_HOST)
    #     # def init_service_list(creator):
    #     #     """
    #     #     初始化服务列表
    #     #     """
    #     #     # print('*************')
    #     #     # global SERVER_HOST

    #     #     # print('creator check',creator)

    #     #     if creator is not None:

    #     #         res = user_list_api(SERVER_HOST,creator)
    #     #         records = res['data']['records']

    #     #         ans, cache = [], {}
    #     #         for x in records:
    #     #             ans.append({
    #     #                 "label": x["service_name"],
    #     #                 "value": x["service_name"]
    #     #             })
    #     #             cache[x["id"]] = x["service_name"]
    #     #         return ans, cache
    #     #     else:
    #     #         return no_update, no_update


    #     ###报警配置框的确认按钮关闭功能定义
    #     @app.callback(
    #         Output("modal_config", "is_open"),
    #         [Input("alarm_config", "n_clicks"), Input('confirm', 'n_clicks'),],
    #         [State("modal_config", "is_open")],
    #     )
    #     @toggle_modal_fun
    #     def compile_2():
    #         pass

    # dynamic_function_loader.load("def foo{i}():\n    return 'bar'")

    # @app.callback(
    #     Output("modal_config", "id"),
    #     [Input("alarm_config", "n_clicks"), Input('confirm', 'n_clicks'),],
    #     [State("modal_config", "is_open")],
    # )
    # try:
    #     if i ==1:
    #         return dynamic_function_loader.load("def foo{i}():\n    return 'bar'")
    # except Exception as e:
    #     print(e)
    #     return no_update
    # exec(dynamic_function_loader.load("def foo{i}():\n    return 'bar'"))

    # @retry()
    # def foo():
    #     pass
    # compile('def gfg(): return "GEEKSFORGEEKS"', "<string>", "exec")
    # @exception_handler
    # def toggle_modal_1(n):
    
    #     return no_update
   