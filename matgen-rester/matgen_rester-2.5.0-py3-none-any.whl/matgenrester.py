# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:56:51 2020

@author: Q Mo
"""

import requests
import json
import warnings
# from .matdata import MatData
from .MatgenError import MatgenError
from concurrent.futures import ThreadPoolExecutor,as_completed
from .auth import SETTINGS, write_matgen_token
from .args import parse_cml_args
import sys

null = ''

class MatgenRester:
  def __init__(self, username=None, password=None, token=None,endpoint=None):
    if endpoint is not None:
      self._preamble = endpoint
    else:
      self._preamble = SETTINGS.get("MATGEN_ENDPOINT")
    if self._preamble is None:
      self._preamble = "https://matgen.nscc-gz.cn/matgenRester/"
    if self._preamble != "https://matgen.nscc-gz.cn/matgenRester/":
      warnings.warn("None-default endpoint used:{}".format(self._preamble))  
    self._DATA_LIMIT = 10
    self.session = requests.Session()
    
    if token is not None:
      self._token = token
      write_matgen_token(self._token)
    elif (username is not None) and (password is not None):
      print('username is ',username)
      self.username = username
      self.password = password
      self._token = self.login()
    else:
      try:
        self._token = SETTINGS.get("MATGEN_TOKEN")
      except KeyError as k:
        raise MatgenError("Authentication returned with {]".format(k))
 
  def __enter__(self):
    return self
  
  def login(self, verbose=True):
    # url=self.preamble + "/token",
    url="https://matgen.nscc-gz.cn/api/token"
    #print('url', url)
    payload = {
      "username":self.username,
      "logged_in":True
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
      response = self.session.post(url, headers=headers, data = json.dumps(payload))
      if response.status_code not in [200,400]:
        raise MatgenError("Request returned with error status code {}"
                          .format(response.status_code))
      else:
        if verbose:
          value = str(response.content,encoding="utf-8")
          #print("logged in (MATGEN_TOKEN={})".format(value))
          write_matgen_token(value)
        return value
        
    except Exception as ex:
      raise MatgenError("Authentication returned with {}".format(str(ex)))
       
  def __exit__(self, ex_type, ex_value, traceback):
    self.session.close()
  
  def reconnect(self):
    self.login(verbose=True)
  
  def _make_request(self, url=None, param=None, payload=None, method="POST"):
    response = None
    _url = self._preamble + url
    #print(_url)
    if self._token != None:
      param['token']=self._token
    else:
      raise MatgenError("can't get token")
    try:
      if method == "POST":
        headers = {
            'Content-Type': 'application/json'
        }
        response = self.session.post(_url, headers=headers, data = json.dumps(payload),params=param)
      else:
        raise MatgenError("Request method error")
      if response.status_code in [200,400]:
        if response.text == '':
          raise MatgenError("Request returned with error, nothing return")
        return json.loads(response.text)
      else:
        raise MatgenError("Request returned with error status code {}"
                          .format(response.status_code))
    except Exception as ex:
      raise MatgenError("Request returned with {}".format(str(ex)))
    
  def get_structure_by_id(self,targetId, idType, fields=['structure']):
    try:
      _url = 'material/'+idType + '/' + str(targetId)
      res = self._make_request(_url, {}, fields)
      if(len(res) > 0):
        return res
      else:
        return {}
    except Exception as ex:
      raise MatgenError("Request returned with {}".format(str(ex)))
  
  def parallel_ids(self,ids,idType, fields=None):
    if len(ids) > self._DATA_LIMIT:
      warnings.warn("query too much")
      ids = ids[0:self._DATA_LIMIT+1]
    with ThreadPoolExecutor(max_workers=self.max_connection) as executor:
      future_to_filter = []
      for index in range(0,len(ids)):
        executor.submit(self.get_structure_by_id,ids[index],idType, fields)
      for future in as_completed(future_to_filter):
          res = future_to_filter[future]
          try:
            yield future.result()
          except Exception as exc:
            raise MatgenError("{} caused exception: {}".format(res,exc))
            
  def get_structure_with_filter(self,filter=None, fields=['structure'],size=1, page=0):
    param={
      "pages": size,
      "pageno": page
    }
    filter['properties'] = fields
    r = self._make_request('material/filter',param=param, payload=filter)
    return r
    
            
  def download_data_set(self,context, filename):
    with open(filename, 'w+') as f:
      f.write(context)
          
if __name__ == "__main__":
  matgenrester = MatgenRester()
  parser = parse_cml_args(sys.argv[1:])
  #print(parser)
  #print(type([parser]))
  if 'token' in parser and parser.token != None:
    write_matgen_token(parser.t)
    matgenrester = MatgenRester(token=parser.t)
  context = ''
  fields = parser.fields
  if fields:
    fields=parser.fields.split(',')
  if parser.id:
    context = matgenrester.get_structure_by_id(parser.idType, parser.id,fields = fields)
  else:
    filter={}
    filter_args=['in', 'not', 'searchType', 'crystalSystem', 'pointGroup', 'spaceGroup', 'volume', 'density', 'ifIcsdid', 'ifCodid','ifOqmdid']
    for item in filter_args:
      if item in parser:
        if item in ['in', 'not']:
          filter[item] = parser[item].split('-')
        elif item in ['crystalSystem', 'pointGroup', 'spaceGroup']:
          filter[item] = parser[item].split(',')
        elif item in ['volume', 'density']:
          if parser[item].trim().index(',') not in [0,len(parser[item].trim())]:
            filter[item] = [float(data) for data in parser[item].split(',')]
          elif parser[item].trim().index(',') == 0:
            filter[item] = [0, float(parser[item].trim().split(',')[1])]
          elif parser[item].trim().index(',') == len(parser[item].trim()):
            filter[item] = [float(parser[item].trim().split(',')[0]),15200]
        else:
          filter[item] = parser[item]
    context = matgenrester.get_structure_with_filter(filter=filter, fields=fields,size=parser.size, page=parser.index)            
  
  if parser.o:
    sp = []
    for specific in context:
      sp.append(specific.__str__())
    matgenrester.download_data_set('\n'.join(sp),parser.o)
  else:
    print(context)