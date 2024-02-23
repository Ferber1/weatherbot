from vkbottle.bot import BotLabeler, Message

from vk.utils.states import Form, dispanser
from vk.utils.keyboards import main_keyboard
from vk.utils.sending import send_weather, send_city_info

from vk.settings import MAIN_PHRASE_RUS

from config.settings import commands

main_labeler = BotLabeler()

#. <--------------- /COMMANDS ---------------> .#

#* /start
@main_labeler.private_message(text=[f'/{commands[0]}', f'!{commands[0]}'])
async def _start(message: Message):
    return await message.answer(MAIN_PHRASE_RUS, keyboard=main_keyboard)

#* /weather
@main_labeler.private_message(text=[f'/{commands[1]} <city>', f'!{commands[1]} <city>'])
async def _weather(message: Message, city: str = None):
    if len(message.text.split()) >= 2: #* if city entered
        city = message.text.split()[1:]
        city = ' '.join(city)

        return await send_weather(message, city)
    
    await dispanser.set(message.peer_id, Form.city_for_weather)
    return (
        await message.answer('Хорошо, теперь введи город! ⌨')
    )

#* /info
@main_labeler.private_message(text=[f'/{commands[2]} <city>', f'!{commands[2]} <city>'])
async def _info(message: Message, city: str = None):
    if len(message.text.split()) >= 2: #* if city entered
        city = message.text.split()[1:]
        city = ' '.join(city)

        return await send_city_info(message, city)
    
    await dispanser.set(message.peer_id, Form.city_for_info)
    return (
        await message.answer('Хорошо, теперь введи город! ⌨')
    )

#. <--------------- KEYBOARD COMMANDS ---------------> .#

#* KEYBOARD [WEATHER]
@main_labeler.private_message(text=['🔎 Выбрать город (погода)'])
async def k_weather(message: Message):
    await dispanser.set(message.peer_id, Form.city_for_weather)
    return (
        await message.answer('Хорошо, теперь введи город ⌨')
    )

#* KEYBOARD [INFO]
@main_labeler.private_message(text=['🔎 Выбрать город (информация)'])
async def k_info(message: Message):
    await dispanser.set(message.peer_id, Form.city_for_info)
    return (
        await message.answer('Хорошо, теперь введи город! ⌨')
    )

#. <--------------- INPUT (FORM) COMMANDS ---------------> .#

#* INPUT [WEATHER]
@main_labeler.private_message(state=Form.city_for_weather)
async def i_weather(message: Message):
    city = message.text
    await dispanser.delete(message.peer_id)
    return await send_weather(message, city)

#* INPUT [INFO]
@main_labeler.private_message(state=Form.city_for_info)
async def i_info(message: Message):
    city = message.text
    await dispanser.delete(message.peer_id)
    return await send_city_info(message, city)
