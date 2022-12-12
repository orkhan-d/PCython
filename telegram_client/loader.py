# aiogram importing
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.contrib.fsm_storage.memory import MemoryStorage

# ssh client
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# setting config variables
import configparser
config = configparser.ConfigParser()

# configurating logging
import logging

logging.basicConfig(
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO
)

# create bot
TOKEN = 'TOKEN' # Add your bot's token

bot = Bot(TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)