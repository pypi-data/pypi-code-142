#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from dataclasses import dataclass
from distutils.version import LooseVersion

from slpkg.configs import Configs
from slpkg.queries import SBoQueries
from slpkg.blacklist import Blacklist


@dataclass
class Upgrade:
    log_packages: str = Configs.log_packages
    sbo_repo_tag: str = Configs.sbo_repo_tag

    def packages(self):
        ''' Compares version of packages and returns the maximum. '''
        print("Do not forget to run 'slpkg update' before.")

        repo_packages = SBoQueries('').names()
        black = Blacklist().get()

        for pkg in os.listdir(self.log_packages):
            inst_pkg_name = '-'.join(pkg.split('-')[:-3])
            if pkg.endswith(self.sbo_repo_tag) and inst_pkg_name not in black:

                if inst_pkg_name in repo_packages:
                    installed_ver = pkg.replace(f'{inst_pkg_name}-',
                                                '').split('-')[0]
                    repo_ver = SBoQueries(inst_pkg_name).version()

                    if LooseVersion(repo_ver) > LooseVersion(installed_ver):
                        yield inst_pkg_name
