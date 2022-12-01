from settings import *
from flask import Response, request, Flask
from aly.bot import *

# helping website https://www.pragnakalp.com/create-telegram-bot-using-python-tutorial-with-examples/
# telegram api https://core.telegram.org/bots/api
app = Flask(__name__)

# Main page

@app.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>Welcome!</h1>"
