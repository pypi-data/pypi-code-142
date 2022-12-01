from . import downloader

from dotenv import load_dotenv

from flask import Flask, request
from werkzeug.exceptions import Forbidden

from super_eureka import logging

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

@app.route('/main/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        body: dict = request.get_json()
        download_link: str = body.get('download_link', '')
        if download_link:
            downloader.download_and_process(download_link)
            return 'The download process was initiated.'
    raise Forbidden


# added because of wsgi
def initialize() -> None:
    logging.initialize()
    load_dotenv()


def serve() -> None:
    initialize()
    app.run(port=5500)


if __name__ == "__main__":
    serve()
