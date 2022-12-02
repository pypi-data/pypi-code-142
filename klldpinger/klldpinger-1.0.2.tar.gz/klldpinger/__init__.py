import requests
import os


#3rd party imports:
import aiohttp
import asyncio

#3rd party from imports:

#exceptions:
from .exceptions import InvalidPermission 
from .exceptions import InvalidPlatform
from .exceptions import AlreadyPinging
from .exceptions import InvalidURL


base = "https://cdf38ef8-3359-474c-a89a-d50d7148febe.id.repl.co"
#Please Do Not Mess with the Database
#It will lead in a blacklist from the pinger and will mess peoples repls!

def get_url(platform=None):
  if platform is None:
    raise InvalidPlatform('Please Enter A Valid Platform!')
  elif platform.lower() in [
    'repl', 
    'replit'
  ]:
    try:
      return f"https://{os.environ['REPL_ID']}.id.repl.co"
    except:
      raise InvalidPlatform('Unable To Obtain URL\nPlease Try manually!')
  elif platform.lower() == 'heroku':
    try:
      return f"https://{os.environ['HEROKU_APP_NAME']}.herokuapp.com"
    except:
      raise InvalidPlatform('Unable To Obtain URL')

def is_online():
  try:
    r = requests.get(base)
  except requests.exceptions.ConnectionError:
    return False
  return True

async def revive_pinger():
  while True:
    async with aiohttp.ClientSession() as session:
      async with session.request(
        method='GET', 
        url=base
      ) as r:
        await asyncio.sleep(600)
  return  

async def post(
  url,
  external_urls: list=None
):
  """Posts URL(s) To klldPinger or Any External Pinger"""
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='POST', 
      url=f'{base}/api/add',
      headers={
        'BASE': url
      },      
      json=(
        {'url': url}
      )
    ) as r:
      response = await r.json()
    if external_urls != None:
      for url in external_urls:
        try:
          async with aiohttp.ClientSession() as session:
            async with session.request(
              method='POST', 
              url=f'{url}/api/add',
              headers={
                'BASE': url
              },      
              json=(
                {'url': url}
              )
            ) as r:
              response = await r.json()
        except Exception as e:
          raise(e)
      if response == {"result": "URL Already Stored!"}:
        raise AlreadyPinging('Already Pinging This URL')
      elif "http" not in url:
        raise InvalidURL('Invalid URL Requested')
      elif "https" not in url:
        raise InvalidURL('Invalid URL Requested')
      elif response == {"result": True}:
        return True
  return

async def remove(
  url,
  external_urls: list=None
):
  """Removes URL(s) To klldPing or Any External Pinger"""
  async with aiohttp.ClientSession() as session:
    async with session.request(
      method='POST', 
      url=f'{base}/api/remove',
      headers={
        'BASE': url
      },
      json=(
        {'url': url}
      )
    ) as r:
      response = await r.json()
    if external_urls != None:
      for url in external_urls:
        try:
          async with aiohttp.ClientSession() as session:
            async with session.request(
              method='POST',
              url=f'{base}/api/remove',
              headers={
                'BASE': url
              },
              json=(
                {'url': url}
              )
            ) as r:
              response = await r.json()
        except Exception as e:
          raise(e)
      if response == {"result": "URL Not Found!"}:
        raise InvalidURL('Unable To Find This URL')
      elif "http" not in url:
        raise InvalidURL('Invalid URL')
      elif "https" not in url:
        raise InvalidURL('Invalid URL')
      elif response == {'result': 'Invalid Permission'}:
        raise InvalidPermission('You Cannot Remove Somone Elses URL!')
      elif response == {"result": True}:
        return True
  return    
