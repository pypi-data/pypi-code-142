from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.chrome.options import Options

'''
   安装IdnsBotCh:
   pip install IdnsBotCh
   
   模块导入:
   import IdnsBotCh
   
   发送一条"helloworld"
   IdnsBotCh.send("helloworld")
   
   如果有人发送hello，回复你好
   if IdnsBotCh.Bot.message=="hello":
       IdnsBotCh.Bot.send_msg("你好")
                   
   使用愉快！！！
'''

headpr = "\033[34m"
endpr = "\033[0m"
headless = Options()
headless.add_argument("--headless")
headless.add_argument("--disable-gpu")

print("机器人初始化中...")
web = webdriver.Chrome(options=headless)
web.get("http://chat.idnsportal.com/idns_cn")
sleep(8)
print(headpr+"机器人初始化完成"+endpr)

class Bot:
    def send_msg(text):
        try:
            finded = web.find_element_by_xpath('//*[@id="message"]')
            finded.send_keys(text)
            web.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/a[2]').click()
            web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except:
            print(headpr + "技能冷却中" + endpr)

    def get_msg():
        ret = web.page_source
        a = '<div class="message-text">(.*?)</div>'
        message = re.findall(a, ret, flags=re.S)[-1]
        return message

    def get_username():
        e = '<div class="message-name">(.*?)</div>'
        username = re.findall(e, ret)[-1].split(" | ")[0]
        return username
