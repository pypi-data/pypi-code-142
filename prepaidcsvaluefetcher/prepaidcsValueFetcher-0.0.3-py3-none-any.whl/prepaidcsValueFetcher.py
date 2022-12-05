import sys


def fetch_value(mobile_no: str, password: str):
    import requests
    from bs4 import BeautifulSoup
    session = requests.Session()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "prepaidcs.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    session.headers = headers
    session.get("https://prepaidcs.com/login")
    payload = {'msisdn': mobile_no, 'password': password}
    session.post("https://prepaidcs.com/login_add", data=payload)
    session.headers = session.headers.update({"Referer": "https://prepaidcs.com/cardinformation"})
    res = session.get("https://prepaidcs.com/usage")

    gbRemain = float(BeautifulSoup(res.text, "html.parser").select("tr")[-1].select("td")[1].text.strip().split(" ")[0])
    return gbRemain

if __name__ == "__main__":
    mobile_no = sys.argv[1]
    password = sys.argv[2]
    print(f"{fetch_value(mobile_no, password)} GB")