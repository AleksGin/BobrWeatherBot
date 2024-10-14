from aiogram.types import Message
from core.schemas import WeatherResponseBase
from core.texts import (
    Phrases,
    WeatherIcon,
)
from pydantic import ValidationError
from repository import (
    CacheRepository,
    WeatherRepository,
)


class WeatherService:
    def __init__(
        self,
        weather_repo: WeatherRepository,
        cache_repo: CacheRepository,
    ) -> None:
        self.weather_repo = weather_repo
        self.cache_repo = cache_repo

    async def welcome_text(self, welcome_text: Message):
        return await welcome_text.answer(Phrases.welcome_text)

    async def get_info_about_city(self, chat_id: int, name_of_city: str) -> str:
        try:
            get_weather_info_model = await self.weather_repo.get_weather_info_by_id(
                city_name=name_of_city
            )
            check_cache = await self.cache_repo.get_weather_info(
                chat_id=chat_id, city_name=name_of_city
            )
            if check_cache:
                return check_cache
            return await self.__prepare_text(
                weather_model=get_weather_info_model, chat_id=chat_id
            )
        except ValidationError:
            return Phrases.validation_error.format(name_of_city)

    async def __prepare_text(
        self,
        weather_model: WeatherResponseBase,
        chat_id: int,
    ) -> str:
        weather = weather_model.weather[0]
        return await self.__text_for_weather(
            city=weather_model.name,
            temp=weather_model.main.temp,
            feels_like=weather_model.main.feels_like,
            weather_description=weather.description,
            weather_type_id=weather.id,
            wind=weather_model.wind.speed,
            chat_id=chat_id,
        )

    async def __text_for_weather(
        self,
        city: str,
        temp: float,
        feels_like: float,
        weather_description: str,
        weather_type_id: int,
        wind: float,
        chat_id: int,
    ) -> str:
        weather_icon = WeatherIcon.weather_icon.get(
            weather_type_id,
        )
        info = Phrases.information_form.format(
            city,
            int(temp),
            int(feels_like),
            weather_icon,
            weather_description.capitalize(),
            int(wind),
        )
        await self.cache_repo.set_weather_info(
            chat_id=chat_id,
            city_name=city,
            info=info,
        )
        return info
