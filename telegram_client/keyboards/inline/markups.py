from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu(vol_mode: bool = True):
    return InlineKeyboardMarkup(
        row_width=3, inline_keyboard=[
            [
                InlineKeyboardButton('🔊', callback_data='volup'+('' if not vol_mode else 'm')),
                InlineKeyboardButton('🔉', callback_data='voldown'),
                InlineKeyboardButton(('🔇' if vol_mode else '🔈'), callback_data=('mute' if vol_mode else 'unmute')),
            ]
        ]
    )