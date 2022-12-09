import os
import json
from daggerml import Resource


TAG = 'com.daggerml.resource.s3'
DAG_NAME = TAG
DAG_VERSION = 1
CONFIG_FILE = os.path.expanduser(os.getenv('DML_S3_CONFIG', '~/.config/dml-s3.json'))


def reload(config_file=CONFIG_FILE):
    if os.path.isfile(config_file):
        with open(config_file, 'r') as f:
            js = json.load(f)
    else:
        js = {}
    group = js.get('group')
    bucket = js.get('bucket')
    secret = js.get('secret')
    executor = js.get('executor')
    if executor is not None:
        executor = Resource.from_dict(executor)
    return group, bucket, secret, executor


GROUP, BUCKET, SECRET, EXECUTOR = reload()
