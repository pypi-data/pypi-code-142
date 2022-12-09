from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.chrome.options import Options

'''
   安装IdnsBot:
   pip install IdnsBot
   
   模块导入:
   import IdnsBot
   
   发送一条"helloworld"
   IdnsBot.send("helloworld")
   
   如果有人发送hello，回复你好
   if Bot.message=="hello":
       Bot.send_msg("你好")
                   
   使用愉快！！！
'''

headpr = "\033[34m"
endpr = "\033[0m"
headless = Options()
headless.add_argument("--headless")
headless.add_argument("--disable-gpu")

web = webdriver.Chrome(options=headless)
web.get("http://chat.idnsportal.com/idns_cn")
sleep(10)


class Bot:
    def send_msg(text):
        try:
            finded = web.find_element_by_xpath('//*[@id="message"]')
            finded.send_keys(text)
            web.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/a[2]').click()
            web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except:
            print(headpr + "技能冷却中" + endpr)

    ret = web.page_source
    a = '<div class="message-text">(.*?)</div>'
    message = re.findall(a, ret, flags=re.S)[-1]
    e = '<div class="message-name">(.*?)</div>'
    username = re.findall(e, ret)[-1].split(" | ")[0]
