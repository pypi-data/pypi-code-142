#!/share/nas2/genome/biosoft/Python//3.7.3/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/7 15:49
# @Author : jmzhang
# @Email : zhangjm@biomarker.com.cn
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)

import json
import time
import numpy as np
import dash_bootstrap_components as dbc

N = 150000
data = pd.read_csv('data_set/demo_data.txt', sep='\t')

app.layout = html.Div(
    [
        html.Label('Point size'),
        dbc.Input(
            id='point_size',
            type="number",
            placeholder="point size",
            min=0.000001,
            value=1,
            style={'width': 80}
        ),
        dcc.Graph(id='graph'),
        html.Div(id='text')
    ]
)


@app.callback(
    Output('graph', 'figure'),
    [Input('point_size', 'value')])
def display_graph(point_size):
    fig = go.Figure(go.Scattergl(x=data['__x'], y=data['__y'],
                                 marker=dict(size=point_size),
                                 mode='markers'))
    fig.update_layout(uirevision='size')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
