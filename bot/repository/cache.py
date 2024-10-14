from redis.asyncio import ConnectionPool


class CacheRepository:
    def __init__(self, pool: ConnectionPool) -> None:
        