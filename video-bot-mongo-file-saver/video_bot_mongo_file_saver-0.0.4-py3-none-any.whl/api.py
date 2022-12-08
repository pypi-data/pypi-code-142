from dotenv import load_dotenv
from os import environ

from flask import Flask
from flask_restful import Resource, Api  #, reqparse
#from flask_pymongo import PyMongo

from file_saver.handler import handler
from file_saver.utils.lambda_helpers import get_json
from file_saver.get_event import get_event

app = Flask(__name__)


API_PORT = environ.get('API_PORT')

class Api:
    
    @app.route('/', defaults={'path': ''}, methods = ['GET', 'POST'])
    @app.route('/<path:path>', methods = ['GET', 'POST'])
    def catch_all(path):
        
        load_dotenv()
        
        event = get_event()
        event = {**event, 'path': '/' + path}

        result = handler(event, None)
        json_str = get_json(result)
        return json_str
         

    def run(self):
        app.run(port=API_PORT)   


    

  








    

    
    
