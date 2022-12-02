import json
from dash import html
from dash.dependencies import State

import dash_bootstrap_components as dbc

from MS_visualizer.components.components import create_slider, \
    create_dropdown, \
    create_checkbox, \
    create_text_input


def create_form_from_scheme(dict_, x_axis, y_axis, z_axis):
    """
    :input: a json with all form elements
    :return: a dash div with the form
    """

    component_list = []
    checkbox_counter = 0

    c = 0

    for t in dict_["components"]:
        for x in t["values"]:
            if t["type"] == "dropdown":
                component_list.append(create_dropdown({"type": "algorithm_settings", "index": c},
                                                      x["label"], x["options"], x["default_value"]))
            elif t["type"] == "checkbox":

                if checkbox_counter == 3:  # this number indicates how many checkboxes will be in one row
                    checkbox_counter = 0

                if checkbox_counter == 0:
                    checkbox_counter = 0
                    row = []
                    component_list.append(dbc.Row(row))

                row.append(dbc.Col(create_checkbox({"type": "algorithm_settings", "index": c}, "",
                                                   [{"label": x["label"], "value": x["value"]}],
                                                   x["default_value"])))

                checkbox_counter += 1

            elif t["type"] == "text_input":
                component_list.append(create_text_input({"type": "algorithm_settings", "index": c},
                                                        "Number",
                                                        x["label"],
                                                        # min_=x["min"],
                                                        # max_=x["max"],
                                                        default_value=x["default_value"],
                                                        ))

            elif t["type"] == "slider":

                if x["label"] == "x scale:":
                    x["label"] = x_axis + " scale:"
                elif x["label"] == "y scale:":
                    x["label"] = y_axis + " scale:"
                elif x["label"] == "z scale:":
                    x["label"] = z_axis + " scale:"

                component_list.append(create_slider({"type": "algorithm_settings", "index": c},
                                                    x["label"],
                                                    {"type": "algorithm_settings_label", "index": c},
                                                    x["min"], x["max"], x["step"], x["default_value"]))

            c += 1

        component_list.append(html.Br())

    return html.Div(component_list)


def algorithm_states(scheme):
    states = []

    dict_ = json.loads(scheme)

    for t in dict_["components"]:
        for x in t["values"]:
            states.append(State(x["id"], "value"))

    return states


def get_id_list(scheme):
    id_list = []

    for t in scheme["components"]:
        for x in t["values"]:
            id_list.append(x["id"])

    return id_list
