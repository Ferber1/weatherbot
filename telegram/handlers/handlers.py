from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config.settings import commands
from telegram.settings import MAIN_PHRASE_ENG, MAIN_PHRASE_RUS

from telegram.utils.keyboards import main_keyboard, main_keyboard_eng
from telegram.utils.states import Form
from telegram.utils.sending import send_weather, send_city_info

main_router = Router()

#. <--------------- /COMMANDS ---------------> .#

#* /start
@main_router.message(Command(commands[0], ignore_case=True, prefix='/!'))
async def _start(message: Message):
    #* if language == ru
    if message.from_user.language_code == 'ru':
        return await message.answer(MAIN_PHRASE_RUS, reply_markup=main_keyboard)
    #* elif language != ru
    return await message.answer(MAIN_PHRASE_ENG, reply_markup=main_keyboard_eng)


#* /weather
@main_router.message(Command(commands[1], prefix='/!', ignore_case=True))
async def _weather(message: Message, state: FSMContext):
	if len(message.text.split()) >= 2: #* if city entered
		city = message.text.split()[1:]
		city = ' '.join(city)
  
		return await send_weather(message, city)

	await state.set_state(Form.city_for_weather)
	return (
    	await message.answer('Хорошо, теперь введи город! ⌨')
		if message.from_user.language_code == 'ru' else
		await message.answer('Ok, now enter city! ⌨')
    )

#* /info
@main_router.message(Command(commands[2], prefix='/!', ignore_case=True))
async def _info(message: Message, state: FSMContext):
    if len(message.text.split()) >= 2: #* if city entered
        city = message.text.split()[1:]
        city = ' '.join(city)
  
        return await send_city_info(message, city)

    await state.set_state(Form.city_for_info)
    return (
    	await message.answer('Хорошо, теперь введи город! ⌨')
		if message.from_user.language_code == 'ru' else
		await message.answer('Ok, now enter city! ⌨')
    )

#. <--------------- KEYBOARD COMMANDS ---------------> .#

#* KEYBOARD [WEATHER]
@main_router.message(F.text.in_(['🔎 Select city (weather)', '🔎 Выбрать город (погода)']))
async def k_weather(message: Message, state: FSMContext):
    await state.set_state(Form.city_for_weather)
    return (
    	await message.answer('Хорошо, теперь введи город! ⌨')
		if message.from_user.language_code == 'ru' else
		await message.answer('Ok, now enter city! ⌨')
    )
    
#* KEYBOARD [INFO]
@main_router.message(F.text.in_(['🔎 Select city (information)', '🔎 Выбрать город (информация)']))
async def k_info(message: Message, state: FSMContext):
    await state.set_state(Form.city_for_info)
    return (
		await message.answer('Хорошо, теперь введи город! ⌨')
		if message.from_user.language_code == 'ru' else
		await message.answer('Ok, now enter city! ⌨')
	)

#. <--------------- INPUT (FORM) COMMANDS ---------------> .#

#* INPUT [WEATHER]
@main_router.message(Form.city_for_weather)
async def i_weather(message: Message, state: FSMContext):
    city = message.text
    await state.clear()
    return await send_weather(message, city)


#* INPUT [INFO]
@main_router.message(Form.city_for_info)
async def i_info(message: Message, state: FSMContext):
    city = message.text
    await state.clear()
    return await send_city_info(message, city)
