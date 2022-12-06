import os
import random
from datetime import datetime
# 传入视频 进行保存
def Mp4(url_list_mp4,save_mp4_url):
    holle = 0
    for i in url_list_mp4:
        holle += 1
        mun = datetime.strftime(datetime.now(),'%Y%m%d%H%M%S')   + str(random.randint(99999,1000000))
        ru = save_mp4_url
        imgs = ru + 'www%s.mp4' % mun
        if not os.path.exists(ru):
            os.makedirs(ru)
        ress = requests.get(i)
        with open(imgs, 'wb') as f:
            f.write(ress.content)

    return '图片保存成功,共%s个'%holle







# 传入一个图片进行保存
def Png(url_list_mig,save_img_url):
    app = 0
    for i in url_list_mig:
        app += 1
        mun = datetime.strftime(datetime.now(),'%Y%m%d%H%M%S')   + str(random.randint(99999,1000000))
        ru = save_img_url
        imgs = ru + 'www%s.png' % mun
        if not os.path.exists(ru):
            os.makedirs(ru)
        ress = requests.get(i)
        with open(imgs, 'wb') as f:
            f.write(ress.content)
    return '图片保存成功,共%s张'%app



import requests
from bs4 import BeautifulSoup
def pa_www_txt(pa_url):
    from fake_useragent import UserAgent
    ua = UserAgent()
    # 写了一个UserAgent池
    lis = [ua.Chrome, ua.Firefox, ua.Safari, ua.Edge, ua.IE, ua.Safari]
    her = random.choice(lis)
    # 防止 反爬
    hd = {"User-Agent": her}
    url = pa_url
    res = requests.get(url, headers=hd)
    res.encoding  =  'UTF-8'
    return res.text





def pa_www_soup(pa_url):
    from fake_useragent import UserAgent
    ua = UserAgent()
    # 写了一个UserAgent池
    lis = [ua.Chrome, ua.Firefox, ua.Safari, ua.Edge, ua.IE, ua.Safari]
    her = random.choice(lis)
    # 防止 反爬
    hd = {"User-Agent": her}
    url = pa_url
    res = requests.get(url, headers=hd)
    res.encoding  =  'UTF-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # 返回的是一个列表
    return soup







