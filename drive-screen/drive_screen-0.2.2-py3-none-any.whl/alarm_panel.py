from itertools import cycle
import pandas as pd
import base64
import dash_bootstrap_components as dbc
import dash_html_components as html
import json
from dash.development.base_component import Component
from dash.dash import no_update
from PIL import Image, ImageDraw as D
from dash import dash_table,dcc
from io import BytesIO as _BytesIO
from drive_screen.alarm_api import *
from drive_screen.style import button_style_full,modal_info_style
import datetime


button_cn_map = {'valid_alarm_button':'有效报警','invalid_alarm_button':'无效报警','respond_button':'添加报警评论'}

class  DriveAlarmPanel(object):
    '''
    __init__ : 初始化参数

    method：
        modal_output_fun： 返回警弹出框
        card_output_fun: 返回报警卡片，符合筛选条件的报警个数，报警总个数
    '''

    def __init__(self,servicename,creator,time_delta = 1,time_cycle =10,SERVER_HOST=None,alarm_number =4,panel_image_width = 500,window_image_width = 400,panel_max_height = 1000, window_size = 'lg'):
        '''
        servicename: 告警服务名称
        creator : 创建者
        SERVER_HOST： api address
        time_delta: int,  unit:hour    recent hours you want to search the alarm
        time_cycle: int,  unit:minute  the update cycle
        panel_number: int, the number of panels you want to show
        panel_image_width": int,  unit:pixel  the width of the image in the panel 
        window_image_width: int,  unit:pixel  the width of the image in the window 
        panel_max_height: int,  unit:pixel  the maximum height of the panel 
        window_size: sm, lg, xl for small, large or extra large sized modals, or leave undefined for default size.
        
        '''
        # print('初始化类')
        self.servicename = servicename
        self.time_delta = time_delta
        self.time_cycle = time_cycle
        self.creator = creator
        self.SERVER_HOST = SERVER_HOST
        self.alarm_number = alarm_number
        self.panel_image_width = panel_image_width
        self.window_image_width = window_image_width
        self.panel_max_height = panel_max_height
        self.window_size = window_size

        if self.SERVER_HOST is None:
            print('SERVER_HOST is not defined')


    def b64_to_pil(self,image_base64, width = 0):
            
            image_base64 = image_base64.replace('data:image/.jpeg;base64,','')
            image_base64 = image_base64.replace('data:image/.png;base64,','')
            image_base64 = image_base64.replace('data:image/png;base64,','')
        #    data:image/png;base64,

            
    #         print(image_base64)
            decoded = base64.b64decode(image_base64)
            buffer = _BytesIO(decoded)
            im = Image.open(buffer)
            # if width  :
            origin_width, origin_height = im.size
            new_height = int(origin_height*width/origin_width)
            newsize = (width, new_height)
            im = im.resize(newsize)

            return im


    def display_modal2(self,i,data, feedback_key,width):
        print('开始 display_modal2')

        ans = []
        # show image
        if data.get("content").get("image_base64"):
            for index, img in enumerate(data.get("content").get("image_base64")):
                if 'data:image/' in img:
                    img_base64_encode = img.split(',')[1]
                else:
                    img_base64_encode = img

                    # print('image_base64_error',data.get("content").get("image_base64"))
                ans.append(
                    # dcc.Graph(id=f'annotation_{str(index)}', figure=b64_to_pil(img_base64_encode)),
                    html.Img(src=self.b64_to_pil(img_base64_encode,width=width)),
                )

        # text
        title, text = "", ""
        if data.get("content").get("alarm_title"):
            title += data.get("content").get("alarm_title") + "  "
        if data.get("content").get("message_title"):
            title += data.get("content").get("message_title")

        if data.get("content").get("message_text"):
            text += data.get("content").get("message_text")
        if title:
            ans.append(html.H5(title))
        if text:
            ans.append(html.P(text))

        # table
        if data.get("content").get("table"):
            ans.append(
                dbc.Table.from_dataframe(pd.DataFrame(json.loads(data.get("content").get("table"))), striped=True,
                                        bordered=True, hover=True)
            )

        # ans.extend(
        #     [
        #         html.Br(),
        #         html.Hr(className="my-2")
        #     ]
        # )
        # button
        buttons = []
        if data.get("content").get("buttons"):
            for obj in data.get("content").get("buttons"):
                buttons.append(
                    dbc.Button(obj.get("title"), href=obj.get("url"), outline=True, className="me-1"),
                    # dbc.Button("无效报警", outline=True, color="warning", className="me-1"),
                    # dbc.Button("添加评论", outline=True, color="secondary", className="me-1"),
                )
        additional_functions_mapping = {
            'valid_alarm_button': "/alarm/respond/valid/",
            'invalid_alarm_button': "/alarm/respond/invalid/",
            'respond_button': "/alarm/comment/",
        }
        if data.get("additional_functions"):
            for name in data.get("additional_functions"):
                buttons.append(
                    dbc.Button(
                        button_cn_map[name],
                        href=self.SERVER_HOST + additional_functions_mapping.get(name) + feedback_key,
                        outline=True, color="secondary", className="me-1"
                    )
                )
        button = [html.P(buttons, className="lead")]
        
        boder_nr = 'default'
        if 'severity' in data:
            severity = data.get("severity")
            if severity <= 20:
                boder_nr = 'green01'
            elif severity <= 40:
                boder_nr = 'green02'
            elif severity <= 60:
                boder_nr = 'yellow'
            elif severity <= 80:
                boder_nr = 'orange'
            elif severity <= 100:
                boder_nr = 'red'


        modal = dbc.Modal(
                    html.Div([
                        dbc.ModalHeader(
                            style = modal_info_style,
                            children = dbc.Label('alarm', style={'text-align': 'left', 'font-size': '150%','font-style': 'italic','font-weight':'bold','font-color': '#0057D8', 'text-transform': 'lowercase'}),
                            close_button = True,
                            class_name = "close-button"
                        ),
                        dbc.ModalBody(
                            children = ans
                        ),
                        dbc.ModalFooter(
                            style = modal_info_style,
                            children = button  
                        ), 
                    ],
                    
                    className='divBorder_'+boder_nr,
                ),
                backdrop = 'static',
                is_open=True,
                centered=True,
                size=self.window_size,
                fullscreen = 'sm-down', #'md-down', 'lg-down', 'xl-down', 'xxl-down',
                scrollable=True,
                style={"max-width": "none", "width": "90%"},
            )

        print('结束 display_modal2')
        

        return modal



    def display_modal1(self, i, data,feedback_key):
        print('开始 display_modal1')
        ans = []
        # text
        title, text = "", ""
        if data.get("content").get("title"):
            title += data.get("content").get("title") + "  "
        if data.get("content").get("sub_title"):
            title += data.get("content").get("sub_title")

        if data.get("content").get("message_text"):
            text += data.get("content").get("message_text")
        if title:
            ans.append(html.H5(title))
        if text:
            ans.append(html.P(text))

        # table
        if data.get("content").get("table"):
            ans.append(
                dbc.Table.from_dataframe(pd.DataFrame(json.loads(data.get("content").get("table"))), striped=True,
                                        bordered=True, hover=True)
            )

        # print('ans1',ans)
        buttons = []
        if data.get("content").get("buttons"):
            for obj in data.get("content").get("buttons"):
                buttons.append(
                    dbc.Button(obj.get("title"), href=obj.get("url"), outline=True,  className="me-1"),
                    # dbc.Button("无效报警", outline=True, color="warning", className="me-1"),
                    # dbc.Button("添加评论", outline=True, color="secondary", className="me-1"),
                )
        additional_functions_mapping = {
            'valid_alarm_button': "/alarm/respond/valid/",
            'invalid_alarm_button': "/alarm/respond/invalid/",
            'respond_button': "/alarm/comment/",
        }
        if data.get("additional_functions"):
            for name in data.get("additional_functions"):
                buttons.append(
                    dbc.Button(
                        button_cn_map[name],
                        href=self.SERVER_HOST + additional_functions_mapping.get(name) + feedback_key,
                        outline=True, color="secondary", className="me-1"
                    )
                )
        button = [html.P(buttons, className="lead")]


        # print('ans2',ans)
        boder_nr = 'default'
        if 'severity' in data:
            severity = data.get("severity")
            if severity <= 20:
                boder_nr = 'green01'
            elif severity <= 40:
                boder_nr = 'green02'
            elif severity <= 60:
                boder_nr = 'yellow'
            elif severity <= 80:
                boder_nr = 'orange'
            elif severity <= 100:
                boder_nr = 'red'

        modal = dbc.Modal(
                    html.Div([
                        dbc.ModalHeader(
                            style = modal_info_style,
                            children = dbc.Label('alarm', style={'text-align': 'left', 'font-size': '150%','font-style': 'italic','font-weight':'bold','font-color': '#0057D8', 'text-transform': 'lowercase'}),
                            close_button = True,
                            class_name = "close-button"
                        ),
                        dbc.ModalBody(
                            children = ans,
                            style={"overflow": "scroll"},
                        ),
                        dbc.ModalFooter(
                            style = modal_info_style,
                            children = button  
                        ), 
                        ],
                        className='divBorder_'+boder_nr
                    ),
                    backdrop = 'static',
                    is_open=True,
                    # centered=True,
                    size=self.window_size,
                    # fullscreen = 'sm-down', #'md-down', 'lg-down', 'xl-down', 'xxl-down',
                    # scrollable=True,
                    style={"max-width": "none", "width": "90%"},
                    id = f'modal_{i}',
                )
                
        print('结束 display_modal1')
        
        return modal



    def modal_output_fun(self,interval,children):
        print('开始modaloutput')

        start_time = '2022-07-06 15:01:06'
        end_time = '2022-07-06 16:00:06'

        # start_time = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(seconds=int(interval/1000)+5) ,'%Y-%m-%d %H:%M:%S')
        # end_time = datetime.datetime.strftime(datetime.datetime.now() ,'%Y-%m-%d %H:%M:%S')

        print('start_time',start_time)
        print('end_time',end_time)
        print('servicename',self.servicename)

        filter1 = {'username': self.servicename, 'start_time': start_time, 'end_time': end_time, 'read':True, 'status':''}
        order = {'field':'create_time', 'direction':'desc'}

        print(filter1)
    
        # res = requests.get(f"{SERVER_HOST}/alarm/list", json={"filter": filter}, verify=False).json()
        # res = requests.get(f"{SERVER_HOST}/alarm/list", json={"filter": filter1,'order':order,'page':1, 'size':4}, verify=False).json()
        res = alarm_list_api(self.SERVER_HOST,filter1,order,1,self.alarm_number)

        # print(res)

        if res['data']['records']==[]:

            print('no_update')

            return no_update

        else:
            print('has_update')

            alarm_data = res['data']['records']

            modal_list = []


            for i in alarm_data:
                data = i["content"]
                feedback_key = i["feedback_key"]
                template = i["content"]["template"]
                # print(template)

                if template in ('message+image_v2', 'message+image_v1'):
                    modal_list.append(self.display_modal2(i, data,feedback_key,width=self.window_image_width))
                elif template == "message_only_v1":
                    modal_list.append(self.display_modal1(i, data,feedback_key))
            

            # print('modal_list',modal_list)
            if children is None:
                children = []
            children.extend(modal_list)
        
            
            return children 

    def screen_msgiv1(self,data,create_time, feedback_key):

        ans_table,ans_title,ans_text,ans_button = [],[],[],[]

        # text
        title, text = "", ""
        if data.get("content").get("title"):
            title += data.get("content").get("title")
        if data.get("content").get("sub_title"):
            text += data.get("content").get("sub_title")

        if title:
            ans_title.append(html.H5(title))
        if text:
            ans_text.append(html.P(text))
        
        # print('ans_title',ans_title)
        # print('ans_text',ans_text)


        # table
        if data.get("content").get("table"):
            df_table = pd.DataFrame(json.loads(data.get("content").get("table")))
            if df_table.shape[0]>3:
                df_table = df_table.iloc[0:3,:]
            ans_table.append(      
                dbc.Table.from_dataframe(
                    df_table, striped=True, bordered=True, hover=True,size = 'sm',responsive =True,
                    style={'padding': '0px 0px 0px 0px'},
                )
            )

        if data.get("content").get("buttons"):
            for obj in data.get("content").get("buttons"):
                ans_button.append(
                    dbc.Button(obj.get("title"), href=obj.get("url"), outline=True, color="secondary",  className="me-1"),
                    # dbc.Button('无效报警', href=obj.get("url"), outline=True, color="success", className="me-1"),

                    # dbc.Button("无效报警", outline=True, color="warning", className="me-1"),
                    # dbc.Button("添加评论", outline=True, color="secondary", className="me-1"),
                )
        additional_functions_mapping = {
            'valid_alarm_button': "/alarm/respond/valid/",
            'invalid_alarm_button': "/alarm/respond/invalid/",
            'respond_button': "/alarm/comment/",
        }
        if data.get("additional_functions"):
            for name in data.get("additional_functions"):
                ans_button.append(
                    dbc.Button(
                        button_cn_map[name],
                        href=self.SERVER_HOST + additional_functions_mapping.get(name) + feedback_key,
                        outline=True, color="secondary", className="me-1",style={'padding': '0px 0px 0px 0px'},
                    )
                )

        
        boder_nr = 'default'
        if 'severity' in data:
            severity = data.get("severity")
            if severity <= 20:
                boder_nr = 'green01'
            elif severity <= 40:
                boder_nr = 'green02'
            elif severity <= 60:
                boder_nr = 'yellow'
            elif severity <= 80:
                boder_nr = 'orange'
            elif severity <= 100:
                boder_nr = 'red'

        if ans_table!=[]:
            card = [dbc.Toast(
                        dbc.Row([
                            dbc.Col(
                                ans_table,
                                width=9,
                                style={'padding': '0px 2px 0px 15px'},
                            ),
                            dbc.Col([
                                html.P(
                                    '报警时间：'+create_time,
                                    className="card-text",
                                    style={'padding': '0px 10px 0px 0px'},
                                ),
                                html.P(
                                    ans_title,
                                    className="card-text",
                                    style={'padding': '0px 0px 0px 0px'},
                                ),
                                html.P(
                                    ans_text,
                                    className="card-text",
                                    style={'padding': '0px 0px 0px 0px'},
                                ),
                                dbc.Col(ans_button,
                                    style={"flexWrap":"nowrap",'padding': '0px 0px 0px 0px'}
                                ),
                                ],
                                width=3,
                                style={'padding': '0px 0px 0px 0px'},
                            )
                            ],
                            style={'padding': '0px 0px 0px 0px'},

                        ),
                        className='divBorder_'+boder_nr,
                        # style={'padding': '0px 5px 0px 0px'},
                        style={"maxWidth": "2000px", "width":800,"maxHeight":self.panel_max_height,'padding': '0px 30px 0px 0px'},


                    )
                ]
        else:
            card = [dbc.Toast(
                        dbc.Row([
                            dbc.Col([
                                html.P(
                                    '报警时间：'+create_time,
                                    className="card-text",
                                    style={'padding': '0px 10px 0px 0px'},
                                ),
                                html.P(
                                    ans_title,
                                    className="card-text",
                                    style={'Margin': '0px 0px 0px 0px'},
                                ),
                                html.P(
                                    ans_text,
                                    className="card-text",
                                    style={'Margin': '0px 0px 0px 0px'},
                                ),
                                dbc.Col(ans_button,
                                    style={"flexWrap":"nowrap",'padding': '0px 0px 0px 0px'}
                                ),
                                ],
                                style={'padding': '0px 0px 0px 0px'},
                            ),
                            ],
                            style={'padding': '0px 0px 0px 0px'},
                        ),
                        className='divBorder_'+boder_nr,
                        # style={'padding': '0px 5px 0px 0px'},
                        style={"maxWidth": "2000px", "width":800,"maxHeight":self.panel_max_height,'padding': '0px 30px 0px 0px'},
                    )
                ]

        card.extend([html.Div(dcc.Markdown('''---''',),style={'padding': '0px 0px 0px 0px'})])
            
        return  card



    def screen_msgiv2(self,data, create_time,feedback_key,width):

        ans_image_table,ans_title,ans_text,ans_button = [],[],[],[]
        # show image
        if data.get("content").get("image_base64"):
            for index, img in enumerate(data.get("content").get("image_base64")):
                if 'data:image/' in img:
                    img_base64_encode = img.split(',')[1]
                else:
                    img_base64_encode = img

                    # print('image_base64_error',data.get("content").get("image_base64"))
                ans_image_table.append(
                    # dbc.Card(
                        dbc.Col(
                            # dcc.Graph(id=f'annotation_{str(index)}', figure=generator_figure(img_base64_encode,width=400)),
                            # dcc.Graph(id=f'annotation_{str(index)}', figure=b64_to_pil(img_base64_encode,width=400)),
                            # b64_to_pil(img_base64_encode,width=400),
                            # html.Img(src=self.b64_to_pil(img_base64_encode,width=width), className="img_responsive"),
                            html.Img(src=self.b64_to_pil(img_base64_encode,width=width),
                            style={'padding': '0px 0px 0px 0px'},),
                            # html.Img(src=self.b64_to_pil(img_base64_encode,width=width), className="img-fluid"),
                            # width = 6
                        ),
                    )

        if data.get("content").get("table"):
            df_table = pd.DataFrame(json.loads(data.get("content").get("table")))
            if df_table.shape[0]>3:
                df_table = df_table.iloc[0:3,:]
            ans_image_table.append(      
                dbc.Table.from_dataframe(
                    df_table, striped=True, bordered=True, hover=True,size = 'sm',responsive =True,
                    style={'padding': '0px 0px 0px 0px'},
                )
            )
                # )

        # text
        title, text = "", ""
        if data.get("content").get("alarm_title"):
            title += data.get("content").get("alarm_title") + "  "
        if data.get("content").get("message_title"):
            title += data.get("content").get("message_title")

        if data.get("content").get("message_text"):
            text += data.get("content").get("message_text")
        if title:
            ans_title.append(html.H5(title))
        if text:
            ans_text.append(html.P(text))

        # table
        

        # ans.extend(
        #     [
        #         html.Br(),
        #         html.Hr(className="my-2")
        #     ]
        # )
        # button
        if data.get("content").get("buttons"):
            for obj in data.get("content").get("buttons"):
                ans_button.append(
                    dbc.Button(obj.get("title"), href=obj.get("url"), outline=True, color="secondary",  className="me-1",style={'padding': '0px 0px 0px 0px'},),
                    # dbc.Button('无效报警', href=obj.get("url"), outline=True, color="success", className="me-1"),

                    # dbc.Button("无效报警", outline=True, color="warning", className="me-1"),
                    # dbc.Button("添加评论", outline=True, color="secondary", className="me-1"),
                )
        additional_functions_mapping = {
            'valid_alarm_button': "/alarm/respond/valid/",
            'invalid_alarm_button': "/alarm/respond/invalid/",
            'respond_button': "/alarm/comment/",
        }
        if data.get("additional_functions"):
            for name in data.get("additional_functions"):
                ans_button.append(
                    dbc.Button(
                        button_cn_map[name],
                        href=self.SERVER_HOST + additional_functions_mapping.get(name) + feedback_key,
                        outline=True, color="secondary", className="me-1",style={'padding': '0px 0px 0px 0px'},
                    )
                )
        boder_nr = 'default'
        if 'severity' in data:
            severity = data.get("severity")
            if severity <= 20:
                boder_nr = 'green01'
            elif severity <= 40:
                boder_nr = 'green02'
            elif severity <= 60:
                boder_nr = 'yellow'
            elif severity <= 80:
                boder_nr = 'orange'
            elif severity <= 100:
                boder_nr = 'red'


        card = [dbc.Toast(
                    dbc.Row([
                        dbc.Col(
                            ans_image_table,
                            width=9,
                            style={'padding': '0px 2px 0px 15px'},

                        ),
                        dbc.Col([
                            html.P(
                                '报警时间：'+create_time,
                                className="card-text",
                                style={'padding': '0px 10px 0px 0px'},
                            ),
                            html.P(
                                ans_title,
                                className="card-text",
                                style={'padding': '0px 10px 0px 0px'},
                            ),
                            html.P(
                                ans_text,
                                className="card-text",
                                style={'padding': '0px 10px 0px 0px'},
                            ),
                            dbc.Col(ans_button,
                                style={"flexWrap":"nowrap",'padding': '0px 0px 0px 0px'}
                            ),
                            ],
                            width=3,
                            style={'padding': '0px 0px 0px 0px'},
                        )
                        ],
                        style={'padding': '0px 0px 0px 0px'},

                    ),
                    # style={"border":"2px black solid dashed solid double"},
                    # style={"border":"2px black solid   "},
                    className='divBorder_'+boder_nr,
                    # style={'padding': '0px 0px 0px 0px'},
                    style={"maxWidth": "2000px", "width":800,"maxHeight":self.panel_max_height,'padding': '0px 30px 0px 0px'},
                )
            ]

        # card.extend([dcc.Markdown('''---''',style={'padding': '0px 0px 0px 0px'},)])
        card.extend([html.Div(dcc.Markdown('''---''',),style={'padding': '0px 0px 0px 0px'})])


        return card

    def card_output_fun(self):
        # print('开始cardoutput')
        # start_time = '2022-07-05 08:01:06'
        # end_time = '2022-07-05 20:01:06'
        # start_time = '2022-07-06 15:01:06'
        # end_time = '2022-07-06 16:00:06'
        start_time = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(hours=int(self.time_delta)) ,'%Y-%m-%d %H:%M:%S')
        end_time = datetime.datetime.strftime(datetime.datetime.now() ,'%Y-%m-%d %H:%M:%S')
        # start_time = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(hours=100) ,'%Y-%m-%d %H:%M:%S')
        # end_time = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(hours=99),'%Y-%m-%d %H:%M:%S')
        # print('time_delta',self.time_delta)

        # print('start_time',start_time)
        # print('end_time',end_time)
        # print('servicename',self.servicename)

        filter1 = {'username': self.servicename, 'start_time': start_time, 'end_time': end_time, 'read':False}
        order = {'field':'create_time', 'direction':'desc'}

        # print(filter1)
    
        # res = requests.get(f"{SERVER_HOST}/alarm/list", json={"filter": filter}, verify=False).json()
        # res = requests.get(f"{SERVER_HOST}/alarm/list", json={"filter": filter1,'order':order,'page':1, 'size':4}, verify=False).json()
        res = alarm_list_api(self.SERVER_HOST,filter1,order,1,self.alarm_number)

        # print(res)

        if res['data']['records']==[]:

            return [
                    html.Br(),
                    html.Br(),
                    html.P('未查询到报警')
                ],0,0

        else:
            alarm_data = res['data']['records']
            
            card_output = []

            # return [html.P("测试card_output new")]
            count = res['data']['filter_count']
            
            for i in alarm_data:
                create_time = i['createTime']
                data = i["content"]
                feedback_key = i["feedback_key"]
                template = i["content"]["template"]
                # print(template)
                # print('create_time',create_time)

                if template in ('message+image_v2', 'message+image_v1'):
                    card_output.extend(self.screen_msgiv2(data,create_time, feedback_key,width=self.panel_image_width))
                elif template == "message_only_v1":
                    card_output.extend(self.screen_msgiv1(data, create_time,feedback_key))
            
            # card_output.insert(0,
            #                     dbc.Row([
            #                             # dbc.Col(
            #                             #     dbc.Alert("显示最近1小时的4条最新报警，共{}条报警".format(5), color="success"),
            #                             #     width = '100px'
            #                             # ),
            #                             dbc.Col(
            #                                 dbc.Button("显示最近1小时的4条最新报警，共{}条报警, 点击查询更多报警信息".format(5), href='https://www.baidu.com', outline=True, color="success", className="me-1")
            #                                 # width = '40px'
            #                             ),
            #                             dcc.Markdown('''---''')
            #                         ] ,
            #                         style = {'padding': '0px 0px 10px 0px'}                                 
            #                     )
            #                 )
    
            return card_output ,count,len(res['data']['records'])