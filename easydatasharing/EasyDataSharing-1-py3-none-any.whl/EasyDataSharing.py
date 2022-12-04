import json
import math
import os,sys
from UniqueIDV import CreateId , getMyId
from time import *

basic = {"data": [], "Alerts": 0, "Authors": []}
home = os.path.join(os.path.dirname(__file__))+ "/"

f = open(home + "data.json")
datas = json.load(f)
f.close()
basicInfo = {"name": "","to": "","data": {}}
AlertsSize = 0
def getFrom(reader,author,id,ValueId):
    global datas
    return datas["data"][id]["data"][ValueId]
def Updates():
    global AlertsSize
    UpdateValue()
    if AlertsSize != datas["Alerts"]:
        AlertsSize = datas["Alerts"]
        return True
    if AlertsSize == datas["Alerts"]:
        return False
def UpdateValue():
    global datas
    f = open(home + "data.json","r")
    if os.stat(home + "data.json").st_size == 0:
        sleep(0.1)
    datas = json.load(f)
    f.close()
def Alert():
    datas["Alerts"] += 1
def IdFromAuthor(author):
    return datas["Authors"].index(author)
def UpdateData(author,reader,ValueId,Value,id=-1):
    global datas
    if id == -1:
        datas["data"].append(basicInfo)
        id = len(datas["data"])-1
        datas["data"][id]["name"] = author
        datas["data"][id]["to"] = reader
        datas["data"][id]["data"][ValueId] = Value
        f = open(home + "data.json","w+")
        f.truncate(0)
        f.seek(0)
        datas["Authors"].append(author)
        Alert()
        f.write(json.dumps(datas))
        f.close()
        return id
    if id == IdFromAuthor(author):
        datas["data"][id]["name"] = author
        datas["data"][id]["to"] = reader
        datas["data"][id]["data"][ValueId] = Value
        f = open(home + "data.json","w+")
        f.truncate(0)
        f.seek(0)
        Alert()
        f.write(json.dumps(datas))
        f.close()
        return