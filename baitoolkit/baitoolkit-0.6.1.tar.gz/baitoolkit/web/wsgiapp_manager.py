# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from xmlrpc.server import CGIXMLRPCRequestHandler

from gunicorn.app.base import BaseApplication

from baitoolkit.common import logger_factory


class CGIXMLRPCReqHandler(CGIXMLRPCRequestHandler):
    """
        Explode CGIXMLRPCRequestHandler._marshaled_dispatch to public method
    """

    def __init__(self, allow_none=True, encoding=None, use_builtin_types=False):
        """
        :param bool allow_none: parameter of CGIXMLRPCRequestHandler
        :param bool encoding: parameter of CGIXMLRPCRequestHandler
        :param bool use_builtin_types: parameter of CGIXMLRPCRequestHandler
        """
        CGIXMLRPCReqHandler.__init__(self, allow_none, encoding, use_builtin_types)

    def marshaled_dispatch(self, data, dispatch_method=None, path=None):
        return self._marshaled_dispatch(data, dispatch_method=dispatch_method, path=path)


class WsgiXmlRpcApplication(object):
    """
        Application to handle xml prc requests.
    """

    __logger = logger_factory.get_logger(__name__)

    def __init__(self, instance=None, methods=None, allow_none=True, encoding=None, use_builtin_types=False):
        """

        :param object instance:  an object which is used to expose method names which have not been registered
                                using register_function().
        :param list|generator methods:  a function list/generator that can respond to XML-RPC requests.
        :param bool allow_none: parameter of CGIXMLRPCRequestHandler
        :param bool encoding: parameter of CGIXMLRPCRequestHandler
        :param bool use_builtin_types: parameter of CGIXMLRPCRequestHandler
        """
        if methods is None:
            methods = []
        self._req_handler = CGIXMLRPCReqHandler(allow_none=allow_none, encoding=encoding,
                                                use_builtin_types=use_builtin_types)
        if instance is not None:
            self._req_handler.register_instance(instance)
        for method in methods:
            self._req_handler.register_function(method)
        self._req_handler.register_introspection_functions()

    def register_instance(self, instance):
        return self._req_handler.register_instance(instance)

    def register_function(self, func, name=None):
        return self._req_handler.register_function(func, name)

    def handler_app(self, environ, start_response):
        """
            xml rpc service for gunicorn to communicate with
        """
        length = int(environ['CONTENT_LENGTH'])

        if environ['REQUEST_METHOD'] in ('POST', 'PUT', 'GET'):
            try:
                data = environ['wsgi.input'].read(length)
                response = self._req_handler.marshaled_dispatch(data, getattr(self.dispatcher, '_dispatch', None))
                response += b'\n'
                start_response("200 OK", [('Content-Type', 'text/xml'), ('Content-Length', str(len(response)),)])
                return [response]
            except Exception as e:
                self.__logger.exception("failed to call due to %s." % str(e))
                start_response("500 Server error %s" % str(e), [('Content-Type', 'text/plain')])
                return []
        else:
            start_response("400 Bad request", [('Content-Type', 'text/plain')])
            return ['']

    def __call__(self, environ, start_response):
        return self.handler_app(environ, start_response)


def start_wsgi_xml_rpc_server(wsgi_xml_rpc_app, **options):
    """
    start wsgi xml rpc server
    :param WsgiXmlRpcApp wsgi_xml_rpc_app: instance of WsgiXmlRpcApplication
    :param options:
    :return: void
    """

    class Application(BaseApplication):

        def __init__(self, app, kwargs=None):
            self.options = kwargs or {}
            self.application = app
            super(Application, self).__init__()

        def init(self, parser, opts, args):
            pass

        def load_config(self):
            config = dict([(key, value) for key, value in self.options.iteritems()
                           if key in self.cfg.settings and value is not None])
            for key, value in config.iteritems():
                self.cfg.set(key.lower(), value)

        def load(self):
            return self.application

    Application(wsgi_xml_rpc_app, options).run()
