#!/usr/bin/env python3
# encoding: UTF-8
# 2022.12.1 by ganjun

import os

def link_pics(inprefix, outprefix):
    os.system("ln -srf %s.png %s" %(inprefix, outprefix))
    os.system("ln -srf %s.pdf %s" %(inprefix, outprefix))