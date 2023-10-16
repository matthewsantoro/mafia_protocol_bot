from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Создать игру")
    kb.button(text="Помощь")
    kb.button(text="Об авторе")
    kb.button(text="Профиль")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def set_role() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    sheriff = InlineKeyboardButton(text='⭐', callback_data='add_sheriff')
    don = InlineKeyboardButton(text='💍 ', callback_data='add_don')
    mafia = InlineKeyboardButton(text='👎🏿', callback_data='add_mafia')
    kb.add(sheriff, don, mafia)
    return kb.as_markup()

def nomination() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    player_1 = InlineKeyboardButton(text='1️⃣', callback_data='player1')
    player_2 = InlineKeyboardButton(text='2⃣', callback_data='player2')
    player_3 = InlineKeyboardButton(text='3⃣', callback_data='player3')
    player_4 = InlineKeyboardButton(text='4⃣', callback_data='player4')
    player_5 = InlineKeyboardButton(text='5⃣', callback_data='player5')
    player_6 = InlineKeyboardButton(text='6⃣', callback_data='player6')
    player_7 = InlineKeyboardButton(text='7⃣', callback_data='player7')
    player_8 = InlineKeyboardButton(text='8⃣', callback_data='player8')
    player_9 = InlineKeyboardButton(text='9⃣', callback_data='player9')
    fouls = InlineKeyboardButton(text='⚠️', callback_data='fouls')
    player_10 = InlineKeyboardButton(text='1⃣0⃣', callback_data='player10')
    next_state = InlineKeyboardButton(text='❎', callback_data='next')
    kb.add(player_1, player_2, player_3,
           player_4, player_5, player_6,
           player_7, player_8, player_9,
           fouls, player_10, next_state)
    kb.adjust(3)

    return kb.as_markup()

def choose_player() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    player_1 = InlineKeyboardButton(text='1️⃣', callback_data='player1')
    player_2 = InlineKeyboardButton(text='2⃣', callback_data='player2')
    player_3 = InlineKeyboardButton(text='3⃣', callback_data='player3')
    player_4 = InlineKeyboardButton(text='4⃣', callback_data='player4')
    player_5 = InlineKeyboardButton(text='5⃣', callback_data='player5')
    player_6 = InlineKeyboardButton(text='6⃣', callback_data='player6')
    player_7 = InlineKeyboardButton(text='7⃣', callback_data='player7')
    player_8 = InlineKeyboardButton(text='8⃣', callback_data='player8')
    player_9 = InlineKeyboardButton(text='9⃣', callback_data='player9')
    player_10 = InlineKeyboardButton(text='1⃣0⃣', callback_data='player10')
    kb.add(player_1, player_2, player_3,
           player_4, player_5, player_6,
           player_7, player_8, player_9,
           player_10)
    kb.adjust(3)

    return kb.as_markup()
