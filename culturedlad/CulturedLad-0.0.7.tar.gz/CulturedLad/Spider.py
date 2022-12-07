import json
import os
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent


# << 传一个域名，查询IP地址 >>
def get_address_by_ip(ip):
    hd = {'User-Agent': FakeUserAgent().random}
    url = 'https://ip.hao86.com/' + ip + '/'
    r = requests.get(url, headers=hd)
    r.encoding = 'UTF-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    address = soup.select(
        'body > div.comm-content-box.clearfloat > div > div.comm-content-left.clearfloat > div > div.xq_toggle > div:nth-child(2) > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)')
    return address[0].string


# IP = input('输入你要查询的IP:')  # 221.218.142.209
# address = get_address_by_ip(IP)
# print(address)


# << 传一个正常数据网址，引用页可以不传，生成soup >>
def get_soup(url, Referer=None):
    hd = {'User-Agent': FakeUserAgent().random, 'Referer': Referer}  # Referer:re_url 设置引用页
    r = requests.get(url, headers=hd)  # 获取网页源代码
    r.encoding = 'UTF-8'
    soup = BeautifulSoup(r.text, 'html.parser')  # 把网页源代码转换成可以操作的html
    return soup


# Re = 'http://tour.jschina.com.cn/gdxw/'
# url = 'http://tour.jschina.com.cn/gdxw/202212/t20221201_3122398.shtml'
# A = get_soup(url, Referer=Re)
# print(A)

# << 传一个异步数据网址，引用页可以不传，生成soup >>
def get_soup_yb(url, key, Referer=None):
    hd = {'User-Agent': FakeUserAgent().random, 'Referer': Referer}  # Referer:re_url 设置引用页
    r = requests.get(url, headers=hd)  # 获取网页源代码
    r.encoding = 'UTF-8'
    dic = json.loads(r.text)  # 字符串转json数据  用 json.loads(内容)
    html_doc = dic.get(key)  # 通过 .get('键')  取出值即可
    soup = BeautifulSoup(html_doc, 'html.parser')  # 把网页源代码转换成可以操作的html
    return soup


# re_url = 'https://www.thecfa.cn/index.html'
# url = 'https://www.thecfa.cn/nvzgjd/dataApi/text/v1?contId=30235&next=-1'
# A = get_soup(url, Referer=re_url)
# print(A)


# << 传一个图片地址,保存图片到本地 >>
def post_img_one(url):
    root = 'E:/Spider/'  # 爬取到的图片存在电脑那个磁盘位置
    img_file = requests.get(url)  # 获取图片对象
    print("文件大小", len(img_file.content) / 1024, "kb")
    try:
        if not os.path.exists(root):  # 判断磁盘制定文件夹是否存在，
            os.makedirs(root)  # 如果不存在就创建文件夹
        time_now = time.time()  # 当前时间戳
        img_new = str(time_now) + url.split('/')[-1]  # 图片名
        path = root + img_new  # 路径+图片名
        with open(path, "wb") as f:
            print("正在保存文件...")
            f.write(img_file.content)  # 向文件中写入二进制内容
            print("文件保存成功")
    except Exception as e:
        print("爬取失败", e)
    return '图片保存完成!'


# x = 'http://img.netbian.com/file/2022/1030/small152024dl9rV1667114424.jpg'
# s = post_img_one(x)
# print(s)


# << 传一个图片地址列表,保存图片到本地 >>
def post_img_arr(arr):
    root = 'E:/Spider/'  # 爬取到的图片存在电脑那个磁盘位置
    for i in arr:
        img_file = requests.get(i)  # 获取图片对象
        print("文件大小", len(img_file.content) / 1024, "kb")
        try:
            if not os.path.exists(root):  # 判断磁盘制定文件夹是否存在，
                os.makedirs(root)  # 如果不存在就创建文件夹
            time_now = time.time()  # 当前时间戳
            img_new = str(time_now) + i.split('/')[-1]  # 图片名
            path = root + img_new  # 路径+图片名
            with open(path, "wb") as f:
                print("正在保存文件...")
                f.write(img_file.content)  # 向文件中写入二进制内容
                print("文件保存成功")
        except Exception as e:
            print("爬取失败", e)
    return '图片保存完成!'


# a = ['http://img.netbian.com/file/2022/1030/small152024dl9rV1667114424.jpg',
#      'http://img.netbian.com/file/2022/1030/small152503ascFA1667114703.jpg',
#      'http://img.netbian.com/file/2022/1030/small233443Tpprj1667144083.jpg',
#      'http://img.netbian.com/file/2022/1030/small233855f9f401667144335.jpg',
#      'http://img.netbian.com/file/2022/1030/small000627niOmk1667059587.jpg',
#      ]
# s = post_img_arr(a)
# print(s)

"""
爬虫常用笔记总结
"""

"""
import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent

hd = {'User-Agent': FakeUserAgent().random}
r = requests.get('https://www.meishij.net/fenlei/zaocan/', headers=hd)
# r.status_code   # 查看状态
# r.encoding  # 编码 ISO-8859-1
r.encoding = 'UTF-8'  # 转换编码格式
soup = BeautifulSoup(r.text, 'html.parser')  # r.content

"""

"""
指定标签
alst = soup.find_all('table')
for i in alst:
    print(i.a.get('title'), i.span.string, '\t', i.p.string)

指定样式 class_
info_all = soup.find_all('div', class_='list_s2_item')
for i in info_all:
    info1 = i.find('a', class_='list_s2_item_info').strong.string
    info2 = i.find('a', class_='list_s2_item_info').span.string

指定元素
address = soup.select(
    'body > div.comm-content-box.clearfloat > div > div.comm-content-left.clearfloat > div > div.xq_toggle > div:nth-child(2) > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)')
print(address[0].string)
"""

"""
获取内容语法
data.get_text()   # 获取data中文本内容
p.string  # <p>张三<p>
a.get('title')  # <a>title='张三'</a>
"""
