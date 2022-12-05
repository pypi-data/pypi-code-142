import datetime
import time
from io import StringIO

import pytz
import streamlit as st
import pandas as pd
import numpy as np
import toml
import requests
import json
from urllib import parse
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


def templates1():
    st.sidebar.title('演示范例')
    st.sidebar.button('我是按钮')
    agree = st.sidebar.checkbox('复选框')

    if agree:
        st.sidebar.write('选中了复选框！')

    genre = st.sidebar.radio(
        "我是单选框",
        ('我是一', '我是二', '我是三'))

    if genre == '我是一':
        # 选中判断
        st.sidebar.write('我选中了"我是一"')
    if genre == '我是二':
        # 选中判断
        st.sidebar.write('我选中了"我是二"')
    if genre == '我是三':
        # 选中判断
        st.sidebar.write('我选中了"我是三"')


def templates2():
    st.sidebar.title('演示范例')
    options = st.sidebar.multiselect(
        '我是多选框',
        ['条件一', '条件二', '条件三', '条件四'],
        ['条件一', '条件一'])

    st.sidebar.write('您选中的内容为:', options)

    uploaded_file = st.sidebar.file_uploader("单个文件上传")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.sidebar.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.sidebar.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.sidebar.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.sidebar.write(dataframe)

    uploaded_files = st.sidebar.file_uploader("多个文件上传", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.sidebar.write("文件名称:", uploaded_file.name)
        st.sidebar.write(bytes_data)


def templates3():
    d = st.sidebar.date_input(
        "请选择时间范围：",
        [datetime.date(2022, 7, 28), datetime.date(2022, 8, 28)])
    st.sidebar.write('选中的时间范围是:', d)

    d = st.sidebar.date_input(
        "请选择时间：",
        datetime.date(2022, 7, 28))
    st.sidebar.write('选中的时间是:', d)

    number = st.sidebar.number_input('插入的数字或浮点数', min_value=0, help='范例示范')
    st.sidebar.write('当前的值为 ', number)

    t = st.sidebar.time_input('输入时间', datetime.time(8, 45))  # 8为时，45为分钟
    st.sidebar.write('输入的时间为', t)


def templates4(star_times=0, end_times=0, vin_code='', signals='', ):
    st.warning('1.历史数据保留最近一个月，最大查询间隔三天。 2.最多导出60个信号数据。 3.图表以秒为单位展示，无数据进行补空，如所查询信号在此时间段内无任何数据则不显示。')
    tz = pytz.timezone('Asia/Shanghai')  # 东八区
    col1, col2, col3, col4 = st.columns(4)
    date_array = datetime.datetime.fromtimestamp(int(time.time()), tz)
    end_date_array = datetime.datetime.fromtimestamp(int(time.time()), tz)
    if int(star_times) > 0:
        date_array = datetime.datetime.fromtimestamp(int(star_times), tz)
    if int(end_times) > 0:
        end_date_array = datetime.datetime.fromtimestamp(int(end_times), tz)

    with col1:
        star_date = st.date_input(
            "请选择开始日期：", date_array, key='star_date')

    with col2:
        star_time = st.time_input('选择时间：', date_array, key='star_time')

    with col3:
        end_date = st.date_input(
            "请选择结束日期：", end_date_array, key='end_date')
    with col4:
        end_time = st.time_input('选择时间：', end_date_array, key='end_time')

    star_time = str(star_date) + ' ' + str(star_time)
    end_time = str(end_date) + ' ' + str(end_time)

    # 转换成时间数组
    star_time_array = time.strptime(star_time, "%Y-%m-%d %H:%M:%S")
    end_time_array = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    star_timestamp = time.mktime(star_time_array)
    end_timestamp = time.mktime(end_time_array)
    star_time = int(star_timestamp)
    end_time = int(end_timestamp)

    char_input = st.text_input(label='车架号', value=vin_code, placeholder='请输入车架号，目前支持单个查询')
    txt = st.text_area('信号名', signals, placeholder='请输入信号名，用英文逗号隔开')
    # 固定值测试
    # char_input = 'LW433B11XM1062283'
    # txt = 'AC_InsideAirTemp'
    # end_time = 1661252300
    # star_time = 1661165900

    enter_char = st.button('查询')

    if enter_char:
        # 确认查询
        if len(txt) > 0 and len(char_input) > 0:
            txt = txt.split(",")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
                'Content-Type': 'application/json;charset=UTF-8',
            }
            FormData = {'endTime': end_time,
                        'signals': txt,
                        'startTime': star_time,
                        'type': "s",
                        'downSample':'1m',
                        'vinCode': char_input,
                        "filterNull": 'false'
                        }
            # data = parse.urlencode(FormData)
            content = requests.post(
                'http://dip-data-api-openapi-prod.chj.cloud/dip-data-api-openapi/v3/vehicle/signals/all',
                data=json.dumps(FormData), headers=headers)
            content_data = json.loads(content.text)
            if content_data['code'] == 0:
                for i in range(len(txt)):
                    # name = content_data['data']['signals'][i]['signalName']
                    name = txt[i]
                    x = []
                    y = []
                    if len(content_data['data']['signals'][i]['dps']) == 0:
                        st.write(name + '暂无数据')
                    else:
                        for key, value in content_data['data']['signals'][i]['dps'].items():
                            # time_array = time.localtime(int(key))
                            # other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                            other_style_time = datetime.datetime.fromtimestamp(int(key), tz).strftime(
                                '%Y-%m-%d %H:%M:%S')
                            x.append(other_style_time)
                            if value is None:
                                y.append(None)
                            else:
                                if int(value) > 9999999999 or int(value) < 1000000000:
                                    y.append(value)
                                else:
                                    if 1000000000 < int(value) < 9999999999:
                                        # time_array = time.localtime(int(value))
                                        # other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                                        time_array = datetime.datetime.fromtimestamp(int(key), tz).strftime(
                                            '%Y-%m-%d %H:%M:%S')
                                        y.append(other_style_time)
                        # 方法可能被弃用了，无法获取到对应的方法
                        # fig = go.FigureWidget()
                        fig = go.Figure()
                        fig.add_trace(go.Scatter(x=x, y=y, name=name, connectgaps=False))
                        fig.update_layout(title='',
                                          xaxis_title='时间',
                                          yaxis_title=name
                                          )

                        st.plotly_chart(fig, use_container_width=True)
            else:
                st.error('接口报错：' + content_data['msg'])
        else:
            st.error('参数不全，请检查')
