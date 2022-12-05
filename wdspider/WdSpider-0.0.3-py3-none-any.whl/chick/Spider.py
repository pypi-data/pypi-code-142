# -----生成soup-----
import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent


def get_soup(url, Referer=None):
    hd = {'User-Agent': FakeUserAgent().random, 'Referer': Referer}  # Referer:re_url 设置引用页
    r = requests.get(url, headers=hd)  # 获取网页源代码
    r.encoding = 'UTF-8'
    # dic=json.loads(r.text)    # 字符串转json数据  用 json.loads(内容)
    # html_doc=dic.get('text')  # 通过 .get('键')  取出值即可
    soup = BeautifulSoup(r.text, 'html.parser')  # 把网页源代码转换成可以操作的html
    return soup


# Re = 'http://tour.jschina.com.cn/gdxw/'
# url = 'http://tour.jschina.com.cn/gdxw/202212/t20221201_3122398.shtml'
# A = get_soup(url, Referer=Re)
# print(A)