# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import types

from flask.cli import ScriptInfo

from baitoolkit.common.context_manager import AppContext
from baitoolkit.parallel import mutex
from baitoolkit.web.flaskapp_manager import app_manager


class ClickContext(ScriptInfo):
    """Command context."""

    def __init__(self, global_context: AppContext, init_app: types.FunctionType):
        super(ClickContext, self).__init__(set_debug_flag=False)
        self._global_context = global_context
        self._init_app = init_app
        self.__loaded_app = None
        self.__lock = mutex.create_lock()

    def is_debug(self):
        """Return True for debug mode."""
        return self._global_context.get_web_config_value("DEBUG")

    def load_app(self):
        """Loaded Flask App"""
        if self.__loaded_app is not None:
            return self.__loaded_app

        def load_create_app():
            web_config_dict = self._global_context.get_web_config_value()
            application = app_manager.create_flask_application(self._global_context.app_id,
                                                               self._global_context.app_root_path,
                                                               web_config_dict)
            return application

        with self.__lock:
            app = load_create_app()
            self._init_app(app, self._global_context)
            self.__loaded_app = app
        return app


def make_click_context(global_context: AppContext, init_app: types.FunctionType):
    class ClickContextWrapper(ClickContext):

        def __init__(self):
            super(ClickContextWrapper, self).__init__(global_context, init_app)

    return ClickContextWrapper
