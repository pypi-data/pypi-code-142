from __future__ import annotations

import collections
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
import selenium.webdriver.support.expected_conditions as EC
import os
import logging
import functools
from contextlib import suppress
from typing import List, Literal
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.utils import get_browser_version_from_os, ChromeType, os_name, OSType
from webdriver_manager.core.constants import DEFAULT_USER_HOME_CACHE_PATH
import shutil
import requests
import xml.etree.ElementTree as elemTree

logger = logging.getLogger(__name__)

CHROME = webdriver.Chrome


def get_web_chrome_link(version):
    """get selenium chromedriver version by major version got from local chrome"""
    logger.info("Try to get target chrome driver in web")

    res = requests.get("https://chromedriver.storage.googleapis.com")
    root = elemTree.fromstring(res.content)
    for k in root.iter('{http://doc.s3.amazonaws.com/2006-03-01}Key'):
        if k.text.find(version + '.') == 0:
            ver = k.text.split('/')[0]
            logger.info(f"found web_version: {ver}")
            return ver
    logger.warning(f"not found matched version of chrome: {version}, use latest")
    return "latest"


def _get_driver_path():
    version = get_browser_version_from_os(ChromeType.GOOGLE).split(".")[0]

    _os_name = os_name()

    if _os_name == OSType.WIN:
        file_name = f"chromedriver_{version}.exe"
    else:
        file_name = f"chromedriver_{version}"

    expect_path = os.path.join(DEFAULT_USER_HOME_CACHE_PATH, file_name)
    if not os.path.exists(expect_path):
        wdm_path = ChromeDriverManager(version=get_web_chrome_link(version), cache_valid_range=1000).install()
        shutil.copy(wdm_path, expect_path)
    return expect_path


def ignore_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with suppress(Exception):
            return func(*args, **kwargs)

    return wrapper


class WaitList:
    ELE_SELECTOR = {'presence': EC.presence_of_element_located,
                    'visible': EC.visibility_of_element_located,
                    'invisible': EC.invisibility_of_element_located,
                    'clickable': EC.element_to_be_clickable}

    URL_SELECTOR = {
        'url_to_be': EC.url_to_be,
        'url_contains': EC.url_contains,
        'url_matches': EC.url_matches,
        'url_changes': EC.url_changes,
    }

    @classmethod
    def validate_value(cls, value):
        if isinstance(value, str):
            return [value]
        elif isinstance(value, list):
            return value
        else:
            raise TypeError(f"Invalid type for wait_list: {type(value)}, expected str or list")

    @classmethod
    def generate_wait_list(cls, user_wait_list, **kwargs) -> list:
        """
        generate wait-list from user_wait_list and kwargs
        :param user_wait_list: pre-defined ExpectedCondition
        :param kwargs: key-value pair for generate selenium expected condition
        :return: list of ExpectedCondition
        """
        wait_list = user_wait_list or []

        for key, value in kwargs.items():
            value = cls.validate_value(value)
            if key in cls.ELE_SELECTOR:
                for v in value:
                    wait_list.append(cls.ELE_SELECTOR[key]((By.XPATH, v)))
            elif key in cls.URL_SELECTOR:
                for v in value:
                    wait_list.append(cls.URL_SELECTOR[key](v))
            else:
                raise ValueError(f"Invalid key for wait_list: {key}, "
                                 f"expected: {list(cls.ELE_SELECTOR.keys()) + list(cls.URL_SELECTOR.keys())}")
        return wait_list


class Element:
    """
    Custom function for selenium chrome element
    """

    def __init__(self, element):
        self.ele = element

    def __getattr__(self, attr: str):
        return getattr(self.ele, attr)

    def get_text(self):
        """get element text"""
        return self.ele.text

    def clear_and_type(self, content: str):
        """clear input and type content"""
        self.clear()
        sleep(0.5)
        self.send_keys(content)

    def select_value(self, value):
        """select element by value"""
        Select(self.ele).select_by_value(value)

    def select_visible_text(self, text):
        """select element by text"""
        Select(self.ele).select_by_visible_text(text)

    def select_index(self, index):
        """select element by index"""
        Select(self.ele).select_by_index(index)

    def get_element(self, xpath) -> Element:
        """get element by Xpath from root element"""
        return Element(self.ele.find_element(by=By.XPATH, value=xpath))

    def get_elements(self, xpath) -> List[Element]:
        """get list of elements by Xpath from root element"""
        return [Element(item) for item in self.ele.find_elements(by=By.XPATH, value=xpath)]

    def find_element_by_xpath(self, xpath) -> Element:
        """get element by Xpath from root element"""
        return self.get_element(xpath)

    def find_elements_by_xpath(self, xpath) -> List[Element]:
        """get list of elements by Xpath from root element"""
        return self.get_elements(xpath)

    def wait_and_click(self, bef: float = 0.5, aft: float = 0):
        """
        wait sometime before and after click
        """
        sleep(bef)
        self.ele.click()
        sleep(aft)

    def wait(self, wait_time: float = 0.5):
        """
            builder pattern for wait
        """
        sleep(wait_time)
        return self.ele

    def __call__(self):
        return self.ele


class Driver:
    _default_wait_time = 30

    def __init__(self, driver_: webdriver.Chrome = None):
        self.driver_: webdriver.Chrome = driver_

    def __getattr__(self, attr):
        return getattr(self.driver_, attr)

    def __del__(self):
        if self.driver_ is not None:
            with suppress(Exception):
                self.driver_.quit()

    @functools.cached_property
    def driver_path(self):
        return _get_driver_path()

    def set_chrome(self, keep_open: str = "Close", download_dir: str = None, load_cookies: bool = False, proxy=""):
        """
        :param keep_open: str: chosen from 'Close', 'Keep_Open', 'headless'
        :param download_dir: download directory
        :param load_cookies: load from user directory or open incognito mode
        :param proxy: proxy_server:port
        :return:
        """
        chrome_options = webdriver.ChromeOptions()

        if download_dir is not None:
            prefs = {"download.default_directory": os.path.abspath(download_dir)}
            chrome_options.add_experimental_option("prefs", prefs)

        if "Keep_Open" in keep_open:
            chrome_options.add_experimental_option("detach", True)
        else:
            chrome_options.add_experimental_option("detach", False)
            if "headless" in keep_open:
                chrome_options.headless = True

        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')

        if ":" in str(proxy):
            chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))

        chrome_options.add_experimental_option("excludeSwitches",
                                               ["ignore-certificate-errors",
                                                "safebrowsing-disable-download-protection",
                                                "safebrowsing-disable-auto-update",
                                                "disable-client-side-phishing-detection",
                                                'enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        if load_cookies:
            dirs = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data"
            chrome_options.add_argument("--user-data-dir=" + dirs)

        else:
            chrome_options.add_argument("--incognito")

        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-logging')

        try:
            self.driver_ = webdriver.Chrome(service=Service(self.driver_path), options=chrome_options)
        except Exception as e:
            print(e)
            print("INSTALL FROM CHROMEDRIVER MANAGER")
            self.driver_ = webdriver.Chrome(service=Service(ChromeDriverManager(cache_valid_range=100).install()),
                                            options=chrome_options)

    def wait(self, wait_time=_default_wait_time):
        return WebDriverWait(self.driver_, wait_time)

    def wait_presence(self, xpath: str, wait_time: int = _default_wait_time, message: str | None = None) -> Element:
        """wait element to presence
        :param xpath: xpath of element
        :param wait_time: wait time
        :param message: message for exception
        :return: element as custom Element
        """

        return Element(self.wait(wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)),
                                                  message=message or f"wait_presence, xpath: {xpath}"))

    def wait_visible(self, xpath: str, wait_time: int = _default_wait_time, message: str | None = None) -> Element:
        """wait element to be visible
        :param xpath: xpath of element
        :param wait_time: wait time
        :param message: message for exception
        :return: element as custom Element
        """
        return Element(self.wait(wait_time).until(EC.visibility_of_element_located((By.XPATH, xpath)),
                                                  message=message or f"wait_visible, xpath: {xpath}"))

    def wait_invisible(self, xpath: str, wait_time: int = _default_wait_time, message: str | None = None) -> Element:
        """wait element to be invisible
        :param xpath: xpath of element
        :param wait_time: wait time
        :param message: message for exception
        :return: element as custom Element
        """

        return Element(self.wait(wait_time).until(EC.invisibility_of_element_located((By.XPATH, xpath)),
                                                  message=message or f"wait_invisible, xpath: {xpath}"))

    def wait_clickable(self, xpath: str, wait_time: int = _default_wait_time, message: str | None = None) -> Element:
        """wait element to be clickable
        :param xpath: xpath of element
        :param wait_time: wait time
        :param message: message for exception
        :return: element as custom Element
        """
        return Element(self.wait(wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath)),
                                                  message=message or f"wait_clickable, xpath: {xpath}"))

    def wait_any_of(self,
                    user_wait_list: list | None = None,
                    timeout_message: str = "",
                    wait_time: int = _default_wait_time,
                    wait_info: dict[str, str | list] = None):
        """
        wait all of the conditions to be true
        :param user_wait_list: predefined ExpectedCondition list
        :param timeout_message: message to show when timeout
        :param wait_time: wait time
        :param wait_info: key, pair values to generate ExpectedCondition,
            - url_to_be, url_contains, url_matches, url_changes,
            - presence, visible, invisible, clickable
        :return: True if ok, else raise TimeOutError with timeout_message
        """
        wait_info = wait_info or {}
        wait_list = WaitList.generate_wait_list(user_wait_list, **wait_info)
        self.wait(wait_time).until(EC.any_of(*wait_list), message=timeout_message)

    def wait_all_of(self,
                    user_wait_list: list | None = None,
                    timeout_message: str = "",
                    wait_time: int = _default_wait_time,
                    wait_info: dict[str, str | list] = None):
        """
        wait all of the conditions to be true
        :param user_wait_list: predefined ExpectedCondition list
        :param timeout_message: message to show when timeout
        :param wait_time: wait time
        :param wait_info: dict of key, pair values to generate ExpectedCondition, key in
            - url_to_be, url_contains, url_matches, url_changes,
            - presence, visible, invisible, clickable
        :return: True if ok, else raise TimeOutError with timeout_message
        """
        wait_info = wait_info or {}
        wait_list = WaitList.generate_wait_list(user_wait_list, **wait_info)
        return self.wait(wait_time).until(EC.all_of(*wait_list), message=timeout_message)

    def wait_none_of(self,
                     user_wait_list: list | None = None,
                     timeout_message: str = "",
                     wait_time: int = _default_wait_time,
                     wait_info: dict[str, str | list] = None):
        """
        wait none of the conditions to be true
        :param user_wait_list: predefined ExpectedCondition list
        :param timeout_message: message to show when timeout
        :param wait_time: wait time
        :param wait_info: key, pair values to generate ExpectedCondition,
            - url_to_be, url_contains, url_matches, url_changes,
            - presence, visible, invisible, clickable
        :return: True if ok, else raise TimeOutError with timeout_message
        """
        wait_info = wait_info or {}
        wait_list = WaitList.generate_wait_list(user_wait_list, **wait_info)
        return self.wait(wait_time).until(EC.none_of(*wait_list), message=timeout_message)

    def get_element(self, xpath) -> Element:
        """get element by Xpath"""
        return Element(self.driver_.find_element(by=By.XPATH, value=xpath))

    def get_elements(self, xpath) -> List[Element]:
        """get list of elements by Xpath"""
        return [Element(item) for item in self.driver_.find_elements(by=By.XPATH, value=xpath)]

    def find_element_by_xpath(self, xpath) -> Element:
        """get element by Xpath"""
        return self.get_element(xpath)

    def find_elements_by_xpath(self, xpath) -> List[Element]:
        """get list of elements by Xpath"""
        return self.get_elements(xpath)

    def set_session_storage(self, key, value):
        """
        :param key: session storage key
        :param value: session storage value
        """
        self.driver_.execute_script("return window.sessionStorage.setItem(arguments[0], arguments[1]);", key, value)

    def set_local_storage(self, key, value):
        """
        :param key: local storage key
        :param value: local storage value
        """
        self.driver_.execute_script("return window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def remove_local_storage(self, key):
        """
        :param key: local storage key to remove
        """
        self.set_local_storage(key, "")
        self.driver_.execute_script("return window.localStorage.removeItem(arguments[0]);", key)

    def get_session_storage(self, key):
        """
        :param key: session storage key to get
        """
        return self.driver_.execute_script("return window.sessionStorage.getItem(arguments[0]);", key)

    def get_local_storage(self, key):
        """
        :param key: local storage key to get
        """
        return self.driver_.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def get_local_storage_keys(self):
        """
        :return: get all current driver local storage keys
        """
        return self.driver_.execute_script("return Object.keys(window.localStorage);")

    def get_cookies_string(self):
        """
        :return: current driver cookies in key=value; key=value format
        """
        cookies = self.driver_.get_cookies()
        cookies_string = '; '.join(['{}={}'.format(cookie['name'], cookie['value']) for cookie in cookies])
        return cookies_string

    def get_user_agent(self):
        """
        :return: get current driver user agent
        """
        return self.driver_.execute_script("return navigator.userAgent;")

    def expand_shadow_element(self, element):
        """
        :param element: element which has shadow root
        :return: tree under shadow root
        """
        return self.driver_.execute_script('return arguments[0].shadowRoot', element)

    @property
    def user_agent(self):
        """
        :return: user_agent as property
        """
        return self.driver_.execute_script("return navigator.userAgent;")

    def wait_redirected(self, limit_redirect=4, limit_time=20):
        """
        sometime page is continuously redirected, this function will wait for some completed redirection
        """
        for tr in range(limit_redirect):
            counter = 0
            while True:
                counter += 0.5
                sleep(0.5)
                if self.driver_.execute_script("return document.readyState") == "complete" or counter > limit_time:
                    break

    @ignore_error
    def remove_element(self, element: Element | WebElement):
        """
        remove element from DOM, surround with try catch, so it will not raise error if element is not found
        """
        ele = element if isinstance(element, WebElement) else element.ele
        self.driver.execute_script("var element = arguments[0];element.parentNode.removeChild(element);", ele)

    @ignore_error
    def remove_element_by_xpath(self, xpath, delay_before: float = 0.5, delay_after: float = 0.5):
        """
        remove element from DOM by xpath
        """
        sleep(delay_before)
        ele = self.get_element(xpath)
        self.remove_element(ele)
        sleep(delay_after)
