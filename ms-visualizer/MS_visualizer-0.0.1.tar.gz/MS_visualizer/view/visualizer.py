import datetime


import dash
from dash import html, dcc, MATCH, ALL
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from MS_visualizer.components.components import create_slider, \
    create_text_input, \
    create_button, \
    create_dropdown, \
    create_plot, \
    create_radio_box, \
    create_min_max_input, \
    create_min_max_input_with_step, \
    create_checkbox, \
    create_headline_button, \
    create_textfield_input, \
    create_clustered_plot, \
    create_searchable_dropdown, \
    create_table, \
    create_bar_chart, \
    create_distribution_plots

from examples.get_data import get_opentims_data, memoized_get_opentims_data, memoized_get_bounds, get_bounds
from MS_visualizer.server import app, cache, Timeout
from MS_visualizer.controller.func import memoized_min_max_values, get_data_path_options, create_table_df, \
    bin_3D_points, max_vote
from MS_visualizer.assets.plotly_colors import css_colors, get_discrete_color_swatches
from MS_visualizer.utils.json_import import create_form_from_scheme, get_id_list

from MS_visualizer.controller.db_interaction import create_standard_user, create_save_dict, save_to_db, get_new_id, \
    get_options, get_loaded_value, get_algo_options, get_algorithm

import pandas as pd
import numpy as np
import opentimspy
import pathlib
import plotly.express as px
import hdbscan
import json
import importlib
import pathlib

# CONFIG
RT_START = 1200
RT_STOP = 1500
FRAME_START = 10
FRAME_STOP = 50
MZ_MIN = 550
MZ_MAX = 551
TOF_MIN = 196000
TOF_MAX = 200000
TRANSFORMED_MZ_MIN = 100
TRANSFORMED_MZ_MAX = 200
SCAN_MIN = 1
SCAN_MAX = 450
INV_ION_M_MIN = 0.6
INV_ION_M_MAX = 1.5
MIN_INTENSITY = 10
DEFAULT_PATH = "/mnt/ms/old/rawdata/gutamine/RAW/G221201_004_Slot1-1_1_7804.d"
BASE_PATH = "/mnt/ms/old/rawdata/gutamine/RAW"
JSON_PATH = "../examples/hdbscan_scaled_basic.json"
DEFAULT_CUSTER_PATH = "MS_visualizer.cluster_algorithms.hdbscan_scaled_basic"

sub = importlib.import_module(DEFAULT_CUSTER_PATH, ".")

# Layout
visualizer = html.Div([

    # store if the graph shows the raw or clustered data
    dcc.Store(id="last_button_id"),

    html.Div(id="test", children=None),

    dcc.Download(id="json_download"),

    html.Div([
        html.Div([
            dbc.Row([
                dbc.Col([  # headline - H3 replaced with button to collapse row
                    # html.H3("Data:"),
                    create_headline_button({"type": "collapse_section_button", "index": 0}, "Data △")
                ], width=3, className="d-grid gap-2"),
                dbc.Col([  # settings column
                    dbc.Collapse([
                        dbc.Row([
                            html.Div(id="refresh_id"),
                            create_searchable_dropdown("data_path_id", "Path", get_data_path_options(BASE_PATH),
                                                       DEFAULT_PATH),
                            create_searchable_dropdown("settings_options", "Saved Settings:", get_options()),
                            create_checkbox("parameters_only", "",
                                            [{"label": "load only algorithm parameter", "value": True}], [True]),
                        ]),
                        html.Br(),
                        create_button("load_settings", "Load from DB"),
                        html.Br(),
                        # create_textfield_input("json_settings", "Copy Json:", "Copy Json content here"),
                        # html.Br(),
                        # create_button("load_json_settings", "Load from Json"),
                        # html.Br(),
                    ], id={"type": "collapse_section_id", "index": 0}, is_open=True)
                ]),
            ]),
        ], className="input_group"),
        html.Br(),

        html.Div([
            dbc.Row([
                dbc.Col([
                    # html.H3("Axes:"),  # headline
                    create_headline_button({"type": "collapse_section_button", "index": 1}, "Axes △")
                ], width=3, className="d-grid gap-2"),
                dbc.Col([  # settings column
                    dbc.Collapse([
                        html.Label("Select Axes for filtering:"),
                        html.Br(),
                        html.Br(),
                        create_radio_box("x_axis", "X Axis:",
                                         [{"label": "mz", "value": "mz"}, {"label": "tof", "value": "tof"},
                                          {"label": "transformed_mz", "value": "transformed_mz"}], "mz"),
                        create_radio_box("y_axis", "Y Axis:", [{"label": "retention_time", "value": "retention_time"},
                                                               {"label": "frame", "value": "frame"}], "retention_time"),
                        create_radio_box("z_axis", "Z Axis:",
                                         [{"label": "inv_ion_mobility", "value": "inv_ion_mobility"},
                                          {"label": "scan", "value": "scan"}], "scan"),
                        html.Br(),
                        html.Label("Select Axes shown in the graph:"),
                        html.Br(),
                        html.Br(),
                        create_radio_box("x_axis_graph", "X Axis:",
                                         [{"label": "mz", "value": "mz"}, {"label": "tof", "value": "tof"},
                                          {"label": "transformed_mz", "value": "transformed_mz"}], "mz"),
                        create_radio_box("y_axis_graph", "Y Axis:",
                                         [{"label": "retention_time", "value": "retention_time"},
                                          {"label": "frame", "value": "frame"}], "retention_time"),
                        create_radio_box("z_axis_graph", "Z Axis:",
                                         [{"label": "inv_ion_mobility", "value": "inv_ion_mobility"},
                                          {"label": "scan", "value": "scan"}], "scan"),
                        html.Br(),
                        # TODO implement resolution with transformed_mz
                        # create_slider("resolution", "resolution:", min_=5000, max_=150000, step=1000,
                        #               default_value=DEFAULT_RESOLUTION),
                    ], id={"type": "collapse_section_id", "index": 1}, is_open=True)
                ]),
            ]),
        ], className="input_group"),
        html.Br(),

        html.Div([
            dbc.Row([
                dbc.Col([
                    # html.H3("MS-1 filter:"),  # headline
                    create_headline_button({"type": "collapse_section_button", "index": 2}, "MS-1 filter △")
                ], width=3, className="d-grid gap-2"),
                dbc.Col([  # settings column
                    dbc.Collapse([
                        dcc.Store(id="min_max_values_x", storage_type='session'),
                        dcc.Store(id="min_max_values_y", storage_type='session'),
                        dcc.Store(id="min_max_values_z", storage_type='session'),
                        html.Div(id="x_axis_value"),
                        html.Div(id="y_axis_value"),
                        html.Div(id="z_axis_value"),
                        html.Br(),
                        create_slider("min_intensity", "min intensity:", default_value=MIN_INTENSITY, min_=0, max_=500),
                        create_checkbox("multiply_charged_only", "", [{"label": "multiply charged only", "value": True}], []),
                    ], id={"type": "collapse_section_id", "index": 2}, is_open=True)
                ]),
            ]),
        ], className="input_group"),
        html.Br(),

        html.Div([
            dbc.Row([
                dbc.Col([
                    # html.H3("MS-1 Points:"),  # headline
                    create_headline_button({"type": "collapse_section_button", "index": 3}, "MS-1 Points △")
                ], width=3, className="d-grid gap-2"),
                dbc.Col([  # settings column
                    dbc.Collapse([
                        dbc.Row([
                            dbc.Col(
                                create_slider("opacity", "opacity:", min_=0.1, max_=1, step=0.1, default_value=0.5), ),
                            dbc.Col(create_slider("point_size", "point size:", min_=0.1, max_=5, step=0.1,
                                                  default_value=2.5), ),
                        ]),
                        dbc.Row([
                            dbc.Col(create_dropdown("color_scale", "color scale:",
                                                    [{"label": i, "value": i} for i in
                                                     sorted(px.colors.named_colorscales())],
                                                    value="inferno")),
                            dbc.Col(create_dropdown("paper_bgcolor", "Graph background color:",
                                                    [{"label": i, "value": i} for i in css_colors],
                                                    value="lightsteelblue")),
                        ]),
                        html.Br(),
                        create_button("plot-raw-data-button", "Plot Raw Data", disabled=True),
                    ], id={"type": "collapse_section_id", "index": 3}, is_open=True)
                ]),
            ]),
        ], className="input_group"),
        html.Br(),

        html.Div([
            dbc.Row([
                dbc.Col([
                    create_headline_button({"type": "collapse_section_button", "index": 4}, "Algorithm △")
                ], width=3, className="d-grid gap-2"),
                dbc.Col([  # settings column
                    dbc.Collapse([
                        create_dropdown("algorithm_selection", "Algorithm: ", get_algo_options(), 2)
                    ], id={"type": "collapse_section_id", "index": 4}, is_open=True)
                ]),
            ]),
        ], className="input_group"),
        html.Br(),

        html.Div([
            dbc.Row([
                dbc.Col([
                    # html.H3("MS-1 HDBSCAN:"),  # headline
                    create_headline_button({"type": "collapse_section_button", "index": 5}, "Clustering △")
                ], width=3, className="d-grid gap-2"),
                dbc.Col([  # settings column - no need for the person input, because there will be a log in
                    dbc.Collapse([

                        html.Div(id="algorithm_config"),

                        create_checkbox("speed_up", "", [{"label": "speed up", "value": True}], []),
                        dbc.Row([
                            dbc.Col(create_dropdown("score", "Score:", [{"label": "★★★★★", "value": 5},
                                                                        {"label": "★★★★", "value": 4},
                                                                        {"label": "★★★", "value": 3},
                                                                        {"label": "★★", "value": 2},
                                                                        {"label": "★", "value": 1}], 3)),
                            dbc.Col(
                                create_dropdown("cluster_color", "Cluster Color:", [{"label": i, "value": i} for i in
                                                                                    sorted(
                                                                                        get_discrete_color_swatches())],
                                                "Alphabet")),
                        ]),

                        html.Br(),
                        dbc.Row([
                            create_textfield_input("comment", "Comment:"),
                        ]),

                        html.Br(),
                        dbc.Row([
                            dbc.Col(create_button("save_settings_button", "save settings")),
                            # dbc.Col(create_button("save_to_json_button", "save as json")),
                            dbc.Col(create_button("plot_clustered_data", "Cluster", disabled=True)),
                        ])
                    ], id={"type": "collapse_section_id", "index": 5}, is_open=True)
                ]),
            ]),
        ], className="input_group"),
        html.Br(),

    ], className="group input"),

    html.Div([
        html.Div([  # output div - will show the graph
            html.Div(id="graph_output"),
        ], className="graph"),
        html.Br(),
        html.Div([  # output div - will show the graph
            html.Div(id="table_output"),
        ], className="table"),
    ], className="group output")

], className="page_group")


# Callbacks

@app.callback(
    Output({"type": "collapse_section_id", "index": MATCH}, "is_open"),
    Output({"type": "collapse_section_button", "index": MATCH}, "children"),
    Input({"type": "collapse_section_button", "index": MATCH}, "n_clicks"),
    State({"type": "collapse_section_id", "index": MATCH}, "is_open"),
    State({"type": "collapse_section_button", "index": MATCH}, "children"),
)
def toggle_collapse(n_clicks, is_open, button_text):
    if n_clicks != 0:
        if "△" in button_text:
            button_text = button_text.replace("△", "▽")
        elif "▽" in button_text:
            button_text = button_text.replace("▽", "△")
        else:
            pass
        return not is_open, button_text
    return is_open, button_text


@app.callback(
    Output("load_settings", "disabled"),
    Input("settings_options", "value")
)
def enable_disable_button(value):
    if value != "":
        return False
    return True


@app.callback(
    Output("data_path_id", "options"),
    Input("data_path_id", "value"),
)
def reload_options(selected_data):
    return get_data_path_options(BASE_PATH)


# Set values for the inputs or loaded values
@app.callback(
    Output("data_path_id", "value"),
    Output("min_intensity", "value"),
    Output("algorithm_config", "children"),
    Output("algorithm_selection", "value"),
    Output("test", "children"),
    Input("data_path_id", "children"),
    Input("load_settings", "n_clicks"),
    Input("algorithm_selection", "value"),
    State("parameters_only", "value"),
    State("settings_options", "value"),
    State("data_path_id", "value"),
    State("min_intensity", "value"),
    State("x_axis", "value"),
    State("y_axis", "value"),
    State("z_axis", "value"),
)
def input_default(path, n_clicks, algorithm_selection, parameters_only, loaded_value, data_path, min_intensity, x_axis,
                  y_axis, z_axis):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split('.')[0]

    global sub
    global JSON_PATH

    if button_id == "load_settings":

        algorithm_id = get_loaded_value("Evaluation", loaded_value, "algorithm").id

        loading_path = get_algorithm(algorithm_id, "loading_path")
        sub = importlib.import_module(loading_path, ".")

        scheme_path = get_algorithm(algorithm_id, "scheme_path")
        scheme = json.load(open(scheme_path))

        if parameters_only:
            return data_path, min_intensity, \
                   create_form_from_scheme(json.loads(scheme), x_axis, y_axis, z_axis), \
                   algorithm_id, ""

        return get_loaded_value("Filter", loaded_value, "path_to_data_folder"), \
               get_loaded_value("Filter", loaded_value, "min_intensity"), \
               create_form_from_scheme(scheme, x_axis, y_axis, z_axis), \
               algorithm_id, ""


    elif button_id == "algorithm_selection":
        loading_path = get_algorithm(algorithm_selection, "loading_path")
        sub = importlib.import_module(loading_path, ".")

        scheme_path = get_algorithm(algorithm_selection, "scheme_path")
        scheme = json.load(open(scheme_path))

        return data_path, min_intensity, create_form_from_scheme(scheme, x_axis, y_axis,
                                                                 z_axis), algorithm_selection, None



    if path is None:
        f = open(JSON_PATH)
        return DEFAULT_PATH, MIN_INTENSITY, create_form_from_scheme(
            json.load(f), x_axis, y_axis, z_axis), algorithm_selection, None
    else:
        f = open(JSON_PATH)
        return path, MIN_INTENSITY, create_form_from_scheme(json.load(f), x_axis, y_axis,
                                                            z_axis), algorithm_selection, None


# update the label in the algorithm parameters - only for hdbscan scaled
@app.callback(
    Output({"type": "algorithm_settings_label", "index": 12}, "children"),
    Input("x_axis", "value"),
    State("algorithm_selection", "value"),
)
def update_label(x_axis, algorithm_selection):
    if algorithm_selection == 3:
        try:
            return x_axis + " scale:"
        except:
            raise PreventUpdate

    raise PreventUpdate


# update the label in the algorithm parameters - only for hdbscan scaled
@app.callback(
    Output({"type": "algorithm_settings_label", "index": 13}, "children"),
    Input("y_axis", "value"),
    State("algorithm_selection", "value"),
)
def update_label(y_axis, algorithm_selection):
    if algorithm_selection == 3:
        try:
            return y_axis + " scale:"
        except:
            raise PreventUpdate

    raise PreventUpdate


# update the label in the algorithm parameters - only for hdbscan scaled
@app.callback(
    Output({"type": "algorithm_settings_label", "index": 14}, "children"),
    Input("z_axis", "value"),
    State("algorithm_selection", "value"),
)
def update_label(z_axis, algorithm_selection):
    if algorithm_selection == 3:
        try:
            return z_axis + " scale:"
        except:
            raise PreventUpdate

    raise PreventUpdate


# load algorithm settings
@app.callback(
    Output({"type": "algorithm_settings", "index": ALL}, "value"),
    Input("test", "children"),
    State("settings_options", "value"),
    State({"type": "algorithm_settings", "index": ALL}, "value"),
    prevent_initial_call=True,
)
def load_settings(child, loaded_value, test):
    if child is not None:
        dict_ = json.loads(get_loaded_value("Evaluation", loaded_value, "algorithm_settings"))
        list_ = list(dict_.values())
        return list_
    else:
        raise dash.exceptions.PreventUpdate


# x axis selection
@app.callback(
    Output("x_axis_value", "children"),
    Output("x_axis", "value"),
    Output("min_max_values_x", "data"),
    Output("settings_options", "options"),
    Input("x_axis", "value"),
    Input("load_settings", "n_clicks"),
    State("settings_options", "value"),
    State("data_path_id", "value"),
    State("parameters_only", "value"),
    State("min_max_values_x", "data"),
)
def update(value, n_clicks, loaded_value, data_path, parameters_only, min_max):
    ctx = dash.callback_context

    button_id = ctx.triggered[0]["prop_id"].split('.')[0]

    if min_max is not None:
        MIN = min_max["min"]
        MAX = min_max["max"]

    if button_id == "load_settings" and not parameters_only:
        if n_clicks != 0:
            value = get_loaded_value("Filter", loaded_value, "x_axis_label")
            MIN = get_loaded_value("Filter", loaded_value, "min_x")
            MAX = get_loaded_value("Filter", loaded_value, "max_x")
            min_max = {"min": MIN, "max": MAX}

    if data_path is None:
        data_path = DEFAULT_PATH

    data = memoized_get_bounds(data_path)

    if value == "mz":
        if button_id != "load_settings":
            MIN = MZ_MIN
            MAX = MZ_MAX
            min_max = {"min": MIN, "max": MAX}
        return html.Div([
            create_min_max_input("x_start", "x_stop", "number", "m/z:", min_=data["mz"][0], max_=data["mz"][1],
                                 default_value=[MIN, MAX]),
        ]), value, min_max, get_options()
    elif value == "tof":
        if button_id != "load_settings":
            MIN = TOF_MIN
            MAX = TOF_MAX
            min_max = {"min": MIN, "max": MAX}
        return html.Div([
            create_min_max_input("x_start", "x_stop", "number", "tof:", min_=data["tof"][0], max_=data["tof"][1],
                                 default_value=[MIN, MAX]),
        ]), value, min_max, get_options()
    else:
        if button_id != "load_settings":
            MIN = TRANSFORMED_MZ_MIN
            MAX = TRANSFORMED_MZ_MAX
            min_max = {"min": MIN, "max": MAX}
        return html.Div([
            create_min_max_input("x_start", "x_stop", "number", "transformed mz:",
                                 default_value=[MIN, MAX]),
        ]), value, min_max, get_options()


# y axis selection
@app.callback(
    Output("y_axis_value", "children"),
    Output("y_axis", "value"),
    Output("min_max_values_y", "data"),
    Input("y_axis", "value"),
    Input("load_settings", "n_clicks"),
    State("settings_options", "value"),
    State("data_path_id", "value"),
    State("parameters_only", "value"),
    State("min_max_values_y", "data"),
)
def update(value, n_clicks, loaded_value, data_path, parameters_only, min_max):
    ctx = dash.callback_context

    button_id = ctx.triggered[0]["prop_id"].split('.')[0]

    if min_max is not None:
        MIN = min_max["min"]
        MAX = min_max["max"]

    if button_id == "load_settings" and not parameters_only:
        if n_clicks != 0:
            value = get_loaded_value("Filter", loaded_value, "y_axis_label")
            MIN = get_loaded_value("Filter", loaded_value, "min_y")
            MAX = get_loaded_value("Filter", loaded_value, "max_y")
            min_max = {"min": MIN, "max": MAX}

    if data_path is None:
        data_path = DEFAULT_PATH

    data = memoized_get_bounds(data_path)

    if value == "retention_time":
        if button_id != "load_settings":
            MIN = round(RT_START / 60, 3)
            MAX = round(RT_STOP / 60, 3)
            min_max = {"min": MIN, "max": MAX}
        return html.Div([
            create_min_max_input("y_start", "y_stop", "number", "Rt:", min_=round(data["retention_time"][0] / 60, 4),
                                 max_=round(data["retention_time"][1] / 60, 4),
                                 default_value=[MIN, MAX]),
        ]), value, min_max
    else:
        if button_id != "load_settings":
            MIN = FRAME_START
            MAX = FRAME_STOP
            min_max = {"min": MIN, "max": MAX}
        return html.Div([
            create_min_max_input("y_start", "y_stop", "number", "Frame:", min_=data["frame"][0],
                                 max_=data["frame"][1],
                                 default_value=[MIN, MAX]),
        ]), value, min_max


# z axis selection
@app.callback(
    Output("z_axis_value", "children"),
    Output("z_axis", "value"),
    Output("min_max_values_z", "data"),
    Output("plot_clustered_data", "disabled"),
    Output("plot-raw-data-button", "disabled"),
    Input("z_axis", "value"),
    Input("load_settings", "n_clicks"),
    State("settings_options", "value"),
    State("data_path_id", "value"),
    State("parameters_only", "value"),
    State("min_max_values_z", "data"),
)
def update(value, n_clicks, loaded_value, data_path, parameters_only, min_max):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split('.')[0]

    if min_max is not None:
        MIN = min_max["min"]
        MAX = min_max["max"]

    if button_id == "load_settings" and not parameters_only:
        if n_clicks != 0:
            value = get_loaded_value("Filter", loaded_value, "z_axis_label")
            MIN = get_loaded_value("Filter", loaded_value, "min_z")
            MAX = get_loaded_value("Filter", loaded_value, "max_z")
            min_max = {"min": MIN, "max": MAX}

    if data_path is None:
        data_path = DEFAULT_PATH

    data = get_bounds(data_path)

    if value == "scan":
        if button_id != "load_settings":
            MIN = SCAN_MIN
            MAX = SCAN_MAX
            min_max = {"min": MIN, "max": MAX}
        return html.Div([
            create_min_max_input("z_start", "z_stop", "number", "Scan:", min_=data["scan"][0],
                                 max_=data["scan"][1],
                                 default_value=[MIN, MAX]),
        ]), value, min_max, False, False
    else:
        if button_id != "load_settings":
            MIN = INV_ION_M_MIN
            MAX = INV_ION_M_MAX
            min_max = {"min": MIN, "max": MAX}
        return html.Div([
            create_min_max_input_with_step("z_start", "z_stop", "number", "inv ion mobility:",
                                           min_=data["inv_ion_mobility"][0],
                                           max_=data["inv_ion_mobility"][1],
                                           default_value=[MIN, MAX],
                                           step=0.1)
        ]), value, min_max, False, False


# button callback
@app.callback(
    Output("graph_output", "children"),
    Output("last_button_id", "data"),
    Output("table_output", "children"),

    Input("plot-raw-data-button", "n_clicks"),
    Input("plot_clustered_data", "n_clicks"),

    Input("opacity", "value"),
    Input("point_size", "value"),
    Input("color_scale", "value"),
    Input("paper_bgcolor", "value"),

    Input("x_axis_graph", "value"),
    Input("y_axis_graph", "value"),
    Input("z_axis_graph", "value"),

    State("multiply_charged_only", "value"),

    State("x_axis", "value"),
    State("y_axis", "value"),
    State("z_axis", "value"),

    State("data_path_id", "value"),
    State("x_start", "value"),
    State("x_stop", "value"),
    State("y_start", "value"),
    State("y_stop", "value"),
    State("z_start", "value"),
    State("z_stop", "value"),
    State("min_intensity", "value"),

    State("last_button_id", "data"),

    State("cluster_color", "value"),
    State("speed_up", "value"),
    State({"type": "algorithm_settings", "index": ALL}, "value"),

    prevent_initial_call=True
)
# @cache.memoize(timeout=Timeout)
def graph_callback(raw_data_button, clustered_data_button, opacity, point_size, color_scale, paper_bgcolor,
                   x_axis_graph, y_axis_graph, z_axis_graph, multiply_charged_only,
                   x_axis, y_axis, z_axis, data_path, x_start, x_stop, y_start, y_stop, z_start, z_stop, min_intensity,
                   last_button_id, cluster_color, speed_up, *args):
    # check which callback triggered
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        button_id = ctx.triggered[0]["prop_id"].split('.')[0]
        if button_id == "plot-raw-data-button" or button_id == "plot_clustered_data":
            last_button_id = button_id

        data_path = pathlib.Path(data_path)

        # check if all start stop values are set correctly
        if x_start is None or x_stop is None or y_start is None or y_stop is None or z_start is None or z_stop is None:
            return "Not all values are set", last_button_id, ""
        if x_start >= x_stop or y_start >= y_stop or z_start >= z_stop:
            return "Supplied minimal value was greater or equal to the maximal value", last_button_id, ""

        if y_axis == "retention_time":
            # convert min to sec
            y_start = y_start * 60
            y_stop = y_stop * 60

        extents = {
            x_axis: (x_start, x_stop),
            y_axis: (y_start, y_stop),
            z_axis: (z_start, z_stop)
        }

        if multiply_charged_only:
            df = get_opentims_data(
                data_path=data_path,
                min_intensity=min_intensity,
                constraint="inv_ion_mobility <= 0.4467452 + 0.00101627*mz and inv_ion_mobility <= 0.5301116 + 0.000849*mz",
                **extents
            )
        else:
            df = get_opentims_data(
                data_path=data_path,
                min_intensity=min_intensity,
                **extents
            )


        if y_axis == "retention_time":
            # convert sec to min
            df["retention_time"] = df["retention_time"].map(lambda retention_time: retention_time / 60)

    if button_id == "plot-raw-data-button" or last_button_id == "plot-raw-data-button":

        if df.empty:
            return "No Data for selected Settings", last_button_id, ""
        else:

            return create_plot('data_plot', df, x_axis_graph, y_axis_graph, z_axis_graph, opacity, point_size,
                               color_scale,
                               paper_bgcolor), last_button_id, ""

    elif button_id == "plot_clustered_data" or last_button_id == "plot_clustered_data":

        if df.empty:
            return "No Data for selected Settings", last_button_id, ""
        else:

            df = sub.cluster(df, x_axis, y_axis, z_axis, *args[0])  # args[0] are the values from the json input scheme
            digits = {
                x_axis: 1,
                y_axis: 1,
                z_axis: 1,
            }
            summary_ops = {
                'intensity': np.sum,  # total intensity in a voxel
                'cluster': max_vote,  # max vote on the voxel's cluster label
                'probability': max_vote,
            }
            if x_axis != x_axis_graph:
                summary_ops[x_axis_graph] = max_vote
            if y_axis != y_axis_graph:
                summary_ops[y_axis_graph] = max_vote
            if z_axis != z_axis_graph:
                summary_ops[z_axis_graph] = max_vote

            if speed_up:
                df = bin_3D_points(df, digits, summary_ops)

            table_df = create_table_df(df)

            # TODO implement display_probability_by_pointsize instead of False - but some algorithms don't return it
            return create_clustered_plot('data_plot', df, x_axis_graph, y_axis_graph, z_axis_graph, opacity, point_size,
                                         paper_bgcolor, cluster_color, False), \
                   last_button_id, \
                   html.Div([
                       create_bar_chart("bar_chart", table_df, "cluster", "number"),
                       create_distribution_plots("test", df, x_axis_graph, y_axis_graph, z_axis_graph)
                   ])

    return "", last_button_id, ""


@app.callback(
    # Output("settings_options", "options"),
    # Output("json_download", "data"),
    Output("refresh_id", "children"),

    Input("save_settings_button", "n_clicks"),
    # Input("save_to_json_button", "n_clicks"),

    # get all the information

    # Evaluation
    State("score", "value"),
    State("comment", "value"),

    # Filter
    State("x_axis", "value"),
    State("y_axis", "value"),
    State("z_axis", "value"),
    State("data_path_id", "value"),
    State("x_start", "value"),
    State("x_stop", "value"),
    State("y_start", "value"),
    State("y_stop", "value"),
    State("z_start", "value"),
    State("z_stop", "value"),
    State("min_intensity", "value"),
    State("algorithm_selection", "value"),
    State("algorithm_selection", "value"),

    # Algorithm
    State({"type": "algorithm_settings", "index": ALL}, "value"),

    prevent_initial_call=True
)
def save_button_action(n_clicks, score, comment, x_axis_label, y_axis_label, z_axis_label,
                       data_path, x_start, x_stop, y_start, y_stop, z_start, z_stop, min_intensity, algorithm_selection,
                       algorithm_id, *args):
    ctx = dash.callback_context

    button_id = ctx.triggered[0]["prop_id"].split('.')[0]

    # if the save button was clicked - save config to the database
    if n_clicks != 0:

        # create a user if there is none
        create_standard_user()

        # create evaluation
        scheme_path = get_algorithm(algorithm_selection, "scheme_path")
        scheme = json.load(open(scheme_path))
        algo_settings = dict(zip(get_id_list(scheme), args[0]))

        if comment is None:
            comment = ""

        evaluation = create_save_dict(
            score=score,
            created=datetime.datetime.now(),
            algorithm_settings=json.dumps(algo_settings),
            user=1,
            algorithm=algorithm_selection,
            comment=comment
        )

        # create filter
        filter_ = create_save_dict(
            min_x=x_start,
            max_x=x_stop,
            min_y=y_start,
            max_y=y_stop,
            min_z=z_start,
            max_z=z_stop,
            min_intensity=min_intensity,
            x_axis_label=x_axis_label,
            y_axis_label=y_axis_label,
            z_axis_label=z_axis_label,
            path_to_data_folder=data_path,
            evaluation=get_new_id(),
        )

        if button_id == "save_settings_button":
            # save to database
            save_to_db(["Evaluation", "Filter"], [evaluation, filter_])

        # update the options from the dropdown
        return dcc.Location(id="refresh_location", href="/visualizer")
