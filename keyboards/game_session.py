from aiogram.filters.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from bot.utils.CustomCallBack import RoleCallback


def main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Создать игру")
    kb.button(text="Помощь")
    kb.button(text="Об авторе")
    kb.button(text="Профиль")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def nomination() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    player_1 = InlineKeyboardButton(text='1️', callback_data='player1')
    player_2 = InlineKeyboardButton(text='2', callback_data='player2')
    player_3 = InlineKeyboardButton(text='3', callback_data='player3')
    player_4 = InlineKeyboardButton(text='4', callback_data='player4')
    player_5 = InlineKeyboardButton(text='5', callback_data='player5')
    player_6 = InlineKeyboardButton(text='6', callback_data='player6')
    player_7 = InlineKeyboardButton(text='7', callback_data='player7')
    player_8 = InlineKeyboardButton(text='8', callback_data='player8')
    player_9 = InlineKeyboardButton(text='9', callback_data='player9')
    fouls = InlineKeyboardButton(text='⚠️', callback_data='fouls')
    player_10 = InlineKeyboardButton(text='10', callback_data='player10')
    next_state = InlineKeyboardButton(text='❎', callback_data='next')
    kb.add(player_1, player_2, player_3,
           player_4, player_5, player_6,
           player_7, player_8, player_9,
           fouls, player_10, next_state)
    kb.adjust(3)

    return kb.as_markup()


def choose_player(role: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for i in range(1, 11):
        kb.button(text=str(i), callback_data=RoleCallback(role=role, number=str(i)))
    kb.adjust(3)
    return kb.as_markup()


def set_role() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    sheriff = InlineKeyboardButton(text='⭐', callback_data='add_sheriff')
    don = InlineKeyboardButton(text='💍 ', callback_data='add_don')
    mafia = InlineKeyboardButton(text='👎🏿', callback_data='add_mafia')
    kb.add(sheriff, don, mafia)
    return kb.as_markup()
