class Response:
    def __init__(self, response):
        self.response = response
        # 自适应编码
        self.response.encoding = self.response.apparent_encoding

    def findall(self):
        pass

    @property
    def status(self):
        return self.response.status_code

    @property
    def headers(self):
        return self.response.headers

    @property
    def content(self):
        return self.response.content

    @property
    def json(self):
        return self.response.json()

    @property
    def text(self):
        return self.response.text

    def __str__(self):
        return f'<Response [{self.response.status_code}]>'
