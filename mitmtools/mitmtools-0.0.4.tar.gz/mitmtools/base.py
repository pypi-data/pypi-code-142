"""
    所有的程序主体结构
"""
from mitmtools.log import Logger
from mitmproxy import http
from urllib.parse import urlparse
from print_dict import format_dict


class MitmproxyBase:

    def __init__(self, encoding: str = 'utf-8'):
        self.logger = Logger()
        self.encoding = encoding

    def request(self, flow: http.HTTPFlow) -> None:
        """
        请求发起之前处理

        :param flow:
        :return:
        """
        self.show_request_detail(flow)

    def response(self, flow: http.HTTPFlow) -> None:
        """
        响应发送之前处理

        :param flow:
        :return:
        """
        self.show_response_detail(flow)

    @staticmethod
    def parse_request_headers(flow: http.HTTPFlow) -> dict:
        return dict(flow.request.headers)

    @staticmethod
    def parse_request_params(flow: http.HTTPFlow) -> dict:
        return dict(flow.request.query)

    @staticmethod
    def parse_request_cookie(flow: http.HTTPFlow) -> dict:
        if isinstance(flow.request.cookies, list):
            return dict(flow.request.cookies)
        else:
            return dict([(c[0], c[1]) for c in flow.request.cookies.fields])

    @staticmethod
    def parse_response_headers(flow: http.HTTPFlow) -> dict:
        return dict(flow.response.headers)

    @staticmethod
    def parse_response_cookie(flow: http.HTTPFlow) -> dict:
        if isinstance(flow.response.cookies, list):
            return dict(flow.response.cookies)
        else:
            return dict([(c[0], c[1]) for c in flow.request.cookies.fields])

    def show_request_detail(self, flow: http.HTTPFlow) -> None:
        """
        显示请求的详情字符串

        :return:
        """
        lines = [
            f'\n********** Request {flow.request.method} {flow.request.url}  **********',
            f'http_version: {flow.request.http_version}',
            f'headers: {format_dict(self.parse_request_headers(flow))}',
            f'params: {format_dict(self.parse_request_params(flow))}',
            f'cookie：{format_dict(self.parse_request_cookie(flow))}'
        ]
        self.logger.debug('\n'.join(lines))

    def show_response_detail(self, flow: http.HTTPFlow) -> None:
        """
        显示响应的详情字符串

        :return:
        """
        lines = [
            f'\n********** Response {flow.response.status_code} {flow.request.url}  **********',
            f'headers: {format_dict(self.parse_response_headers(flow))}',
            f'cookie: {format_dict(self.parse_response_cookie(flow))}',
            f'content_length: {len(flow.response.content)}'
        ]
        self.logger.debug('\n'.join(lines))

    @staticmethod
    def domain(flow: http.HTTPFlow) -> str:
        """
        获取域名

        :param flow:
        :return:
        """
        return urlparse(flow.request.url).netloc
