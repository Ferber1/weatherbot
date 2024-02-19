from api.weather import get_current_weather
# import json
import asyncio

result = asyncio.run(get_current_weather('Sankt-Peterburg'))

# print(json.dumps(result, indent=4))

import requests, json
 
res = requests.get("https://api.nekosapi.com/v3/images/random")
res.raise_for_status()
 
data = res.json()

with open("response.json", "w", encoding='utf-8') as f:
	print(json.dump(result, f, indent=4))