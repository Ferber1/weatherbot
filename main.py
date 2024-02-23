import asyncio

from telegram.bot import bot, dp
from telegram.handlers.handlers import main_router
from aiogram import Bot, Dispatcher

#* class with functions for start telegram bot
class TgBot:
    def __init__(self, bot: Bot = None, dp: Dispatcher = None) -> None:
        """
        Don't forgot install the package "aiogram" 
        >>> pip install aiogram
        """
        if isinstance(bot, Bot) and isinstance(dp, Dispatcher):
            self.bot = bot
            self.dp = dp
            return

        raise TypeError(
            "The 'bot' argument must be an instance of the Bot class and the 'dp' argument must be an instance of the Dispatcher class."
            )
    
    async def start(self) -> None:
        self.dp.include_router(main_router)
        await self.dp.start_polling(self.bot)


#* class with functions for start vk bot
class VkBot:
    def __init__(self, bot: ...) -> None:
        """
        Don't forgot install the package "vkbottle" 
        >>> pip install vkbottle
        """
        ...


if __name__ == '__main__':
	#* for start one of bots uncomment code you need
    
    print('Starting..')
    
    #. <----- Telegram bot ----->
	# tgbot = TgBot(bot, dp)
	# asyncio.run(tgbot.start())
    
    #. <----- Vk bot ----->
    