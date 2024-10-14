from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from repo.weather import WeatherRepo
from services import WeatherService


class RepoMiddleware(BaseMiddleware):
    def __init__(
        self,
        weather_repo: WeatherRepo,
        weather_service: WeatherService,
    ) -> None:
        self.weather_repo = weather_repo
        self.weather_service = weather_service

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data["weather_repo"] = self.weather_repo
        data["weather_service"] = self.weather_service

        return await handler(event, data)
