import asyncio
from aiogram import Bot, Dispatcher

from telegram.handlers.handlers import router

from config.settings import settings

#* Объект бота *#
bot = Bot(settings['telegram-token'], parse_mode='html')

#* Диспетчер *#
dp = Dispatcher()

#* Инициализация других роутеров
dp.include_router(router)

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))