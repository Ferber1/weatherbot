# from api.weather import get_current_weather
# import json
# import asyncio

# result = asyncio.run(get_current_weather('Sankt-Peterburg'))

# print(json.dumps(result, indent=4))

# import requests, json
 
# res = requests.get("https://api.nekosapi.com/v3/images/random")
# res.raise_for_status()
 
# data = res.json()

# with open("response.json", "a", encoding='utf-8') as f:
# 	print(json.dump(data, f, indent=4))

import aiohttp
import asyncio
from config.settings import settings

async def fetch_random_image(api_key: str, query: str) -> str | None:
    url = "https://api.pexels.com/v1/search?query={}".format(query)

    headers = {
        "Authorization": api_key
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            print(f'Response status: {response.status}')
            print(f'Response status: {await response.text()}')
            data = await response.json()

            if response.status == 200:
                return data['photos'][0]['src']['original']
            else:
                print("Error:", data['message'])
                return None

async def main():
    # Ваш API ключ Pexels
    api_key = settings['img-token']

    image_url = await fetch_random_image(api_key, 'nature')
    if image_url:
        print("Random image URL:", image_url)

if __name__ == "__main__":
    asyncio.run(main())