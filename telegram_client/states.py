from aiogram.dispatcher.filters.state import State, StatesGroup

class Creds(StatesGroup):
    name = State()
    passwd = State()
    host = State()
    port = State()