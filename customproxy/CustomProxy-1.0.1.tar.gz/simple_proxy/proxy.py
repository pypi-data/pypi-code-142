import requests
import tempfile
import random
from typing import List, Tuple, Union
try:
    import ujson as json
except ImportError:
    import json
    
from pathlib import Path
from collections import defaultdict
from bs4 import BeautifulSoup

class CustomProxy(object):
    def __init__(self, code: Union[str, List[str], Tuple[str]] = []) -> None:
        assert isinstance(code, (str, list, tuple)), 'Code must be list or str or tuple'
        self.base_url = 'https://free-proxy-list.net/'
        self.session = requests.Session()
        self.code = code
        self.temp_path = tempfile.gettempdir() + '/temp.json'
        self.loads()

    def random(self, pretty=True):
        """
        generate random proxy
        
        args:
            pretty: bool : default True
            
        if pretty is True the ouput will be prettifier e.g http://123.1.1.1:80
        
        return dict or str
        """
        temp = self.temp_path
        with open(temp, 'r') as f:
            js = json.load(f)
            code = self.code if isinstance(self.code, (list, tuple)) else [self.code]
            if code:
                dummy = [i for i in js if i['code'] in code]
            else:
                dummy = [i for i in js]
                
            ret = random.choice(dummy)
            proxy = {
                'host': f'{ret["ip"]}:{ret["port"]}',
                'code': ret['code'],
                'loc': ret['loc']
            }
            if pretty:
                return 'http://' + ret['ip'] + ':' + ret['port']
            
            return proxy
            
    def __request(self, url):
        _RETRIES = 0
        with self.session as session:
            while True:
                req = session.get(url)
                if req.ok:
                    return req
                else:
                    _RETRIES += 1
                    if _RETRIES >= 5:
                        raise Exception('MAX Retries occured. please try again')
                    
                    continue
    
    def save_to_temp(self, data = None):
        temp = self.temp_path
        if not Path(temp).exists():
            file = Path(temp)
            file.touch(exist_ok=True)
            with open(file, 'w') as f:
                json.dump(
                    data,
                    f,
                    indent=4
                )
            
    def loads(self):
        data = defaultdict(list)
        url = self.base_url
        req = self.__request(url)
        soup = BeautifulSoup(req.content, 'lxml')
        table = soup.select('#list > div > div.table-responsive > div > table tr')[1:]
        data = [{'ip': ip, 'port': port, 'loc': loc, 'code': code} for row in table for
                ip, port, loc, code in zip(row.find_all('td')[0], 
                                     row.find_all('td')[1],
                                     row.find_all('td')[3],
                                     row.find_all('td')[2])
                ]
        self.save_to_temp(data)