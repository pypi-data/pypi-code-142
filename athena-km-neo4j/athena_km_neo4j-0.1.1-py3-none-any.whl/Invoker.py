import json
import requests
import httpx
from .URLConstant import URLConstant

limits = httpx.Limits(max_keepalive_connections=50, max_connections=100)
client = httpx.AsyncClient(limits=limits)


class Invoker(object):
    @staticmethod
    def triples_save_sync(request):
        neo_url = URLConstant.TM_BASE_URL + "/restful/service/knowledgegraph/triples/postTriplesSave"
        headers = {"Content-Type": "application/json"}
        data = json.dumps(request)
        response = requests.post(neo_url, headers=headers, data=data)
        return response

    @staticmethod
    async def triples_save_async(request):
        neo_url = URLConstant.TM_BASE_URL + "/restful/service/knowledgegraph/triples/postTriplesSave"
        headers = {"Content-Type": "application/json"}
        data = json.dumps(request)
        res = await client.post(neo_url, headers=headers, data=data)
        return res

    @staticmethod
    def triples_del_sync(request):
        neo_url = URLConstant.TM_BASE_URL + "/restful/service/knowledgegraph/triples/triplesDel"
        headers = {"Content-Type": "application/json"}
        data = json.dumps(request)
        response = requests.post(neo_url, headers=headers, data=data)
        return response

    @staticmethod
    async def triples_del_async(request):
        neo_url = URLConstant.TM_BASE_URL + "/restful/service/knowledgegraph/triples/triplesDel"
        headers = {"Content-Type": "application/json"}
        data = json.dumps(request)
        res = await client.post(neo_url, headers=headers, data=data)
        return res
