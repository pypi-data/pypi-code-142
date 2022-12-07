from lxml.etree import HTML
import requests
from pydantic import BaseModel, constr, HttpUrl
from typing import List
from urllib.parse import unquote
from unicodedata import normalize
from .utils import normalize_html_text, is_all_english
from pathlib import Path
import re


class Info(BaseModel):
    key: str
    values: List[str]
    
    
class Image(BaseModel):
    src: str
    tag: str
    
    def _download(self) -> bytes:
        res = requests.get(url=self.src)
        return res.content
    
    def save(self, file_path: Path):
        with open(file_path, 'wb') as f:
            f.write(self._download())


class Item(BaseModel):
    """百科的一个条目
    - name: 词条名称
    - desc: 词条描述,用于混淆词条
    - summary: 词条摘要
    - synonym: 同义词
    """
    url: HttpUrl = ''
    name: constr(strip_whitespace=True)
    desc: constr(strip_whitespace=True)
    summary: constr(strip_whitespace=True)
    synonyms: List[constr(strip_whitespace=True, min_length=1)]
    information: List[Info] = []
    images: List[Image] = []


class BaiduPedia:
    """百度百科
    """
    item_base_url = "https://baike.baidu.com/item/"
    search_base_url = 'https://baike.baidu.com/search?word='
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' }

    def _get_item_url(self, item_query: str) -> str:
        return self.item_base_url + item_query
    
    def _get_item_html(self, url: str) -> HTML:
        """根据地址读取静态页面
        """
        res = requests.get(url=url, headers=self.headers)
        res.encoding = 'utf-8'
        html = HTML(text=res.text)
        return html
        
    def _get_item_summary(self, html) -> str:
        """获取该词条的简介
        """
        sum_ls = html.xpath('//div[@class="lemma-summary"]//text()')
        summary = ''.join([item.strip('\n') for item in sum_ls])
        summary = normalize('NFKC', summary) # 将\xa0类似的unicode字符转换为正常字符
        return summary
    
    def _get_item_desc(self, html) -> str:
        """获取该词条的描述
        """
        desc_ls = html.xpath('//div[@class="lemma-desc"]//text()')
        return ''.join(desc_ls)
    
    def _get_item_name(self, html) -> str:
        """获取该词条中的名称
        """
        item_name: List = html.xpath('//h1/text()')
        assert len(item_name) == 1
        return item_name[0]
    
    def _get_item_synonyms(self, html) -> List[str]:
        """获取该词条的所有同义词
        """
        return html.xpath('//a[@title="同义词"]//following-sibling::span/text()')
    
    def _get_item_info(self, html) -> List[Info]:
        """获取该词条的知识三元组
        """
        info_ls = []
        keys = html.xpath('//dt[@class="basicInfo-item name"]')
        for k in keys:
            key = normalize_html_text(k.text)
            vs = k.xpath('./following-sibling::dd[@class="basicInfo-item value"][1]//text()')
            v = ''.join(vs)
            vs = v.split('\n')
            new_ls = []
            for v in vs:
                for new in v.split('、'):
                    new = normalize_html_text(new)
                    if len(new)>0 and new != key and new != '展开' and new != '收起':
                        if is_all_english(new):
                            new_ls.append(v)
                        else:
                            new_ls.append(new)
            info = Info(key=key, values=new_ls)
            info_ls.append(info)
        return info_ls
    
    def _get_item_image(self, html) -> List[Image]:
        """获取该词条相关的图片
        """
        images = []
        for img_e in html.xpath('//img'):
            src: str = img_e.get('src')
            alt: str = img_e.get('alt')
            if alt is not None and src is not None:
                if src.startswith('http') or src.startswith('https'):
                    item_name = self._get_item_name(html=html)
                    if item_name in alt:
                        images.append(Image(src=src, tag=alt))
        return images
    
    def _parse_item_html(self, html):
        item_name = self._get_item_name(html)
        item_summary = self._get_item_summary(html)
        item_desc = self._get_item_desc(html)
        item_synonyms = self._get_item_synonyms(html=html)
        item_info = self._get_item_info(html=html)
        images = self._get_item_image(html=html)
        return Item(name=item_name, summary=item_summary, desc=item_desc, synonyms=item_synonyms, information=item_info, images=images)
    
    def _get_search_url(self, search_text) -> str:
        return self.search_base_url + search_text
    
    def _get_search_html(self, url: str):
        res = requests.get(url=url, headers=self.headers)
        res.encoding = 'utf-8'
        html = HTML(text=res.text)
        return html
    
    def _has_search_results(self, html) -> bool:
        no_results = html.xpath('//div[@class="no-result"]/text()')
        return len(no_results) == 0
    
    def _get_searched_item_urls(self, html) -> List[str]:
        urls = []
        for a in html.xpath('//a[@class="result-title J-result-title"]'):
            item_query_ls: List = a.get('href').split('/item/')[-1].split('/')
            item_query = unquote(item_query_ls.pop(0)) # 将urlencode 转码为字符串
            item_query_ls  = [item_query] + item_query_ls
            item_query = '/'.join(item_query_ls)
            item_url = self._get_item_url(item_query=item_query)
            urls.append(item_url)
        return urls
    
    def search(self, search_text: str, num_return_items: int = 1) -> List[Item]:
        """根据搜索的内容自动搜索百科条目

        Args:
            search_text (str): 带搜索的文本
            num_return_items (int, optional): 返回的搜索的条目. Defaults to 1.

        Returns:
            List[Item]: 所有返回条目
        """
        items = []
        url = self._get_search_url(search_text=search_text)
        html = self._get_search_html(url=url)
        if self._has_search_results(html=html):
            urls = self._get_searched_item_urls(html=html)
            num_items = int(max(min(num_return_items, len(urls)), 1))
            for url in urls[0: num_items]:
                item_html = self._get_item_html(url)
                item = self._parse_item_html(html=item_html)
                item.url = url
                items.append(item)
        return items
    
class Answer(BaseModel):
    text: constr(strip_whitespace=True, min_length=1)   
    
class Question(BaseModel):
    url: str
    title: constr(strip_whitespace=True, min_length=1)
    content: constr(strip_whitespace=True, min_length=0)
    answers: List[Answer]
    
    
class BaiduZhidao:
    def __init__(self) -> None:
        super().__init__()
        self.headers = { 'cookie': self._get_cookie(),
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' }

    def _get_cookie(self) -> str:
        """首次访问百度知道获取cookie
        """
        r = requests.get('https://zhidao.baidu.com/')
        cookie_text = r.headers['Set-Cookie']
        span = re.search('BAIDUID=.{37}', cookie_text).span() # 百度知道的cookie位37位字符
        start = span[0] + len('BAIDUID=')
        end = span[1]
        cookie = cookie_text[start: end]
        return cookie
    
    def _get_searched_html(self, url) -> HTML:
        res = requests.get(url=url, headers=self.headers)
        res.encoding = 'utf-8'
        html = HTML(res.text)
        return html
    
    def _get_searched_question_urls(self, query: str, max_questions: int= 10) -> List[str]:
        """通过搜索获取问答的地址
        - query: 带搜索的问题
        - max_questions: 最大问答数
        """
        urls = []
        max_page = max_questions // 10
        for i in range(0, max_page):
            s_url = f'https://zhidao.baidu.com/search?word={query}&pn={i}'
            html = self._get_searched_html(url=s_url)
            for e in html.xpath('//dt[contains(@alog-alias, "result-title")]'):
                a = e.xpath('.//a')[0]
                url: str = a.get('href')
                if len(urls) < max_questions and url is not None:
                    if not url.startswith('https'):
                        url = 'https' + url[4:] # 改为https
                    urls.append(url)
        return urls
            
    def _parse_question_url(self, url) -> Question:
        """将搜索得到的问题的url解析为question对象
        """
        res = requests.get(url=url, headers=self.headers)
        res.encoding = 'gbk'
        html = HTML(res.text)
        title = html.xpath('//span[@class="ask-title"]/text()')[0]
        contents = html.xpath('//div[@class="line mt-5 q-content"]/span[@class="con-all"]/text()')
        content = ''.join(contents).strip()
        ans_eles = html.xpath('//div[@class="rich-content-container rich-text-"]')
        answers = []
        for ans in ans_eles:
            ans_text = ''.join(ans.xpath('.//text()')).strip()
            ans_text = normalize_html_text(ans_text)
            answer = Answer(text=ans_text)
            if answer not in answers:
                answers.append(answer)
        ques = Question(title=title, content=content, answers=answers, url=url)
        return ques
    
    def search(self, query: str, num_return_questions: int = 10) -> List[Question]:
        """搜索查询问题,返回Question对象

        Args:
            query (str): 查询问题
            max_return_questions (int, optional): 最大返回问题数量. Defaults to 10.

        Returns:
            List[Question]: 所有查询到的相关问题
        """
        questions = []
        urls = self._get_searched_question_urls(query=query, max_questions=num_return_questions)
        for url in urls:
            ques = self._parse_question_url(url=url)
            questions.append(ques)
        return questions