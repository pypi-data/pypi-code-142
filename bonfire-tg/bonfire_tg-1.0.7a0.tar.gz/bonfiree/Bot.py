from flask import Flask
from flask import request
from flask import Response
import requests
app = Flask(__name__)


def Bots(TOKEN):
    return TOKEN
    
class bot:
    def handler(func):
     def wrappe():   
      func()   
     return wrappe

def commands(app):
    a=app.route('/',methods=['GET', 'POST'])
    return a
def run (app):
    """start flask server"""
    a=app.run(port=8080,host="0.0.0.0",debug=True)
    return a
