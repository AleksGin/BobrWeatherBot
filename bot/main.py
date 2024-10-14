import asyncio
import logging
import sys

import redis.asyncio as redis
from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp import ClientSession
from core import settings
from handlers.handlers import router as handlers_router
from middlewares import RepoMiddleware
from repository import (
    CacheRepository,
    WeatherRepository,
)
from services import WeatherService


async def main() -> None:
    async with ClientSession() as session:
        bot = Bot(
            token=settings.bot_config.bot_token.get_secret_value(),
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )

        weather_repo = WeatherRepository(
            http_session=session,
            api_key=settings.weather_config.weather_api_key.get_secret_value(),
            url=settings.weather_config.weather_url,
        )
        pool = redis.ConnectionPool.from_url(
            url=settings.redis_config.redis_url
        )
        cache_repo = CacheRepository(pool=pool)

        weather_service = WeatherService(
            weather_repo=weather_repo,
            cache_repo=cache_repo,
        )

        dp = Dispatcher()

        dp.message.middleware(
            RepoMiddleware(
                weather_repo=weather_repo,
                weather_service=weather_service,
                cache_repo=cache_repo,
            )
        )

        dp.include_routers(handlers_router)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
