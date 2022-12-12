from aiogram import executor
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

from loader import dp
import handlers, states

if __name__=='__main__':
    executor.start_polling(dp)