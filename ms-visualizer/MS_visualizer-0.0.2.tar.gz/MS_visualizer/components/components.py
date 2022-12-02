# functions to create page components quickly (e.g. dropdown_menus, sliders, ..)

from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import dash_table

import plotly.graph_objects as go
# from plotly.graph_objects.Figure import add_trace
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

from time import time

from MS_visualizer.controller.db_interaction import general_query

pd.set_option('display.max_columns', None)


# create the navbar on top of the page
def create_navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Visualizer", href="/visualizer")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Add Algorithm", href="/add-algorithm")
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="MS_visualizer",
        brand_href="/",
        color="secondary",
        dark=True,
    )


# create a text input
def create_text_input(id_, type_, label, placeholder="Enter ...", min_=0, max_=10000, default_value=""):
    return html.Div([
        dbc.Label(label),
        dbc.Input(id=id_, placeholder=placeholder, type=type_, min=min_, max=max_, value=default_value)
    ])


# create a textfield input
def create_textfield_input(id_, label, placeholder="Enter ..."):
    return html.Div([
        dbc.Label(label),
        dbc.Textarea(id=id_, placeholder=placeholder)
    ])


# create a slider with some defaults
def create_slider(id_, label, label_id=None, min_=1, max_=100, step=1, default_value=10):
    if label_id is None:
        label_id = id_ + "label"
    return html.Div([
        dbc.Row([
            dbc.Col(dbc.Label(label, id=label_id), width=3),
            dbc.Col(dcc.Slider(min_, max_, step, value=default_value, id=id_, marks=None,
                               tooltip={"placement": "bottom", "always_visible": True})),
        ]),
    ])


# create a rangeslider with some defaults
def create_rangeslider(id_, label, min_=1, max_=100, step=1, default_value=[10, 20]):
    return html.Div([
        dbc.Label(label),
        dcc.RangeSlider(min_, max_, step, value=default_value, id=id_, marks=None,
                        tooltip={"placement": "bottom", "always_visible": True}),
    ])


def create_min_max_input(id_1, id_2, type_, label, placeholder="Enter ...", min_=0, max_=10000, default_value=["", ""]):
    return html.Div([
        dbc.Label(label),
        dbc.Row([
            dbc.Col(
                dbc.Input(id=id_1, placeholder=placeholder, type=type_, min=min_, max=max_, value=default_value[0]), ),
            dbc.Col(
                dbc.Input(id=id_2, placeholder=placeholder, type=type_, min=min_, max=max_, value=default_value[1]), ),
        ]),
    ])


def create_min_max_input_with_step(id_1, id_2, type_, label, placeholder="Enter ...", min_=0, max_=10000,
                                   default_value=["", ""], step=1):
    return html.Div([
        dbc.Label(label),
        dbc.Row([
            dbc.Col(
                dbc.Input(id=id_1, placeholder=placeholder, type=type_, min=min_, max=max_, value=default_value[0],
                          step=step), ),
            dbc.Col(
                dbc.Input(id=id_2, placeholder=placeholder, type=type_, min=min_, max=max_, value=default_value[1],
                          step=step), ),
        ]),
    ])


def create_dropdown(id_, label, options, value=""):
    return html.Div([
        dbc.Label(label),
        dbc.Select(id_, options=options, value=value),
    ])


def create_searchable_dropdown(id_, label, options, value=""):
    return html.Div([
        dbc.Label(label),
        dcc.Dropdown(id=id_, options=options, value=value, style={"color": "black"}),
    ])


def create_checkbox(id_, label, options, default_value=[]):
    return html.Div([
        dbc.Label(label),
        dbc.Checklist(
            options=options,
            value=default_value,
            id=id_,
        ),
    ])


def create_radio_box(id_, label, options, default_value):
    return html.Div([
        dbc.Row([
            dbc.Col(dbc.Label(label), width=3),
            dbc.Col(dbc.RadioItems(
                options=options,
                value=default_value,
                id=id_,
                inline=True,
            )),
        ], justify="start", )
    ])


def create_button(id_, label, disabled=False):
    return dbc.Button(label, id=id_, n_clicks=0, color="primary", className="button", outline=True, disabled=disabled)


def create_headline_button(id_, label):
    return dbc.Button(label, id=id_, n_clicks=0, color="primary", size="lg", className="me-1", outline=True)


def create_plot(id_, df, x_axis, y_axis, z_axis, opacity, point_size, color_scale, paper_bgcolor):
    hovertemplate_ = " "
    for i, col in enumerate(df.columns):
        hovertemplate_ = hovertemplate_ + col + ": %{customdata[" + str(i) + "]}<br>"

    fig = go.Figure(data=[go.Scatter3d(
        x=getattr(df, x_axis),
        y=getattr(df, y_axis),
        z=getattr(df, z_axis),
        mode="markers",
        customdata=df,
        hovertemplate=hovertemplate_ +
                      "<extra></extra>",
        marker=dict(
            size=point_size,
            opacity=opacity,
            color=np.log(df.intensity),
            colorscale=color_scale,
        )
    )],
    )

    fig.update_layout(scene={'xaxis': {'title': x_axis},
                             'yaxis': {'title': y_axis},
                             'zaxis': {'title': z_axis}},
                      # autosize=True,
                      # width=1000,
                      # height=1080,

                      paper_bgcolor=paper_bgcolor,
                      uirevision="Don't change"  # keep the zoom, tilt, ... from the user
                      )

    return dcc.Graph(id=id_, figure=fig, style={'width': '100%', 'height': '90vh'})


def create_clustered_plot(id_, df, x_axis, y_axis, z_axis, opacity, point_size, paper_bgcolor, cluster_color,
                          display_probability_by_pointsize):

    if display_probability_by_pointsize == [True]:
        up = True
    else:
        up = False


    color_dict = dict(list(enumerate(getattr(px.colors.qualitative, cluster_color))))

    hovertemplate_ = " "
    for i, col in enumerate(df.columns):
        hovertemplate_ = hovertemplate_ + col + ": %{customdata[" + str(i) + "]}<br>"

    if 'probability' in df:
        size = [point_size if l == -1 else point_size * 2 * p for l, p in
                zip(df.cluster, df.probability)]
    else:
        size = [3 if l == -1 else point_size for l in df.cluster]

    fig = go.Figure(data=[go.Scatter3d(
        x=getattr(df, x_axis),
        y=getattr(df, y_axis),
        z=getattr(df, z_axis),
        showlegend=True,
        mode="markers",
        customdata=df,
        hovertemplate=hovertemplate_ +
                      "<extra></extra>",
        marker=dict(
            size=size,
            color=['grey' if l == -1 else color_dict[l % len(color_dict)]
                   for l in df.cluster],
            opacity=opacity,
            line=dict(width=0)
        )
    )],
    )


    fig.update_layout(scene={'xaxis': {'title': x_axis},
                             'yaxis': {'title': y_axis},
                             'zaxis': {'title': z_axis}},
                      # autosize=True,
                      # width=1000,
                      # height=1080,

                      margin=dict(
                          l=10,
                          r=10,
                          b=10,
                          t=10
                      ),
                      paper_bgcolor=paper_bgcolor,
                      uirevision="Don't change"  # keep the zoom, tilt, ... from the user
                      )

    return dcc.Graph(id=id_, figure=fig, style={'width': '100%', 'height': '90vh'})


def create_table_from_db(id_, entity, query_dict, title=""):
    df = general_query(entity, query_dict)

    table = html.Div([
        html.H3(title),
        html.Br(),
        dash_table.DataTable(
            id=id_,
            data=df.to_dict('records'),
            style_cell={
                "backgroundColor": "#aabdbd",
                "color": "#002029"
            }
        )
    ])
    return table


def create_table(id_, df):
    table = html.Div([
        dash_table.DataTable(
            id=id_,
            data=df.to_dict('records'),
            style_cell={
                "backgroundColor": "#aabdbd",
                "color": "#002029"
            }
        )
    ])
    return table


def create_bar_chart(id_, df, x_axis, y_axis):
    fig = px.bar(df, x=x_axis, y=y_axis)
    fig.update_layout(margin=dict(
                          l=10,
                          r=10,
                          b=10,
                          t=10
                      ))
    return dcc.Graph(id=id_, figure=fig, style={'width': '100%', 'height': '30vh'})


def create_distribution_plots(id_, df, x_axis, y_axis, z_axis):

    df = df.groupby('cluster')

    fig = make_subplots(rows=4, cols=1, subplot_titles=(x_axis, y_axis, z_axis, "Size"))
    fig.add_trace(go.Histogram(x=df[x_axis].apply(lambda x: len(np.unique(x)))), row=1, col=1)
    fig.add_trace(go.Histogram(x=df[y_axis].apply(lambda x: len(np.unique(x)))), row=2, col=1)
    fig.add_trace(go.Histogram(x=df[z_axis].apply(lambda x: len(np.unique(x)))), row=3, col=1)
    fig.add_trace(go.Histogram(x=np.random.normal(size=100)), row=4, col=1)

    fig.data[3].x = df[x_axis].count()

    fig.update_traces(xbins=dict(
                            start=0.0,
                            end=50.0,
                            size=2
                     ))

    fig.update_layout(title_text="Cluster distributions", showlegend=False, autosize=True, margin=dict(
                          l=10,
                          r=10,
                          b=10,
                          t=50
                      ),)

    return dcc.Graph(id=id_, figure=fig, style={'width': '100%', 'height': '50vh'})
