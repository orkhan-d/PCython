from aiogram.types import (
    KeyboardButton, ReplyKeyboardMarkup,
    InlineKeyboardMarkup, InlineKeyboardButton
)

def get_main_menu(vol_mode: bool = True):
    return InlineKeyboardMarkup(
        row_width=3, inline_keyboard=[
            [
                InlineKeyboardButton('🔊', callback_data='volup'),
                InlineKeyboardButton('🔉', callback_data='voldown'),
                InlineKeyboardButton(('🔇' if vol_mode else '🔈'), callback_data='toggle'),
            ]
        ]
    )