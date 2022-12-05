import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent


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
