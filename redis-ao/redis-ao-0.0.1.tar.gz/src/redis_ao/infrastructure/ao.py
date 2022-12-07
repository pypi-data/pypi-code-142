import redis, pickle
from ddd_objects.lib import get_random_string
from .do import RedisData


class RedisAccessOperator:
    def __init__(self, ip: str, port: int, token: str) -> None:
        self.client = redis.StrictRedis(host=ip, port=port, password=token)


    def send_request(self, domain:str, key:str, request)->str:
        request_id = get_random_string(10)
        key = f'{domain}:{key}'
        obj = RedisData(id=request_id, obj=request)
        obj = pickle.dumps(obj)
        succeed = self.client.lpush(key, obj)
        print(succeed)
        return request_id


    def get_request(self, domain:str, key:str):
        key = f'{domain}:{key}'
        obj = self.client.lpop(key)
        return pickle.loads(obj)


    def set_response(self, domain:str, request_id:str, response, timeout:int=300)->bool:
        obj = pickle.dumps(response)
        key = f'{domain}:{request_id}'
        succeed = self.client.setex(key, timeout, obj)
        return succeed


    def get_response(self, domain:str, request_id):
        key = f'{domain}:{request_id}'
        obj = self.client.get(key)
        return pickle.loads(obj)



