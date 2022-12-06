import re
import traceback

from selenium import webdriver # webdriver 操作一般用
from selenium.webdriver.chrome import service as fs # Chrome を driver として設定する用
from selenium.webdriver.chrome.options import Options # headless モードで作業する用
from bs4 import BeautifulSoup


class Regular():
    """This class gets URLs and retrieve the body text from them 
    with NEWS WEB (regular news site, not the Easy Japanese one) solely.

    Most of methods you'll call on Easy objects are using Selenium 
    or Beautiful Soup.

    This class has 2 roles. 
    1. Access the NEWS WEB and get the list of URLS of the most recent day.
    2. Retrieve the body text of these URLs.

    These methods serves for the 1st role.
      * start(url, url_or_article)
      * shutdown()
      * get_url(soup)

    These methods serves for the 2nd role.
      * start(url, url_or_article)
      * shutdown()
      * get_article(soup)

    Parameters
    ----------
    DRIVER_PATH : str
        The filepath of your Chrome driver. To prevent the tedious work of inputting,
        get this path from the attribute of Easy() class.

    Attributes
    ----------
    DRIVER_PATH : str
        The filepath of your Chrome driver.
    service : selenium.webdriver.chrome.service.Service
        The setting for starting up a browser.
    options : selenium.webdriver.chrome.options.Options
        The setting for starting up a browser.

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
    """
    def __init__(self, DRIVER_PATH):
        """Constructor.
        Define the attributes for start().
        """
        self.DRIVER_PATH = DRIVER_PATH
        self.service = fs.Service(executable_path=self.DRIVER_PATH)
        self.options = Options()
        self.options.add_argument('--window-size=1920,1200')
        self.options.add_argument('--headless')


    def start(self, url, url_or_article=True):
        self.driver = webdriver.Chrome(options=self.options, service=self.service)
        """Open a browser, parse the JavaScript data and save it as HTML data.
        
        Parameters
        ----------
        url : str
            The web page you want to open.
        url_or_article : bool
            Whether you want to start retrieving URL or not.
        """
        self.driver.get(url)
        print('Done starting up a new browser!')
        html = self.driver.page_source.encode('utf-8')
        print('Done parsing the JavaScript data!')
        soup = BeautifulSoup(html, 'html.parser')
        print('Done reading the data as HTML!')
        if url_or_article:
            self.html_url = html 
            self.soup_url = soup
        else:
            self.html_article = html
            self.soup_article = soup

        print('All done start_url(). Hello!')


    def shutdown(self):
        """Shut down the driver.
        """
        self.driver.quit()
        print('All done shutdown(). Goodbye!')


    def get_url(self, soup):
        """Extract the URL from the parsed HTML data.

        Parameters
        ----------
        soup : bs4.BeautifulSoup
            The parsed HTML data.
        
        """
        try:
            reg_url = soup.select_one('#js-regular-news').get('href')
            print('Done retrieving the URL!')
        except:
            print('An unexpected error has occurred during obtaining the URL.')
            traceback.print_exc()
            reg_url = 'Unexpected'
        return reg_url
    
    # soup := each element of self.soup_article
    def get_article(self, soup):
        """Retrieve the body text of the news.

        Parameters
        ----------
        soup : bs4.BeautifulSoup
            The parsed HTML data.
        """
        try:
            for nav in soup(['nav']):
                nav.decompose()
            for title in soup(['h2']):
                title.decompose()
            for fig in soup(['figcaption']):
                fig.decompose()
            for editor in soup.findAll(class_='content--editor-body'):
                editor.decompose()
            print('Done removing the noise!')

        except:
            print('An expected error has occurred during editing the html data.')
            traceback.print_exc()
            soup = None

        try:
            # this shoud be it if there happened an error in the extraction process.
            article = soup.find(class_='content--detail-body').text
            article = re.sub('\n', '', article)
            article = re.sub(' ', '', article)
            reg_article = article

        except:
            print('An expected error has occurred during extracting the text.')
            traceback.print_exc()
            reg_article = 'Unexpected'
        return reg_article