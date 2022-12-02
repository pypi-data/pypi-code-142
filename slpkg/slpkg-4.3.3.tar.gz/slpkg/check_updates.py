#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import urllib3
from dataclasses import dataclass

from slpkg.configs import Configs


@dataclass
class CheckUpdates:
    sbo_repo_url: str = Configs.sbo_repo_url
    sbo_repo_path: str = Configs.sbo_repo_path
    chglog_txt: str = Configs.chglog_txt

    def updates(self):

        local_date = 0
        local_chg_txt = f'{self.sbo_repo_path}/{self.chglog_txt}'

        http = urllib3.PoolManager()
        repo = http.request(
            'GET', f'{self.sbo_repo_url}/{self.chglog_txt}')

        if os.path.isfile(local_chg_txt):
            local_date = int(os.stat(local_chg_txt).st_size)

        repo_date = int(repo.headers['Content-Length'])

        if repo_date != local_date:
            print('\nThere are new updates available.\n')
        else:
            print('\nNo updated packages since the last check.\n')
