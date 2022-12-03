import re
import traceback

from selenium import webdriver # webdriver 操作一般用
from selenium.webdriver.chrome import service as fs # Chrome を driver として設定する用
from selenium.webdriver.chrome.options import Options # headless モードで作業する用
from selenium.webdriver.common.by import By # find_element() で参照したい位置を特定する用
from bs4 import BeautifulSoup

class Easy():
    """This class gets URLs and retrieve the body text from them 
    with NEWS WEB EASY solely.

    Most of methods you'll call on Easy objects are using Selenium 
    or Beautiful Soup.
    
    This class has 2 roles. 
    1. Access the NEWS WEB EASY and get the list of URLS of the most recent day.
    2. Retrieve the body text of these URLs.
    
    These methods serves for the 1st role.
      * start_url()
      * shutdown()
      * get_raw_url_date()
      * get_url(url)

    These methods serves for the 2nd role.
      * start_extract(url)
      * shutdown()
      * get_article(soup)

    if you wish to retrieve the information from the past article, 
    then you can do so by modifying the `start_url()` method, specifically,
    the XPATH of element.

    Attributes
    ----------
    DRIVER_PATH : str
        The filepath of your Chrome driver.
    service : selenium.webdriver.chrome.service.Service
        The setting for starting up a browser.
    options : selenium.webdriver.chrome.options.Options
        The setting for starting up a browser.
    BASE_URL : str
        The web page you start off with when you extract the URL info.
    driver : selenium.webdriver.chrome.webdriver.WebDriver
        The web driver you use for the all process.
    html_url : bytes
        The web page data encoded to HTML for the URL retrieval.
    soup_url : bs4.BeautifulSoup
        The parsed web page data for the URL retrieval.
    html_article : bytes
        The web page data encoded to HTML for the article retrieval.
    soup_article : bs4.BeautifulSoup
        The parsed web page data for the article retrieval.
    easy_urls_raw : bs4.element.ResultSet
        The elements you find and clip from the HTML data.
    date : str
        The date of the retrieved data.
    """
    def __init__(self):
        """Constructor.
        Define the attributes for start_url(), start_extract(), and get_url().
        """
        DRIVER_PATH = input('The filepath, where your Chrome Driver is?')
        self.DRIVER_PATH = DRIVER_PATH
        self.service = fs.Service(executable_path=self.DRIVER_PATH)
        self.options = Options()
        self.options.add_argument('--window-size=1920,1200')
        self.options.add_argument('--headless')
        self.BASE_URL = 'https://www3.nhk.or.jp/news/easy'

        
    def start_url(self):
        """Open the NEWS WEB EASY, display the list of URLS and parse 
        and pass it to Beautiful Soup as HTML.
        
        *** I save html_url and html_article as attribute solely for the debug purpose.
        """    
        self.driver = webdriver.Chrome(options=self.options, service=self.service)
        self.driver.get(self.BASE_URL)
        print('Done starting up a new browser!')

        self.driver.execute_script('window.scrollBy(0, 1200);')
        element = self.driver.find_element(
                By.XPATH, '//*[@id="easy-wrapper"]/div[2]/aside/section[2]/div[1]/a[1]'
                )
        element.click()
        print('Done displyaing the list of the URLs!')

        self.html_url = self.driver.page_source.encode('utf-8')
        print('Done parsing the JavaScript data!')
        self.soup_url = BeautifulSoup(self.html_url, 'html.parser')
        print('Done reading the data as HTML!')

        print('All done start_url(). Hello!')


    def start_extract(self, url):
        """Open the article and parse it to HTML.
        
        Parameters
        ----------
        url : str
            The URL you want to open.
        """
        self.driver = webdriver.Chrome(options=self.options, service=self.service)
        self.driver.get(url)
        print('Done starting up a new browswer!')

        self.html_article = self.driver.page_source.encode('utf-8')
        print('Done parsing the JavaScript data!')
        self.soup_article = BeautifulSoup(self.html_article, 'html.parser')
        print('Done reading the data as HTML!')

        print('All done start_extract(). Hello!')
        return self.soup_article


    def shutdown(self):
        """Shut down the webdriver."""
        self.driver.quit()
        print('All done shutdown(). Goodbye!')

    def get_raw_url_date(self):
        """Extract the URLs from the parsed HTML data.
        
        *** I separate this method from get_url() just because I don't
        want to include this in for-loop done in EasyJapanese() (in
        __init__.py).
        """
        self.easy_urls_raw = self.soup_url.select('#js-archives-list > a')
        self.date = self.soup_url.select_one('#js-pager-date').text
        print('Done getting the raw text of URLs!')


    def get_url(self, url):
        """Retrieve the URL from the get_raw_url_date() data.
        
        Parameters
        ----------
        url : str
            The parsed and clipped HTML data (bs4.element.Tag). You're supposed
            to create bs4.element.Tag input out of bs4.element.ResultSet.
        """
        try:
            raw_url = url.get('href')
            print('Done extracting the raw URL!')
            easy_url = re.sub(r'^./', self.BASE_URL+'/', raw_url)
            print('Done retrieving the URL!')
        except:
            print('An unexpected error has occurred during obtaining the URL.')
            traceback.print_exc()
            easy_url = 'Unexpected'
        return easy_url


    def get_article(self, soup):
        """Retrieve the body text from the parsed HTML data.
        
        Parameters
        ----------
        soup : bs4.BeautifulSoup
            The parsed HTML data.
        """
        try:
            for ruby in soup(['rt']):
                ruby.decompose()
            print('Done removing the noise!')
            article_raw = soup.select_one('#js-article-body').text
            article_raw = re.sub('\n', '', article_raw)
            easy_article = re.sub(' ', '', article_raw) 

        except:
            print('An unexpected error has occurred during obtaining the article.')
            print(f'soup: {soup}\n')
            traceback.print_exc()
            easy_article = 'Unexpected'
        return easy_article
    
