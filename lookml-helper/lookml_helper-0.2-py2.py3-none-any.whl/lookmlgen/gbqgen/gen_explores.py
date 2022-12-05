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



# """## Creating the main explore

# Each field that is an ARRAY we need to unnest. In order to do this we have to create an explore with each join

# """


#
# Create for a GBQ table field that is an array a join
#

def create_base_explore_join(field):
  assert field.modus== "ARRAY" # paranoia check

  # For some fields we have offsets
  if field.nested_dimension_name in get_global_configuration()['fields_w_offset_joins']:
    offset = f" WITH OFFSET as {field.nested_dimension_name}_offset"
  else:
    offset = ""

  # Compile it all together
  array_join_lml = f"""
    {make_header(field, "join for")}
    join: {field.unnested_view_name}{{
      view_label: " {get_global_configuration()['pretty_looker_name']}"
      sql: LEFT JOIN UNNEST(${{{field.nested_view_name}.{field.nested_dimension_name}}}) as {field.unnested_view_name}{offset};;
      relationship: one_to_many
    }}"""

  return array_join_lml


#
# Create all the unnesting joins of the base explore
#

def create_all_base_explore_joins(looker_metadata, verbose=False):
  array_fields = looker_metadata[looker_metadata.modus=="ARRAY"]
  if verbose:
    printDebug("Generating joins for the ", len(array_fields), " arrays found in the table")
    printDebug(array_fields)
  return "".join(list(array_fields.apply(create_base_explore_join, axis=1)))




def write_base_explore(output_path, looker_metadata):


    base_explore_lml = f"""
    ##############
    ## {get_global_configuration()['capital_looker_name']}: BASE EXPLORE
    #
    # - includes GBQ fields 1:1 from the {get_global_configuration()['pretty_looker_name']} GBQ table
    # - all arrays are unnested and JOINED
    # - no JOINs to other tables are included
    #
    ##############


    #####################
    # IMPORTS
    #####################
    include: "{get_global_configuration()['looker_parent_folder']}/{get_global_configuration()['looker_name']}/views/unnested.view"
    #####################


    explore: {get_global_configuration()['looker_name']} {{

    label: "{get_global_configuration()['pretty_looker_name']} Basic"
    view_label: " {get_global_configuration()['pretty_looker_name']}"
    from: {get_global_configuration()['looker_name']}_unnested   # view the Explore derives from
    view_name: {get_global_configuration()['looker_name']}   # name used when referencing fields in JOINs (overrides: Explore name)

    description: "{get_global_configuration()['pretty_looker_name']} Base explore: enhanced the basic explore by extracting
    all nested information as first class objects using supplementary views."



    # ##############
    # #######
    # ## JOINS TO UNNESTED VIEWS
    # #######
    # ##############

    {create_all_base_explore_joins(looker_metadata)}

    
    # ##############
    # ## QUERIES for Quick Start analyses
    # ## https://docs.looker.com/reference/explore-params/query
    # ##############

    ##££ Add more meaningful queries here

    query: count_all {{
        label: "{get_global_configuration()['pretty_looker_name']}: count all"
        description: "Count all entries"
        measures: [{get_global_configuration()['looker_name']}.count]
        # filters: [{get_global_configuration()['looker_name']}.end_date_year: "after 0 minutes ago"]
    }}


    }}
    """


    # printDebug(base_explore_lml)
    f = open(output_path+"/explores/"+get_global_configuration()['looker_name']+".explore.lkml", "w")
    f.write(base_explore_lml)
    f.close()




# """## Creating the joined-up explore
# At this point this is sth that needs to be edited manually. But maybe we can go through the ids and other tables in the data set to suggest sth automatically
# """




def write_joined_explore(output_path, looker_metadata):

    join_explore_lml = f"""
    ##############
    ## {get_global_configuration()['capital_looker_name']}: JOINED EXPLORE
    #
    # This can be used as a blueprint/building block for joining other models to {get_global_configuration()['pretty_looker_name']}.
    #
    # Refining:
    # - import this file into your project
    # - refine the `{get_global_configuration()['looker_name']}_joined` definition
    # - includes JOINs to other tables too
    #
    # Duplicate:
    # - import `{get_global_configuration()['looker_name']}.base.explore` into your project
    # - refine it and implement your own JOINs
    # - use structure below as blueprint
    ##############


    #####################
    # IMPORTS
    #####################
    # Explores
    include: "{get_global_configuration()['looker_parent_folder']}/{get_global_configuration()['looker_name']}/explores/{get_global_configuration()['looker_name']}.explore"

    ££ CHECK IF YOU NEED MORE INCLUDES
    #####################




    explore: {get_global_configuration()['looker_name']}_joined {{

    extends: [{get_global_configuration()['looker_name']}] # explore base+unnest
    label: "{get_global_configuration()['pretty_looker_name']} Joined"

    view_label: " {get_global_configuration()['pretty_looker_name']}"
    hidden: no

    description: "{get_global_configuration()['pretty_looker_name']} Joined explore: include views for tables via joins."



    # ##############
    # #######
    # ## JOINS TO NON-{get_global_configuration()['capital_looker_name']} BASED VIEWS
    # #######
    # ##############

    # £££ take the joins in the old data table and replace nest_* with
    # #__unnested and change type from inner to left_outer
    }}
    """

    # printDebug(join_explore_lml)
    f = open(output_path+"/explores/"+get_global_configuration()['looker_name']+".joined.explore.lkml", "w")
    f.write(join_explore_lml)
    f.close()
