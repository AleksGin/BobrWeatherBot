import logging

from aiogram.types import Message
from core.schemas import WeatherResponseBase
from core.texts import (
    Phrases,
    WeatherIcon,
)
from pydantic import ValidationError
from repo.weather import WeatherRepo


class WeatherService:
    def __init__(self, weather_repo: WeatherRepo) -> None:
        self.weather_repo: WeatherRepo = weather_repo

    async def welcome_text(self, welcome_text: Message):
        return await welcome_text.answer(Phrases.welcome_text)

    async def get_info_about_city(self, name_of_city: str) -> str:
        try:
            get_weather_info_model = await self.weather_repo.get_weather_info_by_id(
                city_name=name_of_city
            )
            return await self.__prepare_text(weather_model=get_weather_info_model)
        except ValidationError:
            return Phrases.validation_error.format(name_of_city)

    async def __prepare_text(
        self,
        weather_model: WeatherResponseBase,
        chat_id: int | None = None,
    ) -> str:
        weather = weather_model.weather[0]
        return self.__text_for_weather(
            city=weather_model.name,
            temp=weather_model.main.temp,
            feels_like=weather_model.main.feels_like,
            weather_description=weather.description,
            weather_type_id=weather.id,
            wind=weather_model.wind.speed,
        )

    def __text_for_weather(
        self,
        city: str,
        temp: float,
        feels_like: float,
        weather_description: str,
        weather_type_id: int,
        wind: float,
    ) -> str:
        weather_icon = WeatherIcon.weather_icon.get(weather_type_id)
        return Phrases.information_form.format(
            city,
            int(temp),
            int(feels_like),
            weather_icon,
            weather_description.capitalize(),
            int(wind),
        )
