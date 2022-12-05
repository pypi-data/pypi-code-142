#!/usr/bin/python
# -*- coding: utf-8 -*-


from string import Template
import pandas as pd
import numpy as np
import re
import os
import shutil
import pandas as pd
import itertools
from datetime import datetime

from .utils import *
from .extract_fields import *
# from ..CONFIG import *



# """## Create views/raw/arrays view

# This is the view file that includes all first level arrays and structs of the main table
# """



def create_nested_dimension(field, add_links_dimensions = True, verbose=False):
  assert field.modus in ["ARRAY", "STRUCT"]


  if field.modus == "ARRAY":
    dimension_lml = f"""
    {make_header(field, "Links-dimensions for array", True)}
    dimension: {field.nested_dimension_name} {{
      hidden: yes
      description: "{field.description}"
      sql: ${{TABLE}}.{field.unnested_sql} ;;
    }}"""

    if add_links_dimensions:
      dimension_lml = dimension_lml + f"""
      dimension: links_{field.nested_dimension_name} {{
        type: number
        hidden:  no
        label: "Nr of {field.label_plural}"
        description: "Non-unique Nr of {field.label_plural}: {field.description}"
        group_label: "Links count"
        sql: ARRAY_LENGTH(${{{field.nested_dimension_name}}}) ;;
      }}
      dimension: has_{field.nested_dimension_name} {{
        description: "Yes if {get_global_configuration()['pretty_looker_name']} has any {field.label_plural}"
        type: yesno
        group_label: "Links check"
        sql: ${{links_{field.nested_dimension_name}}} > 0 ;;
      }}
      """

    if field.nested_dimension_name == "active_years":
      dimension_lml = dimension_lml +"""
    dimension: active_years_string {
      hidden: no
      label: "Active Years (combined)"
      sql: ( SELECT STRING_AGG(CAST(id AS STRING), ',')  FROM UNNEST(${active_years}) id);;
      group_label: "Dates"
    }
    """

  elif field.modus == "STRUCT":
    if verbose: printDebug(field.field_path)
    dimension_lml = f"""
    {make_header(field, "has_dimension for struct", True)}

    dimension: has_{field.nested_dimension_name} {{
      description: "Yes if {get_global_configuration()['pretty_looker_name']} has {field.label}"
      type: yesno
      group_label: "Links check"
      sql: ${{TABLE}}.{field.unnested_sql} is not null ;;
    }}
    """
  else:
    assert 1==1 # FIELDS cannot be used here

  return dimension_lml


#
# Create all the dimensions of the raw/array view
#
def create_all_raw_array_dimensions(looker_metadata, verbose=False):
  top_level_array_struct_fields = looker_metadata[(looker_metadata.nested_view_name == get_global_configuration()['looker_name']) & (looker_metadata.modus.isin(["ARRAY", "STRUCT"]))]
  if verbose:
    printDebug("Generating joins for the top level ", len(top_level_array_struct_fields), " arrays and struct found in the table")
    printDebug(top_level_array_struct_fields)
  return "".join(list(top_level_array_struct_fields.apply(create_nested_dimension, axis=1)))



def write_raw_array_view(output_path, looker_metadata):

    raw_array_view_lml = f"""
    ##############
    ## {get_global_configuration()['capital_looker_name']}: BASE VIEWS - GBQ ARRAY FIELDS
    #
    # - represents GBQ fields 1:1
    # - array field is normally a hidden dimension (used in nested JOINs)
    # - extra dimensions for each array: links count
    # - optional dimensions for each array: HasValue Yes/no (shortcut for quick filtering)
    #
    ##############





    view: arrays_{get_global_configuration()['looker_name']} {{

    sql_table_name: `dimensions-ai.data_analytics.{get_global_configuration()['looker_name']}`
    ;;

    {create_all_raw_array_dimensions(looker_metadata)}

    }}
    """

    # printDebug(raw_array_view_lml)
    f = open(output_path+"/views/raw/array."+get_global_configuration()['looker_name']+".view.lkml", "w")
    f.write(raw_array_view_lml)
    f.close()






# """## Create views/raw/fields view

# This is the view file that includes all first level simple fields of the main table
# """

def create_unnested_dimension(field):
  # if not((field.modus == "FIELD") or (field.modus == "ARRAY" and field.unnested_dimension_name != "")):
  #   display(field)
  #   assert 1==0
  assert (field.modus == "FIELD") or (field.modus == "ARRAY" and 
                                      field.unnested_dimension_name != "" and
                                      not field.data_type.startswith('ARRAY<STRUCT<'))

  #Default values of some sections
  dimension_type = "dimension"
  dimension_name = field.unnested_dimension_name
  header = ""
  extras = ""
  group_label    = field.group_label
  label = field.label

  if field.modus == "FIELD":
    data_type = field.data_type   
    sql = f"${{TABLE}}.{field.unnested_sql}"
  else: # ARRAY
    data_type = field.data_type[6:-1]
    sql = f"${{TABLE}}"  

  if data_type in ["INT64", "FLOAT64", "BIGNUMERIC", "NUMERIC"]: 
    looker_type = "number"
  elif data_type == "BOOL":
    looker_type = "yesno"
  elif (data_type in ["DATE", "TIMESTAMP", "TIME", "DATETIME"]) or field.column_name.endswith("date") or field.column_name.startswith("date_") :
    looker_type = "time"
    dimension_type = "dimension_group"
    extras = """
    timeframes: [
      raw,
      date,
      week,
      month,
      quarter,
      year
    ]
    convert_tz: no
    datatype: timestamp"""

    if field.column_name in ["date_inserted", "date_imported_gbq"]:
      group_label= "Dates - Internal"
    else:
      group_label= "Dates"
    if data_type == "STRING":
      sql = f"CAST({sql} AS DATE)"
 
  elif data_type == "STRING":
    looker_type = "string"
    if "country" in dimension_name or "countries" in dimension_name or "jurisdiction" in dimension_name:
      extras = extras+"""
    map_layer_name: countries"""
  else:
    printDebug("Unknown type:", data_type)
    printDebug(field)
    printDebug(f"""
    #
    # ££££££££
    # Cannot generate code for {field.field_path} because of
    # type {data_type} 
    """)
    assert 1 == 2

  if field.field_path == "id":
    group_label= "Identifiers"
    extras = f"""
    primary_key: yes"""
    label = " Dimensions ID" # --- LEADING SPACE ---
  
  if dimension_name.endswith("_id"):
    group_label= "Identifiers"

  if dimension_name.endswith("year") and looker_type=="number":
    group_label = "Dates"
    label = label +" (number)"
    extras= """
    value_format: "0000" """

  # For some attributes we may need special casts see at the beginning
  sql = get_global_configuration()['special_casts'].get(dimension_name, sql)

  dimension_lml =f"""{make_header(field, "", False)}
  {dimension_type}: {dimension_name} {{
    type:         {looker_type}
    label:        "{label}"
    description:  "{field.description}"{extras}
    group_label:  "{group_label}"
    sql: {sql};;{get_link(field)}
  }}
  """

  # Add a full name for good measure 
  if dimension_name == "last_name":
    dimension_lml = dimension_lml + f"""
  dimension: full_name {{
    type:         string
    label:        "Full Name"
    group_label:  "{group_label}"  #£££ CHECK THIS!
    sql: COALESCE(CONCAT(${{first_name}}, ' ', ${{last_name}}), ${{last_name}}, ${{first_name}});;
    link: {{
      label: "Dimensions"
      url: "https://app.dimensions.ai/details/entities/publication/author/{{{{ researcher_id._value }}}}" #£££ check if correct value
      icon_url: "https://www.dimensions.ai/wp-content/plugins/dimensions-blocks/assets/images/dimensions-hexagon-gradient.png"
    }}
  }}"""

  return dimension_lml
  
#
# Create all the dimensions of the raw/field view
#
def create_all_raw_fields_dimensions(looker_metadata, verbose=False):
  fields = looker_metadata[(looker_metadata.unnested_view_name == get_global_configuration()['looker_name']) & (looker_metadata.modus.isin(["FIELD"]))]
  if verbose:
    printDebug("Generating joins for the top level ", len(fields), " simple fields found in the table")
    printDebug(fields)
  return "".join(list(fields.apply(create_unnested_dimension, axis=1)))



def write_raw_fields_view(output_path, looker_metadata):

    raw_fields_lml = f"""
    ##############
    ## {get_global_configuration()['capital_looker_name']}: BASE VIEWS - MISC FIELDS
    #
    # - represents GBQ fields 1:1
    #
    # https://docs.dimensions.ai/bigquery/datasource-{get_global_configuration()['looker_name']}.html
    ##############


    view: fields_{get_global_configuration()['looker_name']} {{

    sql_table_name: `dimensions-ai.data_analytics.{get_global_configuration()['looker_name']}`
    ;;

    {create_all_raw_fields_dimensions(looker_metadata)}

    }}
    """
    f = open(output_path+"/views/raw/fields."+get_global_configuration()['looker_name']+".view.lkml", "w")
    f.write(raw_fields_lml)
    f.close()






# """## Create views/unnested/array.nested view

# This is the view file that includes all the unnesting of the arrays in the main table
# """



# Create a certain dimension in a particular view
# for a nested array there are two options:
# 1. The unnested array is a hidden dimension in the parent array
# 2. If the array is ARRAY<SIMPLE TYPE> i.e. not ARRAY <STRUCT> then this field is a dimension of its own unnested view
#.   (Example is eg. publications.research_org)
def create_array_unnested_view_dimension(field):
#   display(field)
  if field.modus == "FIELD":
    return create_unnested_dimension(field)
  elif field.modus == "ARRAY":
    return create_nested_dimension(field, False)
  elif field.modus == "STRUCT":
    #do nothing
    return ""
  else:
    assert 1 == 2 # unknown modus

def create_array_unnested_view(field, looker_metadata):
  pat = field.field_path+"\.[a-z_]+$"
  sub_fields = looker_metadata[looker_metadata.field_path.str.fullmatch(pat)]

  if len(sub_fields) > 0:
    # This is an ARRAY of STRUCT: then all fields inside appear as separate fields
    assert field.unnested_dimension_name == ""
    dimensions_lml = "".join(list(sub_fields.apply(create_array_unnested_view_dimension, axis=1)))
  else:
    # This is an ARRAY<STRING> (or another simple type): the field is the "same" as the array
    assert field.unnested_dimension_name != ""
    dimensions_lml = create_unnested_dimension(field)


  if field.field_path in get_global_configuration()['fields_w_offset_joins'] :
    dimensions_lml = f"""
    dimension: {field.field_path}_key {{
      type: string
      hidden: yes
      primary_key: yes

      # TIP: in the explore join, an OFFSET is created and given the alias authors_offset
      # https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#unnest_operator
      sql: CONCAT({field.unnested_sql}_offset, ${{{get_global_configuration()['looker_name']}.id}}) ;;
    }}"""+dimensions_lml

  if field.field_path == "concepts":
    dimensions_lml = dimensions_lml + """
    dimension: is_0_5_plus {
      description: "Yes if concept has a relevance score major than 0.5"
      label: "Has Relevance 0.5+"
      hidden: no
      type: yesno
      group_label: "Concepts"
      sql: ${relevance} > 0.5 ;;
    }

    dimension: is_0_6_plus {
      description: "Yes if concept has a relevance score major than 0.6"
      label: "Has Relevance 0.6+"
      hidden: no
      type: yesno
      group_label: "Concepts"
      sql: ${relevance} > 0.6 ;;
    }
    """

  view_lml = f"""
{make_header(field, "Unnested view for ")}
view: {field.unnested_view_name} {{
  {dimensions_lml}
}}
  """

  return view_lml

def create_all_array_unnested_views(looker_metadata, verbose=False):
  fields = looker_metadata[(looker_metadata.unnested_view_name != get_global_configuration()['looker_name']) & (looker_metadata.modus=="ARRAY")]
  if verbose:
    printDebug("Generating joins for the not top level ", len(fields), " arrays  found in the table")
    printDebug(fields)
  return "".join(list(fields.apply(create_array_unnested_view, axis=1, looker_metadata=looker_metadata)))


def write_unested_array_view(output_path, looker_metadata):

    unnested_array_nested_lml = f"""
    ##############
    ## {get_global_configuration()['capital_looker_name']}: NESTED FIELDS VIEWS - MISCELLANEOUS
    #
    # - represents GBQ nested fields by adding a view for each of them
    #
    # https://docs.dimensions.ai/bigquery/datasource-{get_global_configuration()['looker_name']}.html
    ##############

    include: "{get_global_configuration()['looker_parent_folder']}/{get_global_configuration()['looker_name']}/views/base.view.lkml"
    {create_all_array_unnested_views(looker_metadata)}
    """

    f = open(output_path+"/views/unnested/array.nested.view.lkml", "w")
    f.write(unnested_array_nested_lml)
    f.close()





# """## Create views/base
# This mainly includes:
# - Measures attached to "links" aka arrays
# - Measures attached to number-type of attributes
# """

#
# Build simple measures for number-type
#
def create_base_field_measure(field):
  dimension_ml = f"""{make_header(field, "Measures for ")}
  measure: total_{field.unnested_dimension_name} {{
    type: sum
    label: "Sum {field.label_plural}"
    sql:  ${{{field.unnested_dimension_name}}} ;;
    group_label: "{field.group_label}"
  }}
  measure: avg_{field.unnested_dimension_name} {{
    type: average
    label: "Average {field.label_plural}"
    sql:  ${{{field.unnested_dimension_name}}} ;;
    group_label: "{field.group_label}"
  }}
  """
  return dimension_ml

def create_all_base_field_measures(looker_metadata, verbose=False):
  fields = looker_metadata[looker_metadata.data_type.isin(['INT64', 'FLOAT64', "BOOL"])&
          (~looker_metadata.field_path.str.contains("year")) &
          (looker_metadata.field_path != "concepts.relevance") &
          (looker_metadata.unnested_view_name == get_global_configuration()['looker_name'])]
  if verbose:
    printDebug("Generating joins for the  top level ", len(fields), " fields  found in the table")
    # display(fields)
  return "".join(list(fields.apply(create_base_field_measure, axis=1)))


#
# Create measure for nested attributes i.e. "links"
#
def create_array_measure(field):

  # Not the whole shebang for active years
  if field.field_path == "active_years":
    return f"""
  {make_header(field, "Measures for ")}
  measure: avg_{field.nested_dimension_name}  {{
    type: average
    value_format_name: decimal_2
    label: "Average {field.label}"
    description: "When used on a single {get_global_configuration()['pretty_looker_name']}, returns the average number of active years"
    group_label: "{field.group_label}"
    sql: ${{links_{field.nested_dimension_name}}} ;;
    drill_fields: [detail*]
  }}    
    """

  measure_lml = make_header(field, "Measures for ", True)
  if field.modus == "ARRAY":
    measure_lml = measure_lml+f"""
  measure: total_links_{field.nested_dimension_name}   {{
    type: sum
    label: "Total {field.label_plural}"
    description: "Non unique total number of all {field.label_plural}"
    group_label: "{field.group_label}"
    sql: ${{links_{field.nested_dimension_name}}} ;;
    drill_fields: [detail*]
  }}
  measure: avg_links_{field.nested_dimension_name}  {{
    type: average
    value_format_name: decimal_2
    label: "Average {field.label}"
    description: "Non unique: average  {field.label} links per {get_global_configuration()['pretty_looker_name']}"
    group_label: "{field.group_label}"
    sql: ${{links_{field.nested_dimension_name}}} ;;
    drill_fields: [detail*]
  }}"""
  else:
    measure_lml = ""

  measure_lml = measure_lml + f"""
  measure: count_{get_global_configuration()['looker_name']}_with_{field.nested_dimension_name}  {{
    type: count
    label: "Unique {get_global_configuration()['pretty_looker_name']} with {field.label_plural}"
    group_label: "{field.group_label}"
    filters: [has_{field.nested_dimension_name} : "Yes"]
    drill_fields: [detail*]
  }}
  measure: percent_{get_global_configuration()['looker_name']}_with_{field.nested_dimension_name}  {{
    type: number
    value_format_name: percent_2
    label: "Percent {get_global_configuration()['pretty_looker_name']} with a {field.label_plural}"
    group_label: "{field.group_label}"
    sql:  ${{count_{get_global_configuration()['looker_name']}_with_{field.nested_dimension_name}}} / ${{count}} ;;
    drill_fields: [detail*]
  }}
  """
  return measure_lml

def create_all_link_measures(looker_metadata, verbose=False):
  fields = looker_metadata[(looker_metadata.nested_view_name == get_global_configuration()['looker_name']) & (looker_metadata.modus.isin(["ARRAY", "STRUCT"]))]
  if verbose:
    printDebug("Generating joins for the top level ", len(fields), " arrays  found in the table")
    # display(fields)
  return "".join(list(fields.apply(create_array_measure, axis=1)))


def write_base_view(output_path, looker_metadata):


    base_view_lml = f"""
    ##############
    ## {get_global_configuration()['capital_looker_name']} BASE VIEW
    #
    # - raw fields as they appear in GBQ
    # - basic measures
    # - no 'unnested' views dependencies
    #
    ##############

    include: "{get_global_configuration()['looker_parent_folder']}/{get_global_configuration()['looker_name']}/views/raw/*.view"


    view: {get_global_configuration()['looker_name']}_base {{

    extends: [arrays_{get_global_configuration()['looker_name']}, fields_{get_global_configuration()['looker_name']}]
    sql_table_name: `dimensions-ai.data_analytics.{get_global_configuration()['looker_name']}` ;;

    label: "{get_global_configuration()['pretty_looker_name']}"


    ##############
    ##############
    ##
    # FIELD SETS FOR DRILLING
    ##
    ##############
    ##############



    # default
    drill_fields: [id]


    # ----- Sets of fields for drilling in ------
    set: detail {{
        fields: [{
            ", ".join(looker_metadata[
            (looker_metadata.unnested_view_name == get_global_configuration()['looker_name']) & 
            (looker_metadata.modus == "FIELD") ].unnested_dimension_name.head(4))
            }]
    }}



    ##############
    ##############
    ##
    # MEASURES derived from RAW fields
    ##
    ##############
    ##############

    measure: count {{
        type: count
        label: "Unique {get_global_configuration()['pretty_looker_name']}"
        group_label: " {get_global_configuration()['pretty_looker_name']}"
        drill_fields: [detail*]
    }}
    

    #######################
    #  MEASURES FOR NUMERIC FIELDS
    #
    {create_all_base_field_measures(looker_metadata)}


    #######################
    #  MEASURES FOR ARRAYS/LINKS
    #
    {create_all_link_measures(looker_metadata)}

    }}
    """

    f = open(output_path+"/views/base.view.lkml", "w")
    f.write(base_view_lml)
    f.close()







# """## Create views/unnested

# This view includes all measures which are counts distinct aka unique counts AFTER unnesting. For this we list all ARRAYs of a simple data type like INT64 or STRING and create counts distinct measures.

# """

def create_unnested_measure(field):
  measure_lml = f"""
  {make_header(field, "Measures for ")}
  measure: count_{field.field_path.replace(".","_")} {{
    type: count_distinct
    label: "Unique {field.label_plural}"
    description: "Number of unique {field.label_plural}"
    group_label: "{field.group_label}"
    sql: ${{{field.unnested_view_name}.{field.unnested_dimension_name}}} ;;
  }}
  """
  return measure_lml

def create_all_unnested_measures(looker_metadata, verbose=False):
  fields = looker_metadata[looker_metadata.data_type.str.fullmatch(r'ARRAY<[A-Z0-9]*?>')]
  if verbose:
    printDebug("Generating joins for the  ", len(fields), " fields  found in the table")
    # display(fields)
  return "".join(list(fields.apply(create_unnested_measure, axis=1)))



def write_unnested_view(output_path, looker_metadata):

    unnested_views_lml = f"""
    ##############
    ## {get_global_configuration()['capital_looker_name']}: UNNESTED VIEW
    #
    # - extend BASE by adding unnesting logic
    # - additional measures
    #
    # NOTE: when importing this view into an Explore, you need all
    # the unnesting JOINs for the symbols to resolve
    ##############

    include: "{get_global_configuration()['looker_parent_folder']}/{get_global_configuration()['looker_name']}/views/base.view"
    include: "{get_global_configuration()['looker_parent_folder']}/{get_global_configuration()['looker_name']}/views/unnested/*.view"


    view: {get_global_configuration()['looker_name']}_unnested {{

    extends: [{get_global_configuration()['looker_name']}_base]


    ##############
    ##############
    ##
    # MEASURES THAT REQUIRE UNNESTED DATA
    ##
    ##############
    ##############

    {create_all_unnested_measures(looker_metadata)}

    }}
    """


    f = open(output_path+"/views/unnested.view.lkml", "w")
    f.write(unnested_views_lml)
    f.close()