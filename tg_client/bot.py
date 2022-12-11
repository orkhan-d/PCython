from aiogram import Bot, Dispatcher, executor, types
import paramiko

import logging

logging.basicConfig(
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO
)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

bot = Bot('TOKEN')
dp = Dispatcher(bot)

@dp.message_handler(commands=['voldown'])
async def main(message: types.Message):
    args = message.get_args()
    if not args:
        args = 5
    
    # SET YOUR CREDENTIALS HERE
    creds = {
        'username': 'user',
        'password':'passwd',
        'hostname': 'host', 
        'port': 22
    }

    client.connect(**creds)
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
    
    # SET YOUR CREDENTIALS HERE
    creds = {
        'username': 'user',
        'password':'passwd',
        'hostname': 'host', 
        'port': 22
    }

    client.connect(**creds)
    stdin, stdout, stderr = client.exec_command(f'amixer -c 1 -q set Master {args}%+')

    try:
        server_reply = stdout.read().decode()
        await message.answer(server_reply)
    except:
        pass

    client.close()

if __name__=='__main__':
    executor.start_polling(dp)