from typing import (
    Any,
    Awaitable,
    Callable,
)

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from repository import (
    WeatherRepository,
    CacheRepository,
)
from services import WeatherService


class RepoMiddleware(BaseMiddleware):
    def __init__(
        self,
        weather_repo: WeatherRepository,
        weather_service: WeatherService,
        cache_repo: CacheRepository,
    ) -> None:
        self.weather_repo = weather_repo
        self.weather_service = weather_service
        self.cache_repo = CacheRepository

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data["weather_repo"] = self.weather_repo
        data["weather_service"] = self.weather_service
        data["cache_repo"] = self.cache_repo

        return await handler(event, data)
