import redis
from typing import Optional

class RedisClient:
    def __init__(self, host: str = "redis", port: int = 6379, db: int = 0):
        self.redis = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def get_address(self, phone: str) -> Optional[str]:
        return self.redis.get(phone)

    def set_address(self, phone: str, address: str) -> bool:
        return self.redis.set(phone, address)

    def update_address(self, phone: str, address: str) -> bool:
        return self.set_address(phone, address)

redis_client = RedisClient()
