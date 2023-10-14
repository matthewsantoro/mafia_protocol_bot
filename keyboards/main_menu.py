from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Создать игру")
    kb.button(text="Помощь")
    kb.button(text="Об авторе")
    kb.button(text="Профиль")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
