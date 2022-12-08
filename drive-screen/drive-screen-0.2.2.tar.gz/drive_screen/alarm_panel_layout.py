import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from dash import Input, Output,State, callback


modal_config = [
           dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("报警配置")),
                    dbc.ModalBody(
                        [
                            html.P("请选择报警创建者"),
                            dcc.Dropdown(
                                id='alert_creator',
                                clearable=True,
                                className="dcc_control",
                                multi=False,
                            ),
                            html.P("请选择报警服务名"),
                            dcc.Dropdown(
                                id='alert_tbl_ServiceName',
                                # value='dt-casting-analysis',
                                # options=charts_biz.get_service_list(),
                                clearable=True,
                                className="dcc_control",
                                multi=False,
                            ),
                            html.Br(),
                            html.P("请输入显示最近多少小时的未处理报警",style={'padding': '20px 0px 0px 0px'},),
                            dcc.Input(id="filter_hours", type="text", placeholder="", style={'marginRight':'10px'}, value = '1'),
                           html.P("请输入每隔多少秒刷新一次(最小设置10s)" ,style={'padding': '20px 0px 0px 0px'}),
                            dcc.Input(id="update_cycle", type="text", placeholder="", style={'marginRight':'10px'}, value = '10'),
                            html.P("请输入每次最多显示多少条报警",style={'padding': '20px 0px 0px 0px'}),
                            dcc.Input(id="panel_show_number", type="text", placeholder="", style={'marginRight':'10px'}, value = '4'),
                            html.P("如果有图片，请输入图片的宽度",style={'padding': '20px 0px 0px 0px'}),
                            dcc.Input(id="panel_image_width", type="text", placeholder="", style={'marginRight':'10px'}, value = '300'),
                            html.P("报警卡片最大高度设置",style={'padding': '20px 0px 0px 0px'}),
                            dcc.Input(id="panel_max_height", type="text", placeholder="", style={'marginRight':'10px'}, value = '1000'),
                        ]
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "确认", id="confirm", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                # fullscreen = ['sm-down', 'md-down', 'lg-down', 'xl-down', 'xxl-down'],
                fullscreen = 'xxl-down',
                id="modal_config",
                is_open=False,
                centered=True
            ),
        ]

def alarm_panel_layout_fun(Front_Host, width = 5, height = 800):
    '''
    width: int, the width of the panel (1-12)
    height: int, the height of the panel in unit px
    
    '''
    if width>=4:

        card = dbc.Col(
                    dbc.Container([
                        dcc.Interval(id='interval_1m', interval = 60*1000, n_intervals=0),# ms
                        dcc.Store(id='memory_service_info'),
                        html.Div(children= modal_config),
                        dbc.Button('刷新',id= 'apply'),
                        dbc.Button('配置',id= 'alarm_config',style={"margin-left": "5px"}),
                        dbc.Button(id = 'tips_button',href=Front_Host+'/alert/list/', outline=True, color="success", className="me-1",style={"margin-left": "5px"}),
                        html.Br(),
                        dbc.Toast(
                            dbc.Container([
                                dbc.Container(
                                    id="card_output", 
                                    style={'padding': '0px 0px 0px 0px'},
                                    ),
                                ],
                                id="my_card", 
                                style={'padding': '0px 0px 0px 0px'},
                            ),
                            style={'overflow-y': 'scroll',"maxWidth": "2000px", 'width': 159*width,"height":height,'padding': '0px 0px 0px 0px'},
                        ),
                    ]
                    ),
                    width=width,
                    style={'padding': '0px 0px 0px 0px'},

                )
    else:
         card = dbc.Col(
                    dbc.Container([
                        dcc.Interval(id='interval_1m', interval = 60*1000, n_intervals=0),# ms
                        dcc.Store(id='memory_service_info'),
                        html.Div(children= modal_config),
                        # dbc.Row([
                        #     # dbc.Col(
                        #     #     dbc.Button('刷新',id= 'apply'),
                        #     #     width = 4
                        #     # ),
                        #     # dbc.Col(
                        #     #     dbc.Button('配置',id= 'alarm_config'),
                        #     #     width = 4
                        #     # ),
                        #     dbc.Button('刷新',id= 'apply'),
                        #     dbc.Button('配置',id= 'alarm_config',style={"margin-left": "5px"}),
                        #     ]
                        # ),
                        dbc.Button('刷新',id= 'apply'),
                        dbc.Button('配置',id= 'alarm_config',style={"margin-left": "5px"}),
                        dbc.Row(
                            dbc.Col(
                                dbc.Button(id = 'tips_button',href=Front_Host+'/alert/list/', outline=True, color="success", className="me-1"),
                            ),
                            style={"padding": "5px 0px 0px 0px"}
                        ),
                        dbc.Toast(
                            dbc.Container([
                                
                                dbc.Container(
                                    id="card_output",
                                    style={'padding': '0px 0px 0px 0px'},
                                    ),
                                ],
                                id="my_card",
                                style={'padding': '0px 0px 0px 0px'},
                            ),
                            # style={'overflow-y': 'scroll','overflow-x': 'hidden',"maxWidth": "2000px", 'width': 160*width,"height":height},
                            # style={"maxWidth": "2000px", 'width': 160*width,"height":height},
                            style={'overflow': 'scroll',"maxWidth": "2000px", 'width': 159*width,"height":height,'padding': '0px 0px 0px 0px'},

                        ),]
                    ),
                    width=width,
                )
        
    return card