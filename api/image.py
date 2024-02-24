from random import randint
from asyncio import run

async def get_random_image(a: int, b: int) -> tuple[bytes, str]:
    random_path = f'images/{randint(a, b)}.jpg'
    try:
        with open(random_path, 'rb') as f:
            return (
                f.read(),
                random_path
                )
    except Exception as e:
        print(e)
        #* debug
        with open('debug.txt', 'a') as f:
            f.write(str(e) + '\n')
        return (
            None, None
        )
