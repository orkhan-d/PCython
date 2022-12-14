from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from other.get_pc_state import is_muted, get_dirs
from keyboards.inline.markups import get_main_menu
from keyboards.reply.markups import get_cd_menu

import configparser
import states

from loader import dp

@dp.message_handler(commands=['start'], state=None)
async def set_config(message: types.Message):
    welcome_text = ('Hi! It\'s bot to control your PC from Telegram!\n\n'
    'To start using you should set up SSH server on your PC and send me credetianals to log in\n\n'

    'All credetianals will be saved as .ini file on PC this bot launched and nobody wil have access to them!')
    
    await message.answer(welcome_text,
        reply_markup= ReplyKeyboardMarkup([
            [KeyboardButton('Send credetianals')]
        ], resize_keyboard=True)
    )

@dp.message_handler(commands=['menu'], state=None)
async def main_menu(message: types.Message):
    config = configparser.ConfigParser()
    config.read('config.ini')
    creds = config['CREDETIANALS']
    
    await message.answer(
        '=======Main menu=======', reply_markup=get_main_menu(is_muted(creds))
    )
    await message.answer(
        'Current directory', reply_markup=get_cd_menu(get_dirs(creds))
    )