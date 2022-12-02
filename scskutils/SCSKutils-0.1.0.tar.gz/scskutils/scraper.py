import requests
from bs4 import BeautifulSoup

def get_soup(url):

    ### need to set headers for this url, as it otherwise gives an infinite redirect loop
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',}


    page = requests.get(
                url = url,
                headers=headers,
                verify=False,
                )
    soup = BeautifulSoup(page.content, 'html.parser')
    
    print(url)
    
    return soup