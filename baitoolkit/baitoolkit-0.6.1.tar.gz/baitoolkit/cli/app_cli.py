# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import click

from baitoolkit.common import logger_factory
from baitoolkit.common.context_manager import global_ctx


@click.group()
def webserver_group():
    """Execute relate commands with web server."""


@webserver_group.command(name='start')
@click.option('-h', '--host', default='127.0.0.1', help='The host to listen on.')
@click.option('-p', '--port', default='5000', help='The port to listen on.')
def start_cmd(host, port):
    """Start app."""
    context = click.get_current_context().obj
    app = context.load_app()
    if context.is_debug():
        app.run(host=host, port=port)
    else:
        start_in_gunicorn(app, global_ctx.get_gunicorn_config_value())


def start_in_gunicorn(flask_app, g_conf):
    """Run inside gunicorn.
    :param Application flask_app: Flask app instance
    :param dict g_conf: gunicorn config.
    :return:
    """
    from gunicorn.app.base import Application as BaseApplication

    class Application(BaseApplication):

        def __init__(self, app1, kwargs=None):
            self.options = kwargs or {}
            self.application = app1
            super(Application, self).__init__()

        def init(self, parser, opts, args):
            pass

        def load_config(self):
            for k, v in g_conf.items():
                self.cfg.set(k.lower(), v)

        def load(self):
            return self.application

    gunicorn_logger = logger_factory.get_logger('gunicorn.error')
    flask_app.logger.handlers = gunicorn_logger.handlers
    flask_app.logger.setLevel(gunicorn_logger.level)
    g_app = Application(flask_app)
    g_app.run()
