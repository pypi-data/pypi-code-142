# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
═════════════════════════════
@Time   : 2022/11/24 14:31:49
@Author : Rey
@Contact: reyxbo@163.com
@Explain: Rey's types
═════════════════════════════
'''


def _func(): pass
function = type(_func)

class _obj:
    def _method(): pass
_obj = _obj()
method = type(_obj._method)