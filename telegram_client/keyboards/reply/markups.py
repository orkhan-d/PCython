from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_cd_menu(dirs: list[str]):
    return ReplyKeyboardMarkup(
        keyboard=[
            list(map(lambda t: KeyboardButton(t), dirs[i:i+4]))
                 for i in range(0, len(dirs), 3)
        ], resize_keyboard=True
    )