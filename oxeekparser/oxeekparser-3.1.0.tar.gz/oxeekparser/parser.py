import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Parser:
    _sleep = 0
    _html_body = ''
    _get_code = True
    _search_result = []
    _response_code = None
    _chrome_service = None
    _chrome_options = None
    _chrome_capabilities = None

    def __init__(self, chrome_path, profile_path, get_response_code=True, sleep=10):
        self._set_response_possibility(get_response_code)
        self._set_sleep(sleep)
        self._set_chrome(chrome_path, profile_path)

    def _set_response_possibility(self, get_response_code):
        self._get_code = get_response_code

    def _set_sleep(self, sleep):
        self._sleep = sleep

    def _set_chrome(self, chrome_path, profile_path):
        self._chrome_service = Service(chrome_path)
        self._chrome_options = webdriver.ChromeOptions()
        self._set_chrome_options(profile_path)

        if self._get_response_code:
            self._chrome_capabilities = DesiredCapabilities.CHROME.copy()
            self._set_chrome_capabilities()

    def _set_chrome_options(self, profile_path):
        self._chrome_options.add_argument('--allow-profiles-outside-user-dir')
        self._chrome_options.add_argument('--enable-profile-shortcut-manager')
        self._chrome_options.add_argument(f'user-data-dir={profile_path}')
        self._chrome_options.add_argument('--profile-directory=Default')

    def _set_chrome_capabilities(self):
        self._chrome_capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

    def _parse(self, url):
        with webdriver.Chrome(service=self._chrome_service,
                              desired_capabilities=self._chrome_capabilities,
                              options=self._chrome_options) as driver:
            driver.get(url)

            if self._get_code:
                self._get_response_code(driver.get_log('performance'))

            time.sleep(self._sleep)
            body = driver.page_source
            driver.quit()
            self._html_body = ''.join(body)

        return self

    def _get_response_code(self, logs):
        for log in logs:
            if not log['message']:
                pass
            
            response_logs = json.loads(log['message'])
            try:
                content_type = 'text/html' in response_logs['message']['params']['response']['headers'][
                    'content-type']
                response_received = response_logs['message']['method'] == 'Network.responseReceived'
                if content_type and response_received:
                    self._response_code = int(response_logs['message']['params']['response']['status'])
            except:
                pass
                

    def handle(self, url):
        self._parse(url)
        return self

    def save_html(self, path):
        with open(path, 'w+', encoding='utf-8') as file:
            file.write(self._html_body)
        return self

    def get_html(self):
        return self._html_body
    
    def get_response(self):
        return self._response_code
