from pathlib import Path
import time
import requests
import json


class DeathByCaptcha:
    URL = "http://api.dbcapi.me/api/captcha"

    def __init__(self,token):
        self.token = token


    def config_h_captcha(self,sitekey,pageurl,proxy="",proxytype=""):
        self.sitekey = sitekey
        self.pageurl = pageurl
        self.proxytype = proxytype
        self.proxy = proxy

    # def config_img_captcha(self,token):
    #     self.token = token

    def resolve_HCaptcha(self,timeout=30):
        hcaptcha_params = {
            "proxy": self.proxy,
            "proxytype": self.proxytype,
            "sitekey": self.sitekey,
            "pageurl": self.pageurl
        }

        payload = {
            'authtoken': self.token,
            'type': '7',
            'hcaptcha_params': json.dumps(hcaptcha_params)
        }

        response = requests.request("POST", self.URL, data=payload)
        if response.status_code != 200:
            raise Exception(response.text)
        
        data = {x.split('=')[0]:x.split('=')[1] for x in response.text.split("&")}
        if data["is_correct"] == "0":
            raise Exception("Data Sent is not correct!")

        return self.waitSolution(data["captcha"],timeout=timeout) 



    def resolve_ImageCaptcha(self,captchaImage,timeout=30):
        tempo = 0
        while tempo < 30:
            fName = Path(captchaImage).stem + Path(captchaImage).suffix
            payload = {
                'authtoken': self.token,
            }
            files=[
                ('captchafile',(fName,open(captchaImage,'rb'),'application/octet-stream'))
            ]

            response = requests.request("POST", self.URL, data=payload,files=files)
        
            if response.status_code == 200:
                break
            else:
                time.sleep(2)
                tempo=tempo+2
                
        
        if response.status_code != 200:
            raise Exception(response.text)

        data = {x.split('=')[0]:x.split('=')[1] for x in response.text.split("&")}
        if data["is_correct"] == "0":
            raise Exception("Data Sent is not correct!")
        
        return self.waitSolution(data["captcha"],timeout=timeout)
        
   
    def waitSolution(self,captcha,timeout=30):
        start = time.time()
        response = requests.request("GET", f"{self.URL}/{captcha}")
        data = {x.split('=')[0]:x.split('=')[1] for x in response.text.split("&")}
        if data["is_correct"] == "0":
            raise Exception("Data received is not correct!")
        if timeout <= 0:
            raise Exception("Timeout solving captcha")
        if data["text"] == "":
            count = time.time()- start
            return self.waitSolution(captcha,timeout-count)
        
        return data["text"]

#token = "24O1yDML8D42jvI4fz8N148k9mSFHMqMKHS2aQdQkG7lf1TBY2yretQ1RIR290H0pM9BK6AYlSbj9T93iuB48Dt9VW84BI5ibLaBu9S549ZsV1pWMFKv5Eu7Dte8x4Ohhgx3q4zBKto8rJLv4L6wChR2M66M"
#dth = DeathByCaptcha(token=token)
#dth.config_img_captcha(token=token)
#solved = dth.resolve_HCaptcha("af4fc5a3-1ac5-4e6d-819d-324d412a5e9d","https://solucoes.receita.fazenda.gov.br/",timeout=30)
#solved = dth.resolve_ImageCaptcha(r"C:\Users\user\Downloads\captcha_file.asp",timeout=30)
# print(solved)
#a = 1