import requests
import cloudscraper

def get_mail():
      flat = True
      while flat:
            try:
                  headers1 = {
                        'accept': 'text/plain',
                        'access_key': '123',
                        'Content-Type': 'application/json',
                  }
                  scraper = cloudscraper.create_scraper()
                  response = scraper.post('https://web2.temp-mail.org/mailbox', headers=headers1, timeout=60)
                  data = response.json()
                  token = data['token']
                  email = data['mailbox']

                  if 'token' in data:
                        flat = False
                        return {"token" : f"{token}","email" : f"{email}"}


            except:
                  pass
