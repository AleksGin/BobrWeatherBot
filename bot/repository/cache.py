from redis.asyncio import ConnectionPool, Redis

CHAT_ID_AND_CITY_KEY = "chat_id:{} city:{}"


class CacheRepository:
    def __init__(self, pool: ConnectionPool) -> None:
        self.pool = pool
        
        
    async def set_weather_info(self, chat_id: int, city_name: str, info: str, expire_time: int = 600) -> None:
        async with Redis.from_pool(connection_pool=self.pool) as redis:
            key = CHAT_ID_AND_CITY_KEY.format(chat_id, city_name)
            await redis.set(name=key, value=info, ex=expire_time)
    
    async def get_weather_info(self, chat_id: int, city_name: str):
        async with Redis.from_pool(connection_pool=self.pool) as redis:
            key = CHAT_ID_AND_CITY_KEY.format(chat_id, city_name)
            info = await redis.get(name=key)
            if info is None:
                return None
            return info.decode("utf-8")