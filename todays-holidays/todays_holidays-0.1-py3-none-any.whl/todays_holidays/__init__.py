from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def today(length = -1):
    if type(length) != int:
        raise ValueError("Length value must be integer")
    res = requests.get('https://nationaltoday.com/what-is-today/')
    soup = BeautifulSoup(res.text, 'html.parser')
    result = []
    answer = soup.select(".holiday-title")
    for holi in answer:
        result.append(holi.get_text())
    try: 
        del result[length:]
        return result
    except:
        return result
def tomorrow(length = -1):
    if type(length) != int:
        raise ValueError("Length value must be integer")
    res = requests.get('https://nationaltoday.com/what-is-tomorrow/')
    soup = BeautifulSoup(res.text, 'html.parser')
    result = []
    answer = soup.select(".holiday-title")
    for holi in answer:
        result.append(holi.get_text())
    try: 
        del result[length:]
        return result
    except:
        return result
def day(month, day, holiday = True, length = -1):
    MONTHS = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if type(month) == int:
        if month < 0 or month > 12:
            raise ValueError("Month is not in range")
    elif type(month) != str:
        raise ValueError("Month value must be string or integer")
    if type(month) == str:
        if month not in MONTHS:
            raise ValueError("Month value must be valid month")
    if type(day) == int:
        day = str(day)
    if type(day) != str:
        raise ValueError("Day value must be string or integer")
    if type(holiday) != bool:
        raise ValueError("Holiday value must be boolean")
    if type(length) != int:
        raise ValueError("Length value must be integer")
    if type(month) == int:
        month = MONTHS[month-1]
    day_type = "birthdays"
    if holiday:
        day_type = "holidays"
    try:
        res = requests.get('https://nationaltoday.com/'+month+'-'+day+'-'+day_type+'/')
    except:
        raise ValueError("One of the passed in values is incorrect")
    soup = BeautifulSoup(res.text, 'html.parser')
    result = []
    answer = soup.select(".holiday-title")
    for holi in answer:
        result.append(holi.get_text())
    try:
        if length != -1:
            del result[length:]
            return result
    except:
        pass
    return result