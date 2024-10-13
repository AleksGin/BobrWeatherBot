from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from core.texts import Phrases

router = Router()

@router.message(CommandStart)
async def start_func(message: Message):
    return await message.answer(Phrases.welcome_text)

@router.message(F.text.capitilize())
async def get_weather_for_city(message: Message):
    pass

