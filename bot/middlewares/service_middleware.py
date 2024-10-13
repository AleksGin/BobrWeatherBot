from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from repo.weather import WeatherRepo


class RepoMiddleware(BaseMiddleware):
    def __init__(self, weather_repo: WeatherRepo) -> None:
        self.weather_repo = weather_repo

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data["weather_repo"] = self.weather_repo

        return await handler(event, data)
