import asyncio
import aiohttp
import urllib


class Auth:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.access_token = None
        self.session = None

    def _login(self):
        if not self.session:
            self.session = aiohttp.ClientSession()

        # Add headers to the session
        self.session.headers.update({
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        })

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",

        }



    def __del__(self):
        if self.session:
            self.session.close()
