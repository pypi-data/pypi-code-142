import redis

r = redis.Redis(host="localhost", port=6379, db=0)


class CacheService:
    def set_credentials(self, bind_jwt: str, ttl: int) -> None:
        r.set("bind_jwt", bind_jwt, ttl)

    def get_credentials(self) -> str:
        return r.get("bind_jwt")
