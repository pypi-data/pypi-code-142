from dash import dcc, html
from dash.dependencies import Input, Output, State

import json

from MS_visualizer.components.components import create_text_input, create_button, create_textfield_input, create_table_from_db
from MS_visualizer.controller.db_interaction import add_to_db
from MS_visualizer.server import app

JSON_PATH = "../examples/hdbscan.json"
DEFAULT_CUSTER_PATH = "MS_visualizer.cluster_algorithms.hdbscan"

add_algorithm = html.Div([
    create_text_input("algorithm_name", "text", "Algorithm Name:", default_value="HDBSCAN"),
    create_textfield_input("description", "Description:", placeholder="Enter Description ..."),
    create_text_input("json_path", "text", "Scheme Path:", default_value=JSON_PATH),
    create_text_input("algorithm_path", "text", "Algorithm Loading Path:",
                      default_value=DEFAULT_CUSTER_PATH),
    html.Br(),
    create_button("save_algorithm", "Save Algorithm"),

    html.Div(id="show_algorithms"),

], className="input_group")


@app.callback(
    Output("show_algorithms", "children"),
    Input("save_algorithm", "n_clicks"),
    State("algorithm_name", "value"),
    State("description", "value"),
    State("json_path", "value"),
    State("algorithm_path", "value"),
)
def update(n_cklicks, algorithm_name, description, json_path, algorithm_path):

    if n_cklicks != 0:

        dict_ = {
            "name": algorithm_name,
            "description": description,
            "scheme_path": json_path,
            "loading_path": algorithm_path
        }
        add_to_db("Algorithm", dict_)

    return create_table_from_db(
        "algo_table",
        "Algorithm",
        {"Name": "name", "Description": "description", "Loading Path": "loading_path", "Scheme Path": "scheme_path"},
        title="Algorithms"
    )
