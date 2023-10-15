from typing import NamedTuple


def get_list_players() -> list:
    return ['Питон',
            'Джулс',
            'Вендетта',
            'Инкогнито',
            'Мама',
            'Камень',
            'Эмоционал',
            'Киндер',
            'Ювента',
            'СОБР']


class GameSession(NamedTuple):
    players: list
    roles: list = None
    best_move: list = None
    days: list = None
    nights: list = None

