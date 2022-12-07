import requests
from bs4 import BeautifulSoup

def bian(url):
    # 获取源代码
    r = requests.get(url)
    r.encoding = "UTF-8"
    # print(r.text)

    # 实例化bs对象
    soup = BeautifulSoup(r.text, 'html.parser')
    for i in range(1, 21):
        address = soup.select('#main > div.slist > ul > li:nth-child(' + str(i) + ') > a')
        add = str(address[0].get('href')).split('/')[2]
        addr = add.split('.')[0]
        urls = 'https://pic.netbian.com/tupian/' + addr + '.html'
        rs = requests.get(urls)
        r.encoding = "UTF-8"
        soups = BeautifulSoup(rs.text,'html.parser')
        img = soups.select('#img > img')
        img_url = 'https://pic.netbian.com' + img[0].get('src')
        suffix = img_url.split('/')[-1]
        urlq = requests.get(img_url)
        with open('teacherImage/' + suffix, 'wb') as f:  # wb指示以二进制模式打开文件以进行写入
            f.write(urlq.content)  # 转换二进制字节
        print('>>', img_url)




