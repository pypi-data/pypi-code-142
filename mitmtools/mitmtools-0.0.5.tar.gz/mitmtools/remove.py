"""
    内容去除

    提供以下方法：
        RemoveContentByUrl：根据 url 完全匹配 url，并替换部分响应
        RemoveContentByRegex：根据正则进行判断 url，并替换部分响应
"""
import re
from typing import List
from mitmproxy import http
from abc import abstractmethod
from mitmtools.base import MitmproxyBase


class RemoveBase(MitmproxyBase):
    def __init__(self, rule: str, remove_list: List[str], max_times: int = None, **kwargs):
        """

        :param rule: 匹配规则
        :param remove_list: 移除列表
        :param max_times: 匹配次数，默认无限匹配
        """
        super().__init__(**kwargs)
        self.rule = rule
        self.remove_list = remove_list
        self.max_times = max_times
        self.remove_times = 0  # 移除的次数

    def add_times(self):
        """
        匹配次数 +1

        :return:
        """
        if self.max_times:
            self.remove_times += 1

    @property
    def is_end(self) -> bool:
        """
        是否到最大次数了

        :return:
        """
        if self.max_times and self.remove_times >= self.max_times:
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
        遍历替换响应内容

        :param flow:
        :return:
        """
        if self.is_this_url(flow) and not self.is_end:
            self.add_times()

            for r in self.remove_list:
                flow.response.content = flow.response.content.replace(r.encode(self.encoding), b'')


class RemoveContentByUrl(RemoveBase):

    def __init__(self, url: str, remove_list: List[str], **kwargs):
        """
        取值响应的指定内容

        :param url:
        :param remove_list:
        """
        super().__init__(url, remove_list, **kwargs)

    def is_this_url(self, flow: http.HTTPFlow) -> bool:
        """
        判断是否是当前 url

        :return:
        """
        if flow.request.url == self.rule:
            return True

        return False


class RemoveContentByRegex(RemoveBase):

    def __init__(self, pattern: str, remove_list: List[str], **kwargs):
        """
        取值响应的指定内容

        :param pattern: 正则匹配 url 规则
        :param remove_list: 移除列表
        """
        super().__init__(pattern, remove_list, **kwargs)

    def is_this_url(self, flow: http.HTTPFlow) -> bool:
        """
        判断当前是当前 url

        :param flow:
        :return:
        """
        if re.search(r"%s" % self.rule, flow.request.url):
            return True

        return False
