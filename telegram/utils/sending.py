from datetime import datetime
from aiogram.types import Message
from api.weather import get_current_weather, get_info_city
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

🌬 Ветер:
Скорость: {info['wind']['speed']} м/с
Направление: {info['wind']['deg']}°
Порывы: {info['wind']['gust']} м/с 🌬
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

🌬 Wind:
Speed: {info['wind']['speed']} m/s
Direction: {info['wind']['deg']}°
Gusts: {info['wind']['gust']} m/s 🌬
'''
    return await message.answer(result, reply_markup=main_keyboard_eng)

async def send_city_info(message: Message, city: str) -> None:
    city_info = await get_info_city(city)

    if city_info == 0: #* if city not found
        if message.from_user.language_code == 'ru': #* russian language
            return await message.answer(INFO_ERROR_RUS.format(city), reply_markup=main_keyboard)
		#* else
        return await message.answer(INFO_ERROR_ENG.format(city), reply_markup=main_keyboard_eng)

    elif city_info is None: #* elif there is error
        if message.from_user.language_code == 'ru': #* russian language
            return await message.answer(INFO_EXCEPTION_RUS, reply_markup=main_keyboard)
		#* else
        return await message.answer(INFO_EXCEPTION_ENG, reply_markup=main_keyboard_eng)
    
    
    if message.from_user.language_code == 'ru':  #* russian language
        result = f'''
💙 Информация о городе <b>{city_info['name'].capitalize()}</b>:

🌍 Координаты:
Долгота: {city_info['lon']}
Широта: {city_info['lat']}

👀 Видимость: {city_info['visibility']} м

🌅 Время:
Страна: {city_info['country']}
Восход солнца: {datetime.fromtimestamp(city_info['sunrise']).strftime('%Y-%m-%d %H:%M:%S')}
Закат солнца: {datetime.fromtimestamp(city_info['sunset']).strftime('%Y-%m-%d %H:%M:%S')}
'''
        return await message.answer(result, reply_markup=main_keyboard)
    
    #* else
    result = f'''
💙 Information about the city <b>{city_info['name'].capitalize()}</b>:

🌍 Coordinates:
Longitude: {city_info['lon']}
Latitude: {city_info['lat']}

👀 Visibility: {city_info['visibility']} m

🌅 Time:
Country: {city_info['country']}
Sunrise: {datetime.fromtimestamp(city_info['sunrise']).strftime('%Y-%m-%d %H:%M:%S')}
Sunset: {datetime.fromtimestamp(city_info['sunset']).strftime('%Y-%m-%d %H:%M:%S')}
'''
    return await message.answer(result, reply_markup=main_keyboard_eng)
