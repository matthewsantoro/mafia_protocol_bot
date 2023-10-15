from aiogram.fsm.state import StatesGroup, State


class OrderGame(StatesGroup):
    enter_players = State()
    role_selection = State()
    game_day = State()
    game_night = State()