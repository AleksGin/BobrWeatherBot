from redis.asyncio import ConnectionPool, Redis


class CacheRepository:
    def __init__(self, pool: ConnectionPool) -> None:
        self.pool = pool
        
        
    async def set_weather_info(self, city_name: str, info: str, expire_time: int = 300) -> None:
        async with Redis.from_pool(connection_pool=self.pool) as redis:
            await redis.set(name=city_name, value=info, ex=expire_time)
    
    async def get_weather_info(self, city_name: str):
        async with Redis.from_pool(connection_pool=self.pool) as redis:
            info = await redis.get(name=city_name)
            if info is None:
                return None
            return info.decode("utf-8")