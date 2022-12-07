import os

import tornado.web
from tornado.web import Application

from tornado_replay.base import BaseRequestHandler, NotFoundRequestHandler
from tornado_replay.handler import (
    InspectHttpIndexHandler, InspectHttpLiveHandler, InspectHttpRecordHandler,
)
from tornado_replay.queue import global_inspect_buffer


def init_app(app_: Application, *, record_size: int = 200):
    """Initialize tornado_replay into Tornado Application

    :param app_: Tornado Application instance
    :param record_size: the count of request recorded,
    """
    inspect_handlers = [
        ('/inspect', InspectHttpIndexHandler),
        ('/inspect/http/live', InspectHttpLiveHandler),
        ('/inspect/http/(.+)', InspectHttpRecordHandler),
        # serve static files
        (
            '/inspect/static/(.+)',
            tornado.web.StaticFileHandler,
            {'path': os.path.abspath(
                os.path.join(
                    os.path.dirname(os.path.dirname(__file__)), 'statics'
                )
            )}
        )
    ]
    app_.add_handlers('.*', inspect_handlers)
    app_.settings.update({'default_handler_class': NotFoundRequestHandler})

    global_inspect_buffer.cache_size = record_size
