from aiogram import Bot, Dispatcher

from handlers.handlers import router

from config.config_reader import settings

#* Объект бота *#
bot = Bot(settings['telegram-token'], parse_mode='html')

#* Диспетчер *#
dp = Dispatcher()

#* Инициализация других роутеров
dp.include_router(router)

dp.start_polling(bot)