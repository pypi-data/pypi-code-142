# Builtins
import json
import os
import time
import urllib.parse
from io import BytesIO
import re
import base64
from typing import Tuple

import tls_client

from bs4 import BeautifulSoup

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def invalidToken() -> bool:
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "ACCESS_TOKEN.json")
        with open(path, "r") as f:
            creds = json.load(f)
            expires_at = float(creds["expires_at"])
            if time.time() > expires_at + 3600:
                return True
            else:
                return False
    except FileNotFoundError:
        return True


def accessToken() -> Tuple[str or None, str or None]:
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, "ACCESS_TOKEN.json")
        with open(path, "r") as f:
            creds = json.load(f)
            return creds["access_token"], creds["expires_at"]
    except FileNotFoundError:
        return None, None


class Auth:
    def __init__(self, email_address: str, password: str):
        self.email_address = email_address
        self.password = password
        self.__session = tls_client.Session(client_identifier="chrome_105")

    @staticmethod
    def encodeURL(string: str) -> str:
        return urllib.parse.quote(string)

    def generateToken(self):
        if not self.email_address or not self.password:
            raise Exception("Please provide an email address and password") and print(
                "Please provide an email address and password"
            )
        url = "https://chat.openai.com/auth/login"
        headers = {
            "Host": "ask.openai.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }
        response = self.__session.get(url=url, headers=headers)
        if response.status_code == 200:
            self.csrf()
        else:
            raise Exception("Failed to make the first request, Try that again!")

    def csrf(self):
        url = "https://chat.openai.com/api/auth/csrf"
        headers = {
            "Host": "ask.openai.com",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Referer": "https://chat.openai.com/auth/login",
            "Accept-Encoding": "gzip, deflate, br",
        }
        response = self.__session.get(url=url, headers=headers)
        if response.status_code == 200 and "json" in response.headers["Content-Type"]:
            csrf_token = response.json()["csrfToken"]
            self.authVerify(token=csrf_token)
        else:
            raise Exception("Failed to make the request, Try that again!")

    def authVerify(self, token: str):
        url = "https://chat.openai.com/api/auth/signin/auth0?prompt=login"
        payload = f"callbackUrl=%2F&csrfToken={token}&json=true"
        headers = {
            "Host": "ask.openai.com",
            "Origin": "https://chat.openai.com",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Referer": "https://chat.openai.com/auth/login",
            "Content-Length": "100",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = self.__session.post(url=url, headers=headers, data=payload)
        if response.status_code == 200 and "json" in response.headers["Content-Type"]:
            url = response.json()["url"]
            self.chatSession(url=url)
        elif response.status_code == 400:
            raise Exception("Bad request from your IP address, try again later")
        else:
            raise Exception("Failed to make the request, Try that again!")

    def chatSession(self, url: str):
        headers = {
            "Host": "auth0.openai.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://chat.openai.com/",
        }
        response = self.__session.get(url=url, headers=headers)
        if response.status_code == 302:
            state = re.findall(r"state=(.*)", response.text)[0]
            state = state.split('"')[0]
            self.getLogin(state=state)
        else:
            raise Exception("Failed to make the request, Try that again!")

    def getLogin(self, state: str):
        url = f"https://auth0.openai.com/u/login/identifier?state={state}"
        headers = {
            "Host": "auth0.openai.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://chat.openai.com/",
        }
        response = self.__session.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            if soup.find("img", alt="captcha"):
                svg_captcha = soup.find("img", alt="captcha")["src"].split(",")[1]
                decoded_svg = base64.decodebytes(svg_captcha.encode("ascii"))
                drawing = svg2rlg(BytesIO(decoded_svg))
                renderPM.drawToFile(drawing, "captcha.png", fmt="PNG", dpi=300)
                print(f"Captcha saved to captcha.png" + f" in the current directory")
                captcha_input = input(
                    f"Please solve the captcha and " f"press enter to continue: "
                )
                if captcha_input:
                    self._part_six(state=state, captcha=captcha_input)
                else:
                    raise Exception("You didn't enter anything.")
            else:
                self.state(state=state, captcha=None)
        else:
            raise Exception("Failed to make the request, Try that again!")

    def state(self, state: str, captcha: str or None):
        url = f"https://auth0.openai.com/u/login/identifier?state={state}"
        email_url_encoded = self.encodeURL(self.email_address)
        payload = f"state={state}&username={email_url_encoded}&captcha={captcha}&js-available=true&webauthn-available=true&is-brave=false&webauthn-platform-available=true&action=default"
        if captcha is None:
            payload = f"state={state}&username={email_url_encoded}&js-available=false&webauthn-available=true&is-brave=false&webauthn-platform-available=true&action=default"
        headers = {
            "Host": "auth0.openai.com",
            "Origin": "https://auth0.openai.com",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Referer": f"https://auth0.openai.com/u/login/identifier?state={state}",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = self.__session.post(url, headers=headers, data=payload)
        if response.status_code == 302:
            self.setPassword(state=state)
        else:
            raise Exception("Email not found, Check your email address and try again!")

    def setPassword(self, state: str):
        url = f"https://auth0.openai.com/u/login/password?state={state}"
        email_url_encoded = self.encodeURL(self.email_address)
        password_url_encoded = self.encodeURL(self.password)
        payload = f"state={state}&username={email_url_encoded}&password={password_url_encoded}&action=default"
        headers = {
            "Host": "auth0.openai.com",
            "Origin": "https://auth0.openai.com",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Referer": f"https://auth0.openai.com/u/login/password?state={state}",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = self.__session.post(url, headers=headers, data=payload)
        is_302 = response.status_code == 302
        if is_302:
            new_state = re.findall(r"state=(.*)", response.text)[0]
            new_state = new_state.split('"')[0]
            self.authorize(old_state=state, new_state=new_state)
        else:
            raise Exception("Password was incorrect or captcha was wrong")

    def authorize(self, old_state: str, new_state):
        url = f"https://auth0.openai.com/authorize/resume?state={new_state}"
        headers = {
            "Host": "auth0.openai.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Referer": f"https://auth0.openai.com/u/login/password?state={old_state}",
        }
        response = self.__session.get(url, headers=headers, allow_redirects=True)
        is_200 = response.status_code == 200
        if is_200:
            soup = BeautifulSoup(response.text, "lxml")
            next_data = soup.find("script", {"id": "__NEXT_DATA__"})
            access_token = re.findall(r"accessToken\":\"(.*)\"", next_data.text)
            if access_token:
                access_token = access_token[0]
                access_token = access_token.split('"')[0]
                self.storeAccess(access_token=access_token)
            else:
                raise Exception("Something went wrong, try again later!")

    @staticmethod
    def storeAccess(access_token: str, expiry: int or None = None):
        try:
            expiry = expiry or int(time.time()) + 3600
            path = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(path, "ACCESS_TOKEN.json")
            with open(path, "w") as f:
                f.write(
                    json.dumps({"access_token": access_token, "expires_at": expiry})
                )
        except Exception as e:
            raise e
