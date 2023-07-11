import redis
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    redis_ip: str
    redis_port: int = 6379
    redis_password: str
    redis_db: int = 1

env = Settings(_env_file='.env', _env_file_encoding='utf-8')

class RedisTemplate:
    def __init__(self):
        self.client = redis.Redis(
            host=env.redis_ip,
            port=env.redis_port,
            password=env.redis_password, 
            db=env.redis_db,
            decode_responses=True
        )

    def __call__(self):
        return self

client = RedisTemplate().client;