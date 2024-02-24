
#TODO: (on new branch) ->  testing not sending main_keyboard permanently
from vk.utils.keyboards import main_keyboard
from vk.settings import INFO_ERROR_RUS, INFO_EXCEPTION_RUS

from datetime import datetime

from vkbottle.bot import Message

from api.weather import get_current_weather, get_info_city

async def send_weather(message: Message, city: str) -> None:
    info = await get_current_weather(city)

    if info == 0: #* if city not found
        return await message.answer(INFO_ERROR_RUS.format(city))
    
    elif info is None: #* elif there is error
        return await message.answer(INFO_EXCEPTION_RUS)
    
    result = f'''
💙 Погода в прекрасном городе {city.capitalize()}:

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
Порывы: {info['wind'].get('gust', '0')} м/с 🌬
'''
    return await message.answer(result)

async def send_city_info(message: Message, city: str) -> None:
    city_info = await get_info_city(city)

    if city_info == 0: #* if city not found
        return await message.answer(INFO_ERROR_RUS.format(city))
    
    elif city_info is None: #* elif there is error
        return await message.answer(INFO_EXCEPTION_RUS)
    
    result = f'''
💙 Информация о городе {city.capitalize()}:

🌍 Координаты:
Долгота: {city_info['lon']}
Широта: {city_info['lat']}

👀 Видимость: {city_info['visibility']} м

🌅 Время:
Страна: {city_info['country']}
Восход солнца: {datetime.fromtimestamp(city_info['sunrise']).strftime('%Y-%m-%d %H:%M:%S')}
Закат солнца: {datetime.fromtimestamp(city_info['sunset']).strftime('%Y-%m-%d %H:%M:%S')}
'''
    return await message.answer(result)