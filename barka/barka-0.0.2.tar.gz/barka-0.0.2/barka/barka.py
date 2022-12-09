import requests

api_url = 'https://www.youtube.com/watch?v=0qzLRlQFFQ4'

def use_requests(api_url):
    response = requests.get(api_url)
    print(response)

def greet():
    print('hello world')

use_requests(api_url)
