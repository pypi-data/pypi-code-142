# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:18:46 2020

@author: Q Mo
"""

import os
import yaml
from .MatgenError import MatgenError

__author__ = "Matgen Development Team"
__email__ = "matgen@nscc-gz.cn"
__maintainer__ = "Q Mo"
__maintainer_email__ = ""
__version__ = "2022.12.02"
# print(os.path.expanduser("~"))
SETTINGS_FILE ='.matgenrc.yaml'
#print(SETTINGS_FILE)

def _load_matgen_settings():
  try:
    with open(SETTINGS_FILE, 'rt') as f:
      content = yaml.safe_load(f)
      return dict(content)
  except IOError:
    content = {}
    for key,value in os.environ.items():
      if key == "MATGEN_TOKEN":
        content[key] = value
    content = content or {}
    return dict(content) or {}

def write_matgen_token(s):
  try:
    contentdict = {}
    if os.path.exists(SETTINGS_FILE):
      with open(SETTINGS_FILE, 'rt') as f:
        content = yaml.safe_load(f)
        contentdict = dict(content)
    with open(SETTINGS_FILE, 'w') as f:
      for key in contentdict:
        if key != 'MATGEN_TOKEN':
          f.write(key + ': ' + contentdict[key]+'\n')
      f.write('MATGEN_TOKEN: '+s + '\n')
      return 'success'
  except IOError:
    raise MatgenError("config file can't be found")

SETTINGS = _load_matgen_settings()
print(SETTINGS)
#if 'MATGEN_TOKEN' in SETTINGS:
#  print(SETTINGS["MATGEN_TOKEN"])
#if 'MATGEN_ENDPOINT' in SETTINGS:
#  print(SETTINGS["MATGEN_ENDPOINT"])
