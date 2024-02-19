from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config.settings import commands
from settings import MAIN_PHRASE_ENG, MAIN_PHRASE_RUS, INFO_ERROR_RUS, INFO_ERROR_ENG, \
    INFO_EXCEPTION_ENG, INFO_EXCEPTION_RUS

from api.weather import get_current_weather
from utils.keyboards import main_keyboard, main_keyboard_eng
from utils.states import Form
from utils.sending import send_weather, send_city_info

router = Router()

#* /start *#
@router.message(Command(commands[0], ignore_case=True, prefix='/!'))
async def _start(message: Message):
    #* if language == ru
    if message.from_user.language_code == 'ru':
        return await message.answer(MAIN_PHRASE_RUS, reply_markup=main_keyboard)
    #* elif language != ru
    return await message.answer(MAIN_PHRASE_ENG, reply_markup=main_keyboard_eng)

#* /weather *#
@router.message(Command(commands[1], prefix='/!', ignore_case=True))
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
	

#* KEYBOARD [WEATHER]
@router.message(F.text.in_(['🔎 Select city (weather)', '🔎 Выбрать город (погода)']))
async def k_weather(message: Message, state: FSMContext):
    await state.set_state(Form.city_for_weather)
    return (
    	await message.answer('Хорошо, теперь введи город! ⌨')
		if message.from_user.language_code == 'ru' else
		await message.answer('Ok, now enter city! ⌨')
    )
    
#* KEYBOARD [INFO]
@router.message(F.text.in_(['🔎 Select city (information)', '🔎 Выбрать город (информация)']))
async def k_info(message: Message, state: FSMContext):
    await state.set_state(Form.city_for_info)
    return (
		await message.answer('Хорошо, теперь введи город! ⌨')
		if message.from_user.language_code == 'ru' else
		await message.answer('Ok, now enter city! ⌨')
	)

#* INPUT [WEATHER]
@router.message(Form.city_for_weather)
async def i_weather(message: Message, state: FSMContext):
    city = message.text
    await state.clear()
    await send_weather(message, city)

#* /info
@router.message(Command(commands[2], prefix='/!', ignore_case=True))
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

#* INPUT [INFO]
@router.message(Form.city_for_info)
async def i_weather(message: Message, state: FSMContext):
    city = message.text
    await state.clear()
    await send_city_info(message, city)