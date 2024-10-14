import logging
from core.texts import Phrases
from core.schemas import WeatherResponseBase, Main
from repo.weather import WeatherRepo
from aiogram.types import Message


class WeatherService:
    def __init__(self, weather_repo: WeatherRepo) -> None:
        self.weather_repo: WeatherRepo = weather_repo

    async def welcome_text(self, welcome_text: Message):
        return await welcome_text.answer(Phrases.welcome_text)

    async def get_info_about_city(self, name_of_city: str) -> str:
        get_weather_info_model = await self.weather_repo.get_weather_info_by_id(
            city_name=name_of_city
        )
        return await self.__prepare_text(weather_model=get_weather_info_model)

    async def __prepare_text(
        self,
        weather_model: WeatherResponseBase,
        chat_id: int | None = None,
    ) -> str:
        return await self.__text_for_weather(
            temp=weather_model.main.temp,
            city=weather_model.name,
            feels_like=weather_model.main.feels_like,
        )

    async def __text_for_weather(self, temp: float, city: str, feels_like: float) -> str:
        return f"Погода в {city} {temp}, ощуещается как {feels_like}"
