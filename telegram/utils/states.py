from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    city_for_weather = State()
    city_for_info = State()
