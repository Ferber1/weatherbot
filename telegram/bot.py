import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from telegram.handlers.handlers import main_router

from config.settings import settings

#* Объект бота *#
bot = Bot(settings['telegram-token'], 
        default=DefaultBotProperties(parse_mode='html'))

#* Диспетчер *#
dp = Dispatcher()


#. Запуск бота
if __name__ == '__main__':
    #* Инициализация других роутеров
    dp.include_router(main_router)
    asyncio.run(dp.start_polling(bot))