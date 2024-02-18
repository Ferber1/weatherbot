from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config.settings import commands
from settings import MAIN_PHRASE_ENG, MAIN_PHRASE_RUS, INFO_ERROR_RUS, INFO_ERROR_ENG, \
    INFO_EXCEPTION_ENG, INFO_EXCEPTION_RUS

from api.weather import get_current_weather
from utils.keyboards import main_keyboard, main_keyboard_eng

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
async def _weather(message: Message):
	if len(message.text.split()) >= 2: #* if city entered
		city = message.text.split()[1:]
		city = ' '.join(city)
		info = await get_current_weather(city)
		if info == 0: #* if info not found (None or 0)
			if message.from_user.language_code == 'ru': #* russian language
				return await message.answer(INFO_ERROR_RUS.format(city), reply_markup=main_keyboard)
			#* else
			return await message.answer(INFO_ERROR_ENG.format(city), reply_markup=main_keyboard_eng)
		elif info is None:
			if message.from_user.language_code == 'ru': #* russian language
				return await message.answer(INFO_EXCEPTION_RUS, reply_markup=main_keyboard)
			#* else
			return await message.answer(INFO_EXCEPTION_ENG, reply_markup=main_keyboard_eng)
		if message.from_user.language_code == 'ru': #* russian language
			result = f'''
💙 Погода в прекрасном городе <b>{city.capitalize()}</b>:

🤍 Описание: 
В основном — {info['weather']['main']}
Обстановка — {info['weather']['description']}

🌡 Температура:
{info['main']['temp']:.1f} °C — {'одевайтесь потеплее ❄!' if info['main']['temp'] < 0 else 'жарковато ☀!'}
Ощущается как все {info['main']['feels_like']:.1f} °C.. 🎨
Минимум: {info["main"]['temp_min']:.1f} °C 💄
Максимум: {info["main"]['temp_max']:.1f} °C 🥟
	
'''
			await message.answer(result, reply_markup=main_keyboard)
			#* else
		result = f'''
💙 Weather in a beautiful city <b>{city.capitalize()}</b>:

🤍 Description: 
Basically — {info['weather']['main']}
The situation is {info['weather']['description']}

🌡 Temperature:
{info['main']['temp']:.1f} °C — {'dress warmly ❄!' if info['main']['temp'] < 0 else 'it's a little hot'!'}
Feels like everything {info['main']['feels_like']:.1f} °C.. 🎨
Minimum: {info["main"]['temp_min']:.1f} °C 💄
Maximum: {info["main"]['temp_max']:.1f} °C 🥟

'''
		return await message.answer(result, reply_markup=main_keyboard_eng)
	return (
    await message.answer('Использование команды: /weather <b>«город»</b> 🐍')
    if message.from_user.language_code == 'ru' else
    await message.answer('Using command: /weather <b>«city»</b> 🐍')
         )

#* KEYBOARD [WEATHER]
@router.message(F.text.in_(['Select city', 'Выбрать город']))
async def k_weather(message: Message):
    ...