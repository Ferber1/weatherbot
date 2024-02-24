import asyncio

from aiogram import Bot, Dispatcher
from telegram.bot import bot, dp
from telegram.handlers.handlers import main_router

#* class with functions for start telegram bot
class TgBot:
    def __init__(self) -> None:
        """
        Don't forgot install the package "aiogram" 
        >>> pip install aiogram
        """
        self.bot = bot
        self.dp = dp
    
    async def start(self) -> None:
        """
        Callable with asyncio.run
        >>> asyncio.run(TgBot().start())
        """

        #* Initialisation of another routers
        self.dp.include_router(main_router)

        #* Start the bot
        print('Start the polling..')

        await self.dp.start_polling(self.bot)
