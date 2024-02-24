import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from telegram.handlers.handlers import main_router

from config.settings import settings

#* Object of the bot *#
bot = Bot(settings['telegram-token'], 
        default=DefaultBotProperties(parse_mode='html'))

#* Dispatcher *#
dp = Dispatcher()
