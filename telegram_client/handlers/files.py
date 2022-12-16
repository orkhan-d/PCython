from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from other.get_pc_state import is_muted, get_dirs
from keyboards.inline.markups import get_main_menu
from keyboards.reply.markups import get_cd_menu

import configparser
import states

from loader import dp

from bot import client

@dp.message_handler(lambda m: m.text[-1]=='/', state=None)
async def change_dir(message: types.Message):
    config = configparser.ConfigParser()
    config.read('config.ini')

    client.connect(**(config['CREDETIANALS']))
    stdin, stdout, stderr = client.exec_command('cd {}/{} && pwd'.format(
        config["PC_STATE"]['curdir'], message.text[:-1]
    ))

    res = stdout.read().decode('utf-8')
    err = stderr.read().decode('utf-8')

    print(res)

    if not err:
        config['PC_STATE']['curdir'] = res
        with open('config.ini', 'w') as conf:
            config.write(conf)

        await message.answer(
            'Current directory:\n{}'.format(res),
            reply_markup=get_cd_menu(get_dirs(config['CREDETIANALS']))
        )
    else:
        print(err, res)
        await message.answer(
            'Failed to change directory!\nCurrent directory:\n{}'.format(res),
            reply_markup=get_cd_menu(get_dirs(config['CREDETIANALS']))
        )
    
    client.close()