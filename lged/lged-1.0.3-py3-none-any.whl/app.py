import os
import sys
import urllib.parse
import click

import requests
from bs4 import BeautifulSoup as bs
import re

from lged import config
from lged.settings import param_values
from lged.downloader import download_file

sys.path.append(os.getcwd() + '/..')

class App:
    def __init__(self, **kwargs):
        self.search_config_url = None
        self.search_url = None
        self.keyword = kwargs['keyword']
        self.view = kwargs['view']
        self.page_num = kwargs['page_num']
        self.search_field = kwargs['search_field']
        self.sort = kwargs['sort']
        self.sortmode = kwargs['sortmode']
        self.download_path = kwargs['download'] if kwargs['download'] != "" else config.download_path
            
    def run(self):
        click.echo(click.style(f"LGED is running...", fg="green"))

        self.configSearchURL()

        self.loadEBooks()
    
    def configSearchURL(self):
        params = {}
        params['req'] = self.keyword
        params['phrase'] = 1
        params['res'] = 25

        if self.view in param_values['view']:
            params['view'] = self.view
        else:
            click.echo(click.style(f"The view param is wrong value.", fg="red"))

        if self.search_field in param_values['search_field']:
            params['column'] = self.search_field
        else:
            click.echo(click.style(f"The search_field param is wrong value.", fg="red"))

        if self.sort in param_values['sort']:
            params['sort'] = self.sort
        else:
            click.echo(click.style(f"The sort param is wrong value.", fg="red"))

        if self.sortmode in param_values['sortmode']:
            params['sortmode'] = self.sortmode
        else:
            click.echo(click.style(f"The sortmode param is wrong value.", fg="red"))        
        
        self.search_config_url = f"{config.site_url}?{urllib.parse.urlencode(params)}"
        
    def loadEBooks(self):
        book_count = 1
        download_book_number = 25 * self.page_num
        for page in range(1, self.page_num + 1):
            params = {}
            params['page'] = page
            self.search_url = f"{self.search_config_url}&{urllib.parse.urlencode(params)}"
            print(f"{self.search_url}\n")

            try:
                page_data = requests.get( self.search_url )
                soup = bs(page_data.content, "html.parser")

                ebook_num_element = soup.find("font", string=re.compile("files found"))
                total_number = 0
                if ebook_num_element != None:
                    temp = ebook_num_element.text.split("|")[0]
                    temp = re.findall(r'\d+', temp)
                    numbers = list(map(int, temp))
                    total_number = numbers[0] if len(numbers) > 0 else 0

                total_number = total_number if total_number < download_book_number else download_book_number
                
                ebook_list = soup.find_all("tr", valign="top")
                for index, item in enumerate(ebook_list):
                    if index == 0:
                        continue

                    click.echo(click.style(f"Book: {book_count}/{total_number} - {page} page", fg="green"))
                    temp = item.find(href=re.compile("book"))
                    if temp is not None:
                        ebook_link = temp.get('href')
                        if ebook_link != "":
                            self.loadEbook(ebook_link)
                    
                    book_count = book_count + 1

            except Exception as e:
                click.echo(click.style(f"Error fetching the page!\n{e}", fg="red"))
    
    def loadEbook(self, ebook):
        ebook_link = f"{config.site_url}/{ebook}"
        click.echo(click.style(f"Loading ebook page - {ebook_link}", fg="green"))

        try:
            ebook_page = requests.get(ebook_link)
            soup = bs(ebook_page.content, "html.parser")
            tr_list = soup.find_all("tr", valign="top")
            if len(tr_list) > 0:
                item = tr_list[1]
                a_tag = item.find("a")
                ebook_detail_link = a_tag.get('href')
                if ebook_detail_link != "":
                    self.downloadEbook(ebook_detail_link)
        except Exception as e:
            click.echo(click.style(f"Error loading ebook page!\n{e}", fg="red"))

    def downloadEbook(self, ebook):
        click.echo(click.style(f"Loading ebook detail page - {ebook}", fg="green"))

        try:
            ebook_detail_page = requests.get(ebook)
            soup = bs(ebook_detail_page.content, "html.parser")
            a_tag = soup.find("a", string="GET")
            if a_tag is not None:
                file_link = a_tag.get('href')
                download_file(file_link, self.download_path)
        except Exception as e:
            click.echo(click.style(f"Error loading ebook detail page!\n{e}", fg="red"))