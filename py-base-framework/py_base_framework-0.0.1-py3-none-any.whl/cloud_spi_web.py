import json
import threading

from flask import Flask, request

from cloud_spi_core import app
from cloud_spi_log import log_key


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


@app.route('/base/cloud/spi', methods=['POST'])
def cloud_spi():
    app.logger.info(request.json)
    threading.current_thread().__dict__[log_key] = request.headers.get(log_key)

    method = request.json.get('method')
    for rule in app.url_map.iter_rules():
        if rule.rule == method:
            request.json['data'] = json.loads(request.json.get('data'), object_hook=JSONObject)
            func = app.view_functions[rule.endpoint]
            return func()

    return "null"
