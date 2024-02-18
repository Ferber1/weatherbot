import aiohttp
from config.config_reader import settings

api_key = settings['weather-token']

async def get_current_weather(city: str) -> dict | None:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                return data
    except aiohttp.ClientResponseError as e:
        if e.status == 404:
            print(f'Город {city} не был найден.')
        else:
            print(f'Error: {e}')
            with open("debug.txt", "a", encoding='utf-8') as f:
                f.write(str(e))
        return None
    except aiohttp.ClientError as e:
        print(f'Error: {e}')
        with open("debug.txt", "a", encoding='utf-8') as f:
            f.write(str(e))
        return None
