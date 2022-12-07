"""
    根据 url 替换指定响应内容

    提供以下方法：
        ReplaceFileByUrl：根据 url 完全匹配 url，并替换响应
        ReplaceFileByRegex：根据正则进行判断 url，并替换响应
        ReplaceContentByUrl：根据 url 完全匹配 url，并替换部分响应
        ReplaceContentByRegex：根据正则进行判断 url，并替换部分响应
"""
import re
from typing import Dict
from loguru import logger
from mitmproxy import http
from abc import abstractmethod
from mitmtools.base import MitmproxyBase


class ReplaceBase(MitmproxyBase):

    def __init__(self, rule: str, filepath: str, max_times: int = None, **kwargs):
        """

        :param rule: 匹配规则
        :param filepath: 文件路径
        :param max_times: 匹配次数，默认无限匹配
        """
        super().__init__(**kwargs)
        self.rule = rule
        self.filepath = filepath
        self.max_times = max_times
        self.replace_times = 0  # 替换的次数

    def add_times(self):
        """
        匹配次数 +1

        :return:
        """
        if self.max_times:
            self.replace_times += 1

    @property
    def is_end(self) -> bool:
        """
        是否到最大次数了

        :return:
        """
        if self.max_times and self.replace_times >= self.max_times:
            return True

        return False

    @abstractmethod
    def is_this_url(self, flow: http.HTTPFlow) -> bool:
        """
        判断是否是当前 url

        :return:
        """
        pass

    def response(self, flow: http.HTTPFlow) -> None:
        """
        响应，拦截替换文件

        :param flow:
        :return:
        """
        self.show_response_detail(flow)

        if self.is_this_url(flow) and not self.is_end:
            self.add_times()

            with open(self.filepath, 'rb') as f:
                flow.response.content = f.read()
            logger.debug(f"{flow.request.url} 已替换文件：{self.filepath}")


class ReplaceFileByUrl(ReplaceBase):
    def __init__(self, url: str, filepath: str, max_times: int = None, **kwargs):
        """
        通过 url 的完全匹配 替换响应

        :param url: url
        :param filepath: 文件路径
        :param max_times: 匹配次数，默认无限匹配
        """
        super().__init__(url, filepath, max_times, **kwargs)

    def is_this_url(self, flow: http.HTTPFlow) -> bool:
        """
        判断是否是当前 url

        :return:
        """
        if flow.request.url == self.rule:
            return True

        return False


class ReplaceFileByRegex(ReplaceBase):
    def __init__(self, pattern: str, filepath: str, max_times: int = None, **kwargs):
        """
        通过正则来匹配 url 替换响应

        :param pattern: 正则匹配规则
        :param filepath: 文件路径
        :param max_times: 匹配次数，默认无限匹配
        """
        super().__init__(pattern, filepath, max_times, **kwargs)

    def is_this_url(self, flow: http.HTTPFlow) -> bool:
        """
        判断当前是当前 url

        :param flow:
        :return:
        """
        if re.search(r"%s" % self.rule, flow.request.url):
            return True

        return False


class ReplaceContentByUrl(ReplaceFileByUrl):
    def __init__(self, url: str, replace_dict: Dict[str, str], max_times: int = None, **kwargs):
        """
        通过 url 的完全匹配 替换响应

        :param url: url
        :param replace_dict: 替换的字典
        :param max_times: 匹配次数，默认无限匹配
        """
        super().__init__(url, '', max_times, **kwargs)
        self.replace_dict = replace_dict

    def response(self, flow: http.HTTPFlow) -> None:
        """
        响应，拦截替换文件

        :param flow:
        :return:
        """
        self.show_response_detail(flow)

        if self.is_this_url(flow) and not self.is_end:
            self.add_times()

            for key, value in self.replace_dict.items():
                flow.response.content = flow.response.content.replace(
                    key.encode(self.encoding),
                    value.encode(self.encoding)
                )


class ReplaceContentByRegex(ReplaceFileByRegex):
    def __init__(self, pattern: str, replace_dict: Dict[str, str], max_times: int = None, **kwargs):
        """
        通过正则来匹配 url 替换响应

        :param pattern: 正则匹配规则
        :param replace_dict: 替换的字典
        :param max_times: 匹配次数，默认无限匹配
        """
        super().__init__(pattern, '', max_times, **kwargs)
        self.replace_dict = replace_dict

    def response(self, flow: http.HTTPFlow) -> None:
        """
        响应，拦截替换文件

        :param flow:
        :return:
        """
        self.show_response_detail(flow)

        if self.is_this_url(flow) and not self.is_end:
            self.add_times()

            for key, value in self.replace_dict.items():
                flow.response.content = flow.response.content.replace(
                    key.encode(self.encoding),
                    value.encode(self.encoding)
                )
