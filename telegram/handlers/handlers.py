from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config.settings import commands

from api.weather import api_key

router = Router()

#* /start *#
@router.message(CommandStart(ignore_case=True), Command(commands[0], ignore_case=True, prefix='/!'))
async def _start(message: Message):
    await message.answer('ti gey')

#* /weather *#
@router.message(Command(commands[1], prefix='/!', ignore_case=True))
async def _weather(message: Message):
	...
