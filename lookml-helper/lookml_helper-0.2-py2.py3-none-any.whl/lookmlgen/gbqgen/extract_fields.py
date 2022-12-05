# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import re
from textblob import Word  # making singulars and plurals

from .utils import *


# Get the tables with all fields and nesting for the GBQ Dimensions tables
def inspect_gbq(sql, verbose=False):
  CONFIGURATION = get_global_configuration()  
  if verbose:
    printDebug("==========\nQuerying:")
    printDebug(sql)
    printDebug("...")
  df = pd.io.gbq.read_gbq(sql, project_id = CONFIGURATION['gbq_project_id'])
  if verbose:
    printDebug("\t...loaded ", len(df), " records")
    # display(df)
  return df



# For convenience introduce the the mode
def get_gbq_mode(t, verbose=False):
  if t.startswith("ARRAY"):
    return "ARRAY"
  elif t.startswith("STRUCT"):
    return "STRUCT"
  else:
    return "FIELD"





# """### Create view and dimension names for all fields

# In the following we create the names of all views and dimensions for all attributes

# For arrays we need to construct 2 types of view/dimensions (e.g. patents: orange_book.ingredients)
# 1. UNNESTED: e.g. patents__orange_book__ingredients__unnested.ingredients
# 2. NESTED: patents.orange_book__ingredients

# There are a couple of complications:
# 1. We do not explicitely unnest structs - we simply reference them as struct.attribute
# 2. If an ARRAY is of a single variable (e.g. patents: researcher_ids) the attribute (researcher_ids) is part of the nested path names
# 3. We always add an unnest suffix to all unnested views and dimensions

# Furthermore we also create "nice" labels for each attribute both plural and singular. Users can define their own rules in the first section

# """


def get_parent_field_path(field_path):
    # Helper functions two split a field_path
    path_pat = re.compile(r"(.*?)\.?([^\.]+)$")
    return path_pat.search(field_path).group(1)


def get_array_parent_field_path(field_path, looker_metadata):
    parent_field_path = get_parent_field_path(field_path)
    if parent_field_path:
        parent_field = looker_metadata[looker_metadata.field_path == parent_field_path]
        assert len(parent_field) == 1  # paranoia
        parent_field = parent_field.iloc[0]

        if parent_field.modus == "STRUCT":
            return get_array_parent_field_path(parent_field.field_path, looker_metadata)
        else:
            return parent_field.field_path
    else:
        return ""


def get_attribute(field):
    parent_path_len = len(field.array_parent_field_path)
    if parent_path_len == 0:
        name = field.field_path
    else:
        name = field.field_path[parent_path_len + 1 :]
    return name.replace(".", "_")


def get_unnested_dimension_name(field):
    # a struct or an array of a struct does not represent a dimension and therefore the unnested dimension is empty
    # However ARRAY<STRING> is a repeat dimension and therefore it represents a dimension which we need to turn into a singular
    # FIELD of course are a dimension
    if field.data_type.startswith("ARRAY<STRUCT") or field.data_type.startswith(
        "STRUCT"
    ):
        dimension_name = ""
    elif field.data_type.startswith("ARRAY<"):
        # Often such an ARRAY is plural e.g. grid_ids ARRAY<STRING>
        # We need to singularise this. Hence we split by "_" and singularise the last part of it
        dimension_name = get_attribute(field)
        m = re.search(r"(.*?_?)([^\_]+)$", dimension_name)
        dimension_name = m.group(1) + Word(m.group(2)).singularize()
    else:
        dimension_name = get_attribute(field)

    return dimension_name


def get_unnested_view_name(field):
    if field.modus == "STRUCT":  # We do not explicitely reference or unnest structs
        return ""
    else:
        if field.modus == "ARRAY":
            path = field.field_path
        elif field.array_parent_field_path == "":
            return get_global_configuration()['looker_name']
        else:
            path = field.array_parent_field_path
        return get_global_configuration()['looker_name'] + "__" + path.replace(".", "__") + get_global_configuration()['unnest_suffix']


def get_nested_dimension_name(field):
    if field.modus == "ARRAY" or field.modus == "STRUCT":
        if field.array_parent_field_path:
            good_dimension_path = field.field_path[
                len(field.array_parent_field_path) + 1 :
            ]
        else:
            good_dimension_path = field.field_path
        return good_dimension_path.replace(".", "__")
    else:
        return ""


def get_nested_view_name(field):
    if field.modus == "ARRAY" or field.modus == "STRUCT":
        if field.array_parent_field_path:
            return (
                get_global_configuration()['looker_name']
                + "__"
                + field.array_parent_field_path.replace(".", "__")
                + get_global_configuration()['unnest_suffix']
            )
        else:
            return get_global_configuration()['looker_name']
    else:
        return ""


def get_label(field_path):
    label = field_path.replace(".", "-")
    label = label.lower()  # always true but better be safe

    # Replace all underscore with blank spaces
    label = label.replace("_", " ").strip()
    label = Word(label).singularize()
    if label.endswith("statu"):  # fix a problem with textblob
        label = label + "s"
    label = label.title()

    for special_label, special_new_label in get_global_configuration()['special_labels'].items():
        label = re.sub(
            r"\b" + special_label + r"\b", special_new_label, label, flags=re.IGNORECASE
        )

    return label


def make_label_plural(label):
    # pluralize does not work with capitalised nouns e.g. Country => Countrys
    # Hence a hack

    m = re.search(r"(.*?\s?)([^\s]+)$", label)
    last_word = m.group(2)

    # Last part is all capital letters e.g. ID or abbrev
    if last_word == last_word.upper():
        last_word = m.group(2) + "s"
    else:
        last_word = Word(last_word.lower()).pluralize().title()

    return m.group(1) + last_word


def get_unnested_sql(field):
    if field.array_parent_field_path == "":
        sql = field.field_path
    else:
        sql = field.field_path[len(field.array_parent_field_path) + 1 :]

    # for some weird reason full has to be put in paranthess
    return re.sub(r"\bfull\b", "`full`", sql, flags=re.IGNORECASE)


def get_group_label(field, looker_metadata):
    label = ""
    if field.unnested_view_name == get_global_configuration()['looker_name']:
        if field.modus == "FIELD":
            if "date" in field.field_path or "year" in field.field_path:
                label = "Dates"
            else:
                label = " Core Metadata"
    else:
        label = get_parent_field_path(field.field_path)
        if label:
            label = looker_metadata[looker_metadata.field_path == label].iloc[0].label

    if label == "":
        return field.label
    else:
        return label

