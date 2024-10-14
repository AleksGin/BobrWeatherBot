from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from services import WeatherService

router = Router()


@router.message(CommandStart())
async def start_func(
    message: Message,
    weather_service: WeatherService,
) -> Message:
    return await weather_service.welcome_text(welcome_text=message)


@router.message(F.text)
async def get_weather_for_city(
    message: Message,
    weather_service: WeatherService,
) -> Message:
    if not message.text:
        return await message.answer("Введите название города")

    info = await weather_service.get_info_about_city(
        chat_id=message.chat.id,
        name_of_city=message.text.capitalize(),
    )
    return await message.answer(info)
