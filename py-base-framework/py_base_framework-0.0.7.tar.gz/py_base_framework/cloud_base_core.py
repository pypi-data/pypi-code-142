import json
import threading
from logging.config import dictConfig

from flask import Flask, request

from py_base_framework.cloud_base_exception import extension_service_illegal_resp, extension_service_not_found, \
    extension_service_biz_error
from py_base_framework.cloud_base_log import log_config, log_key

dictConfig(log_config)

app = Flask(__name__)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


@app.route('/base/cloud/spi', methods=['POST'])
def cloud_spi():
    threading.current_thread().__dict__[log_key] = request.headers.get(log_key)
    app.logger.info("Spi handler receive request : %s", request.json)
    try:
        method = request.json.get('method')
        # 遍历寻找对应业务类
        for rule in app.url_map.iter_rules():
            if rule.rule != method:
                continue
            # 反序列化 data 值
            request.json['data'] = json.loads(request.json.get('data'), object_hook=JSONObject)
            func = app.view_functions[rule.endpoint]
            # 调用业务方法
            result = func()
            app.logger.info("Spi handler response : %s", result)
            # 检查不合法返回值
            if 'code' not in result or 'success' not in result:
                app.logger.error("Spi handler response is invalid! Please use #success_result or #failed_result!")
                return failed_result(extension_service_illegal_resp.get('code'),
                                     extension_service_illegal_resp.get('message'))

            return result

        app.logger.error(extension_service_not_found.get('message'))
        return failed_result(extension_service_not_found.get('code'),
                             extension_service_not_found.get('message'))
    except Exception as ex:
        app.logger.error("Failed to call biz api! exception: %s", ex)
        return failed_result(extension_service_biz_error.get('code'),
                             extension_service_biz_error.get('message'))
    finally:
        # reset
        threading.current_thread().__dict__[log_key] = ""


@app.route('/base/cloud/spi', methods=['GET'])
def health_check():
    return "{\"status\":\"UP\"}"


def success_result(data, code="200"):
    return {
        "success": True,
        "code": code,
        "message": "",
        "data": data
    }


def failed_result(code, message, data=""):
    return {
        "success": False,
        "code": code,
        "message": message,
        "data": data
    }
