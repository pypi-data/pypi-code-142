import sys
from threading import Thread
from types import FunctionType

from http_pyparser import response
from wsblib import log, request, route, server

from .encrypt import EncryptCookies


class Mathiz:
    def __init__(self, secret_key: str = None) -> None:
        self._process_request: request.ProcessRequest = None
        self._encrypt_cookies = None
        self._errors_callback = []
        self._routes = []

        if secret_key:
            self._encrypt_cookies = EncryptCookies(secret_key)

    def register_route(self, func: FunctionType, path: str, methods: tuple = ('GET',)) -> None:
        _route = route.Route(func, path, methods)
        self._routes.append(_route)

    def route(self, path: str, methods: tuple = ('GET',)) -> FunctionType:
        def decorator(func):
            self.register_route(func, path, methods=methods)

        return decorator

    def _process(self, client: server.Client, use_globals: bool) -> None:
        request_processed = self._process_request.process(client)

        if request_processed:
            _request = request_processed.request

            if self._encrypt_cookies:
                decrypted_cookies = self._encrypt_cookies.decrypt(_request.cookies)
                _request.cookies = decrypted_cookies
                request_processed.request = _request

            _response = request_processed.get_response(use_globals=use_globals)

            if self._encrypt_cookies and _response.cookies:
                new_cookies = self._encrypt_cookies.encrypt(_response.cookies)
                _response.cookies = new_cookies

            final_response = response.make_response(_response)

            log.log_request(_response, _request)
            client.send_message(final_response)
            client.destroy()

    def run(self, host: str = '127.0.0.1', port: int = 5500, use_globals: bool = True) -> None:
        print('Mathiz Framework started')
        print(f'Creating web server in {host}:{port} address...', end=' ')

        _server = server.Server()

        try:
            _server.start(host, port)
        except OSError as err:
            print(f'\033[31mFAILED\033[m')
            if err.errno == 98:
                print(f'\n\033[31mAddress already in use.\033[m')

            sys.exit(1)
        else:
            print('\033[32mOK\033[m\n')

        self._process_request = request.ProcessRequest(
            self._routes, self._errors_callback
        )

        print('- Learn about Mathiz in https://github.com/firlast/mathiz')
        print(f'- \033[32mThe server is running at http://{host}:{port}\n\033[m')

        try:
            while True:
                client = _server.wait_client()
                th = Thread(target=self._process, args=(client, use_globals))
                th.start()
        except (KeyboardInterrupt, SystemExit, SystemError):
            print('\n\033[31mServer closed!\033[m')
            _server.destroy()
