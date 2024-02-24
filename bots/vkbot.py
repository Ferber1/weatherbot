import asyncio

from vkbottle.bot import Bot
from vk.bot import bot

#* class with functions for start vk bot
class VkBot:
    def __init__(self) -> None:
        self.bot = bot
    
    async def start(self) -> None:
        """
        Callable with asyncio.run
        >>> asyncio.run(VkBot().start())
        """
        await self.bot.run_polling()
