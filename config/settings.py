from dotenv import load_dotenv
from os import getenv

#* Загружаем данные из файла .env *#

load_dotenv()

settings = {
	'weather-token': getenv('WEATHER-TOKEN'),
	'telegram-token': getenv('TELEGRAM-TOKEN'),
    'vk-token': getenv('VK-TOKEN')
}

commands = ['start', 'weather', 'info']
