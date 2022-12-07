import json
import os
import aiohttp
import jwt
import time
import uuid
import asyncio
from datetime import datetime, timedelta
from nerualpha.IBridge import IBridge

class Bridge(IBridge):
    def substring(self,str,start,end):
        return str[start:end]
    def jsonStringify(self,data):
        return json.dumps(data, default=lambda o: o.reprJSON(),
            sort_keys=True, indent=4)
    def jsonParse(self,str):
        return json.loads(str)
    def getEnv(self,name):
        return os.getenv(name)
    async def request(self,params):
        try:
            if not params.url:
                raise Exception('url is required')
            if not params.method:
                raise Exception('method is required')

            url = params.url.host + '/' + params.url.pathname if params.url.pathname else params.url.host
            method = params.method
            headers = params.headers
            data = params.data
            query = params.url.query

            if headers['Content-Type'] == 'multipart/form-data':
                del headers['Content-Type']
            elif headers['Content-Type'] == 'application/json':
                if hasattr(data,'reprJSON'):
                    data = data.reprJSON()
                data = json.dumps(data)

            async with aiohttp.ClientSession() as session:
                async with session.request(method, url, data=data, headers=headers, params=query) as resp:
                    if resp.content_type == 'application/json':
                        return await resp.json()
                    else:
                        return await resp.text()
        except Exception as e:
            print("Exception in request")
            raise e

    def runBackgroundTask(self, task):
        loop = asyncio.get_event_loop()
        loop.create_task(task)

    def createReadStream(self,path):
        return open(path, 'rb')

    async def requestWithoutResponse(self,params):
        await self.request(params)
    def uuid(self):
        return str(uuid.uuid4())
    def isoDate(self):
        my_date = datetime.now()
        return my_date.isoformat()
    def toISOString(self,seconds):
        my_date = datetime.now() + timedelta(seconds=seconds)
        return my_date.isoformat()
    def jwtSign(self,payload,privateKey,algorithm):
        return jwt.encode({
            'api_application_id': payload.api_application_id,
            'api_account_id': payload.api_account_id,
            'exp': payload.exp,
            'aud': payload.aud,
            'sub': payload.sub,
            'iss': payload.iss,
            }, privateKey, algorithm)
    def jwtVerify(self,token,privateKey,algorithm):
        return jwt.decode(token, privateKey, algorithm)
    def jwtDecode(self,token):
        return jwt.decode(token, options={"verify_signature": False})
    def getSystemTime(self):
        return int(time.time())
    def log(self,logAction):
        print(logAction)
    def getObjectKeys(self,obj):
        return obj.keys()
