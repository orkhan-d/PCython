from aiogram.dispatcher import FSMContext
import configparser

from loader import dp, types, ReplyKeyboardMarkup, KeyboardButton
from states import Creds

from bot import client

@dp.message_handler(lambda message: message=='Cancel', state='*')
async def get_name(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        (
            'You should let us know credetianals to use bot.\n\n'
            'Nobody other than you will be able get access to it.'
        ), reply_markup=ReplyKeyboardMarkup(
            [
                [KeyboardButton('Send credetianals')]
            ]
        )
    )

@dp.message_handler(lambda message: message.text=='Send credetianals')
async def get_name(message: types.Message):
    await Creds.name.set()
    await message.answer('Send server username')

@dp.message_handler(state=Creds.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data({
        'username': message.text
    })

    await Creds.next()

    await message.answer('Send server password')

@dp.message_handler(state=Creds.passwd)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data({
        'password': message.text
    })

    await Creds.next()

    await message.answer('Send server hostname (either ip or domain)')

@dp.message_handler(state=Creds.host)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data({
        'hostname': message.text
    })

    await Creds.next()

    await message.answer('Send server port')

@dp.message_handler(state=Creds.port)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data({
        'port': int(message.text)
    })

    config = configparser.ConfigParser()
    config['CREDETIANALS'] = await state.get_data()

    await state.finish()
    await message.answer('Trying to connect...')
    
    try:
        client.connect(**config['CREDETIANALS'])
        stdin, stdout, stderr = client.exec_command('pwd')
        config['PC_STATE']['cur_dir'] = stdout.read()
        with open('config.ini', 'w') as conf:
            config.write(conf)

        client.close()

        await message.answer('Good job! Now you can cntrol your PC! Enter /menu for functions')
    except Exception as e:
        print(e)
        await message.answer('Error! Check credetianals more one time and retry!', 
            reply_markup=ReplyKeyboardMarkup(
                [
                    [KeyboardButton('Send credetianals')]
                ], resize_keyboard=True
            )
        )