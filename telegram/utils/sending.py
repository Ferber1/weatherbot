from aiogram.types import Message
from api.weather import get_current_weather
from settings import INFO_ERROR_ENG, INFO_ERROR_RUS, INFO_EXCEPTION_ENG, INFO_EXCEPTION_RUS
from .keyboards import main_keyboard, main_keyboard_eng

async def send_weather(message: Message, city: str) -> None:
    info = await get_current_weather(city)

    if info == 0: #* if city not found
        if message.from_user.language_code == 'ru': #* russian language
            return await message.answer(INFO_ERROR_RUS.format(city), reply_markup=main_keyboard)
		#* else
        return await message.answer(INFO_ERROR_ENG.format(city), reply_markup=main_keyboard_eng)

    elif info is None: #* elif there is error
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
        return await message.answer(result, reply_markup=main_keyboard)
		#* else
    result = f'''
💙 Weather in a beautiful city <b>{city.capitalize()}</b>:

🤍 Description: 
Basically — {info['weather']['main']}
The situation is {info['weather']['description']}

🌡 Temperature:
{info['main']['temp']:.1f} °C — {'dress warmly ❄!' if info['main']['temp'] < 0 else "it's a little hot ☀!"}
Feels like everything {info['main']['feels_like']:.1f} °C.. 🎨
Minimum: {info["main"]['temp_min']:.1f} °C 💄
Maximum: {info["main"]['temp_max']:.1f} °C 🥟

'''
    return await message.answer(result, reply_markup=main_keyboard_eng)