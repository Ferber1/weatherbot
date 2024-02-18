from api.weather import get_current_weather
import json
import asyncio

result = asyncio.run(get_current_weather('Sankt-Peterburg'))

print(json.dumps(result, indent=4))