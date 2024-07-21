import os
from redis import Redis

HOST: str = os.getenv("REDIS_HOST")
PORT: int = os.getenv("REDIS_PORT")

redis_client = Redis(host=HOST, port=PORT, db=0)
