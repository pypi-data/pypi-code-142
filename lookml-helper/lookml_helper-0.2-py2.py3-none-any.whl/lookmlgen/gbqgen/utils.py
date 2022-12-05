# !/usr/bin/env python
# -*- coding: utf-8 -*-


from string import Template
import click
import pandas as pd
import numpy as np
import re
import os
import shutil
import pandas as pd
import itertools
from datetime import datetime


CONFIGURATION = {}

def get_global_configuration():
    global CONFIGURATION
    return CONFIGURATION






def gen_folders(user_provided_name, default_dir):
  """ """
  if not os.path.exists(default_dir):
      os.mkdir(default_dir)

  output_path = os.path.join(default_dir, user_provided_name)
  if os.path.exists(output_path):
      shutil.rmtree(output_path)

  os.mkdir(output_path)
  os.mkdir(output_path+"/explores")
  os.mkdir(output_path+"/views")
  os.mkdir(output_path+"/views/raw")
  os.mkdir(output_path+"/views/unnested")

  with open(output_path+'/README.MD', 'w') as f:
      f.write(gen_readme())

  return output_path


def gen_readme():
  """Simple README.MD file contents"""

  now = datetime.now() # current date and time
  date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
  text = f"""Auto-generated LookML project
  
  Date: {date_time}
  """
  return text





def make_header(field, template, include_struct=False):
  header = ""
  if field.top_header != "":
    if not(include_struct and field.field_path != field.column_name):
      header = f"""
  # ##############
  # ## {field.top_header}
  # #
  """

  if field.column_name != field.field_path:
    header = header+ f"""
    #
    ## {template} {field.field_path}
    # """
  return header







def printDebug(text, mystyle="", err=True, **kwargs):
    """Wrapper around click.secho() for printing in colors with various defaults.

    :kwargs = you can do printDebug("s", bold=True)

    2018-12-06: by default print to standard error stderr (err=True)
    https://click.palletsprojects.com/en/5.x/api/#click.echo
    This means that the output is ok with `less` and when piped to other commands (or files)

    Styling output:
    <http://click.pocoo.org/5/api/#click.style>
    Styles a text with ANSI styles and returns the new string. By default the styling is self contained which means that at the end of the string a reset code is issued. This can be prevented by passing reset=False.

    This works also with inner click styles eg

    ```python
    uri, title = "http://example.com", "My ontology"
    printDebug(click.style("[%d]" % 1, fg='blue') +
               click.style(uri + " ==> ", fg='black') +
               click.style(title, fg='red'))
    ```

    Or even with Colorama

    ```
    from colorama import Fore, Style

    printDebug(Fore.BLUE + Style.BRIGHT + "[%d]" % 1 + 
            Style.RESET_ALL + uri + " ==> " + Fore.RED + title + 
            Style.RESET_ALL)
    ```


    Examples:

    click.echo(click.style('Hello World!', fg='green'))
    click.echo(click.style('ATTENTION!', blink=True))
    click.echo(click.style('Some things', reverse=True, fg='cyan'))
    Supported color names:

    black (might be a gray)
    red
    green
    yellow (might be an orange)
    blue
    magenta
    cyan
    white (might be light gray)
    reset (reset the color code only)
    New in version 2.0.

    Parameters:
    text – the string to style with ansi codes.
    fg – if provided this will become the foreground color.
    bg – if provided this will become the background color.
    bold – if provided this will enable or disable bold mode.
    dim – if provided this will enable or disable dim mode. This is badly supported.
    underline – if provided this will enable or disable underline.
    blink – if provided this will enable or disable blinking.
    reverse – if provided this will enable or disable inverse rendering (foreground becomes background and the other way round).
    reset – by default a reset-all code is added at the end of the string which means that styles do not carry over. This can be disabled to compose styles.

    """

    if mystyle == "comment":
        click.secho(text, dim=True, err=err)
    elif mystyle == "important":
        click.secho(text, bold=True, err=err)
    elif mystyle == "normal":
        click.secho(text, reset=True, err=err)
    elif mystyle == "red" or mystyle == "error":
        click.secho(text, fg='red', err=err)
    elif mystyle == "green":
        click.secho(text, fg='green', err=err)
    else:
        click.secho(text, err=err, **kwargs)




def printInfo(text, mystyle="", **kwargs):
    """Wrapper around printDebug for printing ALWAYS to stdout
    This means that the output can be grepped etc..
    NOTE this output will be picked up by pipes etc..

    Fixes https://github.com/lambdamusic/Ontospy/issues/76
    """
    printDebug(text, mystyle, False, **kwargs)






#################
# DIMENSIONS specific helpers
#################


# This may require adaption depending on what table you got
def get_link(field):
  if field.field_path == "id":
    return f"""
    link: {{
      label: "Dimensions"
      url: "https://app.dimensions.ai/details/{get_global_configuration()['gbq_table_name'][:-1]}/{{{{ value  | url_encode | url_encode }}}}"
      icon_url: "https://www.dimensions.ai/wp-content/plugins/dimensions-blocks/assets/images/dimensions-hexagon-gradient.png"
    }}"""

  elif field.field_path == "link_out":
    return f"""
    link: {{
      label: "Original URL"
      url: "{{{{ value  }}}}"
    }}"""

  elif field.unnested_dimension_name == "altmetric_id":
    return f"""
    link: {{
      label: "Altmetric"
      url: "https://www.altmetric.com/details/{{{{ value  }}}}"
      icon_url: "https://www.digital-science.com/wp-content/uploads/2020/11/Altmetric-no-padding.webp"
    }}"""

  elif field.unnested_dimension_name.endswith("grant_id"):
    return f"""
    link: {{
      label: "Dimensions"
      url: "https://app.dimensions.ai/details/grant/{{{{ value  }}}}"
      icon_url: "https://www.dimensions.ai/wp-content/plugins/dimensions-blocks/assets/images/dimensions-hexagon-gradient.png"
    }}"""

  elif field.unnested_dimension_name.endswith("publication_id"):
    return f"""
    link: {{
      label: "Dimensions"
      url: "https://app.dimensions.ai/details/publication/{{{{ value  }}}}"
      icon_url: "https://www.dimensions.ai/wp-content/plugins/dimensions-blocks/assets/images/dimensions-hexagon-gradient.png"
    }}"""

  elif field.unnested_dimension_name.endswith("grid_id") and "funder" in field.field_path:
    return f"""
    link: {{
      label: "Dimensions"
      url: "https://app.dimensions.ai/details/{get_global_configuration()['gbq_table_name'][:-1]}/and_facet_funder={{{{ value  }}}}"
      icon_url: "https://www.dimensions.ai/wp-content/plugins/dimensions-blocks/assets/images/dimensions-hexagon-gradient.png"
    }}"""
  
  elif field.unnested_dimension_name.endswith("grid_id"):
    return f"""
    link: {{
      label: "Dimensions"
      url: "https://app.dimensions.ai/details/{get_global_configuration()['gbq_table_name'][:-1]}/and_facet_research_org={{{{ value  }}}}"
      icon_url: "https://www.dimensions.ai/wp-content/plugins/dimensions-blocks/assets/images/dimensions-hexagon-gradient.png"
    }}"""   

  elif field.unnested_dimension_name == "researcher_id":
    return f"""
    link: {{
      label: "Dimensions"
      url: "https://app.dimensions.ai/details/entities/publication/author/{{{{ value  }}}}"
      icon_url: "https://www.dimensions.ai/wp-content/plugins/dimensions-blocks/assets/images/dimensions-hexagon-gradient.png"    
    }}"""
  else:
    return ""
