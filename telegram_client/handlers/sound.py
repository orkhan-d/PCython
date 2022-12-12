from bot import client

from loader import dp, types
from configparser import ConfigParser

@dp.message_handler(commands=['mute', 'unmute'])
async def toggle_mute(message: types.Message):
    creds = ConfigParser()
    creds.read('config.ini')

    client.connect(**(creds['CREDETIANALS']))
    comms = [
        'amixer -c 1 -q set Master toggle',
        'amixer -c 1 -q set Headphone unmute',
        'amixer -c 1 -q set Speaker unmute'
    ]

    stdin, stdout, stderr = client.exec_command(comms[0] if message.get_command()=='mute' else ' && '.join(comms))

    try:
        server_reply = stdout.read().decode()
        await message.answer(server_reply)
    except:
        pass

@dp.message_handler(commands=['voldown'])
async def main(message: types.Message):
    args = message.get_args()
    if not args:
        args = 5

    creds = ConfigParser()
    creds.read('config.ini')

    client.connect(**(creds['CREDETIANALS']))
    stdin, stdout, stderr = client.exec_command(f'amixer -c 1 -q set Master {args}%-')

    try:
        server_reply = stdout.read().decode()
        await message.answer(server_reply)
    except:
        pass

    client.close()

@dp.message_handler(commands=['volup'])
async def main(message: types.Message):
    args = message.get_args()
    if not args:
        args = 5

    creds = ConfigParser()
    creds.read('config.ini')

    client.connect(**(creds['CREDETIANALS']))
    stdin, stdout, stderr = client.exec_command(f'amixer -c 1 -q set Master {args}%+')

    try:
        server_reply = stdout.read().decode()
        await message.answer(server_reply)
    except:
        pass

    client.close()