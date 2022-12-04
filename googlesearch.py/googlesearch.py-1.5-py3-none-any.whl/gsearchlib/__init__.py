import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def Search(query : str):
    results: list = []

    page_source: str = str(urllib.request.urlopen(urllib.request.Request(f"https://www.google.com/search?q={urllib.parse.quote(query)}&num=20&hl=en", headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"})).read())

    try:
        if parser := BeautifulSoup(page_source, "html.parser").findAll("div", attrs={"class" : "yuRUbf"}):
            for i in parser:
                results.append(dict(url = i.find("a").get("href"), title = i.find("h3", attrs={"class" :"LC20lb MBeuO DKV0Md"}).text))
    except AttributeError:
        return None

    if results:
        return results

    return None