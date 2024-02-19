from random import randint
from io import BytesIO
from aiogram.types import InputFile

async def get_random_image(a: int, b: int) -> bytes:
    try:
        #* return random image from folder "images"
        with open(f'images/{randint(a, b)}.jpg', 'rb') as img:
            return InputFile(BytesIO(img.read()))
    except Exception as e:
        #* debug
        print(f'Error: {e}')
        with open("debug.txt", "a", encoding='utf-8') as f:
            f.write(str(e))
        return
