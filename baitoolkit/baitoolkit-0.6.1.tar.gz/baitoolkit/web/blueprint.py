# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import json
import os
import types
import typing
from functools import wraps

import flask
from flask import Blueprint, send_from_directory, current_app

from baitoolkit import exception
from baitoolkit.common import type_util
from baitoolkit.common.context_manager import global_ctx
from baitoolkit.exception import errors
from baitoolkit.web import web_constant
from baitoolkit.web.req_util import is_ajax_request, url_join
from baitoolkit.web.web_constant import HttpStatus


class BaseBP(Blueprint):

    def __init__(self, *args, url_prefix=None, **kwargs):
        super(BaseBP, self).__init__(*args, url_prefix=url_prefix, **kwargs)
        self._auth_method = None

    def register_auth(self, auth_method: str) -> typing.NoReturn:
        self._auth_method = auth_method

    def authenticate(self) -> bool:
        if self._auth_method is None:
            raise exception.InternalError('auth_method is not registered.')
        return self._auth_method()


class ViewBP(BaseBP):

    def __init__(self, *args, url_prefix="/view", **kwargs):
        super(ViewBP, self).__init__(*args, url_prefix=url_prefix, **kwargs)

    def route(self, rule: str, **options) -> typing.Callable:
        """
        the decorator to return view.
        :param str rule: url path rule.
        :return function:
        """

        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                self.authenticate()
                data = f(*args, **kwargs)
                return data

            endpoint = options.pop("endpoint", f.__name__)
            self.add_url_rule(rule, endpoint, wrapper, **options)
            return wrapper

        return decorator


class ApiBP(BaseBP):

    def __init__(self, *args, url_prefix="/api", **kwargs):
        super(ApiBP, self).__init__(*args, url_prefix=url_prefix, **kwargs)

    def route(self, rule: str, **options) -> typing.Callable:
        """the decorator to return data with the standard format for rest api.
        :param str rule: url path rule.
        :return function:
        """

        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                self.authenticate()
                code = web_constant.SUCCESS_CODE
                message = web_constant.SUCCESS_MESSAGE
                data = f(*args, **kwargs)
                return JsonRtn(code, message=message, data=data).make_response()

            endpoint = options.pop("endpoint", f.__name__)
            self.add_url_rule(rule, endpoint, wrapper, **options)
            return wrapper

        return decorator


__page_context_funcs = dict()


def register_page_context(page_path: str, context_func: types.FunctionType) -> None:
    """Register the context function for the template to be used by path_path."""
    global __page_context_funcs
    __page_context_funcs[page_path] = context_func


def get_amis_view_bp(name='amis_view', url_prefix=None, amis_cdn="http://server-host/amis"):
    """Return amis view bp"""
    amis_view_bp = ViewBP(name, __name__, url_prefix=url_prefix)

    def render_tpl(page_path, tpl_path, **kwargs):
        global __page_context_funcs
        context_func = __page_context_funcs.get(page_path)
        context = context_func() if context_func else dict()
        context.update(kwargs)
        return flask.render_template(tpl_path, **context)

    @amis_view_bp.route('/index.html')
    def index_view():
        return render_tpl('/index.html', "/index.html", amis_cdn=amis_cdn)

    @amis_view_bp.route('/pages/site.json')
    def site_view():
        return render_tpl('/pages/site.json', '/pages/site.json')

    @amis_view_bp.route('/pages/<path:page_path>')
    def page_view(page_path):
        tpl_path = '/pages/{}'.format(page_path)
        return render_tpl(page_path, tpl_path)

    @amis_view_bp.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(global_ctx.app_root_path, 'static'), 'favicon.ico',
                                   mimetype='image/vnd.microsoft.icon')

    return amis_view_bp


def get_health_check_api_bp(name="health_check_api", url_prefix=None, health_check_func=None):
    """Return health check bp.
    @param str name:
    @param str url_prefix:
    @param function health_check_func: accept one argument 'option' which is the end segment of the path.
    """

    health_check_api_bp = ApiBP(name, __name__, url_prefix=url_prefix)

    @health_check_api_bp.route('/health/<string:option>')
    def check_health(option):
        result = "OK"
        if health_check_func is not None:
            result = health_check_func(option)
        return result

    health_check_api_bp.register_auth(lambda: True)
    return health_check_api_bp


class JsonRtn(object):

    def __init__(self, code: str, message: str = None, data: typing.Any = None):
        self._code = code
        self._message = message
        self._data = data

    @property
    def code(self) -> str:
        return self._code

    @property
    def message(self) -> str:
        return self._message

    @property
    def data(self) -> typing.Any:
        return self._data

    @staticmethod
    def construct(e_or_res):
        """Create JsonRtn instance from instance of BaseException or requests.Response."""
        if isinstance(e_or_res, errors.BaseError):
            code = e_or_res.code
            message = e_or_res.message
            data = e_or_res.data
        elif isinstance(e_or_res, BaseException):
            code = errors.error_code(e_or_res)
            message = str(e_or_res)
            data = None
        else:
            result = json.loads(e_or_res.text)
            code = result.get('code')
            message = result.get('message')
            data = result.get('data')
        return JsonRtn(code, message=message, data=data)

    def make_response(self):
        rtn = {'code': self._code, 'msg': self._message, 'data': self._data}
        return current_app.response_class(type_util.obj_to_json(rtn),
                                          mimetype=current_app.config["JSONIFY_MIMETYPE"])


def redirect_view(web_context, url, status=None):
    """redirect to url.
    :param str web_context: Web context.
    :param str url: url without site context prefix.
    :param int status:  http status code.
    :return:
    """

    if status is None:
        status = web_constant.HTTP_REDIRECT_AJAX if is_ajax_request() else HttpStatus.HTTP_REDIRECT
    url = url_join(web_context, url)
    return flask.redirect(url, status)
