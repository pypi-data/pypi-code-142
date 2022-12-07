"""
    进行 js hook
    提供如下三种方法
        HookByHtml     通过 html 进行插入 script 标签
        HookByJs       通过获取 html 的第一个含有 url 的 script 标签，在其加载时进行注入
        HookByJsUrl    通过 js 的 url 进行注入

    注意：针对 html
        Content-Security-Policy 简称 csp 可以防止 xss 注入，一般在请求头或者 meta 标签里会有受信任的白名单
        学习链接：http://www.ruanyifeng.com/blog/2016/09/csp.html
        学习链接：https://blog.csdn.net/qq_25623257/article/details/90473859
        因此注入的代码将不会被执行

        突破 csp 的方法（有验证的话也没有用，网页不会正常加载）
            1、手动添加 b"script-src 'self' " 并保证请求头无 nonce-hash 的值
            2、将 nonce-hash 的值放在 script 标签上，none='hash'

    注意：所有方法都可能会被检测影响页面运行，但是方法能出来
"""
from loguru import logger
from mitmproxy import http
from bs4 import BeautifulSoup
from abc import abstractmethod
from urllib.parse import urljoin
from mitmtools.base import MitmproxyBase


class HookBase(MitmproxyBase):
    def __init__(self, filepath: str, domain: str = None, **kwargs):
        """
        通过 html 实现 hook

        :param filepath: hook 文件路径
        :param domain: 指定域名
        """
        super().__init__(**kwargs)
        self.filepath = filepath
        self.domain = domain

    def is_same_domain(self, flow) -> bool:
        """
        判断是否是同一个域名

        :return:
        """

        # 指定域名的话，判断是否是相同的域名
        if not self.domain:
            return True
        elif self.domain and super().domain(flow) == self.domain:
            return True

        return False

    @abstractmethod
    def response(self, flow: http.HTTPFlow) -> None:
        """
        根据响应 hook

        :param flow:
        :return:
        """
        pass

    def load_hook_file(self) -> str:
        """
        加载 hook 文件

        :return:
        """
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return '(() => {\n%s\n})();' % f.read()

    def is_html(self, flow: http.HTTPFlow) -> bool:
        """
        判断响应的是不是 html 文件

        :return:
        """
        is_html = False
        headers = self.parse_response_headers(flow)
        if 'Content-Type' in headers and 'text/html' in headers['Content-Type']:
            is_html = True
        elif 'content-type' in headers and 'text/html' in headers['content-type']:
            is_html = True

        return is_html


class HookByHtml(HookBase):
    def __init__(self, filepath: str, domain: str = None, **kwargs):
        """
        通过 html 实现 hook
        """
        super().__init__(filepath, domain, **kwargs)

    def response(self, flow: http.HTTPFlow) -> None:
        """
        如果响应是 html 则注入 hook
        增加一个 html script 标签

        注意：如果有检测 script 长度的可能会无效

        :param flow:
        :return:
        """
        if not self.is_same_domain(flow):
            return

        # 构造节点并插入 hook
        if self.is_html(flow) and flow.response.content:
            # 构造节点
            soup_text = BeautifulSoup(flow.response.text, 'lxml')
            tag = soup_text.new_tag(name='script')
            tag.string = self.load_hook_file()

            # 插入节点
            head = soup_text.find('head')
            if head:
                head.insert(0, tag)
            else:
                soup_text.find('body').insert(0, tag)

            # 替换响应
            flow.response.text = soup_text.__str__()

            # 是否有 csp 有就警告
            self.has_csp(flow)

            logger.debug(f'已替换响应：{flow.request.url}')

    def has_csp(self, flow: http.HTTPFlow) -> bool:
        """
        判断有无 csp 安全策略

        :return:
        """
        resp = flow.response
        if resp:
            headers = self.parse_response_headers(flow)
            if headers.get('content-security-policy') or headers.get('Content-Security-Policy'):
                logger.warning("网站已启用 CSP 防护，注入将不会生效！")
                return True
            elif 'content-security-policy' in resp.text or 'Content-Security-Policy' in resp.text:
                logger.warning("网站已启用 CSP 防护，注入将不会生效！")
                return True

        return False


class HookByJs(HookBase):
    def __init__(self, filepath: str, domain: str = None, **kwargs):
        """
        通过 html 的第一段外部 js 实现 hook
        """
        super().__init__(filepath, domain, **kwargs)
        self.replace_urls = []

    def response(self, flow: http.HTTPFlow) -> None:
        """
        如果响应是 js 直接注入代码

        :param flow:
        :return:
        """
        if not self.is_same_domain(flow):
            return

        # 解析 html 的第一个 script 标签地址并保存
        if self.is_html(flow):
            soup = BeautifulSoup(flow.response.text, 'lxml')
            scripts = soup.find_all('script')
            for script in scripts:
                if hasattr(script, 'attrs') and script.attrs.get('src') and script.attrs.get('src').endswith('.js'):
                    url = urljoin(flow.request.url, script.attrs.get('src'))
                    self.replace_urls.append(url)
                    break

        # 判断响应的是不是 js 文件
        is_js = False
        if flow.request.url.endswith('.js') or flow.request.url.endswith('.js.map'):
            is_js = True

        # 插入 hook
        if is_js and flow.response.content and flow.request.url in self.replace_urls:
            # 替换响应
            flow.response.content = (self.load_hook_file() + '\n').encode(self.encoding) + flow.response.content
            logger.debug(f'已替换响应：{flow.request.url}')


class HookByJsUrl(HookBase):
    def __init__(self, url: str, filepath: str, **kwargs):
        """
        通过 html 的第一段外部 js 实现 hook
        """
        super().__init__(filepath, **kwargs)
        self.url = url

    def response(self, flow: http.HTTPFlow) -> None:
        """
        如果响应是 js 直接注入代码

        :param flow:
        :return:
        """
        # 插入 hook
        if flow.response.content and flow.request.url == self.url:
            # 替换响应
            flow.response.content = (self.load_hook_file() + '\n').encode(self.encoding) + flow.response.content
            logger.debug(f'已替换响应：{flow.request.url}')
