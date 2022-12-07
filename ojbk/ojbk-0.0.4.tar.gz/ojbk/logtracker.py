#!/usr/bin/env python3
import re
from typing import Callable, Dict, List, Optional, Set, Tuple, Union

import codefast as cf
from codefast.patterns.pipeline import Component, Pipeline

from codefast.io.osdb import osdb
db = osdb('/tmp/logtracker')

from authc import gunload 
import codefast as cf 

def post_to_telegram(msg: str):
    try:
        TOKEN = gunload('hema_bot')
        url = 'https://api.telegram.org/bot{}/sendMessage?chat_id=@messalert&text={}'.format(
            TOKEN, msg)
        _res = cf.net.post(url)
    except Exception as e:
        pass 


class NewErrorCollector(Component):
    def __init__(self) -> None:
        super().__init__()
        self.print_log = False

    def process(self, log_path: str) -> List[str]:
        lns = []
        with open(log_path, 'r') as f:
            pre = ''
            for line in f:
                if 'ERROR' in line:
                    start_mark = True
                if 'INFO' in line:
                    start_mark = False 

                if start_mark:
                    pre += line
                
                if not start_mark:
                    if pre and (pre not in lns):
                        pre = re.sub(r'\[\d+m', '', pre)
                        if not db.exists(cf.md5sum(pre)):
                            lns.append(pre)
                    pre = '' 
        return lns


class Post(Component):
    def __init__(self) -> None:
        super().__init__()
        self.print_log = False

    def process(self, errors: List[str]) -> List[str]:
        for e in errors:
            post_to_telegram(e)
        return errors


class MarkPosted(Component):
    def __init__(self) -> None:
        super().__init__()
        self.print_log = False

    def process(self, errors: List[str]) -> List[str]:
        for e in errors:
            db.set(cf.md5sum(e), e)
        return errors

def logtrack():
    log_path: str='/tmp/cf.log'
    from authc.myredis import rc
    KEY = '5afd94e13aa299ec0efdc4ba'
    if rc.local.set(KEY, 1, ex=60, nx=True):
        p = Pipeline([NewErrorCollector(), Post(), MarkPosted()])
        p.process(log_path)

if __name__ == '__main__':
    logtrack()
