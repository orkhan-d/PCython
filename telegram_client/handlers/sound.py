from bot import client

from loader import dp, types
from configparser import ConfigParser

from keyboards.inline.markups import get_main_menu
from other.get_pc_state import is_muted

@dp.callback_query_handler(lambda msg: msg.data in ['mute', 'unmute'])
async def voldown(query: types.CallbackQuery):
    creds = ConfigParser()
    creds.read('config.ini')

    client.connect(**(creds['CREDETIANALS']))
    comms = [
        'amixer -c 1 -q set Master toggle',
        'amixer -c 1 -q set Headphone unmute',
        'amixer -c 1 -q set Speaker unmute'
    ]

    stdin, stdout, stderr = client.exec_command(comms[0] if query.data=='mute' else ' && '.join(comms))

    try:
        server_reply = stdout.read().decode()
        await query.answer(cache_time=2)
        await query.message.edit_reply_markup(
            get_main_menu(is_muted(creds['CREDETIANALS']))
        )
    except Exception as e:
        print(e)

@dp.callback_query_handler(lambda msg: msg.data=='voldown')
async def voldown(query: types.CallbackQuery):
    creds = ConfigParser()
    creds.read('config.ini')

    client.connect(**(creds['CREDETIANALS']))
    stdin, stdout, stderr = client.exec_command('amixer -c 1 -q set Master 10%-')

    try:
        server_reply = stdout.read().decode()
        await query.answer(cache_time=2)
    except:
        pass

    client.close()

@dp.callback_query_handler(lambda msg: msg.data.startswith('volup'))
async def volup(query: types.CallbackQuery):
    creds = ConfigParser()
    creds.read('config.ini')

    client.connect(**(creds['CREDETIANALS']))

    if query.data=='volupm':
        comms = [
            'amixer -c 1 -q set Master unmute',
            'amixer -c 1 -q set Headphone unmute',
            'amixer -c 1 -q set Speaker unmute'
        ]
        stdin, stdout, stderr = client.exec_command(' && '.join(comms+['amixer -c 1 -q set Master 10%+']))
    else:
        stdin, stdout, stderr = client.exec_command('amixer -c 1 -q set Master 10%+')

    try:
        server_reply = stdout.read().decode()
        await query.answer(cache_time=2)
    except:
        pass

    client.close()

@dp.callback_query_handler(lambda msg: msg.data=='pb-play-pause')
async def volup(query: types.CallbackQuery):
    creds = ConfigParser()
    creds.read('config.ini')

    client.connect(**(creds['CREDETIANALS']))
    
    stdin, stdout, stderr = client.exec_command('playerctl play-pause')

    try:
        server_reply = stdout.read().decode()
        await query.answer(cache_time=2)
    except:
        pass

    client.close()

@dp.callback_query_handler(lambda msg: msg.data=='pb-stop')
async def volup(query: types.CallbackQuery):
    creds = ConfigParser()
    creds.read('config.ini')

    client.connect(**(creds['CREDETIANALS']))
    
    stdin, stdout, stderr = client.exec_command('playerctl stop')

    try:
        server_reply = stdout.read().decode()
        await query.answer(cache_time=2)
    except:
        pass

    client.close()