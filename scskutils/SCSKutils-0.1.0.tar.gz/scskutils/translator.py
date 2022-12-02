from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator

def get_country_code(country):
    url_country_codes = "https://www.scrapingbee.com/documentation/country_codes/"
    response = requests.get(url_country_codes)
    soup = BeautifulSoup(response.content,'html.parser')
    country_codes_dict = {soup.find('table').find_all('td')[a].text:soup.find('table').find_all('td')[a+1].text for a in range(0,len(soup.find('table').find_all('td'))-2)}
    country_codes_dict_lower = {c.lower():country_codes_dict[c] for c in country_codes_dict if len(country_codes_dict[c])==2}
    return country_codes_dict_lower[country.lower()]

def translate(s,origin_lang,target_lang):
    s_translated = GoogleTranslator(source=origin_lang, target=target_lang).translate(s)
    return s_translated