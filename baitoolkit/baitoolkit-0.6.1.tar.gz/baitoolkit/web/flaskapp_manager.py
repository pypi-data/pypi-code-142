# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import os
import typing

from flask import current_app, Flask
from flask import request

from baitoolkit.auth import iam_client
from baitoolkit.auth.iam_client import AuthorizationError
from baitoolkit.common import logger_factory, localization
from baitoolkit.common.context_manager import global_ctx
from baitoolkit.common.type_util import Singleton
from baitoolkit.exception import errors
from baitoolkit.exception.errors import ExternalError
from baitoolkit.web.blueprint import JsonRtn
from baitoolkit.web.web_constant import HttpStatus


class FlaskAppManager(object, metaclass=Singleton):
    __logger = logger_factory.get_logger(__name__)

    def create_flask_application(self, app_id, root_path, flask_conf_dict, error_render=None):
        """
            Create flask app
        :param str app_id:
        :param str root_path:
        :param dict flask_conf_dict:
        :param function error_render:
        Return flask.Application
        """
        static_folder = os.path.join(root_path, 'static')
        template_folder = os.path.join(root_path, 'templates')
        app = Flask(app_id, root_path=root_path, static_folder=static_folder, template_folder=template_folder)
        app.secret_key = flask_conf_dict.get('APP_SECRET_KEY')
        app.config.from_mapping(**flask_conf_dict)
        self.register_error_handler(app, error_render)
        self.register_template_context(app)
        self.init_localization(app)
        self.init_debugger(app)
        self.init_login_manager(app)
        return app

    @staticmethod
    def init_localization(app):
        flask_conf_dict = global_ctx.get_web_config_value()
        for key in flask_conf_dict.keys():
            if key.startswith('BABEL_'):
                localization.init_babel(app)
                return True
        return False

    @staticmethod
    def init_login_manager(app):
        iam_client.init_login_manager(app)

    def init_debugger(self, app):
        flask_conf_dict = global_ctx.get_web_config_value()
        if flask_conf_dict.get("DEBUG"):
            return False

        def query_profiler(response):
            threshold = flask_conf_dict.get('SLOW_QUERY_THRESHOLD')
            if not threshold:
                return response
            for q in global_ctx.db_client_manager.get_debug_queries():
                if q.duration >= threshold:
                    self.__logger.warning(
                        'Slow query: Duration: %fs\n Context: %s\nQuery: %s\n '
                        % (q.duration, q.context, q.statement)
                    )
            return response

        app.after_request(query_profiler)

    def render_exception_response(self, status, title, e):
        """render exception response"""
        msg = '[%s] %s' % (request.path, e)
        self.__logger.exception(msg)
        rtn = JsonRtn.construct(e)
        return rtn.make_response(), status

    def register_error_handler(self, app: Flask, error_render: typing.Callable,
                               handlers: typing.List = None) -> typing.NoReturn:
        """
        Register error handlers to Flask application.
        :param Flask.Application app:
        :param function(status, message, e) error_render: function with 3 arguments.
            int status: Http status code.
            str message: Http status message.
            Exception e: Exception instance.
        :param [(error code or exception, handler function)] handlers: additional error handlers.
        """
        if error_render is None:
            error_render = self.render_exception_response

        @app.errorhandler(HttpStatus.HTTP_BAD_REQUEST)
        def bad_request(e) -> typing.Any:
            return error_render(HttpStatus.HTTP_BAD_REQUEST, 'Bad Request', e)

        @app.errorhandler(HttpStatus.HTTP_NOT_FOUND)
        def page_not_found(e) -> typing.Any:
            return error_render(HttpStatus.HTTP_NOT_FOUND, 'Page Not Found', e)

        @app.errorhandler(HttpStatus.HTTP_INTERVAL_ERROR)
        def internal_server_error(e) -> typing.Any:
            return error_render(HttpStatus.HTTP_INTERVAL_ERROR, 'Internal Server Error', e)

        @app.errorhandler(errors.InternalError)
        def request_error(e):
            return error_render(HttpStatus.HTTP_INTERVAL_ERROR, "Internal Error", e)

        @app.errorhandler(ExternalError)
        def request_error(e):
            return error_render(HttpStatus.HTTP_FORBIDDEN, "External Error", e)

        @app.errorhandler(AuthorizationError)
        def authorization_error(e):
            return error_render(HttpStatus.HTTP_NO_AUTHORIZATION, "Authorization Error", e)

        @app.errorhandler(Exception)
        def unknown_error(e):
            return error_render(HttpStatus.HTTP_INTERVAL_ERROR, 'Unknown Server Error', e)

        if handlers is None:
            return

        for (code_ex, handler) in handlers:
            app.register_error_handler(code_ex, handler)

    @staticmethod
    def register_template_context(app: Flask):
        @app.context_processor
        def make_template_context():
            return dict(version=global_ctx.app_version, t_=localization.t_, l_=localization.l_)

        app.jinja_env.auto_reload = True
        app.jinja_env.trim_blocks = True
        app.jinja_env.add_extension('jinja2.ext.do')
        app.jinja_env.add_extension('baitoolkit.common.jinja_extension.spaceless')
        app.jinja_env.filters['lot'] = localization.to_datetime_of_user_preferred_tz
        return app.jinja_env

    @staticmethod
    def get_all_routes(app: Flask = None) -> str:
        """Return all routes."""
        app = app if app is not None else current_app
        return app.url_map


app_manager = FlaskAppManager()
