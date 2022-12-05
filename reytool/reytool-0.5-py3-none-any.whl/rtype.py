# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
══════════════════════════════
@Time    : 2022/12/05 14:12:16
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's types
══════════════════════════════
'''


# Function type
def _func(): pass
function = type(_func)

# Method type of class
class _obj:
    def _method(): pass
_obj = _obj()
method = type(_obj._method)