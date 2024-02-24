import asyncio

from vkbottle.bot import Bot, BotLabeler

from vk.handlers.handlers import main_labeler
from vk.utils.states import dispanser

from config.settings import settings

#* Object of main labeler *#
labeler = BotLabeler()

#* Labeler settings, download another labeler *#
labeler.vbml_ignore_case = True 
labeler.load(main_labeler)

#* Object of bot *#
bot = Bot(
    token=settings['vk-token'],
    labeler=labeler,
    state_dispenser=dispanser
    )

#* Запуск бота
if __name__ == '__main__':
    asyncio.run(bot.run_polling())
