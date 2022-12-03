import requests
from bs4 import BeautifulSoup 
import os
from pathlib import Path
import json
from optparse import OptionParser
from colorama import *
# resets the colorama colors to default after every call
init(autoreset=True)

# when python3 coinmarketcap -h or --help it shows the project name and options
usage = "usage: %prog --download-logos"

# creates a instance of OptionParser to parser
parser = OptionParser(usage=usage)

def main():
    # when running the file if we use -d or --dowload-logos this parser will return True
    parser.add_option("-d", "--download-logos", dest="logo",
            action="store_true", # if -d is called it will store True
            default=False, # by default it's false which means we are not parsing -d to it
            help="download the top 10 coinmarketcap.com coin logos")

    # storing the values of options and any args
    (options , args) = parser.parse_args()

    # the url to target
    url = "https://coinmarketcap.com/"

    # gets the html of the target as text
    result = requests.get(url).text

    # creates an instance of BeautifulSoup using the result 
    doc = BeautifulSoup(result , "html.parser")

    # getting the tbody tag from text file
    tbody = doc.tbody

    # getting the contents of the tbody tag and storing it into trs
    trs = tbody.contents

    data = [{},{},{},{},{},{},{},{},{},{}]
    listname = []
    listsymbol = []
    listprice = []

    # make a dir named logos if doesn't exists
    os.makedirs("logos",exist_ok=True)

    # cd to the created dir
    os.chdir("logos")

    # a for loop on the first trs of the tbody content (first 10 coins)
    for tr in trs[:10]:
        
        # getting the name and price from tr content in td tags
        name , price = tr.contents[2:4]

        # getting the symbol from tr content in td tags
        symbol = name.find('p' , class_="sc-e225a64a-0 dfeAJi coin-item-symbol")
        
        # if -d is used options.logo will return True
        if options.logo == True:

            # getting the logo from tr content in td tags
            logo = tr.find("img", class_="coin-logo")

            # creating a dynamic cool filename
            filename = f"logo-{symbol.string}.jpg"

            # downloading the logo (logo['src'] is the direct url to the logo )
            reqlogo = requests.get(logo['src'])

            # just acting like a hacker and printing the logo symbol when downloaded in green
            print(f'{Fore.LIGHTGREEN_EX} downloaded {symbol.string} LOGO successfully')
            
            # opening the url and writing the content to the file
            with open(filename , 'wb') as f:
                f.write(reqlogo.content)
            f.close()

        listsymbol.append(symbol.string)
        listname.append(name.p.string)
        listprice.append(price.a.string)
        print(f"{Fore.LIGHTGREEN_EX} {name.p.string} coin data extracted successfully")
        
        # manupilating data to create a [{"name":"bitcoin", "symbol":"BTC", "price":"$000"}]
        for i in range(10):
            try:
                data[i]['name'] = listname[i]
                data[i]['symbol'] = listsymbol[i]
                data[i]['price'] = listprice[i]
            except:
                pass
        



    os.chdir('../')
    os.makedirs('data',exist_ok=True)
    os.chdir('data')

    # wrting the extracted data into a json file
    with open('data.json' , 'w') as f:
        json.dump(data , f ,ensure_ascii=False)



if __name__ == "coinmarketcap_scraper_hp.coinmarketcap":
    main()