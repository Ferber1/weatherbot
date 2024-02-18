from dotenv import load_dotenv
from os import getenv

#* Загружаем данные из файла .env *#

load_dotenv()

TG_TOKEN = getenv('TELEGRAM-TOKEN')

commands = ['start', 'weather', 'info']