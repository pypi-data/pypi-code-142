#!/usr/bin/env python3

import json
import sys

from . import select_post
from . import submit_post

CONFIG_FILENAME = 'config.json'


def read_config():
    with open(CONFIG_FILENAME, "r") as file_pointer:
        config = json.load(file_pointer)
    return config


def post():
    config = read_config()
    post = select_post.main(config["post_list"])
    print(post)
    if "-n" not in sys.argv:
        submit_post.main(config["instance_name"], post)
