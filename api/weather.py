import aiohttp, asyncio
from config.settings import settings

#* api key and url
api_key = settings['weather-token']
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

async def get_current_weather(city: str) -> dict | None:
    try:
        async with aiohttp.ClientSession() as session:
            #* get response
            async with session.get(url.format(city, api_key)) as response:
                response.raise_for_status()
                data = await response.json()
                return {
                    'weather': data['weather'][0],
                    'main': data['main'],
                    'wind': data['wind']
                }
    except aiohttp.ClientResponseError as e:
        if e.status == 404: #* cheking errors
            return 0 #* city not found
        else:
            #* debug
            print(f'Error: {e}')
            with open("debug.txt", "a", encoding='utf-8') as f:
                f.write(str(e))
        return None
    except aiohttp.ClientError as e:
        #* debug
        print(f'Error: {e}')
        with open("debug.txt", "a", encoding='utf-8') as f:
            f.write(str(e))
        return None


async def get_info_city(city: str) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            #* get response
            async with session.get(url.format(city, api_key)) as response:
                response.raise_for_status()
                data = await response.json()
                return {
                    'lon': data['coord']['lon'],
                    'lat': data['coord']['lat'],
                    'visibility': data['visibility'],
                    'country': data['sys']['country'],
                    'sunrise': data['sys']['sunrise'],
                    'sunset': data['sys']['sunset'],
                    'name': data['name']
                }
    except aiohttp.ClientResponseError as e:
        if e.status == 404: #* cheking errors
            return 0 #* city not found
        else:
            #* debug
            print(f'Error: {e}')
            with open("debug.txt", "a", encoding='utf-8') as f:
                f.write(str(e))
        return None
    except aiohttp.ClientError as e:
        #* debug
        print(f'Error: {e}')
        with open("debug.txt", "a", encoding='utf-8') as f:
            f.write(str(e))
        return None

if __name__ == '__main__':
    import json
    print(asyncio.run(get_current_weather('moscow')))
    with open("response.json", "w") as f:
        print(json.dump(asyncio.run(get_info_city('moscow')), f, indent=4))