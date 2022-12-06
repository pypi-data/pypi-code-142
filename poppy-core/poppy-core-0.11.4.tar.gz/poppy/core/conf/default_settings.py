# -*- coding: utf-8 -*-
import collections
import json
import os

ROOT_DIRECTORY = os.environ.get('PIPELINE_ROOT_DIRECTORY', '')

MAIN_DATABASE = 'MAIN-DB'

PLUGINS = [
    'poppy-pop',
]

# load the logger config
conf_dir_path = os.path.dirname(os.path.realpath(__file__))

logger_json_filepath = os.path.join(conf_dir_path, 'logger.json')

with open(logger_json_filepath, 'rt') as json_file:
    LOGGER_CONFIG = json.load(json_file, object_pairs_hook=collections.OrderedDict)
