from dotenv import load_dotenv
from os import getenv

#* Загружаем данные из файла .env *#

settings = {
	'weather-token': getenv('WEATHER-TOKEN')
}