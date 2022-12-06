from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def Ai_Search(name):
    path = r'D:\software\selenium_folder\msedgedriver.exe'

    browser = webdriver.Edge(path)

    browser.get("https://www.baidu.com")

    ele = browser.find_element(By.ID, 'kw')  # 搜索框
    ele.send_keys(name + Keys.RETURN)

    time.sleep(20)

