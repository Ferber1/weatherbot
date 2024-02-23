from vkbottle import BaseStateGroup
from vkbottle import BuiltinStateDispenser

class Form(BaseStateGroup):
    city_for_weather = 0
    city_for_info = 1

dispanser = BuiltinStateDispenser()