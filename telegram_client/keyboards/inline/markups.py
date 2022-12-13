from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu(vol_mode: bool = True):
    return InlineKeyboardMarkup(
        row_width=3, inline_keyboard=[
            [
                InlineKeyboardButton('🔊', callback_data=('volup' if vol_mode else 'volupm')),
                InlineKeyboardButton('🔉', callback_data='voldown'),
                InlineKeyboardButton(('🔇' if vol_mode else '🔈'), callback_data=('mute' if vol_mode else 'unmute')),
            ],
            [
                InlineKeyboardButton('⏯', callback_data='pb-play-pause'),
                InlineKeyboardButton('⏹', callback_data='pb-stop'),
            ]
        ]
    )