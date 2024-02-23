from vkbottle import Keyboard, KeyboardButtonColor, EMPTY_KEYBOARD, Text, Callback
from typing import Literal

def keyboard_builder(
	buttons: tuple[tuple
    [str, Literal['NEGATIVE', 'POSITIVE', 'PRIMARY', 'SECONDARY']]
    ],
	one_time: bool=False
) -> Keyboard:

    keyboard = Keyboard(one_time=one_time)
    
    [
		keyboard.add(Text(txt), color=KeyboardButtonColor[color]).row()
		for txt, color in buttons
	]
    
    return keyboard.get_json()

def inline_builder(
	buttons: tuple[tuple
    [str, Literal['NEGATIVE', 'POSITIVE', 'PRIMARY', 'SECONDARY']]
    ]
) -> Keyboard:

    inline_keyboard = Keyboard(inline=True)
    
    [
		inline_keyboard.add(Text(txt), color=KeyboardButtonColor[color]).row()
		for txt, color in buttons
	]

    return inline_keyboard.get_json()
