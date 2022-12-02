# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-import


import colemen_utils as c
import time
# from flask import Flask,redirect,url_for,request,Blueprint
import apricity.settings as settings


DATA = {
    "log":[]
}


def add(message,style="info"):
    data = {
        "timestamp":time.time(),
        "message":message,
    }

    DATA['log'].append(data)
    if settings.master_control.log_to_console is True:
        c.con.log(message,style)


# class Log:
#     def __init__(self):
#         self.settings = {}
#         self.data = {
#             "log":[]
#         }



#     def add(self,message,style="info"):
#         data = {
#             "timestamp":time.time(),
#             "message":message,
#         }

#         self.data['log'].append(data)
#         if settings.master_control.log_to_console is True:
#             c.con.log(message,style)

