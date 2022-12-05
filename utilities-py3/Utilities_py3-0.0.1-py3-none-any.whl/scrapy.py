from urllib.request import Request, urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import response
import imagehash as im
from PIL import Image
import os, requests
def find_file(target,local = "C:\\", isDir = False, both = False):
    pathName = lambda root,x: os.path.join(root,x)
    for root, dirs, files in os.walk(local):
        if(isDir):
            if(target in dirs):
                return pathName(root,target)
        
        elif(both):
            if(target in dirs or target in files):
                return pathName(root,target)

        elif(target in files):
            return pathName(root,target)

header = {
    "User-Agent":"Mozilla/5.0"
}
def download_img(nome: str, url: str, path: str) -> str:
    with open(f"{path}/{nome}","wb") as f:
        im = requests.get(url)
        f.write(im.content)
    return path + nome

def setup_driver(options: list[str] = ["--start-maximized","--detach"]) -> webdriver:
    driver_opt = webdriver.ChromeOptions()
    [driver_opt.add_argument(i) for i in options]
    driver = webdriver.Chrome(options=driver_opt,executable_path=find_file("chromedriver.exe","C:\\"))
    return driver

list_in_element = lambda element,lst: any([i in element.text if(type(element) != str) else i in element for i in lst])
collect_html = lambda url,headers = header: BeautifulSoup(urlopen(Request(url=url,headers=headers)),"html.parser")
collect_hrefs = lambda bs: [i.attrs["href"] for i in bs.find_all("a")]
collect_imgs = lambda bs: {i.attrs["alt"]:i.attrs["src"] for i in bs.find_all("img") if "alt" in i.attrs and "src" in i.attrs}
html_to_str = lambda bs: rf'{str(bs).encode("utf-8")}'[2:-1]
str_to_html = lambda text: BeautifulSoup(text,"html.parser")

def image_hash(nome,url,path = 'files/imgs/',download = False) -> list:
    if(download):
        download_img(nome,url,path)
    image = Image.open(path + nome)
    hash = im.phash(image,20)
    return hash